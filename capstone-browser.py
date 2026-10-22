from pathlib import Path
import json
from playwright.sync_api import sync_playwright
out=Path('/tmp/pnec-capstone-pr-evidence-2026-10-21');rows=[];url='http://127.0.0.1:8097/capstone/powaynec-2026-2027/'
with sync_playwright() as p:
 browser=p.chromium.launch(channel="chrome");context=browser.new_context();context.route('**/*',lambda r:r.continue_() if r.request.url.startswith('http://127.0.0.1:8097/') else r.abort());context.route('**/api/microblog**', lambda r:r.fulfill(status=200,content_type='application/json',body='[]') if r.request.method=='GET' else r.abort());page=context.new_page();bad=[]
 page.on('response',lambda r:bad.append({'url':r.url,'status':r.status}) if r.url.startswith('http://127.0.0.1:8097/') and r.status>=400 else None)
 response=page.goto(url,wait_until='domcontentloaded');assert response.status==200
 assert page.locator('.pnec-capstone__feature').count()==9
 assert page.locator('.pnec-capstone__acceptance').count()==9
 assert page.locator('.pnec-capstone__board').count()==1
 assert page.locator('.pnec-capstone__lifecycle > section').count()==5
 assert page.locator('#microblog-toggle-btn').count()==1
 page.locator('#microblog-toggle-btn').focus();page.keyboard.press('Enter')
 assert 'open' in page.locator('#microblog-panel').get_attribute('class')
 page.locator('#microblog-close-btn').focus();page.keyboard.press('Enter')
 assert 'open' not in page.locator('#microblog-panel').get_attribute('class')
 assert page.locator('.pnec-capstone [data-ocs-kanban],.pnec-capstone iframe').count()==0
 # Match the color variables used by the site's preference-based themes.
 themes={'dark':{'--pref-bg-color':'#0b1220','--pref-text-color':'#e6eef8','--pref-accent-color':'#60a5fa','--panel':'#0b1220','--ui-border':'#344156'},'light':{'--pref-bg-color':'#ffffff','--pref-text-color':'#172033','--pref-accent-color':'#1d4ed8','--panel':'#ffffff','--ui-border':'#cbd5e1'}}
 for theme,colors in themes.items():
  page.evaluate('''colors=>{document.documentElement.classList.add('user-theme-active');for(const [k,v] of Object.entries(colors))document.documentElement.style.setProperty(k,v);}''',colors)
  for width in [320,390,768,1024,1440]:
   page.set_viewport_size({'width':width,'height':1000});page.wait_for_timeout(150)
   row=page.evaluate('''()=>{const root=document.querySelector('.pnec-capstone'),grid=document.querySelector('.pnec-capstone__features'),h=document.querySelector('.pnec-capstone__section h2'),card=grid.firstElementChild;return {width:innerWidth,scroll:document.documentElement.scrollWidth,gridColumns:getComputedStyle(grid).gridTemplateColumns,fontSize:getComputedStyle(root).fontSize,headingSize:getComputedStyle(h).fontSize,text:getComputedStyle(card).color,background:getComputedStyle(card).backgroundColor,cardWidth:card.getBoundingClientRect().width};}''');row['theme']=theme
   button = page.locator('.pnec-capstone__board .ocs__btn').evaluate('(e)=>({text:getComputedStyle(e).color,background:getComputedStyle(e).backgroundColor})')
   assert button['text'] != button['background'], button
   row['board_button'] = button
   assert row['scroll']<=width,row
   assert float(row['fontSize'].removesuffix('px'))>=18,row
   assert float(row['headingSize'].removesuffix('px'))>=24,row
   assert len(row['gridColumns'].split())==(1 if width<=800 else 2),row
   rows.append(row)
   if width in [390,1440]:
    board=page.locator('.pnec-capstone__board');board.screenshot(path=str(out/f'kanban-{theme}-{width}.png'))
    page.locator('.pnec-capstone__features').screenshot(path=str(out/f'features-{theme}-{width}.png'))
    if theme=='light':page.locator('section[aria-labelledby="delivery-lifecycle"]').screenshot(path=str(out/f'lifecycle-{width}.png'))
 # Verify fragment targets and generated local link destinations.
 links=page.locator('.pnec-capstone a').evaluate_all('(nodes)=>nodes.map(a=>({href:a.getAttribute("href"),url:a.href}))')
 for a in links:
  if a['href'].startswith('#'):assert page.locator(a['href']).count()==1,a
  elif a['url'].startswith('http://127.0.0.1:8097/'):
   assert context.request.get(a['url']).status==200,a
 shell_errors=[x for x in bad if x['url'].endswith('/undefined/api/id')]
 assert not [x for x in bad if x not in shell_errors],bad
 result={'status':'PASS','layouts':rows,'links':links,'static_resource_http_failures':[x for x in bad if x not in shell_errors],'existing_page_shell_api_errors':shell_errors,'external_services':'blocked; Microblog GET uses empty synthetic fixture, no posting or persistence verified; no live board simulated'}
 (out/'browser-results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));browser.close()

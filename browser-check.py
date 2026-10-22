from pathlib import Path
import json
from playwright.sync_api import sync_playwright
out=Path('/tmp/pnec-combined-validation-2026-10-22')
base='http://127.0.0.1:8100'
rows=[]
with sync_playwright() as p:
 browser=p.chromium.launch(channel='chrome')
 context=browser.new_context()
 context.route('**/*',lambda r:r.continue_() if r.request.url.startswith(base+'/') else r.abort())
 context.route('**/api/microblog**',lambda r:r.fulfill(status=200,content_type='application/json',body='[]') if r.request.method=='GET' else r.abort())
 github_requests=[]
 context.on('request',lambda r:github_requests.append(r.url) if r.url.startswith('https://api.github.com/') else None)
 page=context.new_page();bad=[]
 page.on('response',lambda r:bad.append({'url':r.url,'status':r.status}) if r.url.startswith(base+'/') and r.status>=400 else None)
 response=page.goto(base+'/capstone/powaynec-2026-2027/',wait_until='networkidle');assert response.status==200
 root=page.locator('div.ocs__stack.ocs__stack--wide');assert root.count()==1
 features=page.locator('section[aria-labelledby="proposed-improvements"] > .ocs__grid')
 assert features.locator(':scope > section').count()==9
 assert features.locator('.ocs__callout').count()==9
 assert page.locator('section[aria-labelledby="delivery-lifecycle"] > .ocs__grid > section').count()==5
 assert page.locator('[class*="pnec-capstone"]').count()==0
 board=page.locator('[data-ocs-kanban]');assert board.count()==1
 assert board.get_attribute('data-board-url')=='https://github.com/users/samanviy17-crypto/projects/1/views/1'
 assert board.get_attribute('data-filter')==''
 board.scroll_into_view_if_needed()
 page.wait_for_function("document.querySelector('[data-ocs-kanban] [data-hook=status]').textContent.includes('only boards owned by an organization')")
 assert board.locator('[data-hook=status]').is_visible()
 assert board.locator('[data-hook=mount]').is_hidden()
 assert page.locator('.ocs__kanban-board').count()==0
 assert board.locator('a').get_attribute('href')=='https://github.com/users/samanviy17-crypto/projects/1/views/1'
 assert len(github_requests)==0,github_requests

 assert page.locator('#microblog-toggle-btn').count()==1
 page.locator('#microblog-toggle-btn').focus();page.keyboard.press('Enter');assert 'open' in page.locator('#microblog-panel').get_attribute('class')
 page.locator('#microblog-close-btn').focus();page.keyboard.press('Enter');assert 'open' not in page.locator('#microblog-panel').get_attribute('class')
 page.wait_for_function('window.SitePreferences !== undefined')
 for theme in ['Site Default','Light','Midnight']:
  page.evaluate('(name)=>SitePreferences.applyPreferences(SitePreferences.PRESETS[name])',theme)
  for width in [320,390,768,1024,1440]:
   page.set_viewport_size({'width':width,'height':1000});page.wait_for_timeout(100)
   row=features.evaluate("e=>{let card=e.firstElementChild,s=getComputedStyle(card),p=card.querySelector('p');return {width:innerWidth,scroll:document.documentElement.scrollWidth,columns:getComputedStyle(e).gridTemplateColumns,text:s.color,background:s.backgroundColor,font:getComputedStyle(p).fontFamily,fontSize:getComputedStyle(p).fontSize,cardWidth:card.getBoundingClientRect().width}}")
   row['theme']=theme
   assert row['scroll']<=width,row
   assert len(row['columns'].split())==(1 if width<=768 else 2),row
   assert row['text']!=row['background'],row
   rows.append(row)
   if width in [390,1440]:
    features.screenshot(path=str(out/f'features-{theme.replace(" ","-")}-{width}.png'))
    page.locator('section[aria-labelledby="team-kanban-board"]').screenshot(path=str(out/f'board-{theme.replace(" ","-")}-{width}.png'))
 links=root.locator('a').evaluate_all('(nodes)=>nodes.map(a=>({href:a.getAttribute("href"),url:a.href}))')
 for a in links:
  if a['href'].startswith('#'):assert page.locator(a['href']).count()==1,a
  elif a['url'].startswith(base+'/'):assert context.request.get(a['url']).status==200,a
 shell=[x for x in bad if x['url'].endswith('/undefined/api/id')]
 assert not [x for x in bad if x not in shell],bad
 result={'status':'PASS','layouts':rows,'links':links,'static_resource_http_failures':[x for x in bad if x not in shell],'existing_page_shell_api_errors':shell,'theme_method':'Actual SitePreferences.applyPreferences with Site Default, Light, Midnight presets','microblog':'Keyboard open/close only; empty GET fixture, external requests blocked; production posting/auth/persistence not tested','kanban':'Actual shared include: personal-board notice visible, mount hidden, no fake cards, correct link, no GitHub API requests','github_api_requests':github_requests}
 nojs=browser.new_context(java_script_enabled=False)
 nojs_page=nojs.new_page();nojs_page.goto(base+'/capstone/powaynec-2026-2027/',wait_until='domcontentloaded')
 fallback=nojs_page.locator('[data-ocs-kanban] a');assert fallback.is_visible()
 assert fallback.get_attribute('href')=='https://github.com/users/samanviy17-crypto/projects/1/views/1'
 assert nojs_page.locator('[data-ocs-kanban] noscript').is_visible()
 nojs.close();result['javascript_disabled_fallback']='PASS: correct visible link and noscript notice'
 (out/'browser-results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2));browser.close()

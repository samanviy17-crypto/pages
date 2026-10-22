# PNEC Kanban workflow audit — proposed corrections only

**Read-only review: October 21, 2026. No issues, statuses, assignments, settings, code, commits, or deployments changed.**

**Conclusion:** the local capstone describes the required five-stage lifecycle, but the actual board does not yet demonstrate all its gates. Rename **Testing → In Review**, subject to Mr. Mortensen’s confirmation, and audit acceptance before retaining cards in Done. A rename alone will not fix the missing evidence.

## Scope and sources

- [Actual board](https://github.com/users/samanviy17-crypto/projects/1/views/1): all 41 project items retrieved, not just a potentially filtered board view. `board.json` and `fields.json` preserve the read-only snapshot.
- All **43 repository issues**, including two off-board issues, their descriptions/assignments/states, all **nine issue comments**, and the repository PR list were reviewed. Raw files: `issues.json`, `comments-pages.json`, `pulls.json`.
- Requirement source: the supplied instruction attachment, **“Document the required Kanban lifecycle”**, stages 1–5, plus its Quick/Formal issue rules. This is the user-supplied statement of Mr. Mortensen’s requirements, not independent evidence of a teacher approval decision.
- Compared the [published capstone](https://pages.opencodingsociety.com/capstone/powaynec-2026-2027/) with the prepared local `_posts/capstone/2026-09-11-pnec-capstone.md` in `/tmp/pnec-pages-capstone-review`, and the existing release audit/teacher package.
- Missing evidence means **not established by these records**, not proof the activity never occurred privately. Acceptance must be recorded by an authorized reviewer; it cannot be inferred from test counts, issue closure, or a board column.

## Actual board and requirements

| Required stage | Actual cards | Finding and exact gate to enforce |
| --- | --- | --- |
| Parking Lot / Backlog | Backlog: **26** | Includes 16 product proposals and 10 documentation/evidence cards. Proposals have stories, research, outcomes, acceptance criteria, dependencies, and proposed owners. Link stakeholder meeting/needs evidence, POV, HMW, alternatives/design before marking them ready for prioritization. |
| To Do | Todo: **4** | #31–34 have real assignees, but explicit pending PO approval, unassigned PO priorities, and unconfirmed proposed ownership. They are not ready to start under this gate. |
| In Progress | **3** | #28–30 have assigned Samanvi and shared/local progress evidence. #29–30 retain incomplete personal/review requirements; a linked development PR is missing. In Progress is appropriate while those requirements remain unfinished. |
| In Review | Testing: **2** | #10–11 are closed on GitHub but still Testing on the project. No recorded review deployment, presentation, or authorized final acceptance; full review gate is not verified. |
| Done | **6** | #1, #5–9 have no identifiable authorized final acceptance record in descriptions/comments. Five remain OPEN; only #9 is CLOSED. Closure is a consistency flag, not the acceptance criterion itself. |

Total: **41 = 26 + 4 + 3 + 2 + 6**. No Priority field exists in the current project field list. A numeric board field is optional, but a **PO-approved weighted priority/rationale** must be visible in each ready issue. All 20 #42 product scopes still explicitly await PO approval; 16 are Backlog and four are Todo. Only four have GitHub assignees; all 20 proposed owner confirmations remain pending.

## Specific placement and evidence corrections

Links below refer to `samanviy17-crypto/team-portfolio`. All changes are recommendations for later authorization.

| Issues / current placement | Exact proposed correction |
| --- | --- |
| [#31](https://github.com/samanviy17-crypto/team-portfolio/issues/31), [#32](https://github.com/samanviy17-crypto/team-portfolio/issues/32), [#33](https://github.com/samanviy17-crypto/team-portfolio/issues/33), [#34](https://github.com/samanviy17-crypto/team-portfolio/issues/34): Todo | Recommend return to **Backlog** while PO approval/weighted priorities/confirmed owners remain pending. Preserve Joan/Ainsley assignments, technical baseline screenshots, original checklists, comments, and split-scope links. Do not imply assignment grants implementation approval. |
| [#1](https://github.com/samanviy17-crypto/team-portfolio/issues/1), [#6](https://github.com/samanviy17-crypto/team-portfolio/issues/6): Done, OPEN | Empty bodies have substantial ideation/plan comments. Link those comments rather than replacing them; define the actual documentation deliverable and reviewer. Record real acceptance if it exists; otherwise propose Backlog/design-documentation review, not accepted product delivery. |
| [#5](https://github.com/samanviy17-crypto/team-portfolio/issues/5): Done, OPEN | Its lesson comment contains peer feedback and revisions, but not final authorized acceptance/delivery. Classify as **learning/lesson evidence**, outside product-delivery counts. Ask for teacher acceptance evidence before keeping an accepted label; do not discard peer feedback or close automatically. |
| [#7](https://github.com/samanviy17-crypto/team-portfolio/issues/7), [#8](https://github.com/samanviy17-crypto/team-portfolio/issues/8), [#9](https://github.com/samanviy17-crypto/team-portfolio/issues/9): Done | Implementation/test summaries are present, but no source/test/review URLs or acceptance record in the issue bodies/comments. Add exact scope/SHA, commits, PR, dated tests, review environment, presentation, and reviewer decision. Recommend In Review only when review prerequisites are evidenced; unfinished approved work belongs In Progress. If historical delivery was genuinely accepted, retain Done with that evidence and track newer work separately. Do not treat later production defects as proof earlier acceptance never occurred. |
| [#10](https://github.com/samanviy17-crypto/team-portfolio/issues/10), [#11](https://github.com/samanviy17-crypto/team-portfolio/issues/11): Testing, CLOSED | After the label decision, retain as In Review pending missing review evidence, or distinguish accepted local-only historical scope from unresolved production work. #10 explicitly lists concurrency, SMTP, and production configuration limitations. #11’s criteria specify local recovery. Do not add production acceptance retroactively. Reopen only if unfinished work belongs to that issue’s actual scope and a later change is authorized. |
| [#29](https://github.com/samanviy17-crypto/team-portfolio/issues/29), [#30](https://github.com/samanviy17-crypto/team-portfolio/issues/30): In Progress | Keep there. Existing published code/screenshots/tests are useful; missing linked PR/reviewer acceptance and personal explanation/practice/reflection prevent completion. Preserve checked technical accomplishments. Clearly label older “not pushed” passages as dated history where later published evidence supersedes them. No PR currently documents this work in this repository. |
| [#28](https://github.com/samanviy17-crypto/team-portfolio/issues/28): In Progress | Keep as an individual learning/CPT umbrella; it is not an additional product-delivery scope. Show child progress and pending individual evidence separately. |
| [#3](https://github.com/samanviy17-crypto/team-portfolio/issues/3): Backlog | Existing comments establish motivation, feature ideas, and team roles, not a completed stakeholder meeting/interview. Link genuine research/design evidence or leave the corresponding checks pending. |

Repository PR inspection found only **#4, closed without merge**, for team members. No development PR was found for the above implementation issues. Direct commit evidence is still useful, but it does not satisfy the requested PR gate. Do not invent historical PRs or create empty PRs merely to satisfy a checkbox; arrange a real review of the applicable changes when authorized.

## Backlog design-thinking completion

For each of the 20 proposals in [#42](https://github.com/samanviy17-crypto/team-portfolio/issues/42):

- Keep current stories, research, expected outcomes, acceptance criteria, dependencies, owners, and pending PO decision sections.
- Add a **Design thinking evidence** section: actual meeting/date/participants and outcome; interview/survey or cited needs; POV; HMW; alternatives; proposed design/sketch/API contract and acceptance criteria.
- Shared stakeholder records may be linked from multiple issues, with a sentence explaining relevance. Do not fabricate interviews or repeat the same source as 20 independent meetings.
- Each item’s **ready for prioritization** decision stays pending until the solution is understood; Backlog can legitimately hold immature items.
- Before promotion to To Do, record PO scope decision/date/conditions, weighted priority and rationale, confirmed accountable owner, and dependency readiness. Proposed owners in #42 are not confirmed assignments.

The remaining 16 proposals already correctly stay Backlog: **#12–18, #20–22, #24–25, #38–41**. #31–34 are the four misplaced proposals described above. #19 is an off-board duplicate/reference of canonical #20; preserve history and link the canonical item rather than adding duplicate delivery work. #2 is an empty off-board ideation issue, not a ready product scope.

## Keep product delivery distinct from evidence

The board’s 41 cards comprise **20 product proposals + 9 historical implementation/planning/lesson cards (#1, #3, #5–11) + 12 documentation/learning/evidence cards (#23, #26–28, #35–37, #42–44, #29–30)**. Classification reflects present scopes, not whether historical work was valuable.

Recommended later board organization: add an approved **Work type** field/labels and filtered views for **Product delivery**, **Learning/CPT**, and **Documentation/evidence**. Keep existing cards/history intact. Product proposal count stays 20; do not count #42, #43, #44 or a personal reflection as extra product features.

Current Backlog documentation cards **#23, #26, #27, #35–37, #42–44** should keep their present statuses until owners/reviewers decide actual progress. Their Backlog placement does not prove no documentation work occurred. #44 still has unchecked rubric, personal, and stakeholder requirements; #37 has pending reflections. Neither should become Done because shared engineering tests pass.

## Capstone versus board inconsistencies

- **Local redesign:** correctly explains five stages, weighted priority/owner, code/unit tests/PR, review environment/system tests/presentation/acceptance, and accepted delivery. These are the target rules, not demonstrated board compliance. Add an explicit current-board mapping/status note until the approved corrections occur.
- **Published capstone:** still shows the earlier three-step iteration process and does not yet include the prepared five-stage/Kanban redesign. Local preparation is not publication; any capstone update requires separate authorization and maintainer review.
- **Counts and scope:** the nine original capstone improvement areas are not the same as the 20 subsequent investigation/repair scopes. Link #42 and explain that proposals refine inherited/local functionality; do not relabel nine original areas as nine accepted features.
- **Stale claims:** #16’s dependency text refers to “completed #10/#30 work,” although #30 remains In Progress and #10 has unresolved limits. Clarify **completed technical baseline only; issue-level acceptance pending**. Likewise distinguish historical SCSS migration (#9) from subsequent approved auth/profile indented `.sass` changes.
- **Local tests versus review gate:** 158 passing backend tests and account/analytics browser evidence in the existing release packet support technical verification. They do not establish PO approval, production SMTP/CORS/persistence, student-only CPT completion, presentation, or final acceptance. Keep those local packets separate from already published issue evidence.

## Recommended board configuration — not executed

1. Rename **Testing → In Review**, keeping the existing option ID/cards/history; rename **Todo → To Do** for matching terminology. Keep **Backlog**, with “Parking Lot” explained in its description. Order columns **Backlog → To Do → In Progress → In Review → Done**. Teacher/board-owner approval required.
2. Define In Review as **deployed to an approved review environment + system testing + presentation + authorized acceptance**, not only QA. An approved local review environment may qualify if explicitly agreed; public production is not automatically required by the wording.
3. Add visible **Priority** and **Work type** fields only after permission; preserve existing Assignees. Record weighted rationale and PO approval in issues even if no new fields are approved.
4. Review any project workflows/automatic closures before enabling new rules. Do not let issue close/merge automatically certify acceptance. Automation behavior was not established by the field/item snapshot and must be checked before configuration changes.
5. Preserve acceptance scope: closed status, project Done, and public deployment are independent signals. Align them only after an actual scope/reviewer decision, not by bulk closing all Done cards or moving all closed cards to Done.

## Exact proposed issue evidence block

Use the existing Quick/Formal templates rather than replacing issue descriptions or screenshots. Append this only where missing, after documentation-edit approval:

```markdown
## Workflow evidence and decisions
- Work type / exact scope: pending confirmation.
- Stakeholder meeting + needs/POV/HMW/design links: pending.
- PO scope decision / weighted priority / rationale / date: pending.
- Accountable owner / confirmation: pending.
- Development commit(s) / PR: pending.
- Unit tests: source SHA, environment, date, expected/actual, result, evidence URL.
- Review environment / reviewed revision: pending.
- System tests / presentation / feedback: pending.
- Authorized acceptance: reviewer, decision, date, criteria and remaining limits — pending.
- Delivery evidence / retained commit and PR links: pending.
```

Replace “pending” only with actual evidence, keep unchecked requirements unchecked, and preserve all comments/screenshots and accepted historical scope. Quick issues may omit inapplicable fields but cannot bypass the 20-proposal PO approval gate.

## Ordered action plan for later approval

1. Mr. Mortensen confirms stage mapping, acceptance rules, work-type separation, priorities, and scope/owner decisions. User authorizes the exact documentation/board edits.
2. Append evidence/clarifications; link existing records rather than duplicating or rewriting history. Reconcile six Done cards and two closed Testing cards with their actual owners/reviewers.
3. Apply approved label/order changes; propose moving #31–34 to Backlog until ready. Make other moves individually only after their evidence supports the destination.
4. Review capstone wording and templates against the corrected board, then authorize any publication separately. No implementation or deployment is authorized by organizing the board.

See [ISSUE-INVENTORY.csv](ISSUE-INVENTORY.csv) for all 43 issues, current states/owners, and proposed dispositions. No remote changes were made.

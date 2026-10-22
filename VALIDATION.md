# PNEC capstone combined validation — October 22, 2026

Source commit: `f358db0c66112732d35e7c2ade8b70fe986d54af`. Upstream base: `97d3d9451`. These are local results; GitHub Actions is verified separately on the PR. This evidence-only branch contains no application code or deployment workflows and is not a merge target.

- **Jekyll/Sass: PASS**, Jekyll completed in **89.994 seconds**. [Build record](build-result.json). Command: `make -o clean build PYTHON=/Users/samanviyachareni/pages/venv/bin/python3`. Only the global stop/clean prerequisite was skipped in this new worktree to protect other previews; distribution, conversions, Sass generation, Jekyll clean/build ran. Existing unrelated deprecation warnings remain. All 18 compiled CSS files exclude legacy `.pnec-capstone` rules.
- **Kanban tests: 25 passed, 0 failed**. [Actual test output](kanban-tests.log). Command: `node --test tests/kanban_board.test.mjs` using Node 24.21.0 bundled with the local Playwright runtime.
- **15 browser layout/theme combinations passed** at 320/390/768/1024/1440px with the actual Site Default, Light and Midnight presets. No horizontal overflow; mobile single-column and desktop two-column feature grids. [Results](browser-results.json), [test script](browser-check.py).
- **Shared Kanban fallback:** actual YAML URL/title rendered, personal-board message visible, card mount hidden, no fabricated board/cards, zero GitHub API requests. Real link and noscript notice remain visible with JavaScript disabled. [Mobile capture](board-Midnight-390.png).
- **Microblog smoke check:** one panel, keyboard open/close passed with an empty GET fixture and external services blocked. Production posting/authentication/persistence not tested.
- **Links: 21 external URLs returned HTTP 200**; fragment/local destinations passed. [Link results](external-links.json). No static-resource failures. The inherited shared-shell `undefined/api/id` 404 remains recorded separately.
- **Content/partial:** all nine proposals, acceptance criteria, five stages, links, team, permalink and Microblog preserved. Legacy Sass partial matches upstream byte-for-byte, remains unimported, and is absent from the PR diff. [Content assertions](content-checks.json).

No production accounts/data, project configuration, backend, or infrastructure were accessed or changed. No accessibility certification or live-board claim is implied by the layout checks.

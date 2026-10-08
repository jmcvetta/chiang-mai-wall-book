# Inventory stage handoff

- Stage: provisional full-circuit inventory and initial source register (issue #3).
- Status: complete for owner review. Every record is unreviewed and provisional.
- Next action: the owner's plausibility check (issue #4), using the questions below.

## Inputs

| Input | Revision |
| ----- | -------- |
| Planning document | `PLANNING.md` at 08dd2d2fcc31187b47b829b1e97906419bf0dc57 (branch `initial`) |
| Repository base | `master` at 96e3db15b91945314f6f23bd866456300018723d |
| Operational procedure (issue #2) | Not available. No procedure file existed at the base revision. This run followed the planning document directly. |
| OpenStreetMap | API 0.6 `map` call, retrieved 2026-10-08. Element versions are in the extract. |
| Satellite imagery | Esri World Imagery, image date 2026-01-10 (WV03, release 2026.R09). Viewed, not stored. |

## Outputs

| Path | What it is |
| ---- | ---------- |
| `research/inventory/inventory.md` | Clockwise list, route coverage, candidate records, observations, limits |
| `research/inventory/inventory-map.svg` | North-up route map |
| `research/inventory/inventory-map.geojson` | Candidate outlines, schematic reaches and photo points behind the map |
| `research/inventory/handoff.md` | This file |
| `research/inventory/discovery/discovery-thai.md` | Thai-language discovery log (worker output) |
| `research/inventory/discovery/discovery-other-languages.md` | English and other-language discovery log (worker output) |
| `research/inventory/discovery/discovery-images-and-maps.md` | Dated image and historic map discovery log (worker output) |
| `research/shared/sources/register.md` | Source register |
| `research/shared/names.md` | Place-name glossary |
| `research/shared/chronology.md` | Attributed dating statements; no established dates |
| `research/materials/osm/old-city-walls-gates-moat-2026-10-08.geojson` | OpenStreetMap extract (ODbL) |
| `research/materials/RIGHTS.md` | Rights record |

The inventory and map filenames are a local choice for this stage. The planning document's proposed `research/shared/` layout is used for the register, glossary and chronology.

The SVG was rendered from the two GeoJSON files by a one-off script that is not in the repository. The GeoJSON files are the data of record; the SVG is a view of them.

## For the owner: what to check

This asks for a plausibility check, not an expert survey or a walk. Open the map and the clockwise list in `inventory.md`, then say whether anything below looks wrong.

1. Are the nine stops the places you would expect to see on a walk round the moat: five gates and four corners?
2. Is anything you know of missing? In particular, any stretch of wall between the stops, or any brick or stone moat bank.
3. Do the names read sensibly? Two need a choice: Chaeng Katam (several Thai spellings) and Saen Pung Gate (also called Suan Prung Gate).
4. At Chaeng Hua Lin, one record covers the corner and a run of wall about 300 m long to its east. Does that look like one thing or two?
5. Should the outer earthen wall (กำแพงดิน) and its surviving corner (แจ่งหายยา) be in the book at all? They are outside the moat circuit and outside this inventory.

Your answers are a workflow approval. They are not evidence for any claim in the book.

## Findings that matter for the pilots

- The visible wall fabric is concentrated at the gates and corners. No wall fabric was seen between them in the 2026-01-10 image.
- At Chang Phueak Gate, a Fine Arts Office 7 official was reported in 2022 as saying the outer wall face was built in the early 2500s over an older wall. That is the clearest evidence so far that a "gate" record holds more than one phase.
- Tha Phae Gate has the most dating statements, all pointing to a 1980s rebuilding, but the sources disagree on the year.
- No source dates any moat bank lining. Both banks are unexamined almost everywhere.

## Missing inputs

- Human dated observations of every stop and both banks.
- Fine Arts Department conservation and excavation reports; the 1935 registration notice and its extent.
- Hans Penth, *A Brief History of Lanna* (and other monographs) for the c. 1800 campaign.
- The UNESCO tentative-list text and the 2026 nomination dossier (HTTP 403 to automated fetches).
- Viewing the dated Commons photographs listed per stop (rate-limited) and the 1893 and 1945 maps.

## Run record

| Item | Value |
| ---- | ----- |
| Coordinator | Claude Code session https://claude.ai/code/session_01JmVDKakZiBU9Wp5rXzDMJE, model claude-opus-5-5 |
| Discovery workers | Three parallel subagents, model class `sonnet`, one per stream (Thai; other languages; images and maps). Each had a bounded budget of about 25 searches and 30–40 fetches and wrote only its own file. |
| Worker usage, as reported by the harness | Thai: about 118k tokens, 48 tool calls. Other languages: about 103k tokens, 47 tool calls. Images and maps: about 105k tokens, 47 tool calls. Coordinator usage was not measured. Cost in money was not available. |
| Coordinator work | OSM extraction; satellite-image reading at nine stops and nine stretches; overlay of OSM outlines on the image at three stops; viewing two dated photographs; raw-text verification of the consequential quotes; integration of the register, glossary, chronology and inventory. |
| Verification of worker quotes | The workers' fetch tool returns summarised text. The coordinator re-fetched ten pages and matched the passages used in the register against raw page text (marked `raw` in the register). Other worker quotes remain `extractor`. |
| Failed or limited fetches | whc.unesco.org: 403. web.archive.org: blocked for the workers' tool. Wikimedia API: 429 (rate limit); Commons file downloads intermittently 429. Overpass API: connection reset; the OSM main API was used instead. silpa-mag.com, gotoknow.org, matichon.co.th, thairath.co.th: 403. Chulalongkorn repository: 503. Esri imagery export: HTTP 500 for any request finer than about 0.3 m per pixel. |
| Rejected or corrected worker readings | The Thai worker could not place "แจ่งหายยา"; the raw Thai Wikipedia text places it on the outer wall, about 600 m south of Chaeng Ku Hueang. The other-language worker recorded the Chang Phueak Monument article's "last renovated in 1995" as a wall claim; the register marks it as ambiguous and does not use it for the city wall. |
| Frontier escalation | None proposed. The open questions (phase counts, dates, bank materials) need documents and ground observation, not a more capable model. |

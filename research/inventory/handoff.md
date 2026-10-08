# Inventory stage handoff

```text
section:        shared (inventory stage)
stage:          inventory correction: segment-by-segment re-examination of the nine wall candidates (issue #23)
status:         draft
input revision: master 0c91685bd4188b294aada082dc2d95a06033c75e (inventory, register, procedure, PLANNING.md); owner photographs 39c8cb77b33ce8d8e46296a658aaa941c85bc894
outputs:        research/inventory/evidence.md; research/inventory/inventory.md; research/inventory/inventory-map.geojson; research/inventory/inventory-map.svg; research/inventory/render_map.py; research/inventory/handoff.md; research/shared/sources/register.md; research/materials/owner-photos/2026-10-08-chang-phueak-east-wing-border.md (integration note). Inputs carried on this branch, not written by this run: the two owner photographs and the RIGHTS.md rows for them (39c8cb7).
sources used:   esri-world-imagery-wv3-2026-01-10 (zoom-19 tiles, evidence.md I1–I11); owner observations and photographs (evidence.md O1–O4); osm-api-2026-10-08
missing inputs: every Wikimedia Commons photograph listed per stop (HTTP 429 on every image request, 2026-10-08); human dated observations of every stop except the Chang Phueak east wing
next recipient: editorial owner
next action:    check whether the Chang Phueak Gate split on the map matches what you see (question 1 below)
```

## Correction run, issue #23

The owner's plausibility review (#4) failed the inventory: at Chang Phueak Gate each wing has visibly different sections, and the map drew each wing as one block. This run re-read all nine stops segment by segment in zoom-19 imagery, recorded the owner's observations and photographs, and split records where a boundary could be seen and placed.

| Stop | Result | Basis |
| ---- | ------ | ----- |
| 1 Chang Phueak Gate | Split into four: 1a, 1b (west wing), 1c, 1d (east wing) | I1, I2; owner O1–O4 |
| 2 Chaeng Si Phum | Kept composite | I3; canopy over more than half |
| 3 Tha Phae Gate | Kept composite | I4, I5 |
| 4 Chaeng Katam | Kept composite; boundary note (corner lobe) | I6 |
| 5 Chiang Mai Gate | Kept composite; boundary note (possible pier) | I7 |
| 6 Saen Pung Gate | Left unresolved: not readable, no photograph viewable | I8 |
| 7 Chaeng Ku Hueang | Split into two: 7a, 7b | I9 |
| 8 Suan Dok Gate | Kept composite; fabric now partly confirmed | I10 |
| 9 Chaeng Hua Lin | Kept composite; boundary seen under canopy, not placed | I11 |

No Commons photograph could be viewed (HTTP 429 on every image request). The splits rest on the agent's imagery reading and, at Chang Phueak, on the owner's observations and photographs. No new dating claim was made. The map is now rendered by `render_map.py` from the GeoJSON.

## For the owner: what to check now

1. **Chang Phueak Gate first.** Open the map's inset. Each wing is now two sections: a straight-edged block beside the gate (1b, 1c) and a ragged run beyond it (1a, 1d). The boundaries are at 37 m from the west end of the west wing and 17.5 m from the gate end of the east wing. Does that match what you see? You said there may be up to three sections per side. If so, where is the third, and can you photograph it?
2. **Chaeng Ku Hueang.** The east run looks wider and straighter in its last 19 m (7b). Does that match the ground? A photograph of that join would settle it.
3. **Corners.** At Chaeng Katam, Chaeng Ku Hueang and Chaeng Hua Lin the corner's flat or rounded top looks different from the runs from above. This run did not split a corner from its runs on that alone, because it may be a platform top rather than different masonry. Do the corners look like different construction from the walls beside them?
4. **Anything else you have seen.** Chaeng Si Phum, Tha Phae, Chiang Mai, Saen Pung and Suan Dok gates are mostly under trees or in shadow from above. Any photograph showing a visible join along their walls would help. None is required.
5. Questions 2, 3 and 5 from the earlier list below still stand. Question 4 (Chaeng Hua Lin, one thing or two) is now: the east run seems to change along its length under the trees; where, if you know?

Your answers are a workflow approval and owner observations. They are not evidence for any claim in the book.

## Run record

```text
run id:             2
process version:    docs/research-procedure.md and PLANNING.md at 0c91685bd4188b294aada082dc2d95a06033c75e
input commits:      0c91685bd4188b294aada082dc2d95a06033c75e; 39c8cb77b33ce8d8e46296a658aaa941c85bc894
output paths:       research/inventory/evidence.md; research/inventory/inventory.md; research/inventory/inventory-map.geojson; research/inventory/inventory-map.svg; research/inventory/render_map.py; research/inventory/handoff.md; research/shared/sources/register.md; research/materials/owner-photos/2026-10-08-chang-phueak-east-wing-border.md
roles and models:   coordinator, imagery reader and integration: claude-opus-5-5 (Claude Code 2.1.294, session https://claude.ai/code/session_01B9iPhbgxLo95tSL22vv4nw); orchestrator: claude-fable-5-1 (session https://claude.ai/code/session_015qm2XbEoqVgzqF9HSjP8ps); owner: observations and photographs
outstanding work:   view the Commons photographs listed per stop (rate-limited); owner check of the Chang Phueak and Ku Hueang splits; ground photographs for the stops under canopy; the Commons leads listed in inventory.md
defects found:      run 1 read each wing at Chang Phueak Gate as one block although the imagery shows the split (owner finding, #4); run 1 left the map render script out of the repository; Wikimedia returned HTTP 429 for every image in both runs
changes since last: Chang Phueak Gate and Chaeng Ku Hueang split; boundary notes at Chaeng Katam, Chiang Mai Gate and Chaeng Hua Lin; Suan Dok fabric partly confirmed; no claim invalidated, because no claim was linked to a section
usage:              not measured
frontier:           none
```

---

## Previous run: issue #3

- Stage: provisional full-circuit inventory and initial source register (issue #3).
- Status: complete for owner review. Every record is unreviewed and provisional.
- Next action: the owner's plausibility check (issue #4), using the questions below.

### Inputs

| Input | Revision |
| ----- | -------- |
| Planning document | [`PLANNING.md` at 08dd2d2](https://github.com/jmcvetta/chiang-mai-wall-book/blob/08dd2d2fcc31187b47b829b1e97906419bf0dc57/PLANNING.md) (branch `initial`; not on `master`) |
| Repository base | `master` at 96e3db15b91945314f6f23bd866456300018723d |
| Operational procedure (issue #2) | Not available. No procedure file existed at the base revision. This run followed the planning document directly. |
| OpenStreetMap | API 0.6 `map` call, retrieved 2026-10-08. Element versions are in the extract. |
| Satellite imagery | Esri World Imagery, image date 2026-01-10 (WV03, release 2026.R09). Viewed, not stored. |

### Outputs

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

### For the owner: what to check

This asks for a plausibility check, not an expert survey or a walk. Open the map and the clockwise list in `inventory.md`, then say whether anything below looks wrong.

1. Are the nine stops the places you would expect to see on a walk round the moat: five gates and four corners?
2. Is anything you know of missing? In particular, any stretch of wall between the stops, or any brick or stone moat bank.
3. Do the names read sensibly? Two need a choice: Chaeng Katam (several Thai spellings) and Saen Pung Gate (also called Suan Prung Gate).
4. At Chaeng Hua Lin, one record covers the corner and a run of wall to its east; together their outline spans 313 m east–west. Does that look like one thing or two?
5. Should the outer earthen wall (กำแพงดิน) and its surviving corner (แจ่งหายยา) be in the book at all? They are outside the moat circuit and outside this inventory.

Your answers are a workflow approval. They are not evidence for any claim in the book.

### Findings that matter for the pilots

- The visible wall fabric is concentrated at the gates and corners. No wall fabric was seen between them in the 2026-01-10 image.
- At Chang Phueak Gate, a Fine Arts Office 7 official was reported in 2022 as saying the outer wall face was built "ช่วงต้นปี 2500" (literally "early in [the year] 2500"; era not written) to cover an older wall line. That is the clearest evidence so far that a "gate" record holds more than one phase.
- Tha Phae Gate has the most dating statements, all pointing to a 1980s rebuilding, but the sources disagree on the year.
- No source dates any moat bank lining. Both banks are unexamined almost everywhere.

### Missing inputs

- Human dated observations of every stop and both banks.
- Fine Arts Department conservation and excavation reports; the 1935 registration notice and its extent.
- Hans Penth, *A Brief History of Lanna* (and other monographs) for the c. 1800 campaign.
- The UNESCO tentative-list text and the 2026 nomination dossier (HTTP 403 to automated fetches).
- Viewing the dated Commons photographs listed per stop (rate-limited) and the 1893 and 1945 maps.

### Run record (run 1)

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

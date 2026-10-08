```text
section:        shared (inventory stage; nine wall candidates)
stage:          inventory correction, segment-by-segment re-examination (issue #23)
status:         draft
input revision: master 0c91685bd4188b294aada082dc2d95a06033c75e; owner photographs 39c8cb7 (merged into this branch)
outputs:        research/inventory/evidence.md
sources used:   esri-world-imagery-wv3-2026-01-10 (zoom-19 tiles listed per entry); owner-photo-2026-10-08-cp-east-1, owner-photo-2026-10-08-cp-east-2; owner-obs-2026-10-08-issue4-a, owner-obs-2026-10-08-issue4-b; osm-api-2026-10-08
missing inputs: every Wikimedia Commons photograph listed for the nine stops (HTTP 429 on every image request; see "Failed fetches"); human dated observations of eight of the nine stops
next recipient: editorial owner
next action:    check the Chang Phueak Gate split against what you see on the ground (handoff.md, question 1)
```

# Segment-by-segment evidence, nine wall candidates

Status: **unreviewed research staging.** Recorded 2026-10-08 for issue #23. Every reading of imagery below was made by an AI model (the implementing agent, model claude-opus-5-5). It is a remote interpretation, not a field observation. Owner observations are marked as such. They are workflow input, not specialist review and not historical evidence.

Nothing here dates any fabric. "Ragged" and "square" describe what the image shows from above: edge straightness, top-surface regularity, width and shadow. They do not mean old or new.

## Method

### Overhead imagery

- Service: Esri World Imagery tiles, `https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/19/{y}/{x}`, zoom 19 (about 0.28 m per pixel at this latitude).
- Retrieval: 2026-10-08, between 17:12 and 17:14 UTC.
- Image date: the service's `identify` call (layer 2) returned `SRC_DATE2` 1/10/2026, resolution 0.31 m, accuracy 8.47 m and description "Vivid Mosaic Metro" at a point in each of the nine stops, queried 2026-10-08. The tiles themselves carry no date. That they show the 2026-01-10 image is an inference from the metadata, not read from the tiles.
- Processing: the tiles covering each OSM way plus about 18 m of margin were stitched, cropped, auto-contrasted (1 % cut-off) and enlarged with nearest-neighbour scaling (4×; 1× for Chaeng Hua Lin, then 4× sub-crops). The OSM outline was drawn on one copy, with ticks every 10 m along the long axis measured from the outline's west or north end. A plain copy was read alongside it. No tile or crop is stored in the repository; Esri's terms do not clear them for redistribution.
- Distances in the entries are along the outline's long axis (west–east or north–south), from the stated end, read off the tick scale. A boundary position is the agent's judgement of where the change in edge, width or tone occurs. Its stated accuracy covers that judgement only. It does not include the image's 8.47 m absolute accuracy, or the few-metre offset between the OSM outline and the visible fabric noted in the inventory.
- Tile indices are zoom-19 indices. The orchestrator's comment on #23 gives a centre tile x=812607 y=468533 for the same place; those values are about twice the zoom-19 indices used here and may be zoom-20 numbering. This run did not reproduce that read.

### Dated photographs

- Every Wikimedia Commons file page listed in the inventory records was fetched (HTTP 200). Every request for the image itself, at `upload.wikimedia.org`, returned HTTP 429 with `retry-after: 600`. See "Failed fetches". No Commons photograph was viewed in this run.
- The two owner photographs (39c8cb7) were viewed.
- Search for drone or elevated photographs: see "Photograph search".

## Owner observations

```text
id:               O1
source:           owner-obs-2026-10-08-issue4-a locator: https://github.com/jmcvetta/chiang-mai-wall-book/issues/4#issuecomment-6064637049 (2026-10-08)
original wording: recorded by the orchestrator from chat: "Each side has two very visibly different sections, older and newer. The older sections may not all be from one era. There may be as many as three sections per side."
translation:      original
subject:          Chang Phueak Gate, both wings (OSM ways 24871597, 97191493)
scope:            the owner's statement; whether from memory, a visit or imagery is not stated
observation date: 2026-10-08 retrieval date: 2026-10-08
limits:           owner observation, relayed. Not specialist review; not evidence of any date. "Older" and "newer" are the owner's words.
lineage:          independent
```

```text
id:               O2
source:           owner-obs-2026-10-08-issue4-b locator: https://github.com/jmcvetta/chiang-mai-wall-book/issues/4#issuecomment-6064700401 (2026-10-08)
original wording: "You can see the restored section is quite square, whereas the older section is uneven and ragged."
translation:      original
subject:          Chang Phueak Gate, west wing (OSM way 24871597)
scope:            the owner's reading of an enlarged zoom-19 Esri crop shown by the orchestrator
observation date: 2026-10-08 (reading); image date not read from the tiles retrieval date: 2026-10-08
limits:           owner reading of the same imagery as I1. "Restored" and "older" are the owner's words, not sourced claims.
lineage:          same imagery as I1; the reading is independent of the agent's
```

```text
id:               O3
source:           owner-photo-2026-10-08-cp-east-1 locator: research/materials/owner-photos/2026-10-08-chang-phueak-east-wing-border-1.jpg
original wording: not applicable (photograph)
translation:      none
subject:          Chang Phueak Gate east wing, viewed from the south across Sri Phum Road
scope:            camera at North Gate Jazz Co-op (OSM node 2110312355, 18.79519, 98.98700), as stated by the owner; accuracy "at or near the club"
observation date: 2026-10-08 23:52:48 local (EXIF) retrieval date: 2026-10-08
limits:           night photograph, artificial light. Agent's reading: from left, the gate's arched structure, the road gap, a tall crenellated block of evenly coursed brick under a large tree, then a much lower run of brick with no crenellation running east to the right edge of frame. The east end of the low run is out of frame.
lineage:          independent (owner)
```

```text
id:               O4
source:           owner-photo-2026-10-08-cp-east-2 locator: research/materials/owner-photos/2026-10-08-chang-phueak-east-wing-border-2.jpg
original wording: not applicable (photograph); sign in frame reads "ห้ามปีนโบราณสถาน / Please do not climb on the historical ruins"
translation:      sign's own English
subject:          Chang Phueak Gate east wing, the join between the crenellated block and the low run
scope:            same camera position as O3
observation date: 2026-10-08 23:52:54 local (EXIF) retrieval date: 2026-10-08
limits:           agent's reading: the crenellated block ends in a squared corner; its face stands forward (toward the road) of the low run. The low run is about half the block's height, with uneven courses and a ragged top. The change is abrupt at the block's corner. Owner's statement (record file): this is the section border.
lineage:          independent (owner)
```

## Overhead imagery, stop by stop

Image date for every entry: 2026-01-10 (see Method). Retrieval date for every entry: 2026-10-08. Source key for every entry: esri-world-imagery-wv3-2026-01-10. Lineage: one image, read once by the agent.

### 1. Chang Phueak Gate

```text
id:               I1
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406302–406303, y 234266
subject:          west wing, OSM way 24871597 (outline span 54 m west–east)
observation:      0–37 m from the west end: a dark band whose moat-side edge wanders, with a mottled top and a broken shadow line. 37–54 m (to the gate opening): a crisp dark rectangle with two straight parallel edges and a sharp straight shadow on the road side; it is wider than the band to its west and has a lighter strip along its top.
boundary:         at 37 m from the west end (98.98630 E), ± 3 m along the outline
limits:           cannot say whether the 0–37 m stretch is itself more than one thing (O1 allows up to three sections per side); no second change is clear enough to place at this resolution.
```

```text
id:               I2
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406303–406304, y 234266
subject:          east wing, OSM way 97191493 (outline span 41 m west–east)
observation:      0–17.5 m from the west (gate) end: under tree canopy; only the straight road-side edge and shadow of a block show at the canopy's south edge. At about 17.5 m the road-side edge steps back north. 17.5–41 m: a narrower, lighter, uneven band with a ragged moat-side edge to the east end.
boundary:         at 17.5 m from the west end (98.98692 E), ± 3 m along the outline; placed from the step in the road-side edge and checked against O3 and O4, which show the block's east corner at the same relative position
limits:           the canopy hides the top of the block; the boundary rests on the edge step and on the owner photographs
```

### 2. Chaeng Si Phum

```text
id:               I3
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406312–406314, y 234266–234267
subject:          corner and runs, OSM way 263459882
observation:      the corner tip at the moat shows uneven reddish-brown fabric. The south run along the east moat shows as a narrow dark band with a lighter strip in its last 20 m. Most of the corner and both runs are under heavy canopy.
boundary:         none visible
limits:           canopy hides more than half the outline; a boundary under it cannot be excluded
```

### 3. Tha Phae Gate

```text
id:               I4
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406313, y 234277–234278
subject:          north run, OSM way 263464175 (66 m north–south)
observation:      along the whole length: a straight band with a light top strip and a regular toothed shadow on its east side, consistent with crenellation. No change in width, tone or shadow pattern along the run.
boundary:         none visible
limits:           none beyond the plan view
```

```text
id:               I5
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406313, y 234278–234279
subject:          south run, OSM way 263464174 (95 m north–south)
observation:      0–about 35 m from the north end: a narrow dark band with straight edges; no toothed shadow like the north run's. About 35–95 m: under canopy.
boundary:         none visible
limits:           canopy hides about two-thirds of the run. The north run (I4) and the visible part of this run differ in shadow pattern, but they are already separate outlines either side of the gate; no boundary within either run is visible.
```

### 4. Chaeng Katam

```text
id:               I6
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406312, y 234287–234288
subject:          corner, OSM way 791602197
observation:      a curved dark band along the city side of the road (with a parallel inner line), straight dark arms north along the east moat and west along the south moat, and at the corner a lighter, uneven, reddish-brown area matching the outline's projecting lobe.
boundary:         a change in tone and texture at the corner lobe is visible. Not treated as a section boundary: from above it is consistent with the top surface of a corner platform against its parapets, which is a difference of form, not necessarily of fabric. See the inventory record's boundary note.
limits:           a plan view cannot distinguish a platform top from different masonry
```

### 5. Chiang Mai Gate

```text
id:               I7
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406306–406308, y 234287–234288
subject:          west block, OSM way 330870296 (23 m), and east block, OSM way 330870295 (41 m)
observation:      west block: a uniform rectangle in the shadow of buildings to the north; no change along it. East block: the first 5–6 m from the gate end show a light top bar; then about 6–13 m a lighter patterned top; east of about 13 m, deep shadow and canopy.
boundary:         none placed. The change at about 6 m in the east block may be the gate pier against the wall; it cannot be told apart in this image.
limits:           shadow and canopy hide about 28 m of the east block
```

### 6. Saen Pung Gate

```text
id:               I8
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406295–406297, y 234287–234288
subject:          west block, OSM way 1211639140 (27 m), and east block, OSM way 1211639141 (27 m)
observation:      both blocks are almost entirely in shadow from the north and under canopy. Only about the last 7 m of the west block at the gate end shows a top surface.
boundary:         none visible
limits:           not readable; no conclusion either way
```

### 7. Chaeng Ku Hueang

```text
id:               I9
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406290–406291, y 234286–234288
subject:          corner and runs, OSM way 317516851 (outline span 60 m west–east)
observation:      a rounded corner with a flat light-brown top, a narrow north run along the west moat (uneven edges, partly under canopy from about 20 m north of the corner), and an east run along the south moat. Along the east run, from the corner to about 41 m from the outline's west end: narrow, with uneven edges. At about 41 m a light cross-line crosses the run. From 41 m to the east end (about 60 m): a wider dark band with straight parallel edges and a straight shadow.
boundary:         at 41 m from the west end of the outline (98.97823 E), on the east run, ± 3 m
limits:           the light cross-line could be a path or gap rather than a joint. The rounded corner's flat top differs from both runs in form; that is not treated as a boundary (as at Chaeng Katam).
```

### 8. Suan Dok Gate

```text
id:               I10
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406291, y 234276–234277
subject:          south of the opening, OSM way 473546718 (45 m north–south), and north, OSM way 323670037 (18 m)
observation:      way 473546718: canopy over the north 32 m; the south 12 m show a dark rectangle with straight edges. Way 323670037: a rectangular block with straight edges and a partly vegetated top; no change along it.
boundary:         none visible
limits:           canopy hides most of way 473546718. This read confirms mapped fabric at two places where the earlier inventory could not confirm any.
```

### 9. Chaeng Hua Lin

```text
id:               I11
source:           esri-world-imagery-wv3-2026-01-10 locator: z19 tiles x 406291–406296, y 234265–234267
subject:          corner and runs, OSM way 317516852 (313 m west–east)
observation:      a rounded corner with a light top and a dark notch on its city side. South run (about 65 m): a uniform narrow dark band, no change along it. East run, measured from the outline's west end: to about 63 m a continuous dark band with a straight shadow; about 63–160 m under canopy; about 160–270 m an intermittent band with gaps; about 275–313 m a reddish, uneven band.
boundary:         changes are visible along the east run (continuous, then intermittent, then reddish and uneven), but the canopy between 63 m and 160 m hides where the first change happens. Not placed.
limits:           the corner's rounded top differs in form from the runs; not treated as a boundary (as at Chaeng Katam)
```

## Commons photographs: fetch record

All listed in the inventory records or found by the photograph search. File pages fetched 2026-10-08 17:17–17:20 UTC (HTTP 200). Image requests to `upload.wikimedia.org` returned HTTP 429, `retry-after: 600`. Each 429 is a failed fetch.

| File | Stop | Page | Image | Attempts (UTC, 2026-10-08) |
| ---- | ---- | ---- | ----- | -------------------------- |
| 201703291151b P Chiang Mai, City Wall, Chang Phuak Gate.jpg | 1 | 200 | 429 | 17:17 |
| Ancient city wall and Chang Phueak Gate in Chiang Mai.jpg | 1 | 200 | 429 | 17:17 |
| 201703291114c Chiang Mai, City Wall, Tha Phae Gate.jpg | 3 | 200 | 429 | 17:18 |
| 20171105 Tha Phae Gate Chiang Mai 9784 DxO.jpg | 3 | 200 | 429 | 17:18 |
| 201703291051a Chiang Mai, City Wall, Katam Corner.jpg | 4 | 200 | 429 | 17:18 |
| 201703291042a Chiang Mai, City Wall, Chiang Mai Gate.jpg | 5 | 200 | 429 | 17:18 |
| 201703281525c Chiang Mai, City Wall, Suan Prung Gate.jpg | 6 | 200 | 429 | 17:19 |
| 201703281534c P Chiang Mai, City Moat, Ku Ruang Corner.jpg | 7 | 200 | 429 | 17:19 |
| 201703291225a P Chiang Mai, City Wall, Saun Dok Gate.jpg | 8 | 200 | 429 | 17:19 |
| 201703291209c Chiang Mai, City Wall, Hua Lin Corner.jpg | 9 | 200 | 429 | 17:19, 17:21, 17:22 |
| 201703291143a P Chiang Mai, City Moat.jpg | reach 1–2 | 200 | 429 | 17:20 |
| 201703291126a Chiang Mai, City Moat.jpg | reach 2–3 | 200 | 429 | 17:20 |
| 201703291223c Chiang Mai, City Moat.jpg | reach 8–9 | 200 | 429 | 17:20 |
| Category:Si Phum Corner (24 files) | 2 | not fetched | not fetched | — |

A Commons API `imageinfo` query for the same files at 17:16 also returned 429.

A second paced pass, started after the `retry-after` period, fetched every file page again (17:39–17:44 UTC, HTTP 200) and requested every image once more, 8–10 seconds apart. Every image request returned HTTP 429 again. These second attempts are failed fetches too and are not listed per row above.

## Photograph search

Run 2026-10-08.

- Wikimedia Commons full-text file search (`Special:Search`, file namespace), terms "Chiang Mai aerial gate", "Chiang Mai drone wall", "Chang Phuak Gate", "Chang Phueak Gate". The first two returned no relevant file. The last two returned the files above plus: "201703291152b Chiang Mai, City Wall, Chang Phuak Gate.jpg"; a Flickr-derived series "Chang Phuak Gate (1)…(15)" (Flickr ids 12660842365–12661435954); "Chang Phueak Gate (1)…(3).jpg"; "ประตูช้างเผือก อ.เมือง จ.เชียงใหม่ (1)…(10).jpg"; three files "2014 0526 Thailand coup Chang Phueak Gate Chiang Mai 01–03.jpg". None was viewed (same 429). None is titled as aerial or drone. These are leads for a later pass.
- Flickr search page (`flickr.com/search/?text=`), terms "chiang mai gate drone" and "chiang mai old city wall aerial": the server-rendered results named no photograph of a gate or corner. Results rendered by script were not inspected.
- Web search, "Chang Phuak Gate Chiang Mai drone aerial photo flickr" and "commons.wikimedia.org Chiang Mai city wall aerial drone gate": no drone or elevated photograph of a gate or corner found. One lead: a 1963 aerial photograph held by Chiang Mai House of Photography, reported by the search tool as showing Tha Phae Road and Nawarat Bridge, not a gate. Not opened.
- Not searched: Mapillary; Google Earth (no browser in this run).

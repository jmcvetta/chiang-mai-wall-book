# Source register

Status: unreviewed research staging, started 2026-10-08 for issue #3 (provisional full-circuit inventory). This is not book content.

One entry per source. The key is a bibliographic key, not a section identity. Other records cite sources by key.

## How to read an entry

- **Access** says how far the source was taken:
  - `lead`: known from a citation or search result only. Not evidence.
  - `obtained`: the item itself was retrieved.
  - `inspected`: the passage named under **Passages** was read on the item itself.
- **Verification** says how the passage text was read:
  - `raw`: matched in the raw page text with a plain-text search. The wording is exact.
  - `extractor`: relayed by a summarising fetch tool. The wording is not guaranteed exact. Recheck before citing.
- **Lineage** names sources that probably copy each other. Copies are one witness, not several.
- Retrieval date is 2026-10-08 unless an entry says otherwise. A publication or observation date is given only where the source states one.
- Rights describe reuse of the item. Nothing in this register is cleared for reproduction in the book.

Worker discovery logs, with fuller search scope and the leads not followed, are in `research/inventory/discovery/`.

---

## Mapping and imagery

### osm-api-2026-10-08

- Title: OpenStreetMap data, API 0.6 `map` call, bbox 98.9775,18.7795,98.9995,18.7975
- Creator: OpenStreetMap contributors
- URL: https://api.openstreetmap.org/api/0.6/map?bbox=98.9775,18.7795,98.9995,18.7975
- Type: collaborative map database
- Access: obtained. Elements used are listed, with id, version and edit timestamp, in `research/materials/osm/old-city-walls-gates-moat-2026-10-08.geojson`.
- What it supports: the mapped position and outline of features tagged `barrier=city_wall`, `historic=city_gate` and `water=moat`, and their `name` tags. It does not support any date or phase.
- Accuracy: not stated per element. Some elements carry a `source` tag naming the imagery they were traced from (for example `Bing`, `Esri`).
- Rights: ODbL 1.0, attribution "© OpenStreetMap contributors". See `research/materials/RIGHTS.md`.

### esri-world-imagery-wv3-2026-01-10

- Title: Esri World Imagery, tile block `Vivid_Mosaic_30_Chiang_Mai_TH_26Q3`, release `Raster Basemaps 2026.R09`
- Creator: imagery source `Vantor`, sensor `WV03`, per the service's own metadata
- URL (metadata query used): https://services.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/identify (layer 2, queried at each of the nine stops)
- Type: dated satellite mosaic
- Access: inspected. The service's metadata gives, at all nine stops: `DATE (YYYYMMDD)` 20260110, `RESOLUTION (M)` 0.31, `ACCURACY (M)` 8.47.
- Observation date: 2026-01-10, as stated in the service metadata. This is the date of the image, not the retrieval date.
- Use in this inventory: plan-view reading of each stop and each reach by the coordinating agent (an AI model), not by a human observer. A plan view cannot show a vertical moat bank face.
- Rights: not cleared for reproduction. No image from this service is stored in the repository.

### commons-linge-2017

A series of photographs by Hartmann Linge on Wikimedia Commons, taken on 28 and 29 March 2017. Each file page states the date in its `Date` field and an EXIF "date and time of data generation" that agrees with it. Each file page states both CC BY-SA 4.0 (permission text) and CC BY-SA 3.0 (Licensing section); the page does not resolve the conflict. Requested credit: "© Hartmann Linge, Wikimedia Commons, CC-by-sa 4.0". Not cleared for the book; no copy is stored in the repository.

Files used in the inventory (Verification: extractor, for date and description; the image itself was viewed where the entry says so). The map labels two of them: photo A is commons-linge-20170329-1143a and photo B is commons-linge-20170329-1201a.

| Key | File | Date taken | Description on the page | Camera position on the page | Image viewed |
| --- | --- | --- | --- | --- | --- |
| commons-linge-20170329-1201a | [201703291201a P Chiang Mai, City Wall and Moat.jpg](https://commons.wikimedia.org/wiki/File:201703291201a_P_Chiang_Mai,_City_Wall_and_Moat.jpg) | 2017-03-29 12:01:21 | "City moat of Chiang Mai between Hua Rin Corner and Chang Phuak Gate" | 18.795553, 98.982733 | yes |
| commons-linge-20170329-1029a | [201703291029a Chiang Mai, City Moat.jpg](https://commons.wikimedia.org/wiki/File:201703291029a_Chiang_Mai,_City_Moat.jpg) | 2017-03-29 10:29:27 | "City moat of Chiang Mai between Chiang Mai Gate and Suan Prung Gate" | not stated | yes |
| commons-linge-20170329-1143a | [201703291143a P Chiang Mai, City Moat.jpg](https://commons.wikimedia.org/wiki/File:201703291143a_P_Chiang_Mai,_City_Moat.jpg) | 2017-03-29 11:43:03 | "City moat of Chiang Mai between Chang Phuak Gate and Sri Phum Corner" | 18.795245, 98.991489 | no (download rate-limited) |
| commons-linge-20170329-1126a | [201703291126a Chiang Mai, City Moat.jpg](https://commons.wikimedia.org/wiki/File:201703291126a_Chiang_Mai,_City_Moat.jpg) | 2017-03-29 11:26:16 | "City moat of Chiang Mai between Sri Phum Corner and Tha Phae Gate" | not stated | no |
| commons-linge-20170329-1223c | [201703291223c Chiang Mai, City Moat.jpg](https://commons.wikimedia.org/wiki/File:201703291223c_Chiang_Mai,_City_Moat.jpg) | 2017-03-29 12:23:39 | "City moat of Chiang Mai between Suan Dok Gate and Hua Rin Corner" | not stated | no |

Gate and corner files from the same series, one per stop, are listed with dates and rights in `research/inventory/discovery/discovery-images-and-maps.md`. They were not viewed in this pass.

---

## Encyclopedias

### th-wikipedia-wall-r13016262

- Title: กำแพงเมืองเชียงใหม่ (Chiang Mai city wall)
- Creator: Thai Wikipedia contributors. Revision 13016262.
- URL: https://th.wikipedia.org/wiki/กำแพงเมืองเชียงใหม่
- Language: Thai
- Access: inspected. Verification: raw.
- Passages used (section headings as on the page):
  - Inner gates (`ประตูเมืองชั้นใน`): "ประตูช้างเผือก เดิมมีชื่อว่า ประตูหัวเวียง เป็นประตูชั้นในด้านทิศเหนือ". The page gives the same pattern (current name, former name, side) for ประตูเชียงใหม่ (former ประตูท้ายเวียง, south), ประตูท่าแพ (former ประตูเชียงเรือก, east), ประตูสวนดอก (west), and "ประตูแสนปุง หรือ ประตูสวนปรุง" (south).
  - Corners (`แจ่งเมืองเชียงใหม่`): "แจ่งศรีภูมิ เดิมชื่อ แจ่งสะหลีภูมิ เป็นแจ่งทางทิศตะวันออกเฉียงเหนือ"; "แจ่งก๊ะต้ำ หรือ แจ่งขะต๊ำ เป็นแจ่งทางทิศตะวันออกเฉียงใต้"; "แจ่งกู่เฮือง เป็นแจ่งทางทิศตะวันตกเฉียงใต้"; "แจ่งหัวลิน เป็นแจ่งด้านตะวันตกเฉียงเหนือ".
  - Outer corner: "แจ่งหายยา (บ้างก็เรียกแจ่งทิพเนตร) ซึ่งเป็นแจ่งของกำแพงเมืองชั้นนอก ... ตั้งอยู่ทางใต้จากแจ่งกู่เฮืองราว 600 เมตร".
  - History: "บูรณะอีกครั้งในปี พ.ศ. 2361 ในรัชสมัยพระยาธรรมลังกา" (cites วงศ์สักก์ ณ เชียงใหม่, ed., เจ้าหลวงเชียงใหม่, 1996); "ในปี พ.ศ. 2491 ... ทางเทศบาลนครเชียงใหม่จึงได้เริ่มรื้อกำแพงออก".
  - Infobox: registered 8 มีนาคม พ.ศ. 2478, reference number 0003557.
- Limits: the page carries a needs-references tag. It is a lead for the dates and the registration, not evidence of them. The corner compass positions and gate sides are used only to match names to the OSM-mapped features.
- Lineage: Amarin TV 517276 repeats its 2491 wording (see the Thai discovery log).

### th-wikipedia-tha-phae-r12962538

- Title: ประตูท่าแพ (Tha Phae Gate)
- Creator: Thai Wikipedia contributors. Revision 12962538.
- URL: https://th.wikipedia.org/wiki/ประตูท่าแพ
- Language: Thai
- Access: inspected. Verification: raw.
- Passages used:
  - "ประตูท่าแพซึ่งตั้งอยู่ในปัจจุบันนี้ เทศบาลนครเชียงใหม่และกรมศิลปากรได้ร่วมกันสร้างขึ้นมาใหม่ เมื่อปี พ.ศ. 2528" (history section).
  - Infobox: "รื้อถอน พ.ศ. 2491", "สร้างใหม่ พ.ศ. 2529".
  - "ประตูท่าแพ (ชั้นใน) เดิมเป็นประตู 2 ชั้น" (cites a พ.ศ. 2436 map).
- Limits: the text and the infobox disagree (2528 against 2529). Not resolved.

### en-wikipedia-tha-phae-r1360504006

- Title: Tha Phae Gate
- Creator: English Wikipedia contributors. Revision 1360504006.
- URL: https://en.wikipedia.org/wiki/Tha_Phae_Gate
- Language: English
- Access: inspected. Verification: raw.
- Passages used: "The current structure is a reconstruction from 1985–1986"; "The gate was renovated between 1966 and 1967"; "a reconstruction undertaken by the Chiang Mai Municipality and the Fine Arts Department between 1985 and 1987".
- Limits: the page gives two end years (1986, 1987). Lineage with the Thai article is likely but not shown.

### en-wikipedia-chang-phueak-monument-r1360483608

- Title: Chang Phueak Monument
- Creator: English Wikipedia contributors. Revision 1360483608.
- URL: https://en.wikipedia.org/wiki/Chang_Phueak_Monument
- Access: inspected. Verification: raw.
- Passage: "The old wall was last renovated in 1995, and in 2023, it was partially damaged by a car accident and subsequently restored." Cites Thai Rath, 28 March 2023.
- Limits: the article concerns the white-elephant monument outside the gate. Whether "the old wall" means the city wall or the monument's own enclosure is not clear from the passage. Not used for the city wall.

### wikivoyage-chiang-mai

- Title: Chiang Mai (Wikivoyage)
- URL: https://en.wikivoyage.org/wiki/Chiang_Mai
- Access: inspected. Verification: extractor.
- Statements relayed: "Sections of the wall dating to their restoration a few decades ago remain at the gates and corners, but of the rest only the moat remains."; Chiang Mai Gate "Built c.1296 at the founding of the city by King Mangrai." / "Reconstructed c.1800. Rebuilt 1966-1969."; Tha Phae Gate "Built c.1296 ..." / "Rebuilt 1985-1986."; Chang Phuak Gate "Built by King Mangrai c.1296."; Ku Huang Corner "Rebuilt c. 1800".
- Limits: travel wiki, uncited. A lead only.

---

## News

### thestandard-686272

- Title: not recorded (news item on the 25 September 2022 collapse at Chang Phueak Gate)
- Creator: THE STANDARD TEAM
- Date: 25 September 2022 (stated)
- URL: https://thestandard.co/?p=686272
- Language: Thai
- Access: inspected. Verification: raw.
- Passages used:
  - Mayor of Chiang Mai, named on the page as อัศนี บูรณุปกรณ์: "ซึ่งตัวประตูกำแพงเมืองไม่พบว่าได้รับความเสียหาย ส่วนที่พังลงมาเป็นกำแพงที่สร้างขึ้นใหม่ครอบไว้อีกชั้น"
  - Therdsak Yenjura, Director, Monument Conservation Group, Fine Arts Office 7 Chiang Mai: "กำแพงที่พังลงมานั้นเป็นกำแพงที่ก่อขึ้นใหม่ช่วงต้นปี 2500 เพื่อคลุมแนวกำแพงโบราณไว้ ส่วนของกำแพงเก่าไม่พบว่าได้รับความเสียหาย"
  - Unattributed narration about the gate: "สร้างใหม่อีกครั้งในช่วงปี 2503-2512" and "มีการบูรณะล่าสุดเมื่อปี 2552".
- Limits: the years are written without an era marker. Reading them as Buddhist Era is an inference, and no calendar conversion is recorded here. A news report of an official's statement, not the conservation record itself.

### thaipbs-319794

- Title: ฝนตกหนัก! "ประตูช้างเผือก" กำแพงเมืองเก่าเชียงใหม่ถล่ม
- Creator: Thai PBS News
- Date: 25 September 2022 (stated)
- URL: https://www.thaipbs.or.th/news/content/319794
- Access: inspected. Verification: raw.
- Passages used: Therdsak Yenjura: "กำแพงเมืองที่พังลงมา เป็นกำแพงเมืองที่ไม่ได้ก่อเชื่อมต่อกับป้อมประตูเมือง"; "กำแพงเมืองและประตูเชียงใหม่แห่งนี้ ผ่านการบูรณะมาแล้วกว่า 60 ปี".
- Limits: "ประตูเชียงใหม่แห่งนี้" in the second passage refers to the Chang Phueak site in context; the wording is ambiguous on its own.

### thaipbs-319832

- Title: นักวิชาการชี้ "ประตูช้างเผือก" ไม่ใช่โบราณสถาน แต่เอกสารกรมศิลป์บอกว่า "ใช่"
- Creator: Thai PBS News
- Date: 26 September 2022 (stated)
- URL: https://www.thaipbs.or.th/news/content/319832
- Access: inspected. Verification: raw.
- Passages used:
  - Quoting a Facebook post by Surapol Damrikul: "ต่อมาเทศบาลเมืองเชียงใหม่(ในขณะนั้น)เมื่อราวแปดสิบปีที่ผ่านมา (สมัยนายทิม โชตนา เป็นนายกเทศมนตรี) ได้ออกแบบและสร้างประตูขึ้นใหม่ 5 ประตู (โดยไม่มีพื้นฐานของหลักฐานเก่าเลย)"; "ยกเว้นประตูท่าแพในปัจจุบันนั้น ... ขออนุญาตกรมศิลปากรสร้างใหม่ ตามรูปแบบภาพเก่าขึ้นเมื่อ พ.ศ.2529".
  - Quoting a Fine Arts Office 7 web page: "กำแพงดินและคูน้ำไม่ปรากฏหลักฐานว่า สร้างเมื่อใด".
- Limits: the scholar's post is undated, and "about eighty years ago" is relative to an unknown date. The Fine Arts Office 7 page itself was not found (lead).

### nation-40020399

- Title: Chiang Mai in shock after 750-year-old city wall crumbles in rainstorm
- Creator: The Nation (Thailand)
- Date: 25 September 2022 (stated)
- URL: https://www.nationthailand.com/thailand/general/40020399
- Access: inspected. Verification: raw.
- Passages used: "The regional Fine Arts Office said about 10 metres of the wall had toppled due to heavy rain."; "Office director Therdsak Yenjura said the wall around Chang Phuak gate was last maintained about 60 years ago."
- Lineage: same event and official as thestandard-686272 and thaipbs-319794. Not independent of them.

### nation-40027862

- Title: Chiang Mai residents fear ancient gate with ruptured wall will topple
- Creator: The Nation (Thailand)
- Date: 21 May 2023 (stated)
- URL: https://www.nationthailand.com/thailand/general/40027862
- Access: inspected. Verification: raw.
- Passages used: "A two-metre vertical crack is on the north side of the gate."; "The wall is supported by a mound of earth that will prevent it from collapsing, he said." (Therdsak Yenjura); "The ancient gates and walls were restored in 1818."

### citylife-suan-dok-2023

- Title: Concerns over cracks at Suan Dok Gate
- Creator: Chiang Mai CityLife, CityNews
- Date: 18 May 2023 (stated)
- URL: https://www.chiangmaicitylife.com/citynews/general/concerns-over-cracks-at-suan-dok-gate/
- Access: inspected. Verification: raw.
- Passage: "Renovated during the reign of Chao Luang Tham Lanta in 1821, the gates were officially registered as national monuments in 1935".
- Lineage: probably the same Fine Arts Department briefing as nation-40027862. The two give different years (1821, 1818). Not resolved.

### Extractor-only news items

These were read through the extractor only. Their wording is not verified. Details are in `research/inventory/discovery/discovery-thai.md`.

- `mgronline-9520000066170`: MGR Online, 11 June 2009. Fine Arts Department excavation at Chang Phueak Gate to test old photographs showing a two-layer wall. https://mgronline.com/daily/detail/9520000066170
- `thaipbs-336746`: Thai PBS, 6 February 2024. Public hearing on Chang Phueak Gate; excavation after the collapse. https://www.thaipbs.or.th/news/content/336746
- `thansettakij-664349`: Thansettakij, 18 July 2026 (stated as 2569 BE). World Heritage nomination component list. https://www.thansettakij.com/general-news/664349

---

## Historic maps (leads)

Listed on Wikimedia Commons. None was viewed in this pass. Dates and rights are as the file pages state them, via the extractor. See `research/inventory/discovery/discovery-images-and-maps.md`.

- `commons-map-1893-inthawichayanon`: "Chiang Mai City Map for Inthawichayanon 1893.png". The page names the Fine Arts Office, Chiang Mai, as holder. https://commons.wikimedia.org/wiki/File:Chiang_Mai_City_Map_for_Inthawichayanon_1893.png
- `commons-map-1890-mccarthy`: "Chiang Mai City Map (Chiengmai) 1890.png". The page's date fields conflict (1890, 1900). https://commons.wikimedia.org/wiki/File:Chiang_Mai_City_Map_(Chiengmai)_1890.png
- `commons-map-1931`: "Map of Chiengmai (Chiang Mai) City 1931.jpg". British Library via Old Maps Online, per the page. https://commons.wikimedia.org/wiki/File:Map_of_Chiengmai_(Chiang_Mai)_City_1931.jpg
- `commons-map-1945-survey-of-india`: "Chiang Mai 1945.jpg", scale 1:5,000 as stated. UW-Milwaukee Libraries, American Geographical Society Library. https://commons.wikimedia.org/wiki/File:Chiang_Mai_1945.jpg

## Other leads

- `penth-1994-brief-history-of-lanna`: Hans Penth, *A Brief History of Lanna*, Silkworm Books. Seen only as a forum quotation in search results, which dates the surviving fortifications to about 1800. Book not obtained. Highest-value lead for the date of the standing fabric.
- `unesco-tentative-6003`: UNESCO World Heritage tentative list, "Monuments, Sites and Cultural Landscape of Chiang Mai, Capital of Lanna". whc.unesco.org returned HTTP 403 to every fetch.
- `royal-gazette-2478-registration`: the 1935 (พ.ศ. 2478) registration notice. Not located, so its extent is unknown.
- `fad-office-7-wall-moat-page`: the Fine Arts Office 7 web page quoted by thaipbs-319832. Not located.
- Excavation reports for Chang Phueak Gate (2009, and after the 2022 collapse): not located.
- Chulalongkorn University theses on the moat and the old town (handles and DOIs in the discovery logs): catalogue records only.

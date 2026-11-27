# Maps and Charts: Data, Tools, and Production Plan

**Status:** Research and planning document, November 27, 2026. No map, chart, or dataset has been produced, and no manuscript file has been changed. This is a technical supplement, not a competing book outline.

**Authority.** [`README.md`](../README.md) remains the book plan and the register of maps, figures, images, and tables. [`AGENTS.md`](../AGENTS.md) remains the process, evidence, and house-style authority. [`data/app-c/README.md`](../data/app-c/README.md) is the current visual-program overhaul plan; [`docs/kindle.md`](kindle.md) and [`docs/kindle-visuals-research.md`](kindle-visuals-research.md) set the Kindle constraints. This document does not assign display numbers, approve a reduction in the visual program, clear rights, or authorize a new asset. It answers the production question: where the data come from, how to store and process them, what to install on Debian, and how to turn machine-tractable sources into publication PNGs.

**The problem in one paragraph.** The manuscript is largely drafted, but no interior map or chart exists. The current README registers 39 maps, nine figures, and eight images; the Appendix C overhaul proposes 13 maps, three figures, and two images. Either program needs the same foundation: a registered source for every claim, a reproducible data snapshot, a vector master that can be edited without redrawing, and a PNG that survives a 3.5-inch grayscale screen. The foundation can be built once, at low cost, with open-source tools. The expensive mistakes are licensing a dataset that cannot be redistributed, drawing boundaries more precisely than the evidence allows, and baking type into a raster that then cannot be corrected.

**Contents:** [1. The decision in brief](#1-the-decision-in-brief) · [2. What the book needs](#2-what-the-book-needs) · [3. Data sources](#3-data-sources) · [4. Preparation and storage](#4-preparation-and-storage) · [5. Software for Debian](#5-software-for-debian-13) · [6. The production pipeline](#6-the-production-pipeline) · [7. Cartographic and chart standards](#7-cartographic-and-chart-standards) · [8. Rights and provenance](#8-rights-and-provenance) · [9. Quality assurance](#9-quality-assurance) · [10. Implementation plan](#10-implementation-plan) · [11. Risks and decisions](#11-risks-and-open-decisions) · [12. Sources consulted](#12-sources-consulted)

**How to use it:** the author can read §1, §10, and §11 for the decisions and schedule; the cartographer can work from §§3–9; a rights reviewer can start with §3.4 and §8. The source matrices are research targets, not finished citations; each source still needs the chapter’s precise locator and “Used for” note.

---

## 1. The decision in brief

1. **Use one two-track toolchain.** QGIS for geographic maps; Python and Matplotlib for charts and simple schematic diagrams; Inkscape for final vector cleanup; `resvg` or `rsvg-convert` for SVG-to-PNG. All are free and packaged for Debian 13 except `mapshaper`, which is installed through npm. No paid software is needed.
2. **Store the evidence, not just the picture.** Every visual gets a specification, a source registry row, a normalized dataset, a checksum, a script or QGIS project, an SVG master, a PNG derivative, and a QA record. The register in `README.md` remains the display authority; `data/atlas/` becomes the technical record.
3. **Use durable, machine-tractable formats.** Working vector data in GeoPackage; small exchange layers in GeoJSON; tabular series in tidy CSV; large derived tables in GeoParquet; scanned or georeferenced rasters in GeoTIFF. The editable master is plain SVG 1.1; the publication asset is an 8-bit PNG, indexed when that reduces size without harming labels. Shapefile is an export format, not an archive.
4. **Do not put restricted data in Git.** IPUMS NHGIS forbids redistribution without permission; Native Land Digital forbids storing or distributing API data without explicit permission; SlaveVoyages imputed data and Estimates are CC BY-NC; David Rumsey’s terms are ambiguous for a commercial book. For those sources, commit the citation, the download recipe, the checksum, and the derived values, not the raw file.
5. **Pilot before scaling.** Produce Map 5 (Ohio Valley and the Proclamation Line) and Figure 1 (presidential votes and turnout) first. They exercise the full pipeline: historical boundary, route, label hierarchy, grayscale, SVG export, PNG rendering, caption, alt text, and rights record. Then batch the remaining visuals.

The recommended output standard is the one already set in `data/app-c/README.md` §2: 1,600 px wide (2,400 px for dense labels), grayscale-safe, four tones plus hatching, 8–12 labels, 44–56 px labels at 1,600 px, 300 PPI at display size, an 8-bit PNG indexed when that reduces size without harming labels, flattened on white, no transparency, and no title, caption, source line, or credit inside the image.

---

## 2. What the book needs

### 2.1 Two programs, one pipeline

The README’s current register and the Appendix C overhaul differ in scope, not in production method.

| Program | Maps | Figures | Images | Status | Consequence |
|---|---:|---:|---:|---|---|
| **README register, October 29, 2026** | 39 | 9 | 8 | `planned` | The full inherited program; the register remains authoritative until changed. |
| **Appendix C overhaul, November 25, 2026** | 13 | 3 | 2 | Proposed | A smaller, Kindle-first program; not yet approved in the README. |
| **This document** | Either | Either | Unchanged | Technical plan | The pipeline scales to 13 or 39; it does not choose between them. |

The visual program should be resolved in the README before mass production. Building 39 maps and then discarding 26 is waste; building 13 and later restoring 26 is also waste. The written decision belongs in `README.md` and `data/app-c/README.md` §13, with the date and initials. Until then, use the 13-map/3-figure list as the production pilot because it is the smaller, better-specified program.[^appc]

[^appc]: [`data/app-c/README.md`](../data/app-c/README.md), §§1–7, especially §1.4 (the six-question test) and §13 (the decision record). The plan proposes 13 maps, three figures, and two images, but states that no manuscript file has been changed and no asset produced.

### 2.2 What must be drawn, not tabulated

The Appendix C test is the right filter. A visual stays drawn only if all six answers are yes:

1. The argument depends on relative position, route, distance, layering, or tonal contrast.
2. It works as one panel, or two vertically stacked panels that each stand alone.
3. It can carry eight to twelve labels at 44–56 px in a 1,600 px-wide image.
4. It survives four tones: white, 15% gray, 40% gray, black, plus hatching.
5. It is cropped to the theater of the argument, not “all of North America.”
6. Its base data and any reproduced object are rights-clean.

If any answer is no, use a comparison table, a chronology table, a benchmark table, a primary-source exhibit, or a close reading. That decision is an argument decision, not a cartographic preference. A county choropleth that becomes noise at 3.5 inches is not evidence; a table with exact denominators is.

### 2.3 The production constraints that drive every choice

| Constraint | Requirement | Production consequence |
|---|---|---|
| **Kindle screen** | 3.5–4.2 inches usable width; 16-level grayscale on most dedicated devices | Design at 3.5 inches, not at desktop size; no color-only encoding; no hairlines. |
| **KDP format** | PNG or JPEG; SVG unsupported in the EPUB; no transparency | SVG is an editing master; PNG is the publication asset. Flatten on white. |
| **Resolution** | 300 PPI at display size; KDP floor 1,200 × 1,800 px full-page | 1,600 px wide minimum; 2,400 px for dense labels. |
| **File size** | 150–300 KB per map; 80–150 KB per figure; 400 KB hard ceiling for a dense map; 2.5–5 MB total image payload | 8-bit PNG, indexed when it reduces size without harming labels; limited palette; simplified geometry; no embedded raster. |
| **Captions** | HTML `<figcaption>`, not raster text | No title, caption, source line, or credit inside the PNG. |
| **Alt text** | 140 characters or fewer; meaningful images need it | One approved string in Appendix C and the register; no drift. |
| **Evidence** | Every claim traceable to a consulted source with a locator | A source registry row and a citation note key for every layer and series. |
| **Rights** | Each visual has its own license or permission | Public domain is not a global clearance; check the item, not the host. |

These constraints are already documented in [`docs/kindle.md`](kindle.md) §7 and `data/app-c/README.md` §2.3. This plan does not relax them.

---

## 3. Data sources

### 3.1 Source hierarchy

Use sources in this order, and record why a lower tier was necessary:

1. **Primary records and official data.** Statutes, treaties, census returns, agency reports, military records, election canvasses, archival maps. These establish what a document said or what a record counted.
2. **Authoritative compilations and scholarly editions.** NHGIS, the Newberry Atlas of Historical County Boundaries, SlaveVoyages historical data, FRUS, the *Official Records*, the *Statutes at Large*, and peer-reviewed historical atlases. These establish series and boundaries, with documented transformations.
3. **Scholarly monographs and articles.** These establish interpretation, context, and the limits of the data. They do not replace the underlying record for a number.
4. **Reference works and finding aids.** The *Handbook of North American Indians*, Native Land Digital, GNIS, Wikipedia, and encyclopedia entries. Use these to find sources, not to settle a historical claim or draw a boundary.
5. **Commercial aggregators.** Social Explorer, PolicyMap, SimplyAnalytics, Esri, Statista. Use only when the underlying public source is inaccessible or the aggregation is the evidence; cite the aggregator and, where possible, the upstream series.

A map is an argument, not a decoration. The source hierarchy should be visible in the map’s specification: which layer came from which source, what was transformed, and what the source cannot establish.

### 3.2 Free and open sources

The following are the core free sources for this book. “Free” does not always mean “redistributable”; the license column is the operative one.

| Source | What it provides | Access and format | License or terms | Best use in this book |
|---|---|---|---|---|
| **U.S. Census Bureau: TIGER/Line** | Current legal boundaries, roads, hydrography, congressional districts | Shapefile and ASCII; 1992–2026 releases | U.S. federal public domain; cite the Census Bureau | Modern county, state, and district geometry; not historical boundaries. |
| **U.S. Census Bureau: data.census.gov and API** | Decennial census, ACS, County Business Patterns, economic census | API, CSV, tables | Public domain; cite the Bureau | Population, race, housing, employment, and establishment series. |
| **IPUMS NHGIS** | Census summary data and GIS boundary files, 1790–present; states, counties, tracts, blocks | Shapefile + CSV; registration required; API and R/Python access | Free, but **no redistribution without permission**; cite NHGIS | Historical census geography and consistent series; the first stop for 1790–1980 boundaries. |
| **USGS National Map and GNIS** | Boundaries, hydrography, elevation, geographic names, coordinates | Vector, raster, API; GeoTIFF, GeoPackage | U.S. public domain; credit requested | Physical geography, place coordinates, and modern reference layers. |
| **Natural Earth** | World coastlines, countries, states/provinces, rivers, lakes at 1:10m, 1:50m, 1:110m | Shapefile and raster; convert to GeoPackage/GeoJSON on ingest | Public domain; credit unnecessary but welcome | Clean basemaps for continental and world maps; modern coastlines only. |
| **National Archives and Records Administration** | Maps, military records, treaties, agency records, photographs | Catalog API, digitized images, some scans | Mostly public domain; item-level restrictions possible | *Official Records* maps, treaty maps, GLO and railroad records, agency reports. |
| **Library of Congress, Geography and Map Division** | Historical maps, atlases, Sanborn fire insurance maps, military maps | IIIF, JPEG/JP2/TIFF, catalog records | Free to use and reuse unless a Rights Advisory says otherwise; item-level check | Tanner 1840, Civil War maps, Revolutionary War maps, city maps. |
| **National Park Service** | Park maps, battle maps, cultural landscapes, site coordinates | PDF, images, some GIS | Federal public domain, but some maps contain licensed data | Campaign maps, site locations, Trail of Tears corridors. |
| **Smithsonian Open Access** | Collection images and metadata, including the Jefferson peace medal | Images and data; CC0 items marked | CC0 for marked assets; object-level check | Image 1, the Jefferson peace medal; object photography. |
| **Newberry Library, Atlas of Historical County Boundaries** | Every U.S. county boundary change, with dates and legal citations | Shapefile, KMZ, PDF, tab-delimited text | The downloads page permits any lawful purpose, commercial or non-commercial, without fees; older CC notices in the files may be ignored | Historical county boundaries; the best source for 17th–20th-century county change. |
| **SlaveVoyages** | Transatlantic and intra-American slave trade voyages, estimates | CSV, SPSS, database | Historical data public domain; imputed data and Estimates CC BY-NC; commercial use of those needs permission | Map 4’s Atlantic circuit; aggregate counts already in Appendix B Table 6. |
| **MIT Election Data and Science Lab** | County, state, and precinct election returns, 1976–2024 | CSV, Dataverse | Many deposits are CC0; verify each Dataverse record | Modern election maps; not a source for Figure 1’s 1824–1840 series. |
| **A New Nation Votes** | Election returns, 1787–1825 | Searchable database, XML transcriptions | Free; check the project’s terms for reuse | Early republic election context; overlaps 1824 only, not the 1825–1840 series. |
| **American Presidency Project** | Presidential election results, documents, speeches | HTML tables, documents | Free; copyright by the Project; facts are not copyrightable; cite | Figure 1 and modern election tables; cross-check against state canvasses. |
| **FRED** | 800,000+ economic series, including historical series | API, CSV, charts | Free API; third-party series may be copyrighted; check series notes | Figure 2 and long-run economic context. |
| **BEA** | GDP, income, employment by state and county | API, CSV | Public domain; cite | County and state economic maps; Figure 2 context. |
| **BLS** | Employment, unemployment, CPI, wages | API, CSV | Public domain except third-party photographs | Figure 2; labor and price series. |
| **FDIC** | Bank suspensions, failures, deposits, and historical banking statistics | Tables, PDF, CSV | Public domain; cite the Corporation | Figure 2; bank-failure counts and definitions. |
| **Pew Research Center** | Public opinion, including trust in government, 1958–2025 | Reports, tables, datasets | Free with attribution and disclaimer; excerpts only, not full datasets | Figure 3; question wording and survey breaks. |
| **American National Election Studies** | Election surveys, 1948–present | CSV, Stata, R | Free registration; terms apply | Cross-check Figure 3 and turnout context. |
| **OpenStreetMap** | Modern roads, places, land use | API, extracts, GeoJSON | ODbL: attribution and share-alike for derivative databases | Modern reference only; not for historical maps. Prefer Natural Earth and USGS. |
| **David Rumsey Map Collection** | High-resolution historical maps and atlases | JP2, JPEG, IIIF | Site permission page allows publication with credit; collection also displays CC BY-NC-SA; post-1929 items may be copyrighted | Georeferencing and reference; prefer public-domain originals from LoC or NARA for reproduction. |
| **HathiTrust and Internet Archive** | Digitized books, reports, maps | Page images, OCR, PDF | Item-level public domain or permissions | Historical statistics, reports, and map plates. |
| **Native Land Digital** | Indigenous territories, languages, treaties | API, GeoJSON | **Non-commercial; no storage or distribution without explicit permission; no alteration of boundaries** | Finding aid and consultation prompt only. Do not use its geometry as a book boundary. |

The practical free stack is: Census/TIGER for modern boundaries, NHGIS and the Newberry Atlas for historical boundaries, USGS and Natural Earth for physical geography, NARA and LoC for historical maps, and the relevant statistical agency for each series. That stack covers nearly every map in the proposed program without a subscription.

### 3.3 Paid and subscription sources

Paid sources are optional. For a single-authored book, library access is usually a better buy than an individual subscription. Prices below are published or reported as of November 27, 2026; they are planning estimates, not quotes, and should be verified before purchase.

| Service | What it adds | Published price or model | Verdict for this book |
|---|---|---|---|
| **Social Explorer** | Tract-level census mapping, historical census data, reports | Individual about US$195/month; quarterly and annual discounts; site license by quote | Useful for exploring tract patterns; not necessary if NHGIS and Census API are used. Check library access first. |
| **PolicyMap** | Community indicators: income, housing, health, food access, opportunity | Free public edition; paid Basic about US$2,200/year; custom quote | Useful for Chapter 39–40 and county maps; the free edition may be enough. |
| **SimplyAnalytics** | Census, business, marketing, and consumer data; mapping | Library subscription; a 2018 published rate was about US$900/quarter for one concurrent user; current quote | Not needed for this book’s historical argument. Use only through a library. |
| **Esri Business Analyst** | Geocoding, demographics, site selection, Esri basemaps | Web app about US$1,100/user/year; advanced bundles higher; quote | Overkill. QGIS plus public data is sufficient. |
| **Data Axle Reference Solutions** | Business and consumer lists, historical business data | Library subscription; quote | Only if a chapter needs establishment-level historical data not in County Business Patterns. |
| **Statista** | Aggregated statistics and charts | Basic free; Starter about US$199/month; Personal about US$649/month; Professional quote | Secondary aggregator; not a primary source. Avoid for evidence. |
| **Cambridge, *Historical Statistics of the United States*, Millennial Edition** | The standard historical statistical compendium | Print about US$990; individual online about US$1,450 (older published price; verify); library subscription | High value, but many series are available through Census, BLS, FRED, and Appendix B. Use a library copy. |
| **Roper Center iPOLL** | 80+ years of U.S. public opinion polls | Membership and single-user licenses; quote; free trial | Useful for Figure 3 context, but Pew and ANES cover the core series. |
| **ICPSR** | Social science data archive, including historical election returns | Institutional membership; some public data; restricted-use fees | Use through a member library for historical election returns if APP and state canvasses are insufficient. |
| **ProQuest, Gale, Adam Matthew** | Newspapers, archives, primary-source collections | Library subscription | Research access, not a map-data source; do not republish without rights. |
| **Mapbox, Stadia, CARTO** | Modern basemaps and geocoding | Usage-based or subscription | Not appropriate for historical maps; avoid the dependency. |

**Recommendation:** budget US$0 for software and US$0–2,500 for data in the first production year. Start with the free stack. If one paid source becomes essential, prioritize a library subscription to *Historical Statistics* or Roper over an Esri or Social Explorer individual plan. Do not buy a dataset whose license forbids redistributing the derived map.

### 3.4 Licenses and the commercial-book problem

The book’s CC0 dedication covers its original text, not third-party data, maps, or photographs. A CC0 book can still be sold, and a commercial sale can trigger non-commercial restrictions. Treat “NC” and “ND” as unavailable without written permission until the business model is confirmed.

| License or terms | Commercial book | Raw data in the repository | What to do |
|---|---|---|---|
| **U.S. federal public domain** | Yes | Yes | Cite the agency; check item-level third-party content. |
| **CC0** | Yes | Yes | Keep the source record; no attribution required, but credit is good practice. |
| **CC BY** | Yes | Yes, with attribution | Record the attribution string and license URL. |
| **CC BY-SA** | Yes, with share-alike | Yes, with share-alike | Avoid for maps unless the share-alike is acceptable; isolate the licensed layer. |
| **CC BY-NC / CC BY-NC-SA** | No, without permission | No | Seek permission or use a public-domain alternative. |
| **ODbL (OpenStreetMap)** | Yes for a produced map, with attribution | Derivative databases must be ODbL | Use only as a modern reference; credit “© OpenStreetMap contributors” and link the license. |
| **NHGIS terms** | Yes for publication | **No redistribution without permission** | Cite NHGIS; keep only derived values and a download record. |
| **SlaveVoyages** | Historical data: yes; imputed/Estimates: no without permission | Historical data: yes; imputed: no | Use historical data or aggregate published estimates; get permission for the rest. |
| **Native Land Digital** | No commercial use; no storage or distribution without permission | No | Use as a finding aid only; consult nations for any boundary. |
| **Pew Research Center** | Yes, with attribution and disclaimer; excerpts only | No full dataset | Chart the published series; cite the report and question wording. |
| **David Rumsey** | Site permission page allows publication with credit; CC BY-NC-SA notice creates ambiguity; post-1929 rights vary | No raw collection | Prefer a public-domain original; otherwise get written permission. |
| **All rights reserved** | No | No | Permission or a different source. |

An original map drawn from public-domain data can be released under the book’s CC0 dedication, but the underlying data and any reproduced object keep their own terms; record the basis in `sources.csv`. This is a production policy, not legal advice. When a source’s status is unclear, record the ambiguity in `sources.csv` and choose a public-domain alternative. A map that cannot be cleared does not ship.

### 3.5 Source-to-visual matrix: the 13 proposed maps

The matrix follows the Appendix C numbering and is a research target list, not a claim that every source has been consulted. Display numbers are Appendix C’s proposed numbers; stable README IDs such as `ch08-map-01` remain the keys in `registry.csv` and in any cross-reference. Each source still needs a precise locator and a “Used for” note in the owning chapter.

| Visual | Argument | Primary data and geometry | Rights and access | Working format | Main risk |
|---|---|---|---|---|---|
| **Map 1. Cultural regions and centers, c. 1200 CE** | An inhabited, managed continent, not an empty land | NPS and state SHPO site coordinates (Poverty Point, Hopewell, Cahokia, Chaco, Serpent Mound); UNESCO site data; Natural Earth coastlines; original analytical regions | NPS/USGS public domain; state SHPO terms vary; UNESCO facts; *Handbook of North American Indians* for reference only | CSV points + GeoJSON regions | Regional blocks are analytical, not tribal territories; Poverty Point and Hopewell are earlier earthworks and must be dated as such; Serpent Mound’s date is disputed. |
| **Map 2. Norse voyages, c. 1000–1100** | Distinguish documented landfall from saga geography | Parks Canada, L’Anse aux Meadows; saga texts in public-domain translations; Natural Earth; original route lines | Natural Earth public domain; Parks Canada facts; do not copy a modern NPS map | GeoJSON lines + CSV labels | Saga routes are uncertain; use solid documented and dashed inferred lines. |
| **Map 3. Indigenous political worlds, c. 1600** | Political and linguistic diversity, not a single “Indian country” | Nation-specific sources; *Handbook*; treaty and colonial records; original schematic regions | Community review required; Native Land only as a finding aid; no NLD geometry | GeoJSON polygons + CSV labels | Highest-risk map. If names or boundaries cannot be verified, convert to a nation table. |
| **Map 4. The English Atlantic circuit, c. 1680** | Connect sugar, tobacco, and captive labor | SlaveVoyages historical data; Appendix B Table 6; Natural Earth coastlines; original nodes and arrows | SlaveVoyages historical data public domain; imputed/Estimates CC BY-NC; use aggregates or get permission | CSV nodes/edges + GeoJSON coast | Arrow width must not imply volume unless stated; the circuit is a simplification. |
| **Map 5. The Ohio Valley and the Proclamation Line, 1754–1763** | Campaigns, forts, and a claim line, not a surveyed border | NPS battle maps; NARA and colonial/imperial records; the Proclamation text in the *Statutes at Large* or NARA, with Avalon only as a transcription; Natural Earth; original routes | Federal public domain; check NPS map data credits | GeoJSON lines/polygons + CSV labels | A claim is not a survey; distinguish de jure, de facto, and uncertain lines. |
| **Map 6. War for Independence, 1775–1783** | Two connected theaters and French naval power | NPS and LoC maps; Revolutionary War campaign records and orderly books; original campaign arrows; Natural Earth | Federal public domain; verify any Esposito atlas copyright before use | GeoJSON lines + points | Do not draw one arrow from Boston to Yorktown; stack north and south panels. |
| **Map 7. Canals and railroads crossing the Appalachians, 1825–1840** | Uneven market connections, not a national network | Tanner 1840 (LoC); state canal records; railroad maps; georeferenced historical base | Public domain; LoC item-level check | GeoTIFF + GeoJSON corridors | Georeferencing error; distinguish completed from projected lines. |
| **Map 8. Removal corridors and Indian Territory, 1830–1846** | Coerced movement along multiple corridors, not one “Trail of Tears” | NPS Trail of Tears; Cherokee Nation; Royce’s Indian land cessions; emigration rolls; original corridors | Federal public domain; nation-specific review for representation | GeoJSON lines/polygons | A single line erases nations and routes; show resident nations in Indian Territory as a note, not a fill. |
| **Map 9. The Nueces–Río Grande strip and the 1848 cession** | A disputed strip and a conquest, not a natural border | NPS and NARA; Treaty of Guadalupe Hidalgo; Disturnell map; Natural Earth rivers | Public domain | GeoJSON lines/polygons | The strip is a claim, not a surveyed boundary; prewar Mexican states and Indigenous territories differ. |
| **Map 10. Civil War theaters, 1861–1863** | Geography and campaign constraints | NPS; LoC; *Atlas to Accompany the Official Records*; original theater bands | Public domain | GeoJSON polygons/lines | Theater bands are analytical; do not present them as exact fronts. |
| **Map 11. The final campaigns, 1864–1865** | Interlocking fronts and supply routes | NPS; LoC; *Official Records*; original arrows | Public domain | GeoJSON lines | Do not merge the Overland Campaign and the March to the Sea into one arrow. |
| **Map 12. Layered claims in the northern Plains, 1876–1890** | Treaty boundaries, reservations, railroad grants, and range overlap | NARA; NPS; treaty texts; General Land Office and railroad grant maps; original layers | Federal public domain; tribal consultation on the Black Hills | GeoJSON polygons/lines | Layered claims must remain distinguishable in black and white; the Black Hills are a sacred landscape, not a resource. |
| **Map 13. Southeast Asia supply routes, 1954–1968** | A trail network bypassing the DMZ, not a single road | FRUS and NARA; the Pentagon Papers only for documentary text already in the public record; Natural Earth; original network | Federal public domain; Natural Earth public domain | GeoJSON lines | The trail is a network; do not draw a single highway. |

### 3.6 Source-to-visual matrix: the three proposed figures

| Visual | Argument | Data | Rights and access | Working format | Main risk |
|---|---|---|---|---|---|
| **Figure 1. Presidential votes and turnout, 1824–1840** | The electorate expanded, but not universally or evenly | Appendix B Table 2; American Presidency Project; Census/Historical Statistics; state election laws | Facts are not copyrightable; APP terms; HSUS may be paid | Tidy CSV | 1824 popular vote is partial; state selection and eligibility vary; turnout denominator must be stated. |
| **Figure 2. Bank failures and unemployment, 1929–1933** | The banking collapse and the labor-market collapse are related but distinct | FDIC bank suspension tables; BLS/Lebergott and Darby series; FRED; Historical Statistics | Federal public domain; FRED third-party series may be copyrighted | Tidy CSV | Bank “suspension” definitions differ; Lebergott and Darby count work relief differently. |
| **Figure 3. Trust in the federal government, 1958–2025** | A long decline with party and survey breaks, not a single smooth trend | Pew Research Center, *Public Trust in Government: 1958–2025*; ANES for question wording | Pew terms allow excerpt with attribution and disclaimer | Tidy CSV | Question wording, sampled population, and survey-house breaks; do not smooth or imply causation. |

### 3.7 Source records

Every source gets one row in `data/atlas/sources.csv`. The row is not a reader-facing citation; it is the production record that maps to the chapter’s named footnote key.

```csv
source_key,citation,url,accessed,version,license,license_url,redistributable,attribution,local_path,sha256,note_key,notes
natl-earth-10m,"Natural Earth, 1:10m Cultural Vectors, current release",https://www.naturalearthdata.com/,2026-11-27,5.x,public domain,https://www.naturalearthdata.com/about/terms-of-use/,yes,"Made with Natural Earth",data/atlas/raw/ne_10m.zip,<sha256>,ch08-map-05-naturalearth,"Coastlines and country polygons only; modern geometry."
nhgis-1790-1980,"IPUMS NHGIS, historical county boundary files",https://www.nhgis.org/,2026-11-27,2026 release,NHGIS terms,https://nhgis.org/ipums-nhgis-terms-use,no,"IPUMS NHGIS, University of Minnesota",,<sha256>,ch12-map-01-nhgis,"No redistribution; raw extract not committed; derived values only."
```

Fields:

| Field | Meaning |
|---|---|
| `source_key` | Stable production key; never reuse it for a different version. |
| `citation` | Full citation, including edition or version. |
| `url` | Direct URL or DOI to the consulted item, not a home page when a locator exists. |
| `accessed` | Actual access date. |
| `version` | Release, extract ID, or dataset vintage. |
| `license` | Short license name. |
| `license_url` | License or terms URL. |
| `redistributable` | `yes`, `no`, or `derived-only`. |
| `attribution` | Required credit string. |
| `local_path` | Repository path, or empty if the raw file is not committed. |
| `sha256` | Checksum of the file actually used. |
| `note_key` | The chapter’s named footnote key that the source supports. |
| `notes` | Transformations, limitations, and access problems. |

A source without a `note_key` is a production blocker, not a formatting detail. A source with `redistributable=no` and a tracked `local_path` is a rights failure.

For API sources, record the endpoint, query parameters, access date, and a hash of the cached response. For a web table that may change, save a PDF or HTML snapshot with the access date. Do not let a live API or a moving web page be the only copy of a published figure.

---

## 4. Preparation and storage

### 4.1 Directory layout

The existing `data/app-b/` pattern — a README, a ledger, a checks file, and machine-readable data — is the right model. Use a parallel `data/atlas/` tree.

```text
data/atlas/
  README.md                 # purpose, status, how to run
  registry.csv              # one row per visual: id, owner, status, paths, caption, alt
  sources.csv               # one row per source/version/license
  manifest.csv              # input/output hashes, tool versions, build date
  toolchain.txt             # tool versions and OS
  raw/                      # downloads; git-ignored except README and SHA256SUMS
  rights/                   # permission records; private, ignored
  derived/
    geo/                    # GeoPackage, GeoJSON, FlatGeobuf
    series/                 # tidy CSV for charts
    rasters/                # GeoTIFF/COG
  maps/
    map-01/
      spec.md               # argument, extent, layers, labels, sources, checks
      map.qgz               # QGIS project (Git LFS)
      style.qml             # QGIS style
      build.py              # optional PyQGIS export script
      checks.md             # QA record
  figures/
    figure-01/
      spec.md
      build.py              # Matplotlib script
      data.csv              # snapshot used by the figure
      checks.md
assets/
  maps/
    map-01.svg              # editable master
    map-01.png              # publication asset
  figures/
    figure-01.svg
    figure-01.png
scripts/atlas/
  build_map.py              # shared helpers
  render_svg.sh             # SVG -> PNG
  check_atlas.py            # data, SVG, PNG checks
  manifest.py               # hashes and build metadata
```

Folder IDs (`map-01`, `figure-01`) are production keys, not display numbers. The `visual_id` column in `registry.csv` carries the stable README ID (`ch08-map-01`, `ch16-figure-01`), and the `display` column carries the current display number. Do not put final assets in `data/atlas/`. Data and assets have different lifecycles: data may be replaced by a new vintage; a published PNG must remain stable. The chapter references the PNG in `assets/`; the register records both paths.

### 4.2 Formats

| Format | Role | Use it for | Do not use it for |
|---|---|---|---|
| **CSV (UTF-8)** | Tidy tabular data | Series, labels, source registry, ledgers | Geometry with many vertices; binary attachments. |
| **GeoJSON (RFC 7946)** | Small, diffable vector exchange | Simplified boundaries, routes, points; one layer per file | Large national layers; multi-layer projects; non-WGS84 storage. |
| **GeoPackage (`.gpkg`)** | Working vector database | Multi-layer QGIS projects; attributes, CRS, spatial index; editing | Long-term archival of a single CSV; web delivery. |
| **GeoParquet** | Columnar geospatial analysis | Large derived tables; joins; reproducible analysis | QGIS editing; small hand-edited layers. |
| **FlatGeobuf** | Single-file streaming vector | Large read-only layers; fast spatial filtering | Hand editing; text diffs. |
| **GeoTIFF / COG** | Georeferenced raster | Scanned and rectified historical maps; terrain or imagery | Final line art; small schematic maps. |
| **SVG 1.1** | Editable vector master | Maps, charts, diagrams; text and layout edits | EPUB delivery; KDP upload. |
| **PNG** | Publication raster | Kindle EPUB, HTML, PDF proofs | Editing; text search; accessibility. |
| **QML** | QGIS style | Symbology, labels, layout styles | Data storage. |
| **`.qgz`** | QGIS project | Layer list, styles, layout, export settings | Human-readable diffs; it is a zip archive. |
| **Markdown** | Specification and checks | `spec.md`, `checks.md`, `README.md` | Data values; use CSV. |

**Why not Shapefile?** It is a multi-file format with a DBF attribute table, field-name limits, encoding problems, a 2 GB size limit, and inconsistent NULL handling. It is acceptable as an export for a collaborator who requires it; it is not the project archive.

**Why not keep only GeoJSON?** GeoJSON is WGS84-only, has no topology or spatial index, and becomes large quickly. It is excellent for a small, reviewable layer; it is poor for a multi-layer working project.

**Why SVG as master?** SVG is text, editable, diffable, scalable, and convertible. It preserves labels, line styles, and layout in a way a PNG cannot. It is not a delivery format for this book because KDP’s SVG support is minimal and `<text>` is unsupported.

### 4.3 Schemas

**`registry.csv`** — one row per visual. The `caption` and `alt` fields mirror Appendix C and the README register; if they differ, Appendix C and the register control, and the registry is corrected.

```csv
visual_id,display,type,owner,section,title,claim,extent,date_range,crs,svg_path,png_path,width_px,height_px,caption,alt,source_keys,rights_status,status,blocker
ch08-map-01,Map 5,map,Ch. 8,"§§3–5","The Ohio Valley and the Proclamation Line","Campaigns and a claim line, not a surveyed border","Ohio Valley, Great Lakes, and St. Lawrence","1754–1763",EPSG:5070,assets/maps/map-05.svg,assets/maps/map-05.png,1600,2000,"<caption>","<alt>","natl-earth-10m;nps-ohio;statutes-1763",public_domain,planned,"Source locators and label collision check"
```

**`series.csv`** — one row per observation:

```csv
series_id,visual_id,year,value,unit,denominator,universe,source_key,locator,transformation,status,note
fig01-turnout,figure-01,1828,57.6,percent,eligible electorate,"states with popular election",app-1828,"table, 1828",none,unverified,"Eligibility definition pending; do not print until resolved."
```

**`places.csv`** — one row per labeled point:

```csv
place_id,name,alternate_names,lat,lon,valid_from,valid_to,source_key,locator,status,note
place-fort-duquesne,Fort Duquesne,"Fort Pitt; Pittsburgh",40.441,-80.010,1754,1758,nps-fort-duquesne,"site page",verified,"Location approximate; symbol, not a survey."
```

**`layers.csv`** — one row per map layer:

```csv
visual_id,layer_id,path,layer_name,geometry_type,crs,feature_count,source_keys,transformation,status
ch08-map-01,coast,derived/geo/ne_10m_coast.gpkg,coast,LineString,EPSG:4326,1,natl-earth-10m,"clipped to extent; reprojected at render",verified
```

Every cell needs a value. Use `n.a.` for not available and `—` for not applicable; a blank cell is a production error. This mirrors the Appendix B ledger discipline.

### 4.4 What goes in Git

| Item | Commit? | Storage |
|---|---|---|
| Scripts, specs, checks, CSV series, small GeoJSON | Yes | Ordinary Git |
| Final SVG and PNG | Yes | Ordinary Git; PNGs are typically 80–300 KB |
| QGIS projects, GeoPackage, GeoTIFF, large archives | Yes, if rights permit | Git LFS |
| Raw public-domain downloads | Usually no | `data/atlas/raw/` ignored; commit URL + checksum |
| Raw restricted data (NHGIS, Native Land, SlaveVoyages imputed, David Rumsey) | **No** | Ignored cache; commit only citation, recipe, checksum, derived values |
| Build intermediates | No | `build/` ignored |

Add a `.gitattributes` entry:

```gitattributes
*.gpkg  filter=lfs diff=lfs merge=lfs -text
*.qgz   filter=lfs diff=lfs merge=lfs -text
*.tif   filter=lfs diff=lfs merge=lfs -text
*.tiff  filter=lfs diff=lfs merge=lfs -text
*.zip   filter=lfs diff=lfs merge=lfs -text
```

Do not use Git LFS for the final PNGs; they are small and should be available in a normal clone. Do not use Git LFS as a rights workaround: a restricted file in LFS is still redistributed.

### 4.5 Data preparation workflow

1. **Write the specification.** One page in `spec.md`: the claim, the extent, the observation dates, the layers, the labels, the source locators, the caption, the alt text, the rights status, and the checks. If the claim cannot be stated in one sentence, the visual is not ready.
2. **Register the source.** Add `sources.csv` rows before downloading. Record the license and whether the raw file may be committed.
3. **Acquire an immutable raw file.** Download once; record the URL, access date, version, and SHA-256. Do not edit the raw file.
4. **Normalize.** Convert to the working schema: tidy CSV for series, GeoPackage for vector layers, GeoTIFF for rasters. Keep original field names in a crosswalk column; do not silently rename categories.
5. **Transform.** Clip, reproject, simplify, dissolve, join. Record every transformation in `layers.csv` or `series.csv` as `none`, `calculated`, `deflate`, `sum`, `clip`, `reproject`, `simplify`, etc.
6. **Validate.** Row counts, uniqueness, sums, missing values, units, denominators, date ranges, geometry validity, CRS, and label counts. Record results in `checks.md`.
7. **Freeze the snapshot.** Write a `manifest.csv` with the input hashes, output hashes, tool versions, and build date. A change to the data requires a new snapshot and a new hash.
8. **Render.** Produce the SVG master and PNG derivative. Do not edit the PNG by hand; fix the SVG or the data.
9. **Check the render.** 3.5-inch test, grayscale test, font check, PNG check, caption/alt check, and rights check.
10. **Integrate.** Add the PNG reference to the chapter, the row to the README register, and the catalog entry to Appendix C in the same pass.

### 4.6 Historical GIS specifics

- **Boundaries have vintages.** Use the Newberry Atlas of Historical County Boundaries for county change, NHGIS for census geography, and TIGER for modern legal boundaries. Record the vintage in the layer name and the caption. Do not mix a 1850 county boundary with a 2020 census tract and call the result “the county.”
- **Ingest NHGIS deliberately.** NHGIS delivers shapefiles in USA Contiguous Albers (EPSG:5070) with a `GISJOIN` key; join the attributes before reprojecting, convert to GeoPackage, and keep the extract ID. The raw shapefile is not redistributable.
- **Store coordinates in EPSG:4326, project at render.** WGS84 is the interchange CRS; the map’s projection is an argument, not a storage default.
- **Georeference historical maps explicitly.** Use QGIS’s Georeferencer with 8–15 well-distributed control points, record the transformation and RMSE, save the `.points` file, and keep the rectified GeoTIFF. Trace features into a new layer; do not publish the rectified scan unless its rights allow it.
- **Do not modernize historical places silently.** Use the name in force at the map’s date, with the present name in the caption or a note. The gazetteer rules in `data/app-c/README.md` §8 apply.
- **Distinguish claim, survey, occupation, and treaty line.** Line style and caption must say which is which. A dashed line is not a decoration; it is an evidentiary statement.
- **Indigenous territories are not interchangeable with reservations.** Use nation-specific sources, date the layer, and describe the basis. A generic “territory” polygon drawn from a web map is not acceptable.

### 4.7 Indigenous data and consultation

Map 3 (Indigenous political worlds) and Map 12 (northern Plains) require more than a data license. They require a relationship.

- **Native Land Digital is a finding aid, not a boundary authority.** Its Data Sovereignty Treaty permits educational and research use but prohibits storing or distributing API data without explicit permission, modifying boundaries without consultation, and commercial use. Do not put its geometry in `data/atlas/` or trace it into a book map.[^nld]
- **Use nation-specific sources.** Tribal historic preservation offices, nation websites, treaty texts, the *Handbook of North American Indians*, and published nation histories. Cite the nation and the source, not a generic aggregator.
- **Build in review time.** A community reviewer should see the draft map, the labels, and the caption before the asset is called `verified`. Record the review in `checks.md`; do not claim endorsement that was not given.
- **Do not draw a boundary the source does not support.** If the evidence supports a labeled region rather than a line, draw a labeled region. If it supports only a table, use a table.

[^nld]: Native Land Digital, “Data Sovereignty Treaty,” https://api-docs.native-land.ca/data-sovereignty-treaty, accessed November 27, 2026. The treaty permits educational and research uses, prohibits commercial use and storage or distribution without explicit permission, and requires consultation before altering Indigenous land boundaries.

---

## 5. Software for Debian 13

### 5.1 Core install

Debian 13 (trixie) packages everything needed except `mapshaper`, which is a Node package. The following commands install the core stack. They are written for a normal user with `sudo`; review the package list before running.

```bash
sudo apt update

# GIS core
sudo apt install qgis qgis-plugin-grass gdal-bin python3-gdal \
  proj-bin geos-bin spatialite-bin sqlite3 libxml2-utils

# Python analysis and plotting
sudo apt install python3-geopandas python3-shapely python3-pyproj \
  python3-rasterio python3-pyogrio python3-matplotlib python3-pandas \
  python3-mapclassify python3-cartopy python3-pil python3-requests \
  python3-yaml python3-fonttools

# Vector editing, SVG rendering, raster post-processing
sudo apt install inkscape librsvg2-bin resvg imagemagick \
  pngquant optipng zopfli pngcheck

# Build and repository support
sudo apt install git git-lfs make jq csvkit miller nodejs npm

# Optional: R for sf/terra/ggplot2
sudo apt install r-base r-cran-sf r-cran-terra r-cran-ggplot2 \
  r-cran-rmarkdown r-cran-svglite r-cran-jsonlite

# mapshaper is not in Debian; install it through npm
npm install -g mapshaper
```

If a global npm install is not permitted, use `npx mapshaper` or configure a user-level npm prefix. `mapshaper` is optional; GDAL and QGIS can simplify geometry, but mapshaper’s topology-aware simplification is better for crowded boundaries.

### 5.2 Versions in Debian 13

The versions below are the Debian trixie candidates as of November 27, 2026, checked with `apt-cache` on this machine. The packages were not installed for this memo, so the install and rendering commands are a documented plan, not a tested build. Pin them in `data/atlas/toolchain.txt`; do not silently upgrade in the middle of a production batch.

| Package | Version | Role |
|---|---|---|
| `qgis` | 3.40.6 | Desktop GIS, layout, labels, SVG/PDF export, atlas. |
| `qgis-plugin-grass` | 3.40.6 | Optional terrain and raster analysis; not needed for most maps. |
| `gdal-bin` | 3.10.3 | `ogr2ogr`, `gdalinfo`, `gdalwarp`, format conversion, reprojection. |
| `python3-gdal` | 3.10.3 | Python bindings for GDAL/OGR. |
| `proj-bin` | 9.6.0 | `proj`, `cs2cs`, CRS inspection. |
| `geos-bin` | 3.13.1 | Geometry predicates and validation. |
| `spatialite-bin` | 5.1.0a | Spatial SQL on SQLite/GeoPackage. |
| `python3-geopandas` | 1.0.1 | Vector data in pandas; joins, overlays, plotting. |
| `python3-shapely` | 2.1.0 | Geometry operations. |
| `python3-pyproj` | 3.7.1 | CRS transformations. |
| `python3-rasterio` | 1.4.3 | Raster I/O and reprojection. |
| `python3-pyogrio` | 0.10.0 | Fast vector I/O through GDAL. |
| `python3-matplotlib` | 3.10.1 | Charts, schematic maps, SVG output. |
| `python3-pandas` | 2.2.3 | Tabular data. |
| `python3-mapclassify` | 2.8.1 | Choropleth classification; use with care or not at all. |
| `python3-cartopy` | 0.24.1 | Projections and geographic plotting. |
| `python3-pil` | 11.1.0 | Raster image inspection and conversion. |
| `inkscape` | 1.4 | SVG editing, text-to-path, plain-SVG cleanup. |
| `librsvg2-bin` | 2.60.0 | `rsvg-convert` SVG-to-PNG. |
| `resvg` | 0.45.1 | Fast, deterministic SVG-to-PNG. |
| `imagemagick` | 7.1.1 | Flatten, grayscale, palette, metadata, format conversion. |
| `pngquant` | 2.18.0 | Indexed PNG compression. |
| `optipng` | 0.7.8 | Lossless PNG optimization. |
| `zopfli` | 1.0.3 | Slow, high-ratio PNG compression. |
| `pngcheck` | 3.0.3 | PNG structure validation. |
| `git-lfs` | 3.6.1 | Large-file storage. |
| `mapshaper` | npm current | Topology-aware simplification and format conversion. |

QGIS.org also publishes newer packages for trixie (4.2.x and the 3.44 LTR). For a book, the Debian package is the safer default: it is tested against the distribution’s GDAL, PROJ, and Qt versions, and it is reproducible from `apt`. Use the QGIS.org repository or Flatpak only if a specific feature is required, and record the version. Do not mix QGIS packages from Debian and QGIS.org on the same machine.

### 5.3 Fonts

Use one sans-serif family for map labels and chart text. **Inter** is installed on this machine and is packaged as `fonts-inter` (SIL Open Font License). **EB Garamond** is available as `fonts-ebgaramond` and can be used for chart titles if a serif accent is wanted; the book’s body serif is Georgia, which is not a free system font. Do not rely on a font that may be absent on another machine. For final SVG, convert text to paths.

```bash
sudo apt install fonts-inter fonts-ebgaramond
```

Recommended settings:

- Map labels: Inter Medium or SemiBold, 10–13 pt at 300 PPI (roughly 42–54 px at 1,600 px wide).
- Chart labels: Inter Regular, 8–11 pt; chart titles in HTML, not the image.
- No all-caps labels; no letter-spaced small caps inside a 3.5-inch image.
- Label halo: 0.6–0.8 mm white buffer; no drop shadow.

### 5.4 Toolchain verification

Record the versions in `data/atlas/toolchain.txt`:

```bash
qgis --version
gdalinfo --version
ogr2ogr --version
python3 - <<'PY'
import geopandas, shapely, pyproj, rasterio, matplotlib, pandas
print("geopandas", geopandas.__version__)
print("shapely", shapely.__version__)
print("pyproj", pyproj.__version__)
print("rasterio", rasterio.__version__)
print("matplotlib", matplotlib.__version__)
print("pandas", pandas.__version__)
PY
inkscape --version
rsvg-convert --version
resvg --version
magick --version | head -n 1
mapshaper -v
```

If `qgis --version` fails on a headless machine, use `qgis_process --version` or run QGIS with a virtual display. For a reproducible build, record the exact package versions from `dpkg-query -W`.

### 5.5 Tool roles

| Tool | Use it for | Do not use it for |
|---|---|---|
| **QGIS** | Map composition, projections, labels, scale bars, legends, atlas, SVG export | Chart typography; final text editing. |
| **GDAL/OGR** | Format conversion, reprojection, clipping, inspection | Cartographic design. |
| **Python/GeoPandas** | Data cleaning, joins, overlays, validation, simple maps | Complex label placement; final page layout. |
| **R (sf, terra, ggplot2)** | Optional statistical analysis and charts | Duplicating the Python pipeline without a reason. |
| **Matplotlib** | Charts, small multiples, schematic diagrams | Multi-layer geographic maps with many labels. |
| **Inkscape** | SVG cleanup, text-to-path, manual label nudging, final polish | Data analysis; repeated production at scale. |
| **resvg / rsvg-convert** | Deterministic SVG-to-PNG | Editing. |
| **ImageMagick** | Flatten, grayscale, palette, metadata, format conversion | Vector editing. |
| **mapshaper** | Simplification, topology, format conversion | Cartographic design. |

---

## 6. The production pipeline

### 6.1 Overview

```text
source registry
    ↓
raw download (immutable, checksummed)
    ↓
normalized GeoPackage / CSV / GeoTIFF
    ↓
QGIS project  or  Matplotlib script
    ↓
SVG master (live text)
    ↓
outlined SVG (text as paths)
    ↓
PNG (1,600 px wide, 300 PPI, 8-bit, white)
    ↓
QA + caption/alt + register + EPUB
```

The SVG master is the editable source. The outlined SVG is the deterministic render input. The PNG is the publication asset. Do not skip the outlined step if the figure contains text: a renderer without the right fonts will substitute glyphs, change line breaks, or drop labels.

### 6.2 Maps in QGIS

1. **Create the project.** Set the project CRS to the map’s projection, not to WGS84 by default. Load the GeoPackage layers from `data/atlas/derived/geo/`.
2. **Set the page.** For a 1,600 × 2,000 px map at 300 PPI, the layout page is 5.333 × 6.667 inches. For 1,600 × 2,400, use 5.333 × 8 inches. Keep the map item’s aspect ratio locked.
3. **Style for grayscale.** Use the four-tone palette: white land, 15% gray water, 40% gray secondary fill, black boundaries and labels. Use hatching for overlapping claims. Primary lines 4–6 px at final size; secondary 3 px; uncertainty 2 px dotted.
4. **Label with restraint.** Eight labels preferred, twelve maximum. Use a numbered key if more names are needed. Set label priority, a white buffer, and collision avoidance. Check every label at 3.5 inches.
5. **Add only map furniture.** Scale bar, legend, and north arrow if they earn their space. No title, caption, source line, or credit inside the image.
6. **Export SVG.** In the SVG export options, check **Always export as vectors**, **Simplify geometries**, and **Always export text as paths**. Crop to content if the page has excess margin. QGIS’s SVG output is basic because of the underlying Qt library; inspect the result in Inkscape and in `resvg` before accepting it.[^qgissvg]
7. **Save the project and style.** `map.qgz` and `style.qml` are production records. If a GUI step cannot be scripted, write the exact settings in `spec.md`.
8. **Render and inspect.** Convert to PNG with `resvg` or `rsvg-convert`; inspect at 3.5 inches in grayscale; check label collisions and line weights.

[^qgissvg]: QGIS Documentation, “18.3. Creating an Output,” https://docs.qgis.org/3.44/en/docs/user_manual/print_layout/create_output.html, accessed November 27, 2026. The SVG export options include vector export, geometry simplification, and text-as-text-or-outlines; the documentation also notes that SVG output is “very basic” because of the underlying Qt library.

A minimal PyQGIS export script is useful for repeatability. The exact enum names should be checked against the installed QGIS 3.40 API; the structure is:

```python
from qgis.core import Qgis, QgsApplication, QgsLayoutExporter, QgsProject

QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], False)
qgs.initQgis()

project = QgsProject.instance()
project.read("data/atlas/maps/map-05/map.qgz")
layout = project.layoutManager().layoutByName("Map 5")

exporter = QgsLayoutExporter(layout)
settings = QgsLayoutExporter.SvgExportSettings()
settings.exportAsVector = True
settings.simplifyGeometries = True
settings.textRenderFormat = Qgis.TextRenderFormat.AlwaysOutlines
settings.cropToContent = True
exporter.exportToSvg("build/map-05.svg", settings)

qgs.exitQgis()
```

Do not treat this snippet as tested until it runs against the installed QGIS. If the API differs, use the GUI export and record the settings; a documented GUI export is better than an untested script.

### 6.3 Charts in Matplotlib

Matplotlib is the right tool for the three figures and for simple schematic diagrams. It produces clean SVG, has deterministic text-as-path output, and is easy to review in Git.

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({
    "svg.fonttype": "path",          # text as paths, not font references
    "font.family": "Inter",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.linewidth": 0.8,
    "lines.linewidth": 2.0,
    "figure.facecolor": "white",
    "savefig.facecolor": "white",
})

df = pd.read_csv("data/atlas/figures/figure-01/data.csv")
turnout = df[df["series_id"] == "fig01-turnout"].sort_values("year")
fig, ax = plt.subplots(figsize=(5.333, 3.333))  # 1,600 x 1,000 px at 300 PPI
ax.plot(turnout["year"], turnout["value"], marker="o", color="black")
ax.set_xlabel("Year")
ax.set_ylabel("Turnout (percent)")
ax.set_ylim(0, 100)
fig.tight_layout()
fig.savefig("assets/figures/figure-01.svg", format="svg")
```

Matplotlib’s default `svg.fonttype` is `"path"`, which makes the SVG independent of installed fonts; `"none"` keeps editable text but depends on the viewer’s fonts. Use `"path"` for the render copy and keep a separate `"none"` copy only if the text must remain editable.[^mpl]

[^mpl]: Matplotlib, “Fonts in Matplotlib,” https://matplotlib.org/stable/users/explain/text/fonts.html, accessed November 27, 2026. The documentation states that `svg.fonttype` defaults to `'path'`, which computes glyph outlines and makes the SVG look the same on all computers, at the cost of editability.

Chart rules:

- One claim per chart; one to three series.
- No dual axes. If two units cannot share an axis honestly, use two panels or a table.
- No 3D, gradients, drop shadows, or decorative backgrounds.
- No smoothing unless the method, window, and justification are stated. Show observations, not a trend line that hides breaks.
- Label series directly at the end of the line; use a legend only when direct labeling is impossible.
- Put units, denominators, base years, and survey breaks in the caption, not inside the image. Axis labels may be inside.
- For bars, start at zero; for indices, state the base year.
- Use line styles and markers, not color alone; test in grayscale.

### 6.4 SVG standards

The final SVG master should be plain, portable SVG 1.1:

- `xmlns="http://www.w3.org/2000/svg"`.
- A `viewBox` and explicit `width`/`height` in pixels.
- No external references, scripts, fonts, or linked images.
- No `sodipodi:`, `inkscape:`, or RDF metadata in the publication copy.
- No `<text>` in the outlined render copy; text is converted to paths.
- No filters, blurs, drop shadows, or opacity below 100%.
- No embedded raster unless the image is the argument; if embedded, it must be rights-cleared and included in the SVG.
- Stable `id` attributes for groups and layers; named layers matching the QGIS layers.
- Coordinates rounded to the precision the map needs; do not carry 15 decimal places from a reprojection.
- `shape-rendering="geometricPrecision"` only where it helps; test the PNG.

Keep two files when text editing matters:

- `assets/maps/map-05.svg` — live text, editable master.
- `build/map-05-outlined.svg` — text converted to paths, used for rendering.

Do not overwrite the live-text master with the outlined copy. The outlined copy is a build artifact.

### 6.5 SVG to PNG

The preferred renderer is `resvg`: it is fast, has no system-library dependency for rendering, and is designed for reproducible SVG-to-PNG output. `rsvg-convert` is a good second choice. Inkscape is the fallback and the text-to-path tool.

```bash
# 1. Make an outlined, plain-SVG copy for deterministic rendering
mkdir -p build
inkscape assets/maps/map-05.svg \
  --export-text-to-path \
  --export-plain-svg \
  --export-filename=build/map-05-outlined.svg

# 2. Rasterize at 1,600 px wide on white
resvg --width 1600 --background '#ffffff' \
  build/map-05-outlined.svg build/map-05.png

# Alternative renderer (commented; use one renderer per run)
# rsvg-convert -w 1600 -b '#ffffff' \
#   -o build/map-05-rsvg.png build/map-05-outlined.svg

# 3. Flatten, convert to grayscale, set 300 PPI, strip metadata
magick build/map-05.png \
  -background white -alpha remove -alpha off \
  -colorspace Gray -depth 8 -strip \
  -units PixelsPerInch -density 300 \
  PNG24:assets/maps/map-05.png

# 4. Optional: indexed PNG for size
pngquant --quality=65-85 --speed 1 --strip \
  --output build/map-05-indexed.png assets/maps/map-05.png
mv build/map-05-indexed.png assets/maps/map-05.png
```

`resvg` supports `--width` and `--background`; `rsvg-convert` uses `-w` and `-b`, and its DPI options are `--dpi-x` and `--dpi-y`. If the SVG uses physical units, `--dpi-x=300 --dpi-y=300` produces the expected pixel size. If the SVG uses a pixel `viewBox`, `--width` is the reliable control.[^rsvg]

[^rsvg]: Debian manpage, `rsvg-convert(1)`, https://manpages.debian.org/trixie/librsvg2-bin/rsvg-convert.1.en.html, accessed November 27, 2026. The manpage documents `--width`, `--keep-aspect-ratio`, `--background-color`, and `--dpi-x`/`--dpi-y`.

For a grayscale book, `magick` can also map to a fixed palette:

```bash
magick build/map-05.png -colorspace Gray -depth 8 \
  -colors 4 -dither None -strip PNG8:assets/maps/map-05.png
```

Four colors are usually too few for antialiased text. Start with 16 colors, inspect the PNG at 100%, and reduce only if the labels remain clean. `pngquant` usually does a better job than a hard `-colors` quantization. It may remove the PNG’s physical-resolution chunk; if the 300 PPI tag matters for your proof, reset it with `magick ... -units PixelsPerInch -density 300` or keep the truecolor PNG. KDP’s operative check is the pixel dimensions at display size, not the metadata tag.

### 6.6 PNG standards

| Property | Standard | Check |
|---|---|---|
| Width | 1,600 px minimum; 2,400 px for dense labels | `identify -format '%w'` |
| Height | 1,000–2,400 px depending on aspect | `identify -format '%h'` |
| Resolution | 300 PPI metadata at display size | `identify -format '%x x %y'` |
| Color | sRGB RGB (gray pixels are fine); 8-bit | `identify -format '%[colorspace] %[depth]'` |
| Alpha | None; flattened on white | `identify -format '%[channels]'` |
| Format | PNG, not JPEG, for line art | `file` |
| Size | 150–300 KB map target; 80–150 KB figure target; 400 KB hard ceiling | `ls -lh` |
| Text | Lowercase “a” at least 6 px; house target 44–56 px labels | Visual check |
| Background | White; no transparency | Visual check |

KDP accepts PNG and JPEG, not SVG. It recommends 300 PPI at display size, at least 1,200 × 1,800 px for a full-page image, and 960 × 1,440 px at 80% width. The project’s 1,600–2,400 px range is deliberately above that floor so labels survive zoom. A 2,400 × 3,600 indexed PNG can be smaller than a 1,600 × 2,400 RGB PNG; measure the actual file, not the pixel count.[^kdp]

[^kdp]: [`docs/kindle.md`](kindle.md) §7.1, which cites KDP’s image guidelines. The key constraints are PNG/JPEG, 300 PPI at display size, no transparency, sRGB, HTML captions, and no SVG dependence.

### 6.7 Make targets

Add targets to the repository `Makefile` rather than running ad hoc commands. A minimal design:

```make
ATLAS := data/atlas
MAP_IDS := 01 05 07 08 09 10 11 12 13
FIG_IDS := 01 02 03

.PHONY: atlas atlas-check atlas-manifest

atlas: $(addprefix assets/maps/map-,$(addsuffix .png,$(MAP_IDS))) \
       $(addprefix assets/figures/figure-,$(addsuffix .png,$(FIG_IDS)))

assets/maps/%.png: assets/maps/%.svg scripts/atlas/render_svg.sh
	scripts/atlas/render_svg.sh $< $@

assets/figures/%.png: assets/figures/%.svg scripts/atlas/render_svg.sh
	scripts/atlas/render_svg.sh $< $@

atlas-check:
	python3 scripts/atlas/check_atlas.py

atlas-manifest:
	python3 scripts/atlas/manifest.py > $(ATLAS)/manifest.csv
```

The exact pattern rules depend on whether the SVG is generated by QGIS or Matplotlib. Keep the render script idempotent: given the same outlined SVG and the same `resvg` version, it should produce the same PNG bytes, or at least the same pixels. Set `SOURCE_DATE_EPOCH` if a tool embeds a timestamp.

### 6.8 Reproducibility

- **Pin the toolchain.** Record `qgis`, `gdal`, `python3-geopandas`, `matplotlib`, `inkscape`, `resvg`, and `mapshaper` versions in `toolchain.txt`.
- **Pin the data.** Record the source version, extract ID, access date, and SHA-256 in `sources.csv`.
- **Pin the transformation.** Record every clip, reproject, simplify, dissolve, join, and calculation in `layers.csv` or `series.csv`.
- **Pin the render.** Keep the `.qgz`, `.qml`, and `build.py`; export settings are part of the source.
- **Freeze the output.** Final SVGs and PNGs are committed; `build/` is ignored. A release tag identifies the exact assets.
- **Rebuild in a clean environment.** At least once, build the pilot on a fresh Debian 13 container or user account. If it fails, the record is incomplete.

---

## 7. Cartographic and chart standards

### 7.1 Projections

Store in EPSG:4326; project for the argument. Recommended defaults:

| Extent | Projection | Why |
|---|---|---|
| Contiguous United States | **EPSG:5070**, NAD83 / Conus Albers | Equal-area; familiar federal mapping; good for thematic maps. |
| North America | **ESRI:102008**, North America Albers Equal Area Conic | Equal-area continental view; includes Canada and Mexico. |
| World | **EPSG:8857**, Equal Earth, or **ESRI:54030**, Robinson | Equal-area or compromise world; avoid Web Mercator for thematic area. |
| North Atlantic / Arctic | **EPSG:3574**, North Pole LAEA Atlantic | Useful for Norse and Arctic routes; preserves distances from the pole. |
| Alaska | **EPSG:3338**, Alaska Albers | Equal-area; standard for Alaska maps. |
| Southeast Asia | **EPSG:32648**, WGS 84 / UTM zone 48N, or a regional Lambert | Local scale; check the longitude range; use 49N if the theater crosses 108°E. |
| Local or corridor | State Plane or a custom Lambert Conformal Conic | Choose for the corridor; state the CRS in the caption if scale matters. |

Do not use Web Mercator for a choropleth or an area comparison. Do not use a projection that makes the argument look stronger than it is; a route map that exaggerates distance is a historical claim.

### 7.2 Map design

- **One claim per map.** If the map needs a paragraph to explain what it shows, it is a table or a diagram.
- **Crop to the theater.** Empty ocean and irrelevant interior are not neutral; they shrink the evidence.
- **Eight to twelve labels.** Use a numbered key for more. A map with 30 labels fails at 3.5 inches.
- **Four tones plus hatching.** White land, 15% water, 40% secondary fill, black lines and labels. Hatching for overlapping claims, railroad grants, or uncertainty.
- **Line hierarchy.** Primary 4–6 px, secondary 3 px, uncertainty 2 px dotted at final size. Hairlines disappear on E-Ink.
- **No terrain.** No relief shading, satellite imagery, gradients, drop shadows, or 3D. The argument is historical, not pictorial.
- **No color-only encoding.** If two categories need color to differ, they need a pattern or a label.
- **Scale bar and north arrow only if useful.** A schematic flow diagram does not need a north arrow.
- **Date every layer.** A boundary, route, or reservation is dated in the caption or a label. A map without dates is a collage.
- **Distinguish evidence from inference.** Solid documented route, dashed inferred route; solid surveyed boundary, dashed claim; dotted uncertain. Explain the convention in the caption or legend.

### 7.3 Chart design

- **One claim per chart.** The slope, the gap, or the break is the argument.
- **One to three series.** More series become a table or small multiples.
- **No dual axes.** Two units on one frame invite a false comparison. Use two panels or a table.
- **Direct labeling.** Label the line at its end; reserve the legend for cases where direct labeling collides.
- **Show observations.** Do not smooth a series unless the method is stated and the raw observations remain visible.
- **State breaks.** A survey-house change, a definition change, or a missing year is part of the evidence.
- **Zero baseline for bars.** For indices, state the base year. For percentages, state the denominator.
- **Grayscale-safe.** Use line style, marker shape, and direct labels; test with a grayscale conversion.
- **No chartjunk.** No 3D, gradients, drop shadows, background images, or decorative icons.

### 7.4 Labels, legends, captions

- **Inside the image:** map labels, legend, scale bar, axis labels, and data labels. No title, caption, source line, or credit.
- **Outside the image:** figure number, title, caption, source line, credit, and alt text, in HTML.
- **Caption:** what the visual shows, the date or observation years, the geographic unit, the denominator or base year, the transformations, and the limit. It does not repeat the title.
- **Source line:** the data series or object, the repository, the identifier, and the transformation. “Library of Congress” alone is not a source line.
- **Alt text:** 140 characters or fewer; describe the subject and scope, not every label. The approved strings live in Appendix C and the README register; do not invent a second set.
- **Text in the image:** labels at 44–56 px at 1,600 px; at 2,400 px, scale them proportionally to 66–84 px so the physical size stays the same. Lowercase “a” at least 6 px; no rotated vertical labels if a horizontal label fits.

### 7.5 Accessibility

A map that cannot be read by a screen reader needs a text alternative that carries the argument. Provide:

- A short alt text in the `<img>`.
- A longer description in the surrounding prose when the visual carries a claim that the alt cannot.
- A table or list alternative for precise values.
- Patterns and labels, not color alone.
- No essential text baked into the image without an HTML equivalent.

---

## 8. Rights and provenance

### 8.1 Rights workflow

1. **Identify the object and the digital surrogate.** A LoC scan of a 1784 map is not the same rights object as the 1784 map; the scan may have its own terms.
2. **Read the item-level rights statement.** A collection-level “public domain” tag is not a clearance for every item.
3. **Record the license and the attribution string** in `sources.csv`.
4. **Decide whether the raw file may be committed.** If no, commit the citation, URL, checksum, and derived values only.
5. **Clear the map as a whole.** A public-domain base with a copyrighted inset is not clear.
6. **Record the permission.** Keep the permission email or license in a private `rights/` folder; record the status and date in `sources.csv`.
7. **Credit the maker and the repository.** “Drawn for this volume from …” is a production credit, not a rights statement.

### 8.2 License matrix

Use the matrix in §3.4. The most important rules:

- **No NC data in a commercial book without permission.** This affects SlaveVoyages imputed data, Native Land, and some David Rumsey items.
- **No NHGIS raw data in the repository.** Publish derived values and cite the extract.
- **No Native Land geometry in the repository or the map.** Use it as a finding aid; consult nations.
- **No “public domain” claim for a post-1929 map without a rights check.** Copyright may persist, and the host’s tag may be wrong.
- **No AI-generated historical maps.** Use deterministic cartography; record any AI-assisted cleanup.[^ai]

[^ai]: `data/app-c/README.md` §2.8: “Use deterministic cartography and plotting for Maps 1–13 and Figures 1–3: QGIS, Matplotlib, R, or vector drawing. Do not use generative image models for historical maps, routes, boundaries, or labels.” The cover is a separate AI-generated asset and does not authorize interior maps.

### 8.3 Source lines

A finished map’s source line should be specific enough that a reader can find the evidence:

> Sources: Natural Earth 1:10m, coastlines; U.S. Geological Survey, National Hydrography Dataset; National Park Service, Fort Necessity National Battlefield, campaign map; Proclamation of 1763, text from the *Statutes at Large*. Modern state boundaries from TIGER/Line 2026 are a reference frame only. Drawn for this volume.

A chart’s source line:

> Source: Pew Research Center, “Public Trust in Government: 1958–2025,” December 4, 2025; question wording and survey breaks in the notes; includes Pew’s required attribution and disclaimer.

Do not put the source line inside the PNG. The image carries labels; the HTML carries the evidence.

---

## 9. Quality assurance

### 9.1 Data checks

- Row count matches the source extract or the documented subset.
- Every row has a unique stable ID.
- Every value has a unit and an observation year.
- Percentages have a denominator; money has a year and a price index if constant dollars.
- Categories preserve the source’s definitions; no silent merging of “Black” and “enslaved,” “Hispanic” and “Latino,” or “Indian” and “Native American.”
- Sums reconcile, or the note explains why independently rounded components do not add.
- Missing values are `n.a.`, not zero; not applicable is `—`.
- The source version and locator are recorded.

### 9.2 Geometry checks

- Geometry is valid (`ST_IsValid` or GeoPandas `is_valid`).
- No self-intersections, duplicate vertices, or empty geometries.
- CRS is declared and matches the layer’s purpose.
- The layer is clipped to the map extent; no stray features from a global extract.
- Coordinates are rounded to the map’s precision; no 15-decimal noise.
- Polygon fills do not cover water or another category by accident.
- Labels fall inside the correct polygon or on the correct line.
- The map’s scale bar is correct in the projected CRS.

### 9.3 Visual checks

- **3.5-inch test:** view the PNG at 3.5 inches wide, grayscale, at reader default size. Can you understand the claim without zooming?
- **Label test:** eight to twelve labels; no collisions; no label smaller than 44 px at 1,600 px; lowercase “a” at least 6 px.
- **Line test:** primary lines survive; dotted uncertainty is visible; hatching is distinguishable from gray fill.
- **Grayscale test:** convert to grayscale; no two categories collapse into the same tone.
- **Photocopy test:** print at 100% black and white; the map still reads.
- **Caption test:** the caption states date, unit, denominator, and limit; the image does not repeat the caption.
- **Alt test:** the alt text describes the subject and scope in 140 characters or fewer.

### 9.4 Output checks

```bash
# SVG is well-formed and has no external references
xmllint --noout assets/maps/map-05.svg
grep -E '<image|sodipodi:|inkscape:|<script|xlink:href' assets/maps/map-05.svg || true

# PNG properties
identify -format '%f %wx%h %[colorspace] %[depth] %[channels] %x x %y\n' \
  assets/maps/map-05.png
pngcheck -v assets/maps/map-05.png

# File size
ls -lh assets/maps/map-05.png

# Text as paths: the outlined file should have no <text> elements
grep -c '<text' build/map-05-outlined.svg || true
```

Pass conditions: 1,600 px or 2,400 px wide; 300 PPI; 8-bit; no alpha; PNG; 150–300 KB map target or 80–150 KB figure target; no `<text>` in the outlined file; no external references; no missing glyphs.

### 9.5 Integration checks

- The chapter references the visual by its display number, and the number exists in the README register.
- The caption and alt text match Appendix C and the register.
- The source line cites the same source keys as the chapter notes.
- The PNG path resolves from the chapter (`../assets/maps/map-05.png`). Pandoc resolves the image relative to the chapter for the EPUB; the HTML and PDF outputs in `build/` resolve the same path back to the repository `assets/` directory.
- Use the repository’s existing figure markup; if none exists, use a Pandoc figure block or a raw HTML `<figure>` with `<figcaption>`, then verify the EPUB and PDF output.
- The EPUB build embeds the PNG; the PDF proof places it without cropping.
- The visual is not promised in Appendix C unless the asset exists.
- The README status is updated from `planned` to `sourced`, `produced`, or `verified` only when the corresponding evidence exists.

### 9.6 Acceptance checklist

- [ ] Specification, source registry, and checks file exist.
- [ ] Every source has a license, locator, and `note_key`.
- [ ] Raw restricted data is not tracked; derived values are.
- [ ] Data checks pass; unknowns are declared, not guessed.
- [ ] Geometry is valid and correctly projected.
- [ ] The map passes the 3.5-inch and grayscale tests.
- [ ] Labels are 8–12, legible, and collision-free.
- [ ] SVG is plain, outlined, and free of external references.
- [ ] PNG is 1,600/2,400 px wide, 300 PPI, 8-bit, no alpha, and within the 150–300 KB map or 80–150 KB figure target.
- [ ] Caption, alt text, source line, and credit are in HTML.
- [ ] Rights status is `public_domain`, `open_access`, `permission_pending`, `community_pending`, or `cleared`.
- [ ] README register and Appendix C are updated in the same pass.
- [ ] `make check` and the EPUB/PDF builds pass; rendered pages are inspected.

---

## 10. Implementation plan

### 10.1 Phase 0 — Ratify the decisions (1 week)

- Resolve the 13/3/2 versus 39/9/8 program in `README.md` and `data/app-c/README.md` §13.
- Confirm whether the book will be sold commercially; this determines whether NC sources can be used at all.
- Confirm whether a print edition is planned; this determines whether 2,400–3,200 px assets or vector PDFs are needed.
- Appoint a community reviewer for Maps 3 and 12.
- Approve the storage policy: public-domain derivatives in Git, restricted raw data out.

**Gate:** no “TBD” on the visual count, commercial status, or Indigenous review.

### 10.2 Phase 1 — Build the pilot (1–2 weeks)

Produce **Map 5** and **Figure 1** end to end.

- Map 5: Ohio Valley, 1754–1763; NPS/NARA and the *Statutes at Large*; Natural Earth coast; original routes and claim line; 8–10 labels; one grayscale test; one SVG/PNG render.
- Figure 1: votes and turnout, 1824–1840; Appendix B Table 2 and APP; one line/bar combination; direct labels; one caption and alt text.

**Gate:** both assets pass §9.6; the pipeline is documented; the time estimate for a map and a chart is measured, not guessed.

### 10.3 Phase 2 — Build the infrastructure (1 week)

- Create `data/atlas/` with `registry.csv`, `sources.csv`, `toolchain.txt`, `README.md`.
- Add `.gitattributes` for LFS; add `data/atlas/raw/` to `.gitignore`.
- Add `scripts/atlas/render_svg.sh` and `check_atlas.py`.
- Add `make atlas`, `make atlas-check`, `make atlas-manifest`.
- Write the first `spec.md` and `checks.md` templates.
- Add the `assets/maps/` and `assets/figures/` directories; update the Makefile dependencies if needed.

**Gate:** a clean checkout can render the pilot with one command.

### 10.4 Phase 3 — Acquire and normalize data (2–3 weeks)

- Complete `sources.csv` for the 13 maps and three figures.
- Acquire public-domain layers; convert to GeoPackage/GeoJSON; record checksums.
- Request or download NHGIS extracts; keep raw files out of Git.
- Georeference Tanner 1840 for Map 7; save GCPs and rectified GeoTIFF.
- Build the `places.csv` gazetteer for labels.
- Build the `series.csv` for Figures 1–3.
- Record access failures and alternates in `checks.md`.

**Gate:** every layer and series has a source, a license, a locator, and a checksum; no map depends on an unconsulted source.

### 10.5 Phase 4 — Produce in batches (8–14 weeks)

Batch A: Maps 1–4 (deep history, contact, Indigenous worlds, Atlantic circuit).
Batch B: Maps 5–9 (empire, revolution, canals, removal, Mexico).
Batch C: Maps 10–13 (Civil War, final campaigns, Plains, Vietnam).
Batch D: Figures 1–3.

For each visual: spec → data → QGIS/Matplotlib → SVG → outlined SVG → PNG → checks → caption/alt → register.

**Gate:** every visual has a `produced` asset and a `checks.md`; no visual is `verified` until rights, caption, alt, and rendered inspection are complete.

### 10.6 Phase 5 — QA and integration (2 weeks)

- Run `check_atlas.py` across all assets.
- Inspect every PNG at 3.5 inches and in grayscale.
- Reconcile the README register, Appendix C catalog, chapter references, captions, and alt text.
- Build EPUB and PDF; inspect the images, captions, and page breaks.
- Measure the converted EPUB size; confirm the image payload is within the 2.5–5 MB target.
- Archive the final SVG/PNG set and the manifest.

**Gate:** the release build contains every promised visual, no broken image, no missing alt text, and no unresolved rights blocker.

### 10.7 Effort and cost

| Item | Planning estimate | Notes |
|---|---|---|
| Pilot map (Map 5) | 3–4 days | Includes research, data prep, cartography, SVG/PNG, QA. |
| Simple schematic map | 2–3 days | Map 4, Map 13. |
| Complex layered map | 4–6 days | Map 8, Map 12; includes consultation and hatching tests. |
| Chart | 1–2 days | Figure 1 is the simplest; Figure 3 needs survey-break documentation. |
| QA per visual | 0.5–1 day | 3.5-inch, grayscale, PNG, caption, alt, rights. |
| 13 maps + 3 figures | 8–14 weeks full-time; 12–20 weeks part-time | Planning estimate, not a promise; consultation and data access can extend it. |
| Software | US$0 | All core tools are free and open source. |
| Fonts | US$0 | Inter and EB Garamond are OFL. |
| Data | US$0–2,500/year | Only if a paid source becomes essential; library access first. |
| Storage | US$0–5/month | Git LFS data pack if the repository exceeds the free tier. |
| Proofs | US$0–50 | Print proofs for grayscale inspection. |

The largest cost is labor, not software. The second largest is the cost of redoing a map because its source was wrong or its rights were unclear. The pilot and the source registry are the cheapest insurance against both.

---

## 11. Risks and open decisions

### 11.1 Risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| A source’s license forbids commercial use or redistribution | High | High | License review before download; public-domain alternatives; permission record. |
| Historical boundary or route is drawn more precisely than the evidence | High | High | Dashed uncertainty; date every layer; caption limits; reviewer. |
| Indigenous map is extracted from a generic web source | Medium | High | Nation-specific sources; community review; no Native Land geometry. |
| QGIS SVG output is incomplete or renderer-dependent | Medium | Medium | Pilot test; text as paths; `resvg`; Inkscape cleanup; PNG inspection. |
| Font substitution changes labels | Medium | Medium | Outline text; keep a live-text master; test on a clean machine. |
| PNG file size exceeds the Kindle budget | Medium | Medium | Indexed PNG; simplify geometry; measure the converted EPUB. |
| Git repository bloats with rasters and GeoPackages | Medium | Medium | Git LFS; ignore raw; commit only derived layers. |
| Tool versions drift during production | Medium | Medium | Pin versions; record in `toolchain.txt`; rebuild the pilot. |
| AI-generated map is used and triggers disclosure or accuracy problems | Low | High | No generative models for maps; record any AI-assisted cleanup. |
| Schedule slips because the visual program is unresolved | High | Medium | Ratify 13/3/2 or 39/9/8 before mass production; batch. |

### 11.2 Open decisions

| Decision | Options | Recommended | Owner |
|---|---|---|---|
| Visual program | 13/3/2 or 39/9/8 | Approve the smaller program in the README, or explicitly retain the larger one | Author |
| Commercial status | Sold, free, or both | Confirm before relying on NC sources | Author |
| Print edition | EPUB only or print too | Decide before setting final pixel sizes | Author |
| Map engine | QGIS, Python, or both | QGIS for maps; Matplotlib for charts | Cartographer |
| Storage | Git LFS or external archive | Git LFS for working binaries; external archive for raw restricted data | Author |
| Paid data | None, library, or subscription | None initially; library access for HSUS/Roper | Author |
| Community reviewer | Named or deferred | Name before Map 3/12 production | Author |
| Font | Inter, Source Sans, or other | Inter | Cartographer |
| Pilot | Map 5 + Figure 1 | Yes | Cartographer |

### 11.3 Recommended decisions

1. **Adopt the smaller visual program only through the README process.** Do not let a production document silently change the book’s promises.
2. **Use QGIS 3.40.6 from Debian trixie.** It is stable, packaged, and sufficient. Do not mix repositories.
3. **Use `resvg` for SVG-to-PNG.** Keep `rsvg-convert` as a fallback and Inkscape for text-to-path.
4. **Store working vector data in GeoPackage, series in CSV, small exchange layers in GeoJSON, rasters in GeoTIFF.** Do not archive in Shapefile.
5. **Commit final SVG and PNG; keep raw restricted data out.** Use Git LFS for GeoPackage, QGIS projects, and GeoTIFF.
6. **Use public-domain sources first.** Do not buy a subscription until a specific visual cannot be sourced otherwise.
7. **Pilot Map 5 and Figure 1.** Measure the time, then decide whether 13 or 39 is realistic.

---

## 12. Sources consulted

All URLs were accessed November 27, 2026. Prices and terms change; verify before purchase or publication. This is a research memo, not a manuscript unit; its source list is not a substitute for the combined citation notes in the Introduction, chapters, or appendices.

**Project sources**

1. [`README.md`](../README.md) — book plan, visual register, page budget, and status record.
2. [`AGENTS.md`](../AGENTS.md) — evidence, citation, house style, and acceptance standards.
3. [`data/app-c/README.md`](../data/app-c/README.md) — Appendix C overhaul plan, 13/3/2 target, design rules, and stage gates.
4. [`docs/kindle.md`](kindle.md) — KDP format, image, caption, accessibility, and file-size constraints.
5. [`docs/kindle-visuals-research.md`](kindle-visuals-research.md) — Kindle legibility and conversion analysis.
6. [`data/app-b/README.md`](../data/app-b/README.md) — ledger, cell schema, source-key, and status discipline.

**Tools and formats**

7. QGIS, “Installation Guide,” https://qgis.org/resources/installation-guide/
8. Debian, `qgis` 3.40.6, https://packages.debian.org/trixie/qgis
9. Debian, `gdal-bin` 3.10.3, https://packages.debian.org/trixie/gdal-bin
10. Debian, `python3-geopandas` 1.0.1, https://packages.debian.org/trixie/python3-geopandas
11. Debian, `inkscape` 1.4, https://packages.debian.org/trixie/inkscape
12. Debian, `librsvg2-bin` 2.60.0, https://packages.debian.org/trixie/librsvg2-bin
13. Debian, `resvg` 0.45.1, https://packages.debian.org/trixie/resvg
14. QGIS Documentation, “18.3. Creating an Output,” https://docs.qgis.org/3.44/en/docs/user_manual/print_layout/create_output.html
15. Matplotlib, “Fonts in Matplotlib,” https://matplotlib.org/stable/users/explain/text/fonts.html
16. Debian manpage, `rsvg-convert(1)`, https://manpages.debian.org/trixie/librsvg2-bin/rsvg-convert.1.en.html
17. `resvg`, GitHub, https://github.com/linebender/resvg
18. Mapshaper, “The command-line tool,” https://mapshaper.org/docs/essentials/command-line.html
19. GeoParquet 1.1.0 specification, https://geoparquet.org/releases/v1.1.0
20. FlatGeobuf, https://flatgeobuf.org/
21. Git LFS, https://git-lfs.com/

**Data and rights**

22. IPUMS NHGIS, “Terms of Use,” https://nhgis.org/ipums-nhgis-terms-use
23. IPUMS NHGIS, “GIS Files,” https://www.nhgis.org/gis-files
24. U.S. Census Bureau, “TIGER/Line Shapefiles,” https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
25. U.S. Census Bureau, “Citing our Data,” https://www.census.gov/about/policies/citation.html
26. Natural Earth, “Terms of Use,” https://www.naturalearthdata.com/about/terms-of-use/
27. USGS, “Are there any costs or restrictions to usage of data downloaded from The National Map?,” https://www.usgs.gov/faqs/are-there-any-costs-or-restrictions-usage-data-downloaded-national-map
28. National Archives, “Frequently Asked Questions,” https://www.archives.gov/faqs
29. Library of Congress, “Reproductions of Library of Congress Cartographic Material,” https://www.loc.gov/rr/geogmap/reproduce.html
30. Newberry Library, “Atlas of Historical County Boundaries: Download State Files,” https://publications.newberry.org/ahcb/downloads/states.html
31. SlaveVoyages, “Legal,” https://www.slavevoyages.org/blog/legal/180
32. David Rumsey Map Collection, “Copyright and Permissions,” https://www.davidrumsey.com/about/copyright-and-permissions
33. Native Land Digital, “Data Sovereignty Treaty,” https://api-docs.native-land.ca/data-sovereignty-treaty
34. OpenStreetMap, “Copyright and License,” https://www.openstreetmap.org/copyright
35. Pew Research Center, “Terms of Use,” https://www.pewresearch.org/about/terms-and-conditions/
36. FRED, “Terms of Use,” https://fred.stlouisfed.org/docs/api/terms_of_use.html
37. BEA, “Data Application Programming Interface,” https://apps.bea.gov/API/signup/
38. BLS, “Copyright Information,” https://www.bls.gov/opub/copyright-information.htm
39. Smithsonian, “Open Access,” https://www.si.edu/openaccess

**Series and platforms**

40. MIT Election Data and Science Lab, “Data,” https://electionlab.mit.edu/data
41. American Presidency Project, “Election Listing,” https://www.presidency.ucsb.edu/statistics/elections
42. A New Nation Votes, https://elections.lib.tufts.edu/
43. Pew Research Center, “Public Trust in Government: 1958–2025,” December 4, 2025, https://www.pewresearch.org/politics/2025/12/04/public-trust-in-government-1958-2025/
44. FDIC, “Managing the Crisis: Chronological Overview,” https://www.fdic.gov/bank/historical/managing/chronological/pre-fdic.html
45. Social Explorer, https://www.socialexplorer.com/ (individual pricing reported at about $195/month by Software Advice and Capterra; site license by quote).
46. PolicyMap, “Pricing,” https://policymap.com/pricing (public edition free; paid plans by quote; published estimates around $2,200/year for Basic).
47. SimplyAnalytics, https://simplyanalytics.com/ (library subscription; a 2018 *American Libraries* report gave about $900/quarter for one concurrent user).
48. Esri, “ArcGIS Business Analyst,” https://www.esri.com/en-us/arcgis/products/arcgis-business-analyst/buy (quote; a G2 estimate lists about $1,100/user/year).
49. Statista, “Account Overview,” https://www.statista.com/accounts/ (Basic free; Starter about $199/month; Personal about $649/month; Professional by quote).
50. Cambridge, *Historical Statistics of the United States*, Millennial Edition, https://hsus.cambridge.org/ (individual online price reported at about $1,450 in an older review; verify current).
51. Roper Center, “Fees for Membership, iPOLL, and Datasets,” https://ropercenter.cornell.edu/fees
52. ICPSR, “Membership,” https://icpsr.umich.edu/web/pages/membership/datafair/schedule.html
53. Data Axle, “Reference Solutions,” https://www.data-axle.com/platforms-products/reference-solutions/

---

*This document is a production plan. It does not replace the README register, the Appendix C catalog, or the evidence checks in `AGENTS.md`. The next action is to ratify the visual program and run the Map 5 / Figure 1 pilot.*

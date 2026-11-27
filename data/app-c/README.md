# Appendix C visual program overhaul plan

**Status:** Proposed, November 25, 2026; source-image note added November 26, 2026. No manuscript file has been changed, and none of the 56 registered assets has been produced as a publication asset. Two source images are on file: [`images/hiawatha-wampum-belt.jpg`](../../images/hiawatha-wampum-belt.jpg) and [`images/aids-quilt.jpg`](../../images/aids-quilt.jpg). Neither is a cleared or produced publication asset; see §3.4. This is a production plan, not a competing book outline. [`README.md`](../../README.md) remains the book plan; [`AGENTS.md`](../../AGENTS.md) remains the process and style authority. When this plan changes scope, numbering, or a registered visual, the change must be applied to the README, [`chapters/53-appendix-c.md`](../../chapters/53-appendix-c.md), and the owning chapter in the same pass.

**Inputs:** [`docs/kindle-visuals-research.md`](../../docs/kindle-visuals-research.md) for the Kindle constraints and the conversion options; [`docs/kindle.md`](../../docs/kindle.md) for the current KDP rules; the README illustration register for the 56 registered assets; the Appendix C Stage 3 outline for each asset’s argument and evidence.

**Repository note.** This file is not one of the 56 manuscript files, so `tools/check_book.py` does not check it. The manuscript rules in `AGENTS.md` still govern any prose moved from this plan into the book. The file layout follows the `data/app-b` production pattern: a README, a ledger, a checks file, and machine-readable data.

**Contents:** [Why](#1-what-changes-and-why) · [Design rules](#2-design-rules) · [Target program](#3-target-program-and-numbering) · [13 maps](#4-the-13-maps-to-keep) · [3 figures](#5-the-three-figures-to-keep) · [2 images](#6-the-two-images-to-keep) · [Located images](#34-optional-images) · [38 conversions](#7-the-38-conversions) · [Gazetteer](#8-gazetteer-overhaul) · [Step-by-step](#9-step-by-step-plan) · [Change map](#10-file-by-file-change-map) · [Validation](#11-validation-and-acceptance) · [Risks](#12-risks-and-open-decisions) · [Decisions](#13-decision-record) · [Done](#14-what-done-looks-like)

**The decision in one paragraph.** Keep **18 produced visuals**: 13 schematic maps, three line charts, and two archival photographs. Convert **38 registered visuals** into Kindle-native HTML: comparison and chronology tables, primary-source exhibit boxes, and close readings. Convert the 76-row gazetteer table into a dictionary-style list. Renumber the survivors. Move production detail and the caption/alt schedules out of the printed appendix into `data/app-c/`. The result is a smaller, sharper, more accessible visual program that preserves each chapter’s argument and cuts the potential image payload from 15–35 MB to about 2.5–5 MB.

**What this plan does not do.** It does not rewrite the appendix, the chapters, or the README. It does not produce an asset or clear a right. It does not change the 50-chapter architecture. It does not close the separate 46-page gap between the current 954-page PDF proof and the 1,000-page floor. Stage 1 begins only after the decisions in §13 are approved.

---

## 1. What changes, and why

### 1.1 The release target is Kindle

The book is being prepared for a reflowable Kindle EPUB, not a print page. That changes the visual brief in five ways:

- **Screen size.** A 6–7 inch E-Ink Kindle gives roughly 3.5–4.2 inches of usable image width. A continental U.S. county map puts most eastern counties at 2–4 pixels wide. A 13-column table set to the page is worse.
- **Grayscale.** Most dedicated Kindles render 16 levels of gray. Red, blue, and third-party colors in an election map collapse into indistinguishable middle grays. Color cannot be the only carrier of meaning.
- **Reflow.** The reader controls type size and margins. A figure cannot assume a fixed page, a facing caption, or a two-page spread. A table cannot assume a fixed column width.
- **KDP rules.** Images need 300 PPI at display size, maps and charts with text should occupy at least 80% of screen width, line art should be PNG, SVG support is minimal, captions and alt text must be HTML, and tables should be real HTML tables rather than images.
- **Delivery cost.** At the 70% royalty option, KDP deducts US$0.15 per MB in the U.S. based on the converted file size. A 56-image raster program at 0.5 MB per image adds about 28 MB, or about $4.20 per sale. An 18-image program at 150–300 KB per image adds about 2.7–5.4 MB, or about $0.40–$0.81.

The practical target is not “no images.” It is **fewer, bolder, higher-contrast drawings plus more real text**.

### 1.2 The current plan’s failure modes

The Stage 3 outline is a strong piece of research, but much of its visual program assumes print-like page detail. Four failure modes recur:

1. **County choropleths.** Maps 34, 36, 37, 38, and 39 ask a 3.5-inch grayscale screen to carry 3,100 counties. The pattern becomes noise, and the small-denominator distortion the outline itself warns about becomes invisible.
2. **Multi-panel objects.** Maps 2, 9, 33, 34, and 38, and Figures 4 and 7, divide an already small image into panels. Each panel loses the labels that made the argument.
3. **Full-page documents.** Images 4, 5, and 6 reproduce a catalog spread, a newspaper broadsheet, and a legal form. At 3.5 inches, the text is unreadable without pinch-zooming; the reader sees a gray rectangle, not evidence.
4. **Color-coded classifications.** Maps 21, 22, 23, 28, and 35 use color or shading to distinguish legal status, alliance, or regime change. Those are classifications, not terrain. A table states them exactly and survives grayscale, search, and screen readers.

The outline also plans 56 raster assets at once. That is a large cartographic and rights workload for arguments that often fit in a 4-column table.

### 1.3 The target program

| Class | Current | Target | What happens |
|---|---:|---:|---|
| **Maps** | 39 | 13 drawn | 26 convert to tables or a documented merge |
| **Figures** | 9 | 3 drawn | 6 convert to benchmark or chronology tables |
| **Images** | 8 | 2 reproduced | 6 convert to exhibit tables or close readings |
| **Produced visuals** | 56 | **18** | 13 maps + 3 figures + 2 images |
| **Optional images** | 0 | 0–2 | Two candidates on file: a 1909 public-domain Hiawatha Belt halftone and a 1992 AIDS Quilt photograph that is not the panel and is not cleared; ceiling 20 |
| **Source images on file** | 2 | 2 | `images/hiawatha-wampum-belt.jpg` and `images/aids-quilt.jpg`; neither is a publication asset |
| **Gazetteer** | 76-row, 5-column table | 77-entry dictionary list | No table clipping; 77 names reconciled with the README |
| **Appendix C** | About 20,900-word production outline | ~3,000-word reader catalog | Production detail moves to `data/app-c/` |
| **Image payload** | 5.6–22.4 MB at 100–400 KB each | 2.5–5.0 MB | 13 maps, 3 figures, 2 photos |

The 18 survivors sit inside the 15–20 range proposed in `docs/kindle-visuals-research.md`; the 38 conversions sit inside its 35–40 range. The appendix will promise only the 18 baseline visuals and the tables that exist; it will not retain a 56-item catalog of absent assets. That removes the KDP missing-content risk described in `docs/kindle.md`. The 18 survivors are not simply the “best” old visuals. They are the assets whose argument is genuinely spatial or tonal and can be reduced to a single panel, eight to twelve large labels, and four gray tones. Everything else becomes text.

### 1.4 The conversion test

An asset stays drawn only if all six answers are yes:

1. **Spatial or tonal.** The argument depends on relative position, route, distance, layering, or the tonal contrast of a photograph. A list of legal categories does not.
2. **Single panel.** It can be understood in one frame, or in two vertically stacked panels that each stand alone. Side-by-side panels fail.
3. **Label cap.** It can carry eight to twelve labels at 44–56 px in a 1,600 px-wide image. If it needs more, the detail moves to the caption or a table.
4. **Gray-safe.** It still works in four tones: white, 15% gray, 40% gray, black. If two categories need color to differ, it converts.
5. **Cropped.** It shows the theater of the argument, not “all of North America” for a local story. Empty ocean and irrelevant interior are cut.
6. **Rights-clean.** The base data are public domain or licensed; a photograph has a rights basis and a credit. If not, it converts or waits.

If any answer is no, the default is a table, an exhibit, or a close reading. A drawn visual is the exception, not the default.

---

## 2. Design rules

### 2.1 The 3.5-inch test

Every kept visual is judged at 3.5 inches wide, in grayscale, at the reader’s default type size. The test is not “can I zoom in?” It is “can a reader who does not zoom understand the claim?” A map that needs zoom to find the Ohio forks has failed.

Practical consequences:

- **Label size.** At 1,600 px wide and 3.5 inches displayed, a 44–56 px label is about 7–9 pt. That is the working range. The KDP minimum of a 6 px lowercase “a” is a file-level floor, not a readability standard.
- **Label count.** Eight preferred, twelve maximum. Use a numbered key for nine to twelve; put the names in a large legend, not scattered across the image.
- **Line weight.** 4–6 px for primary lines, 3 px for secondary, 2 px dotted for uncertainty. Hairlines disappear on E-Ink.
- **No terrain.** No relief shading, satellite imagery, gradients, drop shadows, or 3D effects. White land, 15% gray water, black lines, one 40% fill, and hatching.
- **No title.** The figure number, title, caption, source line, and credit are HTML. Only map labels, legends, scale bars, and data labels go inside the image.
- **No “see the map below.”** Alt text describes the subject and scope; it does not point.

### 2.2 The grayscale palette

| Tone | Use | Hex | E-Ink behavior |
|---|---|---|---|
| **White** | Land, paper | `#FFFFFF` | Base |
| **15% gray** | Water, background regions | `#D9D9D9` | Visible but quiet |
| **40% gray** | Secondary fill, reservations, urban areas | `#999999` | Distinct from 15% |
| **Black** | Boundaries, routes, labels | `#000000` | Maximum contrast |
| **Hatching** | Overlapping claims, railroad grants | Black lines on white or 15% | Survives photocopy and grayscale |

Do not use more than four tones plus hatching. A 16-level gradient looks smooth on a monitor and muddy on E-Ink. Convert the final art to grayscale and inspect it on a gray palette before export.

### 2.3 KDP production rules

| Rule | Requirement | Project response |
|---|---|---|
| **Format** | JPEG and PNG supported; TIFF, animated GIF, and transparency not. | Maps and figures: indexed PNG, flattened on white, no alpha. Photographs: JPEG, quality 80–85. |
| **Color** | sRGB; CMYK converted. | Author in grayscale, export sRGB-tagged RGB. |
| **Resolution** | 300 PPI at display size; 1,200 × 1,800 px full-page minimum; 960 × 1,440 at 80% width. | Maps 1,600 × 2,400; figures 1,600 × 1,000–2,000; photos 1,600 px long edge. |
| **Display width** | Maps and charts with text at least 80% of screen width. | `width: 100%` on the figure image; one dimension only. |
| **Line art** | PNG; text lowercase “a” at least 6 px. | PNG; labels 44–56 px at 1,600 px width. |
| **SVG** | Minimal support; `<text>` unsupported; more than 25 SVG images breaks Enhanced Typesetting. | SVG only as an editing master in `assets/source/`; PNG in the EPUB. |
| **Captions** | HTML below the image, not raster. | `<figcaption>` with title, caption, source, credit. |
| **Alt text** | 140 characters or fewer; meaningful images need it. | `data/app-c/captions.csv` is the single source of truth. |
| **File size** | No image count limit; delivery fee applies. | 13 maps at 150–300 KB; 3 figures at 80–150 KB; 2 photos at 150–300 KB. These are ceilings, not quotas: a simpler map that passes the 3.5-inch test at 80–120 KB is better. |

### 2.4 Table rules for a 6-inch screen

KDP allows up to 100 rows and 11 columns. That is not the Kindle design limit. On a 6-inch screen, five columns collapse to roughly 0.6 inches each; the table viewer helps, but it does not fix a bad comparison. This plan uses a stricter house standard for new tables:

- **Four columns maximum**, including the leading label column. Five columns are allowed only for a numeric matrix with short cells that passes the font-size-3 test; otherwise split it into two panels.
- **24 rows maximum** per table block. Split at a natural break or move the full series to Appendix B.
- **Twelve words maximum** per cell. Move definitions and caveats to the caption and notes.
- **No merged cells, no nested tables, no images of tables.** Use lettered panels if a matrix needs two levels.
- **Caption and headers.** In Markdown, keep the house caption paragraph and bold leading cell. The build’s Lua filter moves the caption into `<caption>` before the table and the leading cell into `<th scope="row">` (to be added, per `docs/kindle.md` §8.3).
- **One table, one job.** A table that tries to show election results, secession dates, and slave-state status at once will fail.

These rules are stricter than KDP’s because the target is a 6-inch screen, not a desktop table viewer.

### 2.5 The merge-before-add rule

A conversion is not automatically a new table. Before adding one:

1. Open the owning chapter’s existing tables.
2. Open Appendix B Tables 1–8.
3. If the data already exist, **merge** into the existing table or print a short excerpt with a cross-reference.
4. If the data are new but belong to a national series, **add a panel** to the relevant Appendix B table and print an excerpt in the chapter.
5. Only then add a chapter table with the next free display number.

Two known merges are already visible:

- **Old Map 23** duplicates Chapter 30’s existing “Instruments of Caribbean control” table. Expand that table; do not add another.
- **Old Map 16’s election half** duplicates Chapter 20’s existing 1860 election table. Add only the secession chronology.

This rule is what keeps the overhaul from turning every conversion into another table.

### 2.6 Typographic replacement forms

Every converted asset takes one of five forms:

| Form | Use | Shape |
|---|---|---|
| **Comparison table** | Legal status, alliances, regional circuits, program placement | 3–4 columns; 3–12 rows; a caption that states the comparison |
| **Chronology table** | Secession, regime change, neutrality statutes, disfranchisement | Date-led; 4 columns; 6–14 rows |
| **Benchmark table** | Debt, revenue, turnout, industry, media | Year-led; 3–4 columns; 4–6 benchmark years; units in the header |
| **Primary-source exhibit** | Catalog page, radio schedule, literacy test, forecast graphic | A bordered box with a short intro, a 2–4 column transcription table or numbered list, and a source line |
| **Close reading** | Hiawatha Belt, AIDS Quilt panel | The existing In Focus prose, 150–250 words, with no required image |

Sidebars use the existing bold labels. Quantitative comparisons use **The measure.**; object or document readings use **A closer look.** or **In Focus.** Do not invent a “By the Numbers” or “Geography in Brief” label without amending AGENTS §6 in the same change.

### 2.7 Captions, alt text, and rights

- The caption states what the visual shows, its date or observation years, its geographic unit, and its limits. It does not repeat the title.
- The source line names the data series or object and the repository. “Library of Congress” alone is not a source line.
- The credit names the maker or institution. A public-domain object still needs a credit.
- The CC0 dedication covers the book’s original text, not a third-party photograph, map, or facsimile. Each reproduced object has its own rights basis.
- Alt text is 140 characters or fewer. It describes the subject and scope, not every label.
- A community-held object needs community authorization. A photograph of a wampum belt is not the belt; a catalog image of a medal is not the medal’s history.
- Copyright and cultural authority are different questions. The 1909 Hiawatha halftone is public domain as a printed work, but it depicts a belt in the Thacher collection and still needs Haudenosaunee review. The 1992 Quilt photograph is not made public domain by an NIH host page; it carries a visible © NAMES Project credit and is not the first panel.
- If permission fails, withdraw the image and keep the close reading. Do not substitute an unregistered stock image.
- No visual or table enters a chapter or the appendix without a README register row. A table added in Stage 5 gets its register row in the same pass.

### 2.8 AI and asset format

Use deterministic cartography and plotting for Maps 1–13 and Figures 1–3: QGIS, Matplotlib, R, or vector drawing. Do not use generative image models for historical maps, routes, boundaries, or labels. If an AI-assisted tool is used for cleanup or layout, record it and classify it for KDP disclosure. The cover is already AI-generated and recorded for KDP disclosure; it is not part of this program.

Keep SVG or another editable master in `assets/source/`. Export the publication asset to PNG (maps and figures) or JPEG (photographs). The README register’s current `.svg` asset paths are editing intentions, not EPUB assets; change them to `.png` in Stage 3.

---

## 3. Target program and numbering

### 3.1 New sequences

The survivors are renumbered sequentially in narrative order. Sparse old numbers (“Map 32” as the thirteenth map) would look like a production error and would force readers to wonder what happened to Maps 14–31.

**Maps 1–13**

| New | Old | Owner | Title |
|---:|---:|---|---|
| **Map 1** | Map 1 | Ch. 1, §4.1 | Cultural regions and centers, c. 1200 CE |
| **Map 2** | Map 2 | Ch. 2, §2 | Norse voyages in the North Atlantic, c. 1000–1100 |
| **Map 3** | Map 3 | Ch. 3, §4 | Indigenous political worlds, c. 1600, simplified |
| **Map 4** | Map 5 | Ch. 5, §2 | The English Atlantic circuit, c. 1680 |
| **Map 5** | Map 8 | Ch. 8, §§3–5 | The Ohio Valley and the Proclamation Line, 1754–1763 |
| **Map 6** | Map 9 | Ch. 10, §3; Ch. 11, §§2–6 | War for Independence, 1775–1783 |
| **Map 7** | Map 12 | Ch. 15, §1 | Canals and railroads crossing the Appalachians, 1825–1840 |
| **Map 8** | Map 13 | Ch. 17, §2 | Removal corridors and Indian Territory, 1830–1846 |
| **Map 9** | Map 14 | Ch. 18, §§2–5 | The Nueces–Río Grande strip and the 1848 cession |
| **Map 10** | Map 17 | Ch. 21, §§2–3, 6 | Civil War theaters, 1861–1863 |
| **Map 11** | Map 18 | Ch. 22, §§1–2 | The final campaigns, 1864–1865 |
| **Map 12** | Map 20 | Ch. 25, §§1–5 | Layered claims in the northern Plains, 1876–1890 |
| **Map 13** | Map 32 | Ch. 41, §4 | Southeast Asia supply routes, 1954–1968 |

**Figures 1–3**

| New | Old | Owner | Title |
|---:|---:|---|---|
| **Figure 1** | Figure 3 | Ch. 16, §2.3 | Presidential votes and turnout, 1824–1840 |
| **Figure 2** | Figure 7 | Ch. 33, §2.2 | Bank failures and unemployment, 1929–1933 |
| **Figure 3** | Figure 9 | Ch. 50, §3 | Trust in the federal government, 1958–2025 |

**Images 1–2**

| New | Old | Owner | Object |
|---:|---:|---|---|
| **Image 1** | Image 2 | Ch. 14, §2 In Focus | A Jefferson peace medal, both faces, 1801 |
| **Image 2** | Image 3 | Ch. 25, §4 In Focus | Tom Torlino, 1882 and 1885 |

**Located candidates.** Two optional source images are on file and are not part of the 18-visual baseline. They are recorded in §3.4; neither adds a display number until it is cleared.

**Catalog entry shape.** Each entry is 30–40 words, not a production record:

> **New Map 6. War for Independence, 1775–1783.** Two vertical panels trace the northern and southern campaigns, with French naval power and the 1783 settlement shown only where documented. Chs. 10–11.

### 3.2 What happens to the old IDs

The 38 converted assets do not disappear from the record. Each keeps its old ID in `data/app-c/triage.csv`; the 18 survivors also appear in `data/app-c/renumbering.csv`, with their replacement table, exhibit, or close reading. The retired numbers are not reused. The reader-facing appendix does not print “formerly Map 17”; the production record does.

The **38 conversions in one line each**:

- **26 maps:** 4, 6, 7, 10, 11, 15, 16, 19, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39.
- **6 figures:** 1, 2, 4, 5, 6, 8.
- **6 images:** 1, 4, 5, 6, 7, 8.

### 3.3 Stable IDs and display numbers

Existing table IDs in the README (`ch20-table-01`, `ch08-table-03`) encode a display number. They remain as permanent keys even when a new table is inserted before them and the display number changes. The register will show the stable ID and the new display number separately.

New tables use **descriptive stable IDs** (`ch04-table-settlements`, `ch35-table-neutrality`) rather than a number that will shift. This is a deliberate exception to the old `chNN-table-MM` pattern; it prevents a false stability and makes the merge audit readable. The final display number is assigned in Stage 5 by order of first textual reference.

### 3.4 Optional images

The baseline is 18. Two optional source images are now on file. Neither is authorized for baseline use, and neither adds a display number until its checks are met.

| Candidate | File and dimensions | What it is | Rights and status |
|---|---|---|---|
| **Hiawatha Belt** (old Image 1) | [`images/hiawatha-wampum-belt.jpg`](../../images/hiawatha-wampum-belt.jpg); 1,210 × 2,448 px; about 540 KB | A 1909 halftone captioned “Hiawatha Wampum Belt,” printed in *New York at the Jamestown Exposition, Norfolk, Virginia, April 26 to December 1, 1907* (Albany: J.B. Lyon Co., 1909), p. 209, from the belt lent by John Boyd Thacher; the Flickr scan is from scan page 218, while the book’s list of illustrations gives p. 209. The Thacher belts were the subject of *Onondaga Nation v. Thacher*, 189 U.S. 306 (1903). The 1909 volume does not establish that this belt is the object now held by the Onondaga Nation. | Public domain as a 1909 U.S. publication; the scan is from the Internet Archive. Haudenosaunee cultural-protocol review and a provenance note are still required. `sourced`; not a publication asset. |
| **AIDS Memorial Quilt** (old Image 7) | [`images/aids-quilt.jpg`](../../images/aids-quilt.jpg); 1,800 × 1,355 px; about 551 KB | A 1992 photograph of the entire Quilt on the National Mall, with the Washington Monument; the visible credit reads “photograph by Mark Thiessen ©1992 The NAMES Project.” It is not the first panel and does not show Marvin Feldman’s panel. | Not cleared. The Wikimedia Commons public-domain tag rests on an NIH host page; independent records credit Mark Thiessen and The NAMES Project Foundation. Permission from the foundation is required, and the caption must identify the 1992 display, not the first panel. `permission_pending`; blocked as Image 7. |

- **Hiawatha Belt.** If the Haudenosaunee review and the provenance note are accepted, add the halftone as **Image 3** (old Image 1). Do not present it as a new photograph of the present object. The close reading stands without it.
- **AIDS Memorial Quilt.** The 1992 photograph cannot serve as Image 7. If a quilt photograph is wanted, clear the rights and caption it as the 1992 display; otherwise keep the close reading and add no image.

The optional images do not block the baseline, the table of contents, or the page budget. If neither is approved, the book has 18 visuals; if both are, 20. Do not add a stock photograph, a redrawn schematic, or the 1992 wide view as a substitute for the first panel.

### 3.5 Budgets

**Text pages.** The Appendix C allowance rises from 5 to 6 pages after a measured proof. The 38 conversions yield 37 new tables before merges: two are close readings with no table, Map 23 is a merge, and Map 38 becomes three small tables. Two kept visuals also split off small tables — the post-1492 panel of Map 2 and the price panel of Figure 2 — so the working estimate is **39 potential new tables**. After merges, expect about 30–35, which would take the README’s current 80 display tables to roughly 110–115. That adds roughly 12–16 text pages, plus the one-page Appendix C increase. The total planning budget moves from 1,031 to about 1,044–1,048 text pages, still above the 1,000-page floor. This is an estimate; the proof governs.

**Image payload.**

| Class | Count | Target each | Total |
|---|---:|---:|---:|
| Maps | 13 | 150–300 KB | 2.0–3.9 MB |
| Figures | 3 | 80–150 KB | 0.24–0.45 MB |
| Photographs | 2 | 150–300 KB | 0.30–0.60 MB |
| Optional images | 0–2 | 150–300 KB | 0–0.60 MB |
| Text and EPUB overhead | — | 2.11 MB | 2.11 MB |
| **Total** | **18–20** | — | **4.6–7.7 MB** |

At US$0.15 per MB, the 70% delivery fee is about $0.69–$1.16. If KDP classifies the CC0 book as public domain and limits it to the 35% option, no delivery fee is deducted; the size still matters for download time and for the 70% scenario. Measure the converted file in KDP or Kindle Previewer, not the raw EPUB.

---

## 4. The 13 maps to keep

Each map below is a **single-panel schematic** unless the row says two vertical panels. “Labels” means the maximum large labels inside the image, not the number of names in the caption.

| New | Owner | Crop and labels | Grayscale form | Source and limit |
|---|---|---|---|---|
| **Map 1** | Ch. 1, §4.1 | North America; 6 regional blocks and 4 dated centers; 10 labels | White land, 15% water, black boundaries, 40% fill for earlier earthworks, dotted Serpent Mound symbol | NPS, UNESCO, Ohio History Connection; site dates approximate; Serpent Mound date disputed |
| **Map 2** | Ch. 2, §2 | North Atlantic; 6 labels: Scandinavia, Iceland, Greenland, L’Anse aux Meadows, Labrador, Vinland | Solid documented route, dashed saga or uncertain route, 15% water | Parks Canada; no post-1492 panel; Tordesillas moves to a Chapter 2 table |
| **Map 3** | Ch. 3, §4 | Eastern North America; 8 numbered regions, 2 confederacy symbols; 12 labels | Dotted range boundaries, no fills, 15% water, names in a key | Nation-specific sources; Native Land as a finding aid only. If names or boundaries cannot be verified, convert to a Chapter 3 table |
| **Map 4** | Ch. 5, §2 | Four-node schematic: West Africa, Caribbean, mainland colonies, Britain; 8 labels | Boxes and simple coastlines only; thick solid arrows for captive labor and staples, dashed for manufactures | SlaveVoyages and Appendix B Table 6; do not imply arrow width equals volume unless stated |
| **Map 5** | Ch. 8, §§3–5 | Ohio Valley, Great Lakes, St. Lawrence; 10 labels; Proclamation Line labeled “continues beyond frame” | Black campaign arrows, dashed claim line, 15% water, no imperial color fills | NPS and Avalon Project; distinguish a claim from a surveyed border |
| **Map 6** | Ch. 10, §3; Ch. 11, §§2–6 | Two vertical panels: North and Canada; South and alliance; 6 labels each | Solid and dashed arrows; French fleet as a double line; 15% water; no color | NPS and Library of Congress; one object, one number; no single arrow from Boston to Yorktown |
| **Map 7** | Ch. 15, §1 | Mohawk–Pennsylvania–Ohio corridor; 8 labels; no national network | Solid completed, dashed projected; black lines; 15% water; no terrain | Tanner 1840; show the Erie Canal’s Mohawk crossing; do not imply all canals crossed the Appalachians |
| **Map 8** | Ch. 17, §2 | Southeast and Indian Territory; four principal corridors, each labeled by the nations it carried; 8 labels | Broad 15% bands for routes, black outlines; dates in the caption; no single “Trail of Tears” line | NPS and Cherokee Nation; show resident nations in Indian Territory as a note, not a fill |
| **Map 9** | Ch. 18, §§2–5 | Texas and northeastern Mexico; 8 labels; “Pacific theater not shown” | Black boundary lines, dotted disputed strip, three campaign arrows; no color | NPS and National Archives; distinguish the cession from prewar Mexican states and Indigenous territories |
| **Map 10** | Ch. 21, §§2–3, 6 | Eastern states through the Mississippi; three theater bands; 10 labels | Black lines, 15% water, no color; the Mississippi as the spine; dates in the caption | NPS and Library of Congress; include the Trans-Mississippi as a labeled edge, not an arrow |
| **Map 11** | Ch. 22, §§1–2 | Two vertical panels: Virginia; Georgia and the Carolinas; 6 labels each | Black arrows; supply routes dotted; no color | NPS and American Battlefield Trust; do not merge the Overland Campaign and the March to the Sea |
| **Map 12** | Ch. 25, §§1–5 | Northern Plains; 8 labels; Black Hills marked with a sacred-site symbol | Thick dashed treaty boundary; 15% reservation fill; diagonal hatching for railroad grants; dotted range outline | National Archives and NPS; date every layer; Black Hills as a sacred landscape, not a resource |
| **Map 13** | Ch. 41, §4 | Vietnam, Laos, Cambodia; 6 labels; no world map | Braided dashed trail; other routes dotted; 15% water; black borders | Pentagon Papers and FRUS; the trail is a network, not a single road |

**Map-specific notes.**

- **Map 1** must label the six blocks as analytical cultural regions, not political territories. It must show Poverty Point and Hopewell as earlier earthworks, not as active c. 1200 CE centers. Cahokia’s population is a range, not a point.
- **Map 2** drops the post-1492 Atlantic exchange. That material becomes Chapter 2’s “Voyages, claims, and exchanges after 1492” table, counted separately in §3.5. The map is stronger as a Norse story than as a two-panel world.
- **Map 3** is the highest-risk survivor. If the nation names, ranges, and confederacy forms cannot be verified with nation-specific sources, convert it to the Chapter 3 nation table and drop the drawn count to 12. Do not draw approximate boundaries from a single web map.
- **Map 4** is a flow diagram, not an atlas map. It belongs in the Map sequence because its argument is spatial, but it uses no basemap beyond simple coastlines.
- **Map 6** keeps two panels because the war’s two connected fronts are the argument. Stack them vertically; do not put them side by side.
- **Map 12** is the only map that uses hatching. It must survive a photocopy: treaty boundary, reservation fill, railroad grant, and range outline must be distinguishable in black and white.

---

## 5. The three figures to keep

| New | Owner | Chart form | Data and limit |
|---|---|---|---|
| **Figure 1** | Ch. 16, §2.3 | Five observations, 1824–1840; turnout line over vote bars; denominator in the caption | American Presidency Project and *Historical Statistics*; mark legislative-selection states; do not imply a universal electorate |
| **Figure 2** | Ch. 33, §2.2 | Two vertical panels: bank suspensions (bars); unemployment, Lebergott and Darby (two lines); prices move to a Chapter 33 table | FDIC, BLS, FRED; label both unemployment definitions; no single unlabeled “unemployment” line |
| **Figure 3** | Ch. 50, §3 | Individual poll observations, 1958–2025; survey-house breaks; no moving average | Pew Research Center; state question wording and sampled population; declining trust is not by itself democratic decline |

**Figure notes.**

- **Figure 1** is the one chart where the visual slope carries the argument: the 1828 and 1840 jumps are the story. Keep it simple. Put the state-law caveats in the caption and the chapter text.
- **Figure 2** is a two-panel chart, not a triptych. Moving prices to the Chapter 33 price table (counted in §3.5) removes the third panel and the incompatible units. The contrast between Lebergott and Darby is the analytical point; two lines on one panel make it visible.
- **Figure 3** is a single-series line with dots. Do not smooth it. The breaks between survey houses are part of the evidence.

---

## 6. The two images to keep

| New | Owner | Object | Reproduction specification | Rights |
|---|---|---|---|---|
| **Image 1** | Ch. 14, §2 In Focus | Jefferson peace medal, obverse and reverse, 1801 | Both faces at the same scale; 1,600 × 1,000 px; JPEG 85; high contrast; no book caption inside the image | Smithsonian National Museum of American History, object 1990.0466.0001; confirm the media’s open-access status; credit the museum |
| **Image 2** | Ch. 25, §4 In Focus | Tom Torlino, 1882 and 1885, Carlisle Indian Industrial School | The paired composite as one image; preserve the original object captions; 1,600 px long edge; JPEG 85 | Dickinson College, Carlisle Indian School Digital Resource Center, CIS-I-0039; the underlying 1882 and 1885 photographs are in the public domain in the U.S.; confirm the archive’s terms for the composite; credit |

**Image notes.**

- **Image 1** works because the object is two high-contrast metal faces with almost no small text. The engraver dispute (Robert Scot versus John Reich) belongs in the caption and note, not in the image.
- **Image 2** works because the before-and-after contrast is tonal and emotional. Reproduce the pair as the archive published it; do not separate the two portraits or crop out the original captions. The original captions are object content, not the book’s caption; the book’s caption remains HTML below the image.

**Optional candidates.** The two optional source images are not in this baseline table. A 1909 public-domain Hiawatha halftone and a 1992 AIDS Quilt photograph are recorded in §3.4; the quilt photograph is not the first panel and is not cleared.

---

## 7. The 38 conversions

The tables below are the working disposition. Each replacement gets a full one-page specification in Stage 2. “New table” means a chapter table with a descriptive stable ID and a display number assigned in Stage 5. “Merge” means no new table.

**Numbering note.** In §§7.1 and 7.4, map numbers refer to the **old** sequence; the new drawn maps run only to 13. Old figures above 3 and old images above 2 are likewise retired numbers.

### 7.1 Maps to tables, exhibits, or merges (26)

| Old | Owner | Replacement | Form | Content specification | Merge and evidence rule |
|---:|---|---|---|---|---|
| **Map 4** | Ch. 4, §§1–5 | Ch. 4, `ch04-table-settlements` | Comparison table | 4 cols: Settlement; Founded; Homeland and colonial body; Key event. 7 rows: Jamestown, Plymouth, Massachusetts Bay, Providence, Connecticut, New Haven, Pequot. | No existing data table. Compare the two regions without a two-region map. |
| **Map 6** | Ch. 6, §4 | Ch. 6, `ch06-table-wars` | Chronology matrix | 4 cols: Conflict; Dates; Parties and alliances; Outcome or instrument. 6 rows: Metacom’s War, King William’s War, Queen Anne’s War, Covenant Chain, 1713 settlement, Tuscarora War. | No existing data table; debate table stays last. |
| **Map 7** | Ch. 7, §§1–3 | Ch. 7, `ch07-table-regions` | Regional comparison | 4 cols: Region; Staples and exports; Ports and migration; Revival or event. 4 rows: Chesapeake, Lowcountry, Middle Colonies, New England. | No existing data table. Keep Salem, Stono, Enfield, and New York in separate rows or notes, not one causal frame. |
| **Map 10** | Ch. 12, §§1, 5 | Ch. 12, `ch12-table-ratification` | Chronology table | 4 cols: State; Ratification date and vote; Western claim or cession; Note. 13 rows. | Check Appendix B Table 3 for cessions; do not duplicate. The inset map retires. |
| **Map 11** | Ch. 14, §2 | Ch. 14, `ch14-table-louisiana` | Document comparison | 4 cols: Instrument or expedition; Dates; Claim or route; Documentation. 5 rows: treaty, Lewis and Clark, Pike, Spanish presence, Indigenous nations. | No existing table. Distinguish a treaty claim from a traveled route; no continental route map. |
| **Map 15** | Ch. 19, §3 | Ch. 19, `ch19-table-kansas` | Legal chronology | 4 cols: Government or territory; Dates; Legal basis; Status or violence. 5 rows: Kansas Territory, Nebraska Territory, proslavery government, free-state government, Lecompton. | Ch. 19 already has fugitive-cases and 1856-election tables. This is new; place it before the debate table and renumber. |
| **Map 16** | Ch. 20, §§1–4 | Merge election into `ch20-table-01`; add `ch20-table-secession` | Merge plus chronology | Election data already in Table 1; add a “States carried” column so the state-level result survives. Secession table: 4 cols: State; Ordinance date; Vote; Note. 11 rows. | **High-renumbering chapter.** The secession table becomes Table 2; resources becomes Table 3; debate becomes Table 4. Update every reference. |
| **Map 19** | Ch. 23, §§2–4 | Ch. 23, `ch23-table-reconstruction` | Institutional matrix | 4 cols: District or state; Dates; Legal basis; Violence or participation. 6 rows: five military districts plus the South Carolina counties. | No existing data table. No county choropleth; violence and martial law in separate columns. |
| **Map 21** | Ch. 27, §§4–5 | Ch. 27, `ch27-table-empire` | Legal-status table | 4 cols: Place; Year; Instrument; Practical status. 5 rows: Hawaii, Guam, Puerto Rico, Philippines, Cuba. | No existing table. Annexation, occupation, and treaty control in separate cells; no imperial color fill. |
| **Map 22** | Ch. 29, §5 | Ch. 29, `ch29-table-suffrage` | Classification table | 3 cols: Status; States with year and scope; Note. 3 rows: full, presidential or partial, none. | Ch. 29 already has the 1912 election table. New table is separate; use state lists, not a 48-row cross-hatched map. |
| **Map 23** | Ch. 30, §1.4 | **Merge into `ch30-table-01`** | Existing table expansion | Add rows or columns for leased bases, occupations, customs receiverships, and treaty rights; keep the instruments distinct. | **Do not add a table.** The existing Chapter 30 Table 1 covers the same ground. Expand it and update its caption and source line. |
| **Map 24** | Ch. 31, §2.4 | Ch. 31, `ch31-table-aef` | Campaign table | 4 cols: Engagement; Date; Sector or units; Outcome or casualties. 5 rows: Cantigny, Belleau Wood, Château-Thierry, Saint-Mihiel, Meuse-Argonne. | Check `ch31-table-01` for overlapping casualty rows; merge if possible; do not duplicate. |
| **Map 25** | Ch. 32, §5 | Ch. 32, `ch32-table-migration` | Demographic table | 4 cols: Place; Black population 1910; Black population 1930; Change. 8 rows: origins and destinations. | Appendix B Table 1 supplies national and regional counts; print an excerpt. No proportional-symbol map at 3.5 inches. |
| **Map 26** | Ch. 34, §§1.5, 3.5 | Ch. 34, `ch34-table-newdeal` | Program table | 4 cols: Program; Sites or units; Dates; Measure or limit. 4 rows: TVA dams, CCC camps, public works, Dust Bowl migration. | Appendix B Table 8 supplies national benchmarks; cite it. No point-symbol map. |
| **Map 27** | Ch. 36, §§1–2 | Ch. 36, `ch36-table-theaters` | Theater comparison | 4 cols: Theater; Command; Principal campaigns; Supply problem. 3 rows: European, Mediterranean, Pacific. | No existing table. The argument is command and supply, not a world map. |
| **Map 28** | Ch. 37, §2 | Ch. 37, `ch37-table-containment` | Commitment matrix | 4 cols: Country or region; Instrument; Year; Status. 12 rows: NATO founders, Greece and Turkey 1952, bilateral treaties, occupied territories, bases. | No existing table. No world shading; date the snapshot to the end of 1952. |
| **Map 29** | Ch. 38, §2.5 | Ch. 38, `ch38-table-metro` | Regional table | 4 cols: Region or metro; 1940; 1960; Change or note. 8 rows. | Appendix B Table 1; print an excerpt. Distinguish total and Black population change in notes. |
| **Map 30** | Ch. 39, §§1–6 | Ch. 39, `ch39-table-rights` | Campaign and registration table | 4 cols: Campaign or site; Dates; Action; Registration before and after. 8 rows. | No existing table. Keep campaign sites and registration results in separate columns; state the Black voting-age denominator. |
| **Map 31** | Ch. 40, §2 | Ch. 40, `ch40-table-poverty` | Need and provision table | 4 cols: Region or group; Poverty rate; Program placement; Note. 6 rows. | Appendix B Table 7 for national context. State the retrospective poverty definition; no choropleth. |
| **Map 33** | Ch. 42, §1 and Legacies | Ch. 42, `ch42-table-elections` | Election matrix | 4 cols: Year; Candidate; Popular vote share; Electoral vote. 6 rows: 1968 three candidates, 1972 two. | Appendix B Table 2; print an excerpt. No red, blue, and third-party map. |
| **Map 34** | Ch. 43, §1 | Ch. 43, `ch43-table-work` | Regional table | 4 cols: Region or metro; Employment 1969 to 1979; Absolute change; Percent change. 8 rows. | Appendix B Table 7. Do not let small-count areas dominate; keep both absolute and percentage columns. |
| **Map 35** | Ch. 44, §§3, 5 | Ch. 44, `ch44-table-1989` | Chronology table | 4 cols: State; Date; Event; Legal form or note. 14 rows. | No existing table. Date each regime change; distinguish a state boundary, a declared independence, and an uncertain claim. |
| **Map 36** | Ch. 45, §1 | Ch. 45, `ch45-table-boom` | Regional table | 4 cols: Region or metro; Population growth; Employment growth; Note. 8 rows. | Appendix B Table 7. No county choropleth; state units and dates. |
| **Map 37** | Ch. 46, §5 | Ch. 46, `ch46-table-housing` | Exposure table | 4 cols: Metro or county group; Lending measure; Foreclosure measure; Coverage note. 8 rows. | No existing table. State HMDA coverage; no county average as individual risk. |
| **Map 38** | Chs. 47–49 | `ch47-table-electoral`, `ch48-table-electoral`, `ch49-table-electoral` | Three small matrices | Panel A, 4 cols: Year; Winner; Popular vote share; Electoral vote. Panel B, 4 cols: Year; Metro margin; Suburb margin; Non-metro margin. 3–6 rows each. | Appendix B Table 2; no duplicate full series. Do not leak 2020 or 2024 into an earlier chapter. |
| **Map 39** | Ch. 49, §§1, 4 | Ch. 49, `ch49-table-border` | Regional table | 4 cols: County or metro; GDP; Employment; Sector or trade note. 8 rows. | Appendix B Table 7. GDP is not household income; source trade exposure separately. |

**Why these 26 convert.**

- Maps 4, 6, 7, 10, 11, 15, and 16 are comparisons or chronologies plotted on geography. Their arguments are about sequence, legal form, or regional difference, not distance.
- Maps 19, 21, 22, 23, 28, and 35 are legal or institutional classifications. A table states the categories exactly; a map collapses them into shades.
- Maps 24, 25, 26, 27, 29, 30, 31, 33, 34, 36, 37, and 39 are event inventories or county-level statistics. At 3.5 inches, the pattern is noise; a table with exact denominators is stronger.
- Map 38 is a multi-panel electoral sequence. Three small chapter tables preserve the dated panels without reprinting a shared map.

### 7.2 Figures to tables (6)

| Old | Owner | Replacement | Form | Content specification | Merge and evidence rule |
|---:|---|---|---|---|---|
| **Figure 1** | Ch. 9, §1 | Ch. 9, `ch09-table-debt` | Benchmark table | 4 cols: Year; Debt series A; Debt series B; Colonial revenue. 4 rows: 1756, 1763, 1765, 1770. | Show the range; do not choose one series silently. No dual-axis chart. |
| **Figure 2** | Ch. 13, §2 | Ch. 13, `ch13-table-debt` | Benchmark table | 4 cols: Year; Funded debt; Customs revenue; Ratio or note. 4 rows: 1790, 1795, 1800, 1801. | Appendix B Table 7. Distinguish stock and flow; state the fiscal year. |
| **Figure 4** | Ch. 24, §1 | Ch. 24, `ch24-table-industry` | Benchmark table | 4 cols: Year; Rail mileage; Steel output; Urban share and threshold. 4 rows: 1865 or 1870, 1880, 1890, 1900. | Appendix B Tables 1 and 7. Three units, no shared axis; state urban thresholds. |
| **Figure 5** | Ch. 26, §4.3 | Ch. 26, `ch26-table-disfranchise` | Chronology matrix | 4 cols: State; Year; Instrument; Mechanisms. 10 rows. | No existing table. Adoption date is not observed effect; check each constitution or convention journal. |
| **Figure 6** | Ch. 28, §1.2 | Ch. 28, `ch28-table-media` | Benchmark table | 4 cols: Year; Newspaper circulation per person; Telephones; Coverage note. 4 rows: 1870, 1880, 1890, 1900. | Appendix B Table 7. Mark missing years; state the circulation denominator. |
| **Figure 8** | Ch. 35, §1.2 | Ch. 35, `ch35-table-neutrality` | Legal chronology | 4 cols: Date; Statute; Prohibition; Executive discretion. 6 rows: 1935, 1936, 1937, 1939, 1940, 1941. | No existing table. Distinguish enactment, amendment, and repeal; cite *Statutes at Large*. |

**Why these six convert.** Figures 1, 2, 4, and 6 combine stocks, flows, percentages, and missing years. A table with named units is more honest than a dual-axis chart. Figure 5 is a state-by-state repertoire; a matrix is the natural form. Figure 8 is a sequence of statutes; a table preserves the exact provisions and dates.

### 7.3 Images to exhibits or close readings (6)

| Old | Owner | Replacement | Form | Content specification | Rights and evidence rule |
|---:|---|---|---|---|---|
| **Image 1** | Ch. 3, §3 In Focus | `ch03-focus-belt` | Close reading | Keep the 150–250-word In Focus reading. A 1909 public-domain halftone is on file and would become Image 3 if the cultural-protocol review is accepted. | Haudenosaunee authorization and a provenance note required; the halftone is a period reproduction of the Thacher belt, not an authorized photograph of the present object. No stock photo, no redrawn schematic without consent. |
| **Image 4** | Ch. 28, §2 In Focus | `ch28-exhibit-sears` | Exhibit table | 3 cols: Item; Specification; Price. 6 rows: men’s frame, women’s frame, tires, clothing, accessories, price range. | Public-domain 1897 catalog; fix the exact page; transcribe exact copy; no scan. |
| **Image 5** | Ch. 32, §2 In Focus | `ch32-exhibit-radio` | Exhibit table | 4 cols: Time; Station and call letters; Wavelength; Program type. 8–10 rows. | 1924 public-domain page; verify against the page image, not OCR; exact headings. |
| **Image 6** | Ch. 39, §5 In Focus | `ch39-exhibit-literacy` | Exhibit table | 2 cols: Question; Registrar’s rule or note. 6 rows. | Exact form, parish, and date. If provenance fails, use a documented excerpt or no exhibit; no composite. |
| **Image 7** | Ch. 44, §4 In Focus | `ch44-focus-quilt` | Close reading | Keep the In Focus reading. No image by default. A 1992 photograph of the whole Quilt is on file, but it is not the first panel and cannot stand in for it. | Maker or caretaker consent and rights clearance required. The 1992 file carries a © NAMES Project credit; do not treat the NIH-host public-domain tag as clearance. No stock photo. |
| **Image 8** | Ch. 48, §5 In Focus | `ch48-exhibit-dorian` | Exhibit table | 3 cols: Item; Official record; Displayed or altered version. 4 rows: forecast date, cone extent, Alabama status, NOAA statement. | No photograph by default. The official graphic is a government work; a displayed photograph needs a rights-cleared source. |

**Why these six convert.**

- **Images 1 and 7** are community-held or maker-held objects. The close reading is the argument; a small, decontextualized photograph is not worth the consent risk. If the Hiawatha review is accepted or the quilt rights are cleared, add the image; do not make the chapter depend on it.
- **Image 4** is a catalog spread. At 3.5 inches, the prices and specifications are unreadable. A transcription table preserves the exact copy and makes the gender and price argument visible.
- **Image 5** is a newspaper broadsheet. A clean excerpt of eight to ten station rows is more legible than the full page and avoids the OCR errors.
- **Image 6** is a legal form with unresolved provenance. A verified excerpt of questions, paired with the registrar’s discretion, is stronger than an unidentified scan. If the exact form cannot be established, the chapter keeps the close reading without a facsimile.
- **Image 8** is two different objects: an official forecast graphic and a photograph of an altered display. The argument is the alteration, not the room. A text exhibit with exact quotations from NOAA and the inspector general is more precise than a wide Oval Office photograph; if a photograph is used, crop to the chart and clear the rights.

### 7.4 Argument-preservation audit

A conversion is only successful if the chapter’s argument survives. These are the ten most consequential replacements and where the argument goes:

| Conversion | Argument | Where it lives after conversion |
|---|---|---|
| **Map 21 → table** | American empire was a patchwork of legal instruments, not one policy | “Instrument” and “Practical status” columns |
| **Map 22 → table** | Woman suffrage was a patchwork of full, partial, and no rights | Three status rows with state lists and years |
| **Map 23 → merge** | Informal empire had formal instruments | Expanded Chapter 30 Table 1 |
| **Map 25 → table** | The Great Migration was a demographic transformation, not a single journey | Origin and destination counts with a change column |
| **Map 30 → table** | Campaign geography and registration results are different evidence | Separate “Action” and “Registration” columns |
| **Map 31 → table** | Program placement only partly matched measured need | Poverty rate and program placement columns |
| **Map 34 → table** | Absolute and percentage change tell different stories | Two separate change columns |
| **Map 38 → tables** | Spatial coalitions changed; an election map does not show motives | Vote and margin columns with a “not motives” note |
| **Figure 1 → table** | Debt stock and annual revenue are different quantities, and the debt series disagree | Two debt columns plus a revenue column |
| **Figure 5 → table** | Disfranchisement was a sequence and a repertoire | Chronological rows and a mechanism column |

If a Stage 2 specification cannot state where the old argument lives, the conversion is rejected and the visual returns to the drawn list or the argument moves into prose.

---

## 8. Gazetteer overhaul

### 8.1 The count discrepancy

The README says the gazetteer retains 76 entries. Its list actually contains **77 names**. The Appendix C outline has **76 entries** and omits **Montgomery**, which the README list includes. The target is **77 primary entries**, plus short cross-reference lines for alternate names.

This is not a cosmetic count. The gazetteer is a reader-facing finding aid; a missing Montgomery or a miscount undermines the appendix’s authority. Stage 1 reconciles the names one by one, and Stage 4 prints the verified list.

### 8.2 The dictionary format

Replace the planned five-column, 76-row table with a dictionary-style hanging list:

> **Cahokia** *Illinois; Ch. 1* — Mississippian city and mound center, c. 950–1350 CE; UNESCO site.
>
> **Cherokee Nation** *Oklahoma; Chs. 17, 25* — Sovereign government with its capital at Tahlequah; not a generic place.
>
> **Guåhan (Guam)** *Mariana Islands; Chs. 2, 27* — CHamoru homeland; Spanish colony, U.S. territory after 1898, major Pacific base.

Rules:

- **Bold** the preferred name.
- *Italicize* the present jurisdiction and chapter numbers on the first line.
- An em dash introduces an 8–12 word note.
- Alphabetize by preferred name. Put alternate names in parentheses or a short “see” line.
- Print the nation’s name first where the book uses it; put the federal or colonial name in parentheses.
- No coordinates in print. Coordinates live in `data/app-c/gazetteer.csv` for production.
- No per-entry footnote unless the entry makes a claim not already cited in the chapter. Use grouped notes for the base name sources.

This format flows across font sizes, does not clip at the right edge, and reads naturally on a 6-inch screen. It is also searchable and screen-reader friendly.

### 8.3 Production schema

`data/app-c/gazetteer.csv` holds the structured data:

| Field | Meaning |
|---|---|
| `place_id` | Stable key, e.g. `gaz-cherokee-nation` |
| `preferred_name` | Name printed first |
| `alternate_names` | Parenthetical or cross-reference forms |
| `jurisdiction` | Present jurisdiction or region |
| `chapters` | Chapter numbers, comma-separated |
| `note` | The 8–12 word printed note |
| `coordinates` | Latitude and longitude, production only |
| `name_source` | Nation, community, GNIS, or other name authority |
| `note_source` | Chapter section or appendix note key |
| `status` | `verified`, `community_pending`, or `target` |
| `print` | `yes`, `cross_reference`, or `no` |

### 8.4 Names, dates, and sources

- Use the book’s date policy: Julian through September 2, 1752; Gregorian from September 14, 1752. Retain a source’s double year for January–March dates before 1752.
- Do not silently modernize a colonial name. “New Amsterdam” becomes “New York” in 1664; “San Juan Pueblo” becomes “Ohkay Owingeh” in 2005; “Indian Territory” becomes Oklahoma in 1907. The entry says so.
- An Indigenous name is not a synonym for a colonial name. Give the nation and the source.
- A nation is not a place. “Cherokee Nation” is a sovereign government with a capital at Tahlequah; “Dinétah” is a homeland, not a reservation boundary.
- GNIS supplies federal names and coordinates. It does not settle the book’s preferred name or a nation’s territory.
- Native Land Digital is a finding aid and a prompt for consultation, not a legal authority.
- The chapter numbers are a reading aid, not evidence. Every historical note summarizes a claim already cited in that chapter or carries its own note.

### 8.5 Page estimate

At 77 entries and about 22 words per entry, the gazetteer is about 1,700 words. The 18-entry catalog, group introductions, name note, and apparatus add about 1,100 words. The appendix lands at about 2,800 words, or 5.6 pages at 500 words per page. Plan for **6 pages**, with a measured proof in Stage 4. If the proof runs to 7 pages, cut catalogue repetition before cutting names.

---

## 9. Step-by-step plan

The sequence is gated. Do not start a later stage until the prior gate is met. Stages 5 and 6 can run in parallel after Stage 3, but the chapter text and the artwork must use the same frozen numbering.

### Stage 0 — Ratify the design

**Purpose:** lock the decisions that every later stage depends on.

**Tasks**

1. Read this plan against `docs/kindle-visuals-research.md`, `AGENTS.md`, `README.md`, and `docs/kindle.md`.
2. Decide the eleven items in §13. The recommended choices are the baseline.
3. Decide whether to pursue the two optional images now or defer them. The baseline must not depend on either.
4. Record the decisions in §13 with the date and initials.
5. If a decision is rejected, revise the affected rows in §§3–7 before Stage 1.

**Outputs:** a completed decision record.

**Gate:** no baseline item is “TBD.” A deferred optional image is allowed; an undecided baseline is not.

### Stage 1 — Build the triage ledger

**Purpose:** turn the dispositions into one auditable record.

**Tasks**

1. Create `data/app-c/triage.csv` from §§4–7. Fields: `old_id` (e.g. `ch04-map-01`), `old_display` (e.g. `Map 4`), `owner`, `old_title`, `verdict`, `new_form`, `new_id`, `display_number`, `merge_target`, `rationale`, `source_status`, `rights_status`, `size_target`, `blocker`. Use `source_status` values `consulted`, `target`, `discovered`, or `blocked`; use `rights_status` values `public_domain`, `open_access`, `permission_pending`, `community_pending`, `cleared`, or `not_applicable`.
2. Add one row for each of the 56 registered assets. The counts must be 39 maps, 9 figures, and 8 images.
3. Add the two optional images as separate rows with `verdict=optional`.
4. Validate: every old ID appears once; every new ID is unique; every conversion has a form and a merge target; every kept asset has a production brief.
5. Create `data/app-c/renumbering.csv` from §3.1. Fields: `old_id`, `old_display`, `new_id`, `new_display`, `owner`, `status`.
6. Create `data/app-c/gazetteer.csv` with the 77 names and the schema in §8.3. Reconcile the README list against the appendix entries and add Montgomery.
7. Record the known discrepancies: 77 README names versus 76 appendix rows; the missing Montgomery; the `.svg` asset paths that must become `.png`; and the checker’s three `table-uncaptioned` INFO findings in Appendix C, which are the production schedules that move to `captions.csv`.

**Outputs:** `triage.csv`, `renumbering.csv`, `gazetteer.csv`.

**Gate:** counts reconcile; no blank verdict; no duplicate new ID; the gazetteer count is 77.

### Stage 2 — Write the specifications and run the merge audit

**Purpose:** define every replacement before touching prose.

**Tasks**

1. Create `data/app-c/specs/` with four files: `maps.md`, `figures.md`, `images.md`, `tables.md`.
2. For each kept visual, write a one-page brief: argument, crop, labels, line styles, data sources, caption, alt text, dimensions, file name, and rights.
3. For each converted asset, write a one-page spec: argument, columns and rows, data sources, definitions, merge target, caption, note, and textual reference.
4. Run the table merge audit. For each conversion, open the owning chapter’s existing tables and Appendix B Tables 1–8; record `merge`, `replace`, or `add`.
5. Assign descriptive stable IDs to new tables. Do not encode a display number.
6. Identify high-renumbering chapters. At minimum: Chapters 19, 20, 31, and 49. List every affected table reference.
7. Run the data-feasibility check. If a table’s data cannot be sourced, narrow the table or move the argument to prose. Do not invent cells.
8. Draft the 18 baseline caption, source, credit, and alt strings in `data/app-c/captions.csv`. Alt text must be 140 characters or fewer.

**Outputs:** four specification files, `merge-audit.csv`, `captions.csv`.

**Gate:** every conversion has a source locator and a merge decision; every kept visual has a production brief; no table depends on an unsourced series.

### Stage 3 — Freeze the numbering and repair global references

**Purpose:** make one numbering authority before prose is rewritten.

**Tasks**

1. Freeze Maps 1–13, Figures 1–3, and Images 1–2. No further changes without a written decision.
2. Update `chapters/53-appendix-c.md` catalog headings and numbers. The full rewrite is Stage 4.
3. Update the README:
   - the register’s counts and introduction;
   - the map, figure, and image rows (retire the old, renumber the survivors);
   - the asset paths from `.svg` to `.png`;
   - the table register with the new descriptive stable IDs;
   - the page budget and status table;
   - the Appendix C purpose and draft status;
   - the gazetteer list and count.
4. Update `docs/kindle.md`: §1, §7.2, §7.3, §8.2, §10, §12.3, §13 P0, and every “56 visuals” and Appendix C schedule reference.
5. Replace old map, figure, and image numbers in chapters that keep a visual. Leave a worklist for converted references.
6. Update `repo-mapNN` source keys in the README and chapter notes.
7. Run the greps and the checker:

```bash
grep -Rno "Map [0-9]\+" chapters/*.md README.md docs/*.md
grep -Rno "Figure [0-9]\+" chapters/*.md README.md docs/*.md
grep -Rno "Image [0-9]\+" chapters/*.md README.md docs/*.md
grep -Rno "repo-map[0-9]\+" chapters/*.md README.md docs/*.md
python3 tools/check_book.py --strict
```

**Outputs:** `renumbering.csv`, a reference-repair report, updated README and `docs/kindle.md`.

**Gate:** no old number remains for a kept visual; every remaining old number is on the Stage 5 conversion worklist; the mapping file records every retired number; every new number has one owner; the checker passes. Do not build a release candidate between Stages 3 and 5.

### Stage 4 — Rewrite Appendix C

**Purpose:** turn an about 20,900-word production outline into a reader-facing catalog.

**Tasks**

1. Move production sections §1.2–§1.6, §2.1–§2.6, §3.1–§3.2, §4.1–§4.4, §5.1–§5.4, and §§6–7 to `data/app-c/production.md`. Move, do not delete, any note that supports a claim or records a source; delete only duplicated planning boilerplate.
2. Move the caption and alt schedules to `data/app-c/captions.csv`.
3. Write the new appendix:
   - a note on the visual program: what the catalog covers, how tables differ, why there are fewer drawn visuals, and a pointer that tables replacing former maps are listed in the owning chapters and the README register;
   - a map catalog of 13 entries, 30–40 words each, grouped by part;
   - a figure catalog of three entries;
   - an image catalog of two entries;
   - the 77-entry gazetteer in the dictionary format;
   - a note on names and dates;
   - one combined footnote list.
4. Reclassify the 83 existing notes: keep reader-facing citations; move production sources and editorial checks to `data/app-c/production.md`; rekey only when a reference changes subject.
5. Remove the old 39/9/8 counts and the five-page justification. Replace them with the actual counts.
6. Proof the appendix at 6 pages. If it runs longer, cut catalog repetition before cutting names or definitions.
7. Run `python3 tools/check_book.py --strict chapters/53-appendix-c.md`.

**Outputs:** the new `chapters/53-appendix-c.md`, `production.md`, `captions.csv`, and a note map.

**Gate:** about 3,000 words; 13/3/2 catalog entries; 77 gazetteer entries; no production fields in the printed text; the checker passes.

### Stage 5 — Rewrite chapters and build the typographic replacements

**Purpose:** put each converted argument where the old visual did its work.

Work in four batches: Chapters 1–12, 13–25, 26–38, and 39–50. For each chapter:

1. Open the chapter and its Stage 2 specification.
2. Place the table or exhibit at the section where the old visual did its argument.
3. Merge into an existing table or add a new one. Assign the display number by order of first textual reference.
4. Renumber later tables in the chapter. Update every “Table N” reference in prose, captions, study questions, summary, and notes.
5. Write the table or exhibit with the house caption paragraph, source line, and textual reference. The build filter supplies the HTML `<caption>` and row headers.
6. Replace the old map, figure, or image reference in the prose with the new table or exhibit reference.
7. Update the In Focus box for a converted image: transcribe the document or write the close reading; do not leave a promise of a scan.
8. Update the editorial notes: remove “no asset exists” for a converted asset; add “table drafted, needs verification” where appropriate.
9. Add the table or exhibit to the README table register.
10. Run `python3 tools/check_book.py --strict chapters/NN-chapter-N.md`.

**Outputs:** 38 replacements drafted; chapter notes updated; README table register updated.

**Gate:** every converted asset has a textual reference; no orphan “Map N” reference remains; no table exceeds four columns or 24 rows without a documented exception; the checker passes per chapter.

### Stage 6 — Produce the 18 baseline visuals

**Purpose:** make the survivors legible at 3.5 inches, not merely present.

**Tasks**

1. Set up `assets/source/maps/`, `assets/source/figures/`, `assets/maps/`, `assets/figures/`, and `assets/images/`.
2. Acquire public-domain base data: Natural Earth, Census cartographic boundary files, and the Newberry Atlas of Historical County Boundaries. Record the version and download date.
3. Produce Maps 1–13 in order. For each: draft, proof at 1,600 × 2,400, check labels at 3.5 inches, check grayscale, check file size.
4. Produce Figures 1–3 at 1,600 × 1,000–2,000. Use direct labels, no gridlines unless the argument needs them, and no smoothing.
5. Acquire and prepare Images 1–2 at 1,600 px on the long edge, JPEG 85, high contrast. Do not upscale a small file.
6. Write the source record for each: data, projection, transformations, script or version, date, and credit.
7. Export maps and figures as indexed PNG at four to eight shades; export photographs as JPEG. Strip metadata, flatten on white, remove alpha.
8. Run the 3.5-inch test, the grayscale test, the font-size-3 test, and the file-size test.

**Outputs:** 18 publication assets, source files, and production records.

**Gate:** all 18 pass legibility, grayscale, caption, alt, rights, and size checks; no text is baked into an image except map labels, legends, scale bars, and data labels; total image payload is 2.5–5.0 MB.

### Stage 7 — Clear rights and community authorization

**Purpose:** make every reproduced object publishable and properly credited.

**Tasks**

1. Build `data/app-c/rights.csv` with 18 rows plus the two optional rows.
2. For each image, record the object ID, repository, rights basis, credit, permission status, evidence URL, and date.
3. Jefferson medal: confirm the Smithsonian media’s open-access status; download the exact file; record the object number.
4. Torlino: confirm Dickinson’s terms; use the archival composite; credit the archive.
5. Hiawatha Belt: review the 1909 halftone on file, its Thacher provenance, and the *Onondaga Nation v. Thacher* record with the Onondaga Nation or the appropriate Haudenosaunee cultural office. If the review is accepted, add the halftone as Image 3 with a caption identifying the 1909 volume; if not, no image.
6. AIDS Quilt: the 1992 photograph on file is credited to Mark Thiessen and The NAMES Project Foundation and is not the first panel. Do not use it as Image 7. If a quilt photograph is wanted, obtain permission from the foundation and caption the 1992 display; otherwise keep the close reading and add no image.
7. Dorian: use the official National Hurricane Center graphic, a U.S. government work, and exact NOAA and inspector-general quotations. Do not use a news photograph of the Oval Office display without a cleared source.
8. For maps and figures, record the data licenses and the original-compilation copyright.
9. If an image fails, withdraw it from the register and the chapter, keep the close reading, and update the counts.

**Outputs:** `rights.csv`, permission correspondence, and final credit lines.

**Gate:** no image is placed without a rights basis; optional images only after Haudenosaunee review or a cleared quilt-photograph license; credits match the register and the caption file.

### Stage 8 — Verify

**Purpose:** separate a plausible conversion from a checked one.

**Tasks**

1. **Evidence.** Every table cell has a source locator; every map label and claim has a source; every caption states date, units, and limits.
2. **Quotations.** Every exhibit transcription matches its source character by character, with a locator.
3. **Captions and alt text.** The 18 rows match `captions.csv`; alt text is 140 characters or fewer; no caption, source line, or credit is inside an image.
4. **Layout.** Every new table is four columns or fewer and 24 rows or fewer; the font-size-3 test passes; no cell clips; captions are `<caption>`; leading cells are row headers.
5. **Grayscale and legibility.** Each visual is checked at 3.5 inches and 6 inches; the four tones remain distinct.
6. **File size.** Total is 8 MB or less; each class is within its target.
7. **Links.** Every visual is cited by number; every table is cited; every footnote resolves.
8. **Structural check.** `python3 tools/check_book.py --strict` passes on every changed file.
9. **Kindle Previewer.** Run it on Windows or macOS, or use the KDP Online Previewer. Check conversion, Enhanced Typesetting, tables, images, notes, and the backlinks.
10. Record every result in `data/app-c/checks.md` with the date and the exact test.

**Outputs:** `checks.md`, proof PDFs, and a Previewer report.

**Gate:** all checks pass or are declared blockers; no unsupported central claim and no unresolved factual correction remain.

### Stage 9 — Integrate and release

**Purpose:** make the counts, the prose, and the files agree.

**Tasks**

1. Reconcile the counts: 13 maps, three figures, two images, 18 baseline, optional ceiling 20; the gazetteer at 77; the table count after merges.
2. Reconcile the Appendix C catalog against the actual assets. Every entry has an asset or is removed.
3. Reconcile the README register, `docs/kindle.md`, chapter captions, and `captions.csv`.
4. Measure the page count: the Appendix C proof, the chapter table proofs, and the total text pages.
5. Measure the file size: the EPUB without a cover, and the KDP converted size if available.
6. Run the repository builds:

```bash
make epub
make epubcheck
make pdf
make html
```

7. Run Kindle Previewer or the KDP Online Previewer. Check the cover, TOC, notes, tables, images, and emphasis.
8. Update the status: Appendix C from `drafted` to `checked` only after the checks; then `integrated`. Record the remaining blockers.
9. Report what was not run. Linux cannot run the desktop Kindle Previewer; do not claim it passed.

**Outputs:** a release candidate, a build report, and a status update.

**Gate:** all acceptance checks pass; no promised visual is missing; no unregistered visual exists.

---

## 10. File-by-file change map

| File | Change | Stage | Validation |
|---|---|---|---|
| `chapters/53-appendix-c.md` | Replace the production outline with the reader-facing catalog and gazetteer | 3–4 | Checker; 13/3/2; 77 entries |
| `README.md` | Counts, register rows, asset paths, table register, budget, status | 3, 5, 9 | Count reconciliation; checker |
| `chapters/01–50` | Replace visual references; add the replacement tables, exhibits, and close readings; renumber chapter tables | 3, 5 | Per-chapter checker; greps |
| `docs/kindle.md` | Counts, schedule location, PNG rule, file-size budget, P0 | 3, 9 | Manual review |
| `AGENTS.md` | No change unless a new bold label is adopted | 0 | Author decision |
| `data/app-c/README.md` | This plan, decision record, and status | 0–9 | Manual |
| `data/app-c/triage.csv` | 56-row disposition ledger | 1 | Count and ID validation |
| `data/app-c/renumbering.csv` | Old-to-new mapping | 1, 3 | Grep validation |
| `data/app-c/gazetteer.csv` | 77-row structured gazetteer | 1, 4 | Count and name validation |
| `data/app-c/specs/*.md` | Four specification files with 56 sections | 2 | Source and merge audit |
| `data/app-c/captions.csv` | 18 caption, source, credit, and alt rows | 2, 8 | Length and string validation |
| `data/app-c/rights.csv` | Four image-rights rows plus 16 map and figure data-license rows | 7 | Permission evidence |
| `data/app-c/checks.md` | Dated check results | 8 | All checks |
| `assets/maps/map-01.png` … | 13 maps | 6 | Visual tests |
| `assets/figures/figure-01.png` … | Three figures | 6 | Visual tests |
| `assets/images/image-01.jpg` … | Two photographs | 6–7 | Rights and visual tests |
| `styles/epub.css` | Exhibit and gazetteer styles | 5 | Kindle Previewer |

**Styles.** Add only reflow-safe rules: a left border and indent for exhibits, a hanging indent for the gazetteer, bold headwords, and no background colors or forced fonts. Body text keeps Kindle defaults. The existing `.appendix-table` style can be reused; do not create a fixed-width layout.

---

## 11. Validation and acceptance

### 11.1 Commands

```bash
# Structural check on the changed files
python3 tools/check_book.py --strict chapters/53-appendix-c.md
python3 tools/check_book.py --strict

# Find stale visual references
grep -Rno "Map [0-9]\+" chapters/*.md README.md docs/*.md
grep -Rno "Figure [0-9]\+" chapters/*.md README.md docs/*.md
grep -Rno "Image [0-9]\+" chapters/*.md README.md docs/*.md
grep -Rno "repo-map[0-9]\+" chapters/*.md README.md docs/*.md

# Builds
make epub
make epubcheck
make pdf
make html

# Checker tests, if the checker changes
python3 -m unittest discover -s tools -p 'test_*.py'
```

### 11.2 Visual tests

- **3.5-inch test:** view or print each map at 3.5 inches wide in grayscale. Read every label without zooming.
- **6-inch test:** view at 6 inches. Check that the hierarchy still reads.
- **Grayscale test:** convert to grayscale; confirm that no two categories depend on color.
- **Font-size-3 test:** in Kindle Previewer, set the reader to font size 3. Check captions, tables, and figures.
- **File-size test:** each map 150–300 KB, each figure 80–150 KB, each photo 150–300 KB; total image payload 2.5–5.0 MB.
- **Text-in-image test:** the image contains only labels, legends, scale bars, and data labels. The title, caption, source, and credit are HTML.

### 11.3 Table tests

- Four columns or fewer; 24 rows or fewer.
- No merged cells, nested tables, or images of tables.
- The caption is a `<caption>` before the table; the source line follows.
- The leading cell is a row header.
- At font size 3, no cell is cut off and no row breaks mid-cell.
- The table is cited by number in the prose.

### 11.4 KDP tests

- EPUB validates under EPUBCheck.
- Kindle Previewer reports Enhanced Typesetting as supported.
- The cover appears once; the interior has no cover page.
- Notes open and return; repeated notes link to the first definition.
- Tables and figures reflow at font sizes 1–7.
- The converted file size is measured in KDP or Previewer, not inferred from the EPUB.

### 11.5 Acceptance checklist

- [ ] **Scope:** 13 maps, three figures, two images, 18 baseline; optional ceiling 20; 38 conversions drafted or merged; 77 gazetteer entries; no unregistered visual.
- [ ] **Evidence:** every table cell and map label has a source locator; every caption states date, units, and limits.
- [ ] **Quotations:** every exhibit matches its source character by character.
- [ ] **Reasoning:** every conversion preserves the old argument; no table is used to prove a causal claim.
- [ ] **Chronology:** dates in captions and tables agree with Appendix D and the chapters.
- [ ] **Statistics:** units, denominators, base years, and rounding are stated.
- [ ] **References:** every visual and table is cited by number; no old number remains; every note resolves.
- [ ] **Rights:** every image has a rights basis and a credit; optional images have Haudenosaunee review or a cleared quilt-photograph license.
- [ ] **AI disclosure:** every AI-assisted visual is recorded and classified for KDP disclosure; deterministic maps and figures are marked as such.
- [ ] **Architecture:** In Focus boxes and tables sit where the argument needs them; no visual is decorative.
- [ ] **Language:** captions read aloud cleanly; no “see below” or file names in alt text.
- [ ] **Notes:** one combined list per manuscript unit; no separate Sources list.
- [ ] **Integration:** README, Appendix C, chapters, and `docs/kindle.md` agree.
- [ ] **Structural:** `python3 tools/check_book.py --strict` passes.
- [ ] **Rendering:** builds pass; Previewer passes; tables and images survive font size 3.
- [ ] **Budget:** page and file-size measurements are recorded; the text total remains above 1,000 pages.

---

## 12. Risks and open decisions

| Risk | Why it matters | Response |
|---|---|---|
| **Catalog promises more than the assets** | KDP treats a missing promised image section as a critical issue | The appendix lists only the 18 baseline visuals and the tables that exist; no 56-item catalog of absent assets |
| **Author rejects the 18/38 split** | Every later stage depends on it | Stage 0 gate; revise §§4–7 before any prose |
| **Map 3 cannot be verified** | Indigenous names and ranges need nation-specific sources | Convert Map 3 to a Chapter 3 table; the map count becomes 12 and the produced count 17 |
| **Jefferson medal or Torlino rights fail** | The baseline drops to 1 or 0 photographs | Keep the close readings; add no stock substitute; record the count |
| **Hiawatha Belt or Quilt consent fails** | The Hiawatha file is a 1909 public-domain halftone but still needs cultural-protocol review; the Quilt file is a copyrighted 1992 wide view, not the first panel | Baseline is unaffected; no image; keep the close reading; do not substitute the 1992 wide view for the first panel |
| **Converted data cannot be sourced** | A table is not evidence | Narrow the table, qualify the claim, or move the argument to prose |
| **Table fatigue** | 30–39 new tables can overwhelm the book | Merge before add; four-column cap; 24-row cap; sidebars where a table is overkill |
| **Renumbering cascade** | Chapters 19, 20, 31, and 49 have multiple tables | Per-chapter reference audit; do not append tables just to avoid renumbering |
| **Appendix C exceeds 6 pages** | The gazetteer grows when it becomes readable | Cut catalog repetition first; request a 7th page only with a measured proof |
| **Kindle Previewer unavailable on Linux** | The final rendering cannot be checked locally | Run on Windows or macOS, or use the KDP Online Previewer; report the limitation |
| **The 954-page PDF gap remains** | This overhaul is not a page-count fix | Treat the 46-page shortfall as a separate production issue; do not pad tables |
| **Generative AI in maps** | KDP disclosure and historical accuracy | Use deterministic cartography; disclose any AI-assisted asset |
| **A conversion loses the argument** | The visual was doing real analytical work | Run the §7.4 audit; if the argument has no home, keep the visual |

**Open decisions for the author**

1. Approve the 18/38 split and the 13/3/2 survivor list.
2. Approve the sequential renumbering and the retirement of the old numbers.
3. Approve the dictionary-style gazetteer and the 6-page Appendix C allowance.
4. Approve the four-tone grayscale standard and PNG-only EPUB assets.
5. Decide whether to pursue the two optional images now or after the baseline is complete.
6. Decide whether any converted table should instead become a **The measure.** sidebar. The default is a table; a sidebar is allowed only when it carries three or four comparisons and no aligned columns.
7. Confirm that no new bold label is needed. If one is, amend AGENTS §6 in the same change.
8. Confirm the AI classification for the new maps and figures.

---

## 13. Decision record

Complete this table in Stage 0. “Recommended” is the plan’s baseline; “Alternative” is the cost of a different choice.

| Decision | Recommended | Alternative | Consequence |
|---|---|---|---|
| **Release target** | Kindle ebook only; design for 3.5–4.2-inch grayscale | Dual Kindle and print | Grayscale, print-safe drawings; no color dependence |
| **Produced visual count** | 18: 13 maps, 3 figures, 2 images | 15–20 | Smaller file; sharper arguments |
| **Conversions** | 38 to tables, exhibits, or close readings | Keep more maps | Fewer illegible rasters; more real text |
| **Renumbering** | Sequential 1–13, 1–3, 1–2 | Keep sparse old numbers | Cleaner references; one-time repair |
| **Gazetteer** | Dictionary list, 77 entries | Five-column table | Readable on Kindle; about one extra page |
| **Appendix C** | Six pages, reader-facing, about 3,000 words | Five pages with production detail | Production moves to `data/app-c/` |
| **Image format** | PNG for maps and figures; JPEG for photos; SVG masters only | SVG in the EPUB | KDP-safe; no Enhanced Typesetting cap |
| **Table format** | Real HTML tables, never images of tables | Rasterized tables | Accessible, reflowable, searchable |
| **Palette** | Four tones plus hatching | 16-level grayscale | Crisp on E-Ink; print-safe |
| **AI policy** | Deterministic cartography; disclose any AI-assisted image | Generative maps | KDP compliance; historical accuracy |
| **Optional images** | Two candidates on file; review the 1909 Hiawatha halftone with Haudenosaunee stewards; do not use the 1992 Quilt photograph as the first panel | Drop both | Ceiling 20; no dependency; the quilt photograph needs permission |

**Signed:** ____________________  **Date:** ____________________

---

## 14. What “done” looks like

- The appendix catalogs **13 maps, three figures, and two images**, each with a 30–40 word reader-facing entry.
- **38 former visuals** have a table, exhibit, close reading, or documented merge, and every one preserves its old argument.
- The gazetteer is a **77-entry dictionary list**, with Montgomery restored and the count reconciled.
- The README register, the appendix, the chapters, and `docs/kindle.md` agree on every count and number.
- The 18 baseline assets exist within their class targets: maps at 1,600 × 2,400 px and 150–300 KB, figures at 1,600 × 1,000–2,000 px and 80–150 KB, photographs at 1,600 px on the long edge and 150–300 KB; all are four-tone grayscale or high-contrast JPEG; the optional images exist only after Haudenosaunee review and rights clearance, and the 1992 Quilt photograph is not used as the first panel.
- Every image has a caption, source line, credit, alt text, and rights basis; no caption or credit is baked into an image.
- Every new table has four columns or fewer, 24 rows or fewer, a real caption, and a textual reference.
- The EPUB is **under 8 MB** without a cover; the image payload is 2.5–5.0 MB; the 70% delivery fee is about $1.16 or less.
- `python3 tools/check_book.py --strict` passes, the EPUB validates, and Kindle Previewer or the KDP Online Previewer passes.
- The text-page total is measured against the 1,000-page floor, and the separate 954-page PDF gap is reported, not hidden.
- No promised visual is missing and no unregistered visual has entered the book.

---

*This plan is a production proposal. It does not claim that any map, figure, image, table, or right exists. The first action is the Stage 0 decision, not a manuscript edit.*

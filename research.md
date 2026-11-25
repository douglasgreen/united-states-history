You are in luck because none of the 56 assets in `53-appendix-c.md` have been produced yet. Catching this at the Stage 3 outline phase saves months of cartography, dozens of rights clearances, and a steep per-unit delivery penalty on Kindle.

You should **not** dump all visuals and go 100% text-only, nor should you try to salvage all 39 maps, 9 figures, and 8 images. On Kindle E-Ink, roughly **two-thirds of the planned visuals** will work far better—and convey your actual historical arguments more honestly—if converted into Kindle-native HTML formats, leaving **~15–20 ultra-clean, high-contrast schematic drawings and charts** where geometry or trend shape genuinely beats prose.

---

### Why the current plan breaks on Kindle (and hurts royalties)

1. **Grayscale & screen size destroy county maps and multi-panel figures:** Most dedicated Kindles display 16-level grayscale on a 6–7 inch screen (~3.5–4.2 inches wide). Any continental U.S. county map (Maps 34, 36, 37, 38, 39) renders eastern counties at 2–4 pixels wide. Multi-panel maps (Maps 2, 9, 33, 34, 38) and multi-panel charts (Figures 4, 7) shrink each panel further, while color distinctions (e.g., red vs. blue vs. third-party in Maps 33 and 38) collapse into indistinguishable middle grays.
2. **Dense documents turn into gray blur:** Full-page newspaper grids (Image 5, *Evening Star* radio schedule), mail-order spreads (Image 4, 1897 Sears catalog), and legal forms (Image 6, Louisiana literacy test) are illegible without sluggish E-Ink pinching and zooming.
3. **KDP delivery fees penalize image bloat:** Under Amazon KDP’s 70% royalty tier ($2.99–$12.99 price band as of July 2026), Amazon deducts **$0.15 per MB** in the U.S. based on the converted file size. Even a 400,000-word text-only book compresses to roughly 1–2 MB (~$0.15–$0.30). Fifty-six detailed raster maps, shaded charts, and archival scans can easily push the file to 15–35 MB—costing **$2.25–$5.25 per sale** in delivery fees.

---

### Four Kindle-Native Alternatives (Applied to Your Catalog)

#### 1. Structured HTML Tables & Comparison Matrices (Best for "fake maps")
Many of your planned maps aren't really spatial arguments—they are **legal classifications, state-by-state inventories, or chronologies** plotted onto geography. Putting them in an HTML table (kept to **3–4 columns max** so columns don't crush on a 6-inch screen) makes the argument sharper, searchable, and essentially 0 KB:

* **Legal-status & alliance maps → Comparative Jurisdiction Tables:**
  * **Map 21 (American empire, 1898–1902)** & **Map 23 (American Caribbean, 1898–1917):** Tiny dots across the Pacific and Caribbean can't communicate legal distinctions on a small gray screen. A crisp 4-column table (`Place | Year | Legal Instrument | Practical Status`) directly shows *why* Puerto Rico, Cuba, the Philippines, Haiti, and the Canal Zone differed.
  * **Map 22 (Woman suffrage by state, 1916):** Instead of cross-hatching Rhode Island or Delaware on a tiny U.S. map, use a 3-column table or grouped list (`Full Suffrage` | `Presidential / Partial` | `No Suffrage`) with the enacting year and statutory scope.
  * **Map 28 (Containment, 1952)** & **Map 35 (Eastern Europe & USSR, 1989–1991):** Replace world/regional shading with a chronological regime/treaty table distinguishing founding NATO members, 1952 accessions, bilateral pacts, and occupation zones.
* **Chronology figures → Vertical HTML Timelines:**
  * **Figure 5 (Disfranchising constitutions, 1890–1910):** A matrix table with states ordered chronologically (MS 1890 through OK 1910) and `●` / `—` markers for Poll Tax, Literacy/Understanding, Grandfather/Property, and Convention vs. Amendment lets readers scan the "repertoire" cleanly at any font size.
  * **Figure 8 (Neutrality’s statutory architecture, 1935–1941):** A vertical table (`Act & Year | Congressional Prohibitions | Executive Discretion`) communicates the legal loosening far better than tiny text boxes inside a raster timeline image.
* **Multi-unit figures → Side-by-Side Benchmark Tables:**
  * **Figure 1 (Imperial debt vs. colonial revenue)**, **Figure 2 (Funded debt vs. customs)**, and **Figure 4 (Rail mileage, steel output, urban share)** all struggle with incompatible units (stocks vs. flows vs. percentages). A compact 6–8 row table of key benchmark years eliminates dual-axis confusion while displaying exact ranges (such as the £70M–£75M vs. £133M–£140M debt dispute in Figure 1).

#### 2. "By the Numbers / Geography in Brief" Sidebars (Best for county choropleths & crowded event maps)
Your own editorial rules in `53-appendix-c.md` note that county maps mislead readers about voter motives (Maps 33, 38), let tiny-population rural counties visually overwhelm cities, and shouldn't force unrelated events into one causal map (Map 7). Replace these with a styled **HTML callout box** (subtle left border, slight indent, bold kicker—pure reflowable text):

* **County economic & housing maps (Maps 34, 36, 37, 39):** Replace illegible 3,100-county choropleths with a **"Regional & Metro Pattern" Sidebar** pairing regional totals with a 6-row table comparing *absolute* vs. *percentage* gains (or top metro/border hubs vs. rural non-metro counties). That eliminates the small-denominator visual distortion you warn against in Map 34 and Map 36.
* **Electoral maps (Maps 16, 33, 38):** Replace multi-panel red/blue county maps with an **Electoral Shift Matrix** breaking out Popular Vote %, Electoral Vote, and Metro/Suburban/Non-Metro margins across 1968/1972 or 2016/2020/2024.
* **Overstuffed narrative maps (Maps 6, 7, 10, 26, 30, 31):** Break **Map 7** (staples, ports, Scots-Irish/German streams, Whitefield, plus Salem/Stono/Enfield/NY) into a concise **Regional Circuit Box** (Chesapeake, Lowcountry, Mid-Atlantic, New England) so distinct episodes aren't visually fused together. Replace **Map 10's** convention inset with a clean 13-state ratification countdown table (State | Date | Vote Margin).

#### 3. Typographic "Primary-Source Exhibits" + Close Readings (Replacing illegible document scans)
For the `In Focus` sections (Images 1–8), `53-appendix-c.md` already plans to fall back on textual close readings if permissions fail (Images 1, 6, 7, 8). On Kindle, **typographic transcription exhibits** inside a bordered CSS box look crisp, require zero permissions for public-domain/factual excerpts, and let readers actually read the text:

* **Image 4 (1897 Sears bicycle ad):** Set a clean HTML catalog-style box reproducing the exact copy, men's vs. women's frame specs, and $25–$56 pricing tiers.
* **Image 5 (1924 *Evening Star* radio page):** Reconstruct a clean excerpted schedule box listing 8–10 local and distant stations, call letters, wavelengths, and program types—far more legible than a shrunk 1924 newspaper broadsheet.
* **Image 6 (Louisiana literacy test, c. 1963):** Set an exhibit box printing a documented sample of actual registration/civic questions alongside the statutory "good character" and registrar-discretion rules—avoiding both an unreadable scan and the unverified provenance problem noted in §4.3.
* **Image 7 (AIDS Quilt panel) & Image 1 (Hiawatha Belt):** Keep as rich `In Focus` close-reading sidebars (optionally using a tiny ~5 KB schematic black-and-white diagram of the Hiawatha Belt's 5-nation geometry rather than an unpermitted photograph of the physical wampum).

#### 4. What *Does* Draw Well on Kindle: "Woodcut / Subway-Map" Schematics & Bold Line Charts
Do **not** abandon drawings where visual geometry is irreplaceable. Instead, redesign the survivors specifically for 3.5-inch grayscale E-Ink (and export them as **flat 4-to-8-shade indexed PNGs or GIFs** rather than raw `<svg>` tags, which KDP's guidelines caution against in reflowable HTML; clean line art compresses to **20–50 KB per image**, keeping 15–20 images under **1 MB total**):

* **Rules for Kindle-proof schematic maps (keep ~10–14):**
  * **Zero terrain shading, zero color choropleths, zero multi-panel layouts.** Use pure white land, 15% pale gray water, thick solid/dashed black lines, and bold diagonal hatching. Stack two-part wars (Map 9, Map 27) vertically as separate figures rather than side-by-side.
  * **Crop tightly to the theater:** Don't show all of North America to explain the Mohawk Canal corridor (Map 12), Tidewater/New England (Map 4), Bleeding Kansas (Map 15), or the Nueces vs. Río Grande strip (Map 14).
  * **Cap at 8–12 large labels per map:** Put nuance, caveats, and date ranges in the HTML `<figcaption>`, never baked into the image (matching your existing §1.6 rule).
  * **Best candidates to keep as schematic maps:**
    * **Map 5 (English Atlantic c. 1680):** Turn into a bold 4-node schematic flow diagram (*West Africa ↔ Caribbean ↔ Mainland Colonies ↔ Britain*) with thick directional arrows—clearer than a geographic atlas.
    * **Maps 8, 12, 13, 14, 17, 18, 20, 32:** Each makes a geometric argument (Ohio Forks/Proclamation Line; Mohawk/PA/OH canal crossings; Removal corridors; Nueces–Río Grande strip; Civil War strategic arcs; overlapping Treaty/Railroad/Range hatching on the Northern Plains; Ho Chi Minh Trail bypassing the DMZ through Laos/Cambodia).
    * **Maps 1, 2, 3, 11, 27:** Keep only if stripped down to broad-stroke regional blocks/arcs with <12 labels each.
* **Best figures to keep as bold charts (keep ~3–4):**
  * **Figure 3 (Turnout 1824–1840)** and **Figure 9 (Trust in Government 1958–2025):** Bold 1-series or 2-series trajectories where the *visual slope* (the 1828/1840 jump; the 1964–2025 decline) carries the chapter's insight instantly.
  * **Figure 7 (Great Depression, 1929–1933):** Works nicely if stacked cleanly or simplified to two crisp 1-color charts (bank failures + Lebergott vs. Darby unemployment) with price indices moved to the caption/table.
* **Best archival images to keep as real photographs (keep ~2–3):**
  * **Image 2 (Jefferson peace medal)** and **Image 3 (Tom Torlino, 1882 & 1885):** Both have stark tonal contrast, minimal tiny text, high emotional/analytical payoff that prose cannot replicate, and clear archival sources. (If keeping **Image 8**, crop strictly to the forecast cone graphic with the hand-drawn Alabama loop rather than a wide Oval Office photo.)

---

### Bonus Fix in Appendix C Itself: The 76-Row Gazetteer
In §5.1, `App. C, Table 1` is planned as a **5-column, 76-row HTML table**. On a 6-inch Kindle screen, 5-column tables squeeze columns to ~0.6 inches wide, forcing awkward mid-word line wraps and messy page breaks across 10+ screens.

Formatting the Gazetteer as a **dictionary-style hanging list** (bold headword, jurisdiction & chapter numbers in italics on the first line, 8–12 word historical/name note below) looks completely native on Kindle, flows seamlessly across font sizes, and eliminates horizontal table clipping altogether.

### Suggested Next Step
If you want to publish both **Kindle** and **Print** down the road, you don't have to lock yourself into two completely different manuscripts—you can run a quick triage across the 56 entries right now:
* **~15–20 visuals:** Build once as clean, high-contrast black-and-white schematics/charts/photos (great in *both* Kindle and B&W paperback!).
* **~35–40 visuals:** Permanently convert to **HTML tables, primary-source exhibit boxes, and Spatial/Statistical Sidebars**. Your chapters get stronger, clearer, and more accessible, your KDP delivery fee drops from several dollars to pennies, and—as a side benefit—converting dense graphics into concise tables and sidebars organically adds crisp, readable content toward your page-count floor.

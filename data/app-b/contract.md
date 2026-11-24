# Appendix B — Stage 4 drafting contract

**Status:** Step 0 complete; Step 1 complete; Step 2 pilot complete; Step 3 in progress, Table 1 drafted, November 24, 2026. This is a production record, not manuscript text.

**Scope:** [`chapters/52-appendix-b.md`](../../chapters/52-appendix-b.md), Stage 3 researched outline to Stage 4 draft.

**Allowance:** 20 text pages; 255 ledger rows, of which 254 are printed and one is the Table 6 trade-panel reserve (Stage 3 estimate 254–260).

## 1. Decisions frozen at Step 0

1. **Panel layout.** One pipe table per panel. Each panel carries a `**Caption.**` line that repeats the display number and panel letter, for example `**Caption.** App. B, Table 1, Panel A. National population and urban share, 1630–2020.` One table-level source line and one set of notes follow the last panel.
2. **Heading scheme.** An unnumbered `## Note on the Tables`, then numbered `## 1.` through `## 8.` for the eight tables. Display numbers remain `App. B, Table 1` through `App. B, Table 8` in captions and text. Panels do not create new display numbers.
3. **Verification.** No unverified numeric cell appears in the drafted file. A failed source check becomes a declared blocker, not a blank, a guess, or a flagged cell.
4. **Fallback order if the typeset tables exceed 20 pages.** First tighten Table 2 to 10–11 columns without losing the 60-election scope; then cut Table 8's three state land-use rows to one; then drop Table 3's 1763 row and retitle the table 1783–1917. Definitions and source lines are not cut.
5. **Location.** Contract and production files live in `data/app-b/`.
6. **Source access at Step 0.** HSUS Millennial and image-only PDFs can be supplied or confirmed. WID, CQ Press, and print/archival items were not listed as available. Their table-level consequences are in §5.
7. **Table 1 design (Step 3).** Panel A prints year, total population, urban population in thousands, and urban share; the White, Black, and enslaved columns are not printed in Table 1 because Table 6 owns race and legal status. Panel B prints regional counts in thousands and shares; the 1860 and 1900 rows use the HSUS retrospective series with a note and regional-sum shares because those counts do not sum to the national census totals. Panel C prints the five largest legal city-proper places.
8. **Table form and style (Step 2 pilot).** Table 3 uses eight columns with a combined area cell and letter-keyed row notes. Appendix tables use a `.appendix-table` style at 8-point type, reduced cell padding, header repetition, and row-level break avoidance; the style is added to `styles/pdf.css`. Table 2 uses the ten-column packing: winner (party), winner EV, runner-up (party), runner-up EV, other EV, winner PV (share), runner-up PV (share), turnout (VEP; rate), and notes; Panel A uses the shorter header without popular-vote columns. Table 3's pilot length of about 2.5 pages, including row notes, is accepted provisionally; the 1.75-page allocation will be reconciled at the full 20-page proof.

## 2. Verification standard

- **`verified`:** the printed value has been checked against the exact locator named in the table's source line. If that locator is a secondary work reporting an original, the cell is verified only for what the secondary work reports; the source line must say “as cited in …” and the table note must state that the original was not consulted.
- **`pending_image`:** the value is in a page-image PDF that has not yet been read or confirmed against the printed cell.
- **`pending_paywall`:** the value is behind a subscription or registration barrier that has not been opened.
- A cell is not `verified` because it appears in the Stage 3 outline, a search snippet, or a secondary summary. The outline's values are benchmarks.
- Interpretive and scholarly notes may retain “consulted in part” or “not read in full” limitations. Those limitations do not block a table when the note does not supply a cell value, but they must not be silently upgraded.

## 3. The eight-table contract

| Display | Rows | Structure | Universe, dates, breaks | Principal sources | Residual verification |
|---|---|---|---|---|---|
| **App. B, Table 1** | 41 | A: 14 national (total, urban thousands, urban share); B: 7 regional (counts in thousands, shares); C: 20 city | Conterminous through 1940; 50 states and D.C. from 1950; Puerto Rico and Island Areas in a note; 1790 Midwest and West n.a.; 1860/1900 shares use the regional sum | HSUS 1975; 1960, 2000, 2010, 2020 Censuses; Gibson | Verified: totals, urban, regions, cities. 1860/1900 regional sum mismatch noted; race/slavery in Table 6 |
| **App. B, Table 2** | 60 | A: 1789–1824 short header; B: 1828–1900 full; C: 1904–2024 full | 60 elections; no 1824 popular vote; voting-eligible-population turnout; pre-1828 rates partial or n.a. | HSUS Y; American Presidency Project and Ratcliffe; NARA; CRS; FEC; Election Lab | All 60 rows; pre-1828 turnout; 1828–1900 state coverage; FEC and Clerk reconciliation |
| **App. B, Table 3** | 13 | A: 9 continental; B: 4 overseas | 1763–1917; gross square miles; nominal cost; control versus sovereignty | 1947 Statistical Abstract; BLM; treaty texts; 1940 Canal Zone census | 1947 gross areas; BLM cells; 2010 measurement notes; 1977 and 1917 dates |
| **App. B, Table 4** | 13 | A: 1775–1898; B: 1917–1991; C: 2001–2021 | Uniformed military only; CRS FY2011 base; DoD OCO current dollars | CRS RL32492 and RS22926; DoD August 2021; Barceló and Hacker; Crawford | CRS cells; frozen DoD snapshot; Confederate row; Heitman; OCO components |
| **App. B, Table 5** | 42 | A: 21; B: 6; C: 3; D: 8; E: 4 | 1820–2024; recorded-arrivals and LPR labels; ACS stock; DHS January 1 estimates | DHS 2022 and 2024 Yearbooks; ACS B05002; 1921, 1924, and 1929 instruments | Decade totals; 2022/2024 splice; 688,230 Unknown; ACS vintages; 1921 allotments |
| **App. B, Table 6** | 25 | A: 3; B: 8; C: 6 (24 printed; one reserve); D: 8 | British Caribbean only; 1790–1860 census; net forced migrants; Bb210 price series | HSUS 1975 and Millennial; SlaveVoyages; Pritchett and Tadman; Dunn and Southey | Dunn and Southey pages; Bb210 and Cc2 values; 1860 page images; 388,747 imports |
| **App. B, Table 7** | 38 | A: 15; B: 9; C: 7; D: 7 | Fiscal years; 1900/1930 breaks; Panel D ends 2000 | OMB FY2027; HSUS; BLS, BEA, and Maddison; WID and Census; Editor & Publisher | 15 OMB values; Ba475 and BLS; CPI and GDP bases; WID; Gini; newspaper sub-series |
| **App. B, Table 8** | 23 | A: 7; B: 5; C: 6; D: 5 | 1930–1944; 48-state 1940 universe; modern TVA capacity | TVA; Statistical Abstract 1943; 1940 Agriculture and Population; Long and Siu | TVA dates and capacity; five CCC values; Kansas, Oklahoma, and Texas cells; California and migration |

**Page allocation:** Table 1, 2.5; Table 2, 4; Table 3, 1.75; Table 4, 2; Table 5, 2.5; Table 6, 2; Table 7, 2; Table 8, 1.75; note, captions, definitions, and notes, 1.5. Total, 20. Table 3 measured about 2.5 pages in the Step 2 pilot, including row notes, and Table 1 measured about 3 pages in the Step 3 proof; both allocations are provisional and the total will be reconciled at the full proof. Do not cut evidence to protect the estimate.

## 4. Common rules

- **§1.2 conventions apply verbatim:** time labels; present-day geography with historical boundaries stated; resident population; nominal dollars plus a named deflator; numerator and denominator for rates; historical race and status categories; `n.a.`, `—`, and `0`; `(p)`; source rounding; full source lines; rights.
- **§10.2 forbidden comparisons apply verbatim.** All 34 bullets remain drafting checks and, where relevant, table notes. None is dropped for space.
- **§10.3 production rules apply verbatim:** CSV or JSON production file per table; caption, source line, and notes; original-compilation rights; real header rows, no merged cells, legibility at 8-point type.
- **Source keys** remain the 153 keys defined in the Stage 3 note list. Keys are not renamed at Stage 4. A key that no longer supports a surviving reference is removed only after its evidence is either reassigned or explicitly retired.
- **Display numbers** are frozen as App. B, Table 1 through App. B, Table 8.

## 5. Open items and access consequences

### 5.1 Editorial notes carried into drafting

- **`app-b-state-selection-check`.** Still an editorial task. It affects Table 2's Notes column for 1828–1900: South Carolina through 1860, Florida in 1868, Colorado in 1876, and any other legislative-selection or non-reporting state. The outline allows the American Presidency Project or CQ Press; with CQ Press unavailable, the check closes only if APP confirms the state list. Record the APP pages used and state the choice in the table note.
- **`app-b-map26-ccc-check`.** Open, but it is a Map 26 task, not a Table 8 cell. It belongs in the Map 26 production record with Fechner's *First Report* and NARA RG 35, Entry 3. It does not block Table 8's national CCC rows and must not be deleted.

### 5.2 Source-access consequences

- **HSUS Millennial: available.** Tables Bb209–214, Cc1–2, and Ba470–477 can be opened. This closes the main Table 6 price-series and Table 7 unemployment-series access gap.
- **Image-only PDFs: available for confirmation.** The 1860 Census, 1940 Agriculture, 1940 Population, and 1960 Census pages can be read and ambiguous cells confirmed. This addresses Table 1's 1950 cells, Table 6's 1860 totals, and Table 8's 1940 cells.
- **WID: not supplied.** The top-1-percent pre-tax national income share is a headline column in Table 7, Panel C, and the outline forbids substituting the 2022 PSZ appendix tables or a different vintage. A public WID download will be tested at Table 7. If it cannot be opened, Table 7 cannot be drafted under the no-unverified-cells rule; the options are a WID export, a documented scope change removing the column, or a declared blocker. No action is needed for Step 1.
- **CQ Press: not supplied.** The outline permits APP or CQ Press. Use APP, record the pages, and keep the `app-b-state-selection-check` note only if APP leaves a state unresolved.
- **Print and archival items: not supplied.** Tadman 1989 and Dunn 1972 remain second-hand: Tadman's 1,110,000 is cited through Pritchett, and Dunn's Barbados and Jamaica figures through the DOI record and the research review. The affected source lines must say “as cited in …” and the notes must carry the limitation. Southey's 1673 return is an OCR text and needs a printed-page check. Heitman 1903 and the 1902 War Department report can be approached through the Internet Archive copy and the 1914 *Congressional Record* transcription, each with its limitation. Fechner and RG 35 remain a Map 26 task.

### 5.3 Cell-level caveats

- **Table 6, Panel C, Tadman row.** Print 1,110,000 only as “Tadman, as cited in Pritchett.” Do not present it as read from Tadman.
- **Table 6, Panel A.** The Barbados 38,782 and Jamaica 7,768 and 9,504 values need either the printed Dunn and Southey pages or a named secondary locator. Until then they are not `verified`.
- **Table 4, Panel A note.** The 1902 War Department figures are quoted through the 1914 *Congressional Record*; the 2,818 wounded figure is from Heitman's OCR text. Both need page confirmation.
- **Notes that are not cell sources.** Hacker 2011, Kotlikoff 1979, Margo 1993, Auten–Splinter 2024, and Pritchett 2001 support notes or alternatives. Keep their limitations; do not upgrade them.

## 6. Step 2 pilot record

- **Artifacts.** `build/app-b-pilot.md` and `build/app-b-pilot.pdf`; the PDF is a five-page Letter proof. `build/` is gitignored, so the pilot is a review artifact, not a manuscript file.
- **Table 3.** 113 cells: 100 `verified`, 6 `n_a`, 6 `not_applicable`, and 1 `unverified` (the 1845 row note’s 1850 stock terms). Twelve of thirteen rows are `verified`; the 1845 Texas row remains `unverified` pending 9 Stat. 446–47.
- **Sources opened.** BLM *Public Land Statistics 2020*, Table 1-1; *Statistical Abstract 1947*, Table 1; 1940 Canal Zone Census, p. 4; 2010 State Area Measurements; the 1763, 1783, 1819, 1846, 1853, 1898 Spain, and 1903 texts; the 1845 Texas resolution; the 1848, 1867, and 1898 Hawaii NARA pages; the 1917 FRUS circular; the 1977 Panama milestone; the 1993 Apology Resolution; *Hawaii v. OHA*; and the Silva petitions page.
- **Design.** Eight-column Table 3 with a combined area cell and letter-keyed row notes; `.appendix-table` at 8-point type with reduced padding and row-level break avoidance; ten-column packed Table 2 header; Table 3’s ~2.5-page pilot length accepted provisionally.
- **Open.** The 1845 stock-term note (EX-17); Table 3 is not yet in the appendix; the full 20-page measurement remains for the layout proof.

## 7. Step 0–2 exit

- [x] Contract recorded.
- [x] Panel layout, heading scheme, verification rule, fallback order, and file location frozen.
- [x] Source-access gaps listed with their table impact.
- [x] No manuscript file changed.
- [x] Step 1: eight production CSVs, the ledger, and the row ledger created; benchmarks seeded as `unverified`.
- [x] Step 2: Table 3 verified and drafted in the pilot; Table 2 width proof produced; template decisions recorded; `.appendix-table` style added.
- [ ] Step 3: verify and draft the remaining tables in display order, beginning with Table 1.

# Appendix B exceptions and open items

**Status:** Step 1 register, November 24, 2026. These are production blockers, not manuscript notes. Each item closes only when the evidence is checked and the affected cell's status changes.

## EX-01 — Table 6 trade panel reserve row

- **Affected:** `app-b-table-06`, Panel C, row `t06-c-06` (“Reserve (not printed)”).
- **Issue:** The trade panel's row cap is six with one slack. The published panel has five rows; the sixth ledger row is a reserve.
- **Resolution:** Keep the reserve row in the ledger, exclude it from the printed table, and do not count it in the published row total. The published Table 6 has 24 rows, not 25.
- **Owner:** Agent, at Table 6 drafting.
- **Status:** Closed as a design decision; no evidence needed.

## EX-02 — Table 7 top-share column and WID

- **Affected:** `app-b-table-07`, Panel C, column `top1_share`, all seven rows.
- **Issue:** The series is WID `sptinc_p99p100_z`, 2025/2026 vintage. WID was not supplied at Step 0. The outline forbids splicing the 2022 PSZ appendix tables or using a different vintage.
- **Resolution:** Test the public WID download at Table 7. If it fails, the options are a WID export, a documented scope change removing the column, or a declared blocker. Do not substitute another series.
- **Owner:** Agent tests; human supplies export or decides scope.
- **Status:** Resolved November 24, 2026. The WID public API returned the 2026 release series `sptinc_p99p100_992_j`; Table 7 Panel C uses one vintage. No scope change is needed.

## EX-03 — Table 2 state-selection check

- **Affected:** `app-b-table-02`, Panel B, 1828–1900, Notes column.
- **Issue:** `app-b-state-selection-check` says CQ Press was not consulted. The outline permits the American Presidency Project or CQ Press. CQ Press was not supplied.
- **Resolution:** Confirm South Carolina through 1860, Florida in 1868, Colorado in 1876, and any other legislative-selection or non-reporting state against APP. Record the APP pages. If APP leaves a state unresolved, keep the editorial note and mark the row.
- **Owner:** Agent; human confirms the APP pages if the site blocks access.
- **Status:** Open for verification, not a table-design change.

## EX-04 — Tadman 1,110,000 cited through Pritchett

- **Affected:** `app-b-table-06`, Panel C, “Domestic trade, Tadman, 1790–1860.”
- **Issue:** Tadman 1989, p. 12, was not read. The figure is reported in Pritchett 2017, p. 3 n. 2.
- **Resolution:** Print the value with the source line “Tadman, as cited in Pritchett.” The note must say the original was not consulted. Do not present it as verified against Tadman.
- **Owner:** Agent; human may supply the book page later.
- **Status:** Resolved for drafting November 24, 2026. Table 6 Panel C prints 1,110,000 with the source cell “Pritchett, citing Tadman”; the note says the book was not consulted. The value is verified only as Pritchett reports it.

## EX-05 — Dunn and Southey print pages

- **Affected:** `app-b-table-06`, Panel A: Barbados 1679/80 enslaved 38,782; Jamaica 1673 White 7,768 and enslaved 9,504; Dunn's adjacent White benchmarks.
- **Issue:** Dunn 1969 was consulted through its DOI record and published citations, not full text. Dunn 1972 was not read. Southey is an OCR text, and the earlier note cited the wrong volume.
- **Resolution:** Confirm the printed pages, or name the secondary locator and label the values “as cited in ….” Do not upgrade them to `verified` against the original without the page.
- **Owner:** Agent; human supplies access if available.
- **Status:** Resolved for drafting November 24, 2026. Southey’s 1673 return was read at vol. 2, p. 104 as a printed-page image; the earlier “vol. 1, pp. 104–106” citation was wrong. Barbados 38,782 and Dunn’s 21,725/19,568 benchmarks remain “as cited in” published citations because Dunn was not read in full. The note carries the limitation.

## EX-06 — Heitman and the 1902 War Department report

- **Affected:** `app-b-table-04`, Panel A note: 2,818 Philippine-American War wounded; 4,374 all-cause deaths and 126,468 served.
- **Issue:** Heitman 1903 is an OCR copy; the 1902 report is quoted through the 1914 *Congressional Record*.
- **Resolution:** Confirm the Heitman page and the *Congressional Record* page. Keep the note's warning that the categories do not reconcile cell for cell. Do not add a fourteenth row.
- **Owner:** Agent.
- **Status:** Open for verification; no table-design change.

## EX-07 — Page-image cells

- **Affected:**
  - `app-b-table-01`, 1950 race, urban, and regional cells (1960 Census PC(S1)-4 and Table 44).
  - `app-b-table-06`, 1860 enslaved and Black totals (1860 Census pp. ix and 599).
  - `app-b-table-08`, Panel C land-use cells (1940 Census of Agriculture, Tables 4, 9, 10) and Panel D population (1940 Census of Population, Table 3).
- **Issue:** The PDFs are page images or OCR with no reliable text layer. The user can confirm ambiguous cells.
- **Resolution:** Read the image, record the printed cell, and set `verified`. If a cell is illegible, leave `pending_image` and record it here.
- **Owner:** Agent reads; human confirms ambiguous cells.
- **Status:** Resolved for Table 6 on November 24, 2026: the 1860 Census pp. ix and 599 were read as images, confirming 3,953,760 enslaved, 487,970 free “colored,” 4,441,730 “colored,” and 3,542,147 “black” plus 411,613 “mulatto.” Table 1’s 1950 cells and Table 8’s 1940 cells remain open.

## EX-08 — Table 1 universes and 1790/1970/2020 rules

- **Affected:** `app-b-table-01`, rows 1790, 1950, 1970, 2000, 2010, 2020; Panel B 1790; Panel C.
- **Issue:** The Stage 3 decisions are closed but the cells are not all transcribed: 1790 Midwest and West are n.a.; 1950 uses the 50-state retrospective; 1970 uses the official total with the 23,372 tabulation difference in a note; 2020 uses race alone in the cells and the combination figures in the note.
- **Resolution:** Transcribe the remaining cells, preserve the notes, and do not mix conterminous and 50-state bases. Confirm the 1790 correction and the 2020 alone/combination rule in the table note.
- **Owner:** Agent.
- **Status:** Open for row-level verification; the design is closed.

## EX-09 — Table 2 2024 FEC and Clerk reconciliation

- **Affected:** `app-b-table-02`, 2024 row.
- **Issue:** The FEC official results are the primary series; the House Clerk's 2024 state returns are not yet reconciled.
- **Resolution:** Reconcile in the production file when the Clerk PDF is available. Print the FEC series; put any difference in the note. Do not mix FEC and Clerk cells in one row.
- **Owner:** Agent.
- **Status:** Open.

## EX-10 — Table 5 2024 Unknown and 2020 ACS vintages

- **Affected:** `app-b-table-05`, Panel A 2020–2024 and 2024; Panel D 2020 and 2024.
- **Issue:** The FY 2024 region-of-last-residence distribution is 32.3 percent Unknown; the 2020 stock row is a 2016–2020 ACS 5-year estimate; the 2024 stock is a 1-year estimate with a margin.
- **Resolution:** Keep the 688,230 Unknown total and the 440,430 FY 2024 Unknown in the note. Label the 2020 row “2016–2020 (ACS 5-yr)” and the 2024 row “2024 (ACS 1-yr).” Do not read the 2024 last-residence declines as real declines.
- **Owner:** Agent.
- **Status:** Open for row-level verification; the design is closed.

## EX-11 — Table 8 and Map 26 CCC counts

- **Affected:** `app-b-table-08`, Panel B; Map 26 production file.
- **Issue:** `app-b-map26-ccc-check` is open: the 48-state CCC counts need Fechner's *First Report* and NARA RG 35, Entry 3. Table 8 does not print state counts.
- **Resolution:** Keep the state counts in the Map 26 production CSV. Collate them before Map 26 publication. Do not add them to Table 8.
- **Owner:** Agent for the map record; human for archive access.
- **Status:** Open, not a Table 8 blocker.

## EX-12 — Table 3 sovereignty and termination cells

- **Affected:** `app-b-table-03`, Hawaii, Spanish treaty, Canal Zone, Danish West Indies rows.
- **Issue:** The legal forms and current statuses are partly seeded; the counterparty, cost coverage, sovereignty/control, and termination columns are not yet fully transcribed.
- **Resolution:** Use the closed rules: Hawaii joint resolution and contested sovereignty; Philippines independent 1946; Canal Zone control, not sovereignty, abolished 1979, canal transferred 1999; Danish West Indies $25 million in gold, paid March 31, 1917. Keep the 1947 gross-area standard and the 2010 notes separate.
- **Owner:** Agent.
- **Status:** Resolved November 24, 2026. All 13 Table 3 rows are `verified`; the 1845 stock terms are confirmed in EX-17.

## EX-13 — Table 7 non-seeded series

- **Affected:** `app-b-table-07`, Panels A, B, C, D.
- **Issue:** Only the unemployment and a few n.a. cells are seeded. OMB receipts/outlays/debt, railroad mileage, steel, CPI, GDP per capita, WID top shares, Gini, union density, LFP, newspapers, and telephones remain to be transcribed.
- **Resolution:** Work panel by panel. Keep the FY2024 actuals, the Darby–Weir cells, the CPI and GDP bases, the 2000 Panel D endpoint, and the single WID vintage. Do not fill a panel with a series from a different definition.
- **Owner:** Agent; WID export from human if needed.
- **Status:** Resolved November 24, 2026. Table 7 is drafted with 38 rows and 191 cells (147 verified, 44 n.a.); OMB, HSUS, BLS, BEA, Maddison, Census, and Editor & Publisher values are transcribed. See the Table 7 notes.

## EX-14 — Table 2 election rows not seeded

- **Affected:** `app-b-table-02`, 55 of 60 rows.
- **Issue:** The ledger has all 60 elections, but most cells are `not_started`. The 1824 rule, the 1872 and 1876 counts, and the 2020 and 2024 results are seeded.
- **Resolution:** Transcribe the remaining elections from HSUS Y 79–83, NARA, the House Clerk, and the Election Lab. Label pre-1828 turnout partial or n.a. Apply the 1828–1900 coverage notes. Do not invent a popular vote for legislative-selection states.
- **Owner:** Agent.
- **Status:** Open.

## EX-15 — Table 1 historical city ranks

- **Affected:** `app-b-table-01`, Panel C, 1790, 1860, and 1920.
- **Issue:** Only Philadelphia (1860), Brooklyn (1860), and New York City (1920) are seeded. The other ranks need Gibson's tables.
- **Resolution:** Transcribe the top five legal city-proper places for each year; add the boundary notes. Do not substitute urban areas or metropolitan areas.
- **Owner:** Agent.
- **Status:** Open.

## EX-16 — Table 5 decade regional cells

- **Affected:** `app-b-table-05`, Panel A.
- **Issue:** Only six decade totals and the 2020–2024 partial are seeded. The regional columns (Europe, Asia, Americas, Africa, Oceania, Unknown) remain to be transcribed.
- **Resolution:** Use the 2022 Yearbook Table 2 for 1820s–2010s; use the 2024 Table 2 for the 2020–2024 splice. Keep the 2022 “America” row and the 2024 North America plus South America separate; do not add them.
- **Owner:** Agent.
- **Status:** Open.

## EX-17 — Texas 1850 stock terms

- **Affected:** `app-b-table-03`, 1845 Texas row, `notes` cell.
- **Issue:** The note says the 1850 act authorized $10 million in 5 percent stock. The BLM compiled cost of $15,496,448 is verified, but the act’s page image was not opened in the pilot; the page 447 PDF was not available from the GovInfo one-page endpoint.
- **Resolution:** Opened 9 Stat. 446–47 at GovInfo page 447 and confirmed the $10 million, 5 percent, fourteen-year terms. The note cell and Table 3 row are `verified`.
- **Owner:** Agent.
- **Status:** Resolved November 24, 2026.

## EX-18 — Table 1: 1860 and 1900 regional counts do not sum to the national total

- **Affected:** `app-b-table-01`, Panel B, 1860 and 1900 rows.
- **Issue:** HSUS A 172–194 gives 1860 regional counts of Northeast 12,295,000; North Central 9,097,000; South 11,133,000; and West 619,000, which sum to 33,144,000 against the 1860 national total of 31,443,321. The 1900 counts (21,047,000; 26,333,000; 24,524,000; 4,309,000) sum to 76,213,000 against 75,994,575. The difference is not rounding. The source’s regional series allocates population on a geographic basis that does not reconcile to the census total for these years; the 1790 values likewise include 51,000 North Central and 179,000 West outside the enumerated total, which is why the plan prints those cells `n.a.`.
- **Resolution options:** (a) print the source regional counts with a note and calculate shares against the regional sum, not the national total; (b) use a different regional series that sums to the census total; (c) drop 1860 and 1900 from Panel B and begin the regional series in 1910, when the Census historical series reconciles.
- **Owner:** Human decision; agent implements.
- **Status:** Resolved November 24, 2026. Table 1 Panel B prints the source counts with the double-dagger marker and uses regional-sum shares; the table note explains the mismatch. See `chapters/52-appendix-b.md`, Table 1, Panel B.

## EX-19 — Table 1: race columns duplicate Table 6 and are costly to extract

- **Affected:** `app-b-table-01`, Panel A, White, Black, and enslaved columns.
- **Issue:** The Stage 3 design carries White, Black, and enslaved counts for every national benchmark row. HSUS A 91–104 and A 73–81 print the race totals by sex and residence on rotated, OCR-poor pages; extracting every benchmark year would add about a page and duplicate the race and slavery series that Table 6 already owns. The colonial rows (1630–1780) cannot supply White and Black on the same basis, and the 1950 50-state race cells come from a different source than the conterminous series.
- **Resolution options:** (a) drop the three race columns from Table 1 and add a note pointing to Table 6; (b) keep Black and enslaved only, dropping White; (c) keep all three and complete the extraction, accepting the added page and the duplication.
- **Owner:** Human decision; agent implements.
- **Status:** Resolved November 24, 2026. Table 1 no longer prints the race columns; Table 6 owns race and legal status. The 14 former cells are in `table-01-race-reference.csv`, marked reference only.

## EX-20 — Z 1–19 enslaved values shifted by one decade

- **Affected:** the Table 6 source bullet in §7.3 and the `app-b-hsus-z1-19` note; the Table 1 race reference file.
- **Issue:** The Stage 3 outline gave 1780 = 675,420 enslaved, 1760 = 459,822, and 1750 = 325,806. The printed table shows 1780 = 575,420; 1770 = 459,822; 1760 = 325,806; and 1750 = 236,420. The outline had shifted the values by one decade. The 1780 total (2,780,369) was correct.
- **Resolution:** Corrected the Table 6 bullet, the note’s “Used for” sentence, and the two reference cells on November 24, 2026. The printed Table 1 does not use these cells; Table 6 will use the corrected values when it is drafted.
- **Owner:** Agent.
- **Status:** Resolved. Recheck the Table 6 draft against the printed Z 1–19 page.

## EX-21 — Table 2 values seeded from a secondary compilation

- **Affected:** `app-b-table-02`; all 710 cells.
- **Issue:** Table 2’s candidate names, electoral votes, and popular-vote shares are verified against the American Presidency Project compilation. The electoral-vote values are the standard series but have not been checked row by row against HSUS Y 79–83 or NARA. Turnout is from the Election Lab v1.4 CSV. The table is drafted and inserted under §3; the official cross-check remains for Stage 5.
- **Resolution:** Verify the electoral votes against HSUS Y 79–83 and NARA for the elections the outline already resolved; verify the popular-vote shares against the APP election pages or HSUS; record the exact locators. The table remains `drafted`, not `checked`, until that pass is complete.
- **Owner:** Agent.
- **Status:** Resolved for the APP compilation on November 24, 2026; the HSUS/NARA/FEC row-level cross-check remains for Stage 5.

## EX-22 — Table 2 is five pages against a four-page allowance

- **Affected:** `build/app-b-table-02.pdf`.
- **Issue:** At the adopted 8-point appendix-table style, the 60-row table runs five pages. Candidate and party cells wrap, and the 1828–1900 notes are long.
- **Resolution options:** (a) abbreviate party labels and candidate names further and shorten the notes; (b) move the special-election notes to a letter key below the table; (c) accept a one-page overrun and reconcile the appendix total at the full proof. The contract’s fallback order puts column tightening before row cuts.
- **Owner:** Human decision; agent implements.
- **Status:** Resolved November 24, 2026: the five-page length is accepted provisionally and will be reconciled at the full 20-page proof.

## EX-23 — Table 4 is three pages against a two-page allowance

- **Affected:** `build/app-b-table-04.pdf`.
- **Issue:** The 13-row, ten-column table plus the Civil War, Panel C, Philippine, and cost notes runs three pages at the adopted 8-point setting.
- **Resolution:** Accepted provisionally on November 24, 2026; reconcile the appendix total at the full 20-page proof. If compression is needed, shorten the notes before cutting rows or definitions.
- **Owner:** Human decision; agent implements.
- **Status:** Open, accepted provisionally.

## EX-24 — Table 5: 2020 stock row reserved; three-page proof

- **Affected:** `app-b-table-05`, Panel D 2020 row; `build/app-b-table-05.pdf`.
- **Issue:** The 2020 ACS 5-year estimate was not transcribed in this pass, so the 2020 stock row is not printed; the 2010 and 2024 ACS 1-year estimates bracket the period. The 41-row table plus notes runs three pages against the 2.5-page allowance.
- **Resolution:** The 2020 row is recorded as a reserve with a note. The three-page length is accepted provisionally and will be reconciled at the full 20-page proof. If the 2020 estimate is supplied later, restore the row and its label.
- **Owner:** Human decision; agent implements.
- **Status:** Open, accepted provisionally.

## EX-25 — SlaveVoyages Mainland North America totals changed between releases

- **Affected:** `app-b-table-06`, Panel C, U.S. imports row; `app-b-slavevoyages-estimates`.
- **Issue:** The Stage 3 outline and earlier releases give 472,381 embarked and 388,747 disembarked for Mainland North America. The live SlaveVoyages estimates table, read in a browser session on November 24, 2026, gives 472,372 embarked and 388,744 disembarked. The nine-person and three-person differences are vintage differences, not definitional changes.
- **Resolution:** Table 6 prints the live totals, 472,372 and 388,744, with the earlier figures in the note. The transatlantic totals remain 12,521,354 embarked and 10,702,644 disembarked. Update any chapter reference to 472,381/388,747 at Stage 6; do not silently mix the two vintages.
- **Owner:** Agent; human should confirm the choice if a chapter quotes the older figures.
- **Status:** Open for Stage 6 cross-reference reconciliation; the Table 6 cells are drafted.

## EX-26 — Table 6 is three pages against a two-page allowance

- **Affected:** `build/app-b-table-06.pdf`.
- **Issue:** The 24-row, four-panel table plus the Panel A row notes, Panel B–D definitions, source line, and alt text runs three pages at the adopted 8-point setting. The Stage 3 allowance is two pages.
- **Resolution:** Accepted provisionally on November 24, 2026; reconcile the appendix total at the full 20-page proof. If compression is needed, shorten the Panel B and C notes before cutting rows or definitions.
- **Owner:** Human decision; agent implements.
- **Status:** Open, accepted provisionally.

## EX-27 — Appendix proof duplicates notes when a key is reused

- **Affected:** `build/app-b-full.pdf`; the combined note list in the appendix and the book.
- **Issue:** The appendix has 154 named note definitions but 279 footnote references. The current Pandoc build creates one rendered note per reference, so a note used in a table cell, a row note, and a source line appears two or three times. The appendix proof is 87 pages, and the note list is inflated; the 20-page text allowance cannot be measured from this build.
- **Resolution:** `tools/dedupe-notes.lua` keeps the first rendered note for each distinct note body and replaces later copies with a link to that note. It is wired into the EPUB, HTML, and print targets in the `Makefile`. The full-book HTML now renders 3,355 definitions once each; all 15,120 references resolve to an existing note ID. One pair of editorial notes in Chapters 36 and 37 had identical bodies and was made chapter-specific so the filter would not merge them.
- **Owner:** Agent; build-pipeline change reviewed at Stage 5/7.
- **Status:** Resolved November 24, 2026. Recheck after any change to note text or filter order.

## EX-28 — Table 7 design corrections from the sources

- **Affected:** `app-b-table-07`, Panels A–D; the Table 7 caption and notes.
- **Issue:** The Stage 3 design assumed a 1790 first row, a single “gross federal debt” series, one “miles operated” series, BLS LNS annual values, and a 1960 start for household telephone data. The sources do not support those assumptions without qualification.
- **Resolution:**
  - The first Panel A row is the combined **1789–1791** account; the federal government published no separate 1790 fiscal-year account. The table is titled 1789–2024.
  - Debt is **public debt through 1930** (HSUS Y 338 / Ea587) and **gross federal debt from 1940** (OMB Table 7.1); the note states the break.
  - Railroad mileage is **road operated** in 1830 and 1860 (Q 321) and **road owned** in 1900–1950 (Q 284, column 287); 1970 is `n.a.` because the 1975 scan omits the 1956–1970 rows.
  - Unemployment for 1950–2024 uses BLS **annual averages, LNU04000000**; the monthly seasonally adjusted LNS14000000 does not publish an annual row in the BLS annual table. LFP uses **LNU01300000** for the same reason. The notes name the series.
  - Union density is **D 951, percent of nonagricultural employment**, for 1950 and 1970, and the **BLS union membership rate** for wage and salary workers for 2000–2024; the denominators differ and the note says so.
  - Panel D keeps the 1850 row as all `n.a.` because the daily-newspaper series begins in 1880; the 1950 household telephone rate is 61.8 percent from HSUS R 3, before the Census series begins in 1960.
- **Owner:** Human review of the printed table; agent implemented.
- **Status:** Open for human approval of the design corrections; the cells are drafted.

## EX-29 — Table 7 is three pages against a two-page allowance

- **Affected:** `build/app-b-table-07.pdf`.
- **Issue:** The 38-row, four-panel table plus the panel definitions, source line, and notes runs three pages at the adopted 8-point setting.
- **Resolution:** Accepted provisionally on November 24, 2026; reconcile the appendix total at the full 20-page proof. If compression is needed, shorten the Panel B and C notes before cutting rows or definitions.
- **Owner:** Human decision; agent implements.
- **Status:** Open, accepted provisionally.

## EX-30 — Table 8 is three pages against a 1.75-page allowance

- **Affected:** `build/app-b-table-08.pdf`, `build/app-b-table-08-clean.pdf`.
- **Issue:** The 23-row, four-panel table plus its row notes, source line, definitions, universe note, and alt text runs three pages at the adopted 8-point setting. The table-only portion is about two pages; the evidence notes add the third. The handoff predicted about 2.5 pages and allowed a provisional overrun.
- **Resolution:** Accepted provisionally on November 24, 2026; reconcile the appendix total at the full 20-page proof. If compression is needed, shorten the Panel B camp-count and Panel D migration notes before cutting rows or definitions. Do not delete the 48-state universe note, the TVA capacity discrepancy, or the 20-county definition.
- **Owner:** Human decision; agent implements.
- **Status:** Open, accepted provisionally.

## EX-31 — Long and Siu page locator corrected

- **Affected:** `app-b-long-siu-2016`; Table 8, Panel D; `table-08.csv`.
- **Issue:** The Stage 3 note gave “pp. 1002, 1007, and 1012” without assigning claims to pages. The 20-county totals (120,859 to 97,606) are at p. 1007, not p. 1002; p. 1002 supplies the Southern Plains 1890–1930 context. The California destination finding is at pp. 1012 and 1014–17.
- **Resolution:** The note now assigns the 20-county totals to p. 1007, the Southern Plains context to p. 1002, and the destination finding to pp. 1012 and 1014–17. The table-08 locators were corrected to p. 1007. The California migration counts themselves are from *Statistical Abstract 1946*, Table 31, not from Long and Siu.
- **Owner:** Agent; verified against the Cambridge PDF of the 2018 article.
- **Status:** Resolved November 24, 2026.

## EX-32 — Appendix B body is 25 pages against a 20-page allowance

- **Affected:** `build/app-b-body.pdf`; `chapters/52-appendix-b.md`; the README Appendix B allowance.
- **Issue:** After final assembly and the duplicate-note filter, the body proof—eight tables plus the Note on the Tables, with citation references removed—measures 25 pages at the adopted 8-point setting. The combined note list adds 27 pages and is excluded from the text-page goal under the book’s page metric. The measured table sections are Table 1, 3; Table 2, 5; Table 3, 3; Table 4, 3; Table 5, 3; Table 6, 3; Table 7, 3; Table 8, 3; Note on the Tables, about 1. The 20-page allocation was 2.5 + 4 + 1.75 + 2 + 2.5 + 2 + 2 + 1.75 + 1.5.
- **Resolution:** Recorded, not resolved. The contract fallback order is (1) tighten Table 2 to 10–11 columns without losing the 60-election scope, (2) cut Table 8’s three state land-use rows to one, and (3) drop Table 3’s 1763 row. Those cuts are not applied because each would remove promised material or require a new table design; the overrun is largely the accumulated provisional table overruns already recorded in EX-22, EX-23, EX-24, EX-26, EX-29, and EX-30.
- **Owner:** Human decision on a revised 25-page allowance or the fallback cuts.
- **Status:** Open. The appendix remains `drafted`, not `checked`.

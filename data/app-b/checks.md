# Appendix B checks

**Status:** Step 1, November 24, 2026. No check has been run. This file records the checks to run as each table is verified and drafted. Add the date, the values checked, and the result. A check is not “passed” because the arithmetic is plausible; it passes when the printed cells and the cited source agree.

## 1. Structural checks

Run after every table edit.

- [ ] Every ledger row has at least one cell, or is the Table 6 reserve.
- [ ] Every cell has a non-empty `value`, `unit`, `source_key`, and `locator`.
- [ ] No duplicate `(table_id, panel, row_id, column_id)`.
- [ ] No cell status is `unverified` in a table marked `drafted`.
- [ ] Panel and row counts match the contract: 41, 60, 13, 13, 42, 25 (24 printed), 38, 23.
- [ ] No column or panel outside the contract.
- [ ] `n.a.` and `—` are used only as defined; no blank cells.

## 2. Table 1 — Population and urbanization

- [x] National totals match HSUS A 1–5 and the decennial Census for 2000–2020.
- [x] 1790: 3,929,214 corrected total; Northeast and South only; Midwest and West `n.a.`; Vermont correction applied.
- [x] 1950: 151,325,798 total; 96,846,817 urban; 64.0 percent; 50-state retrospective.
- [x] 1970: 203,235,298 official total; 23,372 tabulation difference in a note.
- [x] 2000: 281,421,906 total; 222,360,539 urban; 79.0 percent.
- [x] 2010: 308,745,538 total; 249,253,271 urban; 80.7 percent.
- [x] 2020: 331,449,281 total; 265,149,027 urban; 80.0 percent.
- [x] Urban shares 1790–1970 match HSUS A 57–72 when the thousands are converted to persons.
- [x] Regional counts 1950–2020 sum to the national totals; 1860 and 1900 do not, and the table note explains the regional-sum shares.
- [x] 1790 Midwest and West are `n.a.`, not zero.
- [x] 2020 Puerto Rico 3,285,874 and Island Areas 338,021 are in the note, not the national row.
- [x] City rows use legal city-proper boundaries; 1790 towns, 1854 Philadelphia, and 1898 Brooklyn notes are present.
- [x] City shares use the same national universe as the city row.
- [x] White, Black, and enslaved columns are not printed in Table 1; Table 6 owns race and legal status. The former cells are in `table-01-race-reference.csv`, reference only.

**Arithmetic to record**

| Check | Formula | Expected |
|---|---|---|
| 1790 urban share | 202,000 / 3,929,214 × 100 | 5.1 |
| 1820 urban share | 693,000 / 9,638,453 × 100 | 7.2 |
| 1860 urban share | 6,217,000 / 31,443,321 × 100 | 19.8 |
| 1900 urban share | 30,160,000 / 75,994,575 × 100 | 39.7 |
| 1920 urban share | 54,158,000 / 106,021,537 × 100 | 51.1 |
| 1950 urban share | 96,846,817 / 151,325,798 × 100 | 64.0 |
| 1970 urban share | 149,325,000 / 203,235,298 × 100 | 73.5 |
| 2000 urban share | 222,360,539 / 281,421,906 × 100 | 79.0 |
| 2010 urban share | 249,253,271 / 308,745,538 × 100 | 80.7 |
| 2020 urban share | 265,149,027 / 331,449,281 × 100 | 80.0 |
| 1970 difference | 203,235,298 − 203,211,926 | 23,372 |
| 1860 regional sum | 12,295 + 9,097 + 11,133 + 619 (thousands) | 33,144 |
| 1900 regional sum | 21,047 + 26,333 + 24,524 + 4,309 (thousands) | 76,213 |

*Table 1 run November 24, 2026. HSUS A 1–5, A 57–72, A 172–194, and Z 1–19, the 1960 Census retrospective tables, the 2000/2010/2020 Census pages, the Historical Population Change Data, Gibson Tables 2, 9, and 15, and the 2020 Decennial Census Historical Facts were opened. The 1860/1900 regional mismatch is recorded in EX-18 and the table note; the race/slavery columns were moved to Table 6 under EX-19.*

## 3. Table 2 — Presidential elections

*Drafted November 24, 2026. The 710 cells are verified against the American Presidency Project compilation; the HSUS/NARA/FEC row-level cross-check and the 1828–1900 state-coverage check remain for Stage 5. The table prints popular-vote shares only, not counts.*

- [x] 60 rows, one per election, 1789–2024.
- [x] No popular-vote total or share in 1824.
- [x] 1796, 1808, and 1820 early deviations are in the Notes column, not a separate column.
- [x] 1872: 286 Grant + 63 other = 349 counted; 352 cast; Greeley 0; Arkansas and Louisiana absent.
- [x] 1876: 185 Hayes + 184 Tilden = 369; 20 disputed votes; majority 185.
- [x] 2020: 306 Biden + 232 Trump = 538; objections noted.
- [x] 2024: 312 Trump + 226 Harris = 538; FEC popular vote and shares; turnout 64.3 (p).
- [x] Pre-1828 turnout is “partial” or `n.a.`, never a computed national rate.
- [ ] 1828–1900 legislative-selection states have no popular-vote zero; coverage in the Notes.
- [x] Faithless electors counted only as counted presidential deviations; abstentions separate; unpledged electors excluded.

**Arithmetic to record**

| Check | Formula | Expected |
|---|---|---|
| 2024 turnout | 156,766,239 / 243,803,423 × 100 | 64.30 |
| 2024 FEC vote check | 77,302,580 / 155,238,302 × 100 | 49.80 |
| 1872 counted | 286 + 63 | 349 |
| 1876 total | 185 + 184 | 369 |
| 2020 total | 306 + 232 | 538 |
| 2024 total | 312 + 226 | 538 |

## 4. Table 3 — Territory and treaties

- [x] BLM acres divided by 640 exactly: land + water = gross for 1803, 1819, 1846, 1848, 1853, 1867, and the Texas cession.
- [x] 1947 gross areas used for 1783, Texas, Hawaii, Puerto Rico, Guam, the Philippines, and the Virgin Islands; land and water `n.a.` where the 1947 table does not split them.
- [x] Canal Zone uses 1940 Census: 362 land + 191 water = 553.
- [x] Costs: 1803 $23,213,568; 1819 $6,674,057; 1845 $0; 1850 $15,496,448; 1846 $0; 1848 $16,295,149; 1853 $10,000,000; 1867 $7,200,000; 1898 Spain $20,000,000; 1903 $10,000,000 + $250,000 annuity; 1917 $25,000,000 gold.
- [x] 1763 row is an imperial baseline; area and cost `—`.
- [x] Hawaii is a joint resolution, not a treaty; sovereignty contested.
- [x] Philippines is a sub-entry, not a separate row; independent 1946.
- [x] Canal Zone is control, not sovereignty; abolished 1979; canal transferred 1999.
- [x] Do not sum the area column across rows; bases differ.

*Table 3 run November 24, 2026. BLM Table 1-1, 1947 Statistical Abstract Table 1, 1940 Canal Zone Census p. 4, and the 2010 State Area Measurements were opened and the printed cells checked. The 1845 Texas row note’s 1850 stock terms were verified against 9 Stat. 446–47 (GovInfo page 447); the BLM compiled cost is checked.*

**Arithmetic to record**

| Row | Land + water | Gross |
|---|---|---|
| 1803 | 817,885 + 10,102 | 827,987 |
| 1819 | 67,723 + 4,378 | 72,101 |
| 1846 | 282,257 + 4,284 | 286,541 |
| 1848 | 522,624 + 6,565 | 529,189 |
| 1853 | 29,628 + 42 | 29,670 |
| 1867 | 570,833 + 20,171 | 591,004 |
| Texas cession | 123,192 + 131 | 123,323 |
| Canal Zone | 362 + 191 | 553 |

## 5. Table 4 — Wars, mobilization, and cost

- [x] Every row: total deaths = battle + other, or the note explains the difference.
- [x] Service totals, deaths, and wounds match CRS RL32492 (July 29, 2020).
- [x] Costs match CRS RS22926, FY2011 base; cost definition in the row.
- [x] Civil War rows are roster counts; Barceló 698,000, Hacker 752,000, and conventional 618,222 in the note only.
- [x] Confederate row: service 600,000–1,500,000; deaths 133,821 (74,524 + 59,297); wounded `n.a.`; prison deaths 26,000–31,000 in the note.
- [x] Panel C: uniformed military only; DoD August 31, 2021 snapshot; OCO current dollars; constant-dollar cells `—`.
- [x] Panel A note carries the Philippine-American War and Boxer Rebellion; no fourteenth row.
- [x] Persian Gulf gross cost in cells; $4.7 billion net in the note.
- [x] Do not add DoD civilians or contractors to any cell.

*Table 4 run November 24, 2026. CRS RL32492 Table 1, CRS RS22926 Table 1, the August 31, 2021 DoD casualty status, Crawford Table 2, and Barceló et al. 2024 were opened and the cells checked. The 1902 Philippine report and Heitman remain OCR/secondary-locator items in the note.*

**Arithmetic to record**

| Row | Battle + other | Total |
|---|---|---|
| Mexican War | 1,733 + 11,550 | 13,283 |
| Civil War, Union | 140,414 + 224,097 | 364,511 |
| Civil War, Confederate | 74,524 + 59,297 | 133,821 |
| Spanish-American | 385 + 2,061 | 2,446 |
| World War I | 53,402 + 63,114 | 116,516 |
| World War II | 291,557 + 113,842 | 405,399 |
| Korea | 33,739 + 2,835 | 36,574 |
| Vietnam | 47,434 + 10,786 | 58,220 |
| Persian Gulf | 148 + 235 | 383 |
| Afghanistan | 1,910 + 415 | 2,325 |
| Iraq | 3,519 + 973 | 4,492 |

## 6. Table 5 — Immigration

- [x] Panel A decade totals match the 2022 Yearbook Table 2; the 2020–2024 row is a calculated partial.
- [x] 2020–2024 total 5,002,710; regional cells 5,002,750; difference 40 explained by rounding.
- [x] 2024 regional cells sum to 1,364,100 against 1,364,090; difference 10 explained.
- [x] 688,230 Unknown for 2020–2024, including 440,430 in FY 2024; 32.3 percent of FY 2024.
- [x] 2022 “America” row and the 2024 North America + South America splice are not added together.
- [x] Panel B 2024 uses region of birth; Mexico 202,600; Cuba and China in the note.
- [x] Panel C: 1921 formula and administrative allotments; 1924 164,667; 1929 153,714.
- [ ] Panel D: 2010 and 2024 ACS 1-year; the 2020 ACS 5-year row is reserved, not printed; no decennial labels.
- [x] Panel E: DHS residual, January 1, 2010/2015/2020/2022; subset of Panel D; do not add.
- [x] No post-2022 unauthorized estimate.

*Table 5 run November 24, 2026. The 2022 and 2024 DHS Yearbook tables, the 1921/1924/1929 instruments, Gibson and Jung, the 2010/2024 ACS B05002 tables, and the DHS unauthorized reports were opened and the cells checked. Panel D’s 2020 row is reserved because the 2016–2020 ACS 5-year estimate was not transcribed; 2010 and 2024 bracket the period.*

**Arithmetic to record**

| Check | Formula | Expected |
|---|---|---|
| 2020–2024 total | 707,360 + 740,000 + 1,018,350 + 1,172,910 + 1,364,090 | 5,002,710 |
| FY 2024 regional sum | 47,150 + 326,470 + 400,420 + 56,500 + 89,470 + 3,660 + 440,430 | 1,364,100 |
| FY 2024 Unknown share | 440,430 / 1,364,090 × 100 | 32.3 |
| 2020–2024 regional sum | see production file | 5,002,750 |

## 7. Table 6 — Slavery and coerced movement

- [x] 1790: 697,681 enslaved + 59,527 free Black = 757,208 Black; 17.8 percent of 3,929,214; 92.1 percent of Black.
- [x] 1860: 3,953,760 enslaved + 488,070 free Black = 4,441,830 Black; 12.6 percent of 31,443,321; 89.0 percent of Black.
- [x] Census years 1800–1850 match HSUS A 91–104 footnote 1, with the Black totals summed from the male and female columns.
- [x] Barbados 1643: 18,600 White, 6,400 enslaved (Collins, p. 305).
- [x] Barbados 1679/80: 38,782 enslaved; White `n.a.`; adjacent benchmarks 21,725 (1676) and 19,568 (1684) in the note (Dunn, as cited).
- [x] Jamaica 1673: 7,768 White, 9,504 enslaved; 800 privateers and Maroons excluded in the note (Southey, vol. 2, p. 104, read as an image).
- [x] Transatlantic: 12,521,354 embarked; 10,702,644 disembarked; the page describes the latter as about 10.7 million.
- [x] U.S. imports: 472,372 embarked, 388,744 disembarked in the live table; earlier 472,381/388,747 in the note; do not use 305,326.
- [x] Goldin 835,000 and Tadman 1,110,000 are alternatives, not a range or components.
- [x] Prices: nominal × 100 / Cc2; eight real values as listed.
- [x] Do not add the enslaved column to the Black column.

**Arithmetic to record**

| Check | Formula | Expected |
|---|---|---|
| 1790 Black total | 697,681 + 59,527 | 757,208 |
| 1860 Black total | 3,953,760 + 488,070 | 4,441,830 |
| 1790 enslaved share of total | 697,681 / 3,929,214 × 100 | 17.8 |
| 1790 enslaved share of Black | 697,681 / 757,208 × 100 | 92.1 |
| 1860 enslaved share of total | 3,953,760 / 31,443,321 × 100 | 12.6 |
| 1860 enslaved share of Black | 3,953,760 / 4,441,830 × 100 | 89.0 |
| 1800–1850 Black totals | sum male + female columns | 1,002,037; 1,377,808; 1,771,656; 2,328,642; 2,873,648; 3,638,808 |
| 1804 real price | 700 × 100 / 142 | 493 |
| 1861 real price | 1,440 × 100 / 106 | 1,358 |

*Table 6 run November 24, 2026. HSUS A 1–5 and A 91–104, Bb209–214, and Cc1–2 were opened; the 1860 Census pp. ix and 599 were read as page images; the live SlaveVoyages estimates table was read in a browser session; Pritchett note 2, Collins p. 305, the EHS pilot page, and Southey vol. 2 p. 104 were read. Barbados 38,782 and the Dunn 1972 adjacent benchmarks remain “as cited” because the print works were not consulted directly; the U.S. imports row uses the live 472,372/388,744 values, with the earlier 472,381/388,747 in the note.*

## 8. Table 7 — Economic and communications benchmarks

- [ ] Panel A: receipts, outlays, deficit, debt, and percentages match OMB Tables 1.1, 1.2, and 7.1; FY2024 is an actual; percentages `n.a.` before 1930.
- [ ] Deficit = receipts − outlays; debt is not deficit.
- [ ] Panel B: railroad miles (operated, ends 1970), steel (1887–1960), unemployment (Ba475 for 1900/1930/1940; BLS from 1950), CPI (CPI-U 1982–84 = 100 from 1930; E 135 in the note), GDP per capita (Maddison 2011 intl dollars 1830–1900; BEA chained 2017 dollars 1930–2024).
- [ ] Panel C: one WID vintage; top share pre-tax national income; Gini H-4 from 1967; union density from 1930; LFP BLS LNS11300000 from 1950; n.a. rules as printed.
- [ ] Panel D: daily newspapers and weekday circulation; 2000 Editor & Publisher; telephones in service ends 1970; household telephone 1960–2000; 97.6 percent in 2000.
- [ ] No Pew post-2014 print-and-digital series; no FCC line count as “telephones in service.”
- [ ] No averaging of Lebergott and Darby–Weir.

**Arithmetic to record**

| Check | Formula | Expected |
|---|---|---|
| 1900 unemployment | Ba475 | 5.00 |
| 1940 Darby–Weir | Ba475 | 9.5 |
| 1940 Lebergott (note) | D 85–86 | 14.6 |
| 2000 household telephone | 100 − 2.4 | 97.6 |

## 9. Table 8 — Land use, public works, and settlement

- [ ] Seven TVA rows; dates and capacities match the dam pages; capacity is modern summer net dependable; Watts Bar 196 and Chickamauga 142 (Facts & Figures values).
- [ ] CCC five June 30 rows: 279,722; 358,558; 321,243; 200,079; 42,315; peak 505,782 in August 1935 in the note; no camp-count series.
- [ ] Land use: national 1930/1935/1940 and Kansas/Oklahoma/Texas 1940; farms, land in farms, and cropland harvested are distinct; dates labeled.
- [ ] Dust Bowl: 120,859 to 97,606; change −23,253 (−19.2 percent).
- [ ] California: 5,677,251 to 6,907,387; +1,230,136 (21.7 percent); in-migrants 876,829; out-migrants 211,963; net +664,866; residual +565,270 not migration.
- [ ] 48-state 1940 universe; do not mix with 50-state series.
- [ ] No state CCC rows in Table 8.

**Arithmetic to record**

| Check | Formula | Expected |
|---|---|---|
| Dust Bowl change | 120,859 − 97,606 | 23,253 |
| Dust Bowl rate | 23,253 / 120,859 × 100 | 19.2 |
| California change | 6,907,387 − 5,677,251 | 1,230,136 |
| California net migration | 876,829 − 211,963 | 664,866 |
| California residual | 1,230,136 − 664,866 | 565,270 |

## 10. Cross-table checks

- [ ] 1790 total in Table 1 and Table 6 is 3,929,214.
- [ ] 1860 total in Table 1 and Table 6 is 31,443,321; enslaved 3,953,760.
- [ ] 1940 conterminous total in Table 1 and Table 8 is 131,669,275; 1930 is 122,775,046.
- [ ] 1970 official total and 203,211,926 tabulated base agree across Table 1 panels.
- [ ] 2000 and 2010 totals in Table 1 and Table 7 match.
- [ ] 2020 total in Table 1 and Table 5 is 331,449,281; Puerto Rico and the Island Areas are separate.
- [ ] Appendix B references in Chapters 12, 13, 16, 21, 22, 31, 36, 37, 41, 46, and 49 point to a table that supports the claim. Record any mismatch for Stage 6; do not edit the chapter here.
- [ ] No table prints a ninth display number or an unregistered panel.

## 11. Result log

Add one line per check run. A passing line names the table, the check, the date, and the person who ran it.

| Date | Table | Check | Result | Run by |
|---|---|---|---|---|
| 2026-11-24 | Table 1 | Totals, urban shares, regions, cities; 1860/1900 mismatch noted | Pass; 41 rows verified; race/slavery moved to Table 6 | Agent |
| 2026-11-24 | Table 2 | 60 rows, 710 cells; electoral-vote sums | Pass except the 2000 abstention (537 of 538); APP compilation verified; HSUS/NARA row-level check pending | Agent |
| 2026-11-24 | Table 4 | CRS service/casualties/costs; DoD Panel C; Crawford OCO; Civil War note | Pass; 130 cells (123 verified, 4 not applicable, 3 n.a.) | Agent |
| 2026-11-24 | Table 5 | DHS decade/regional matrix; 2024 cells; quotas; stock; unauthorized | Pass; 41 printed rows, 246 cells (244 verified, 2 n.a.); 2020 stock row reserved | Agent |
| 2026-11-24 | Table 3 | BLM area conversion; 1947 gross areas; 1940 Canal Zone; 2010 notes; costs; legal forms/dates; Texas stock terms | Pass; 113 cells (101 verified, 6 n.a., 6 not applicable) | Agent |
| — | — | Structural checks | Not run | — |
| — | — | Table 2 arithmetic | Not run | — |
| — | — | Table 4 arithmetic | Not run | — |
| — | — | Table 5 arithmetic | Not run | — |
| 2026-11-24 | Table 6 | Panels A–D; 24 printed rows and one reserve; 104 cells | Pass; 103 verified, 1 n.a.; Southey vol. 2 p. 104; live SlaveVoyages 472,372/388,744; Dunn and Tadman as cited; three-page proof | Agent |
| 2026-11-24 | Table 6 | Arithmetic: 1790/1860 shares; 1800–1850 Black totals; eight deflations | Pass | Agent |
| 2026-11-24 | Appendix B | `python3 tools/check_book.py --strict chapters/52-appendix-b.md` | Pass; 0 errors, 0 warnings, 154 notes, 20 tables | Agent |
| — | — | Table 7 arithmetic | Not run | — |
| — | — | Table 8 arithmetic | Not run | — |
| — | — | Cross-table checks | Not run | — |

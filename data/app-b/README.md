# Appendix B production files

**Status:** Step 1 complete; Step 3 and final assembly complete, November 24, 2026. Tables 1–8 are drafted, the production sections are removed, the table sections are renumbered 1–8, and the duplicate-note filter is wired into the build. The body proof measures 25 pages against the 20-page allowance; the combined note list is separate. `chapters/52-appendix-b.md` is `drafted`; it is not `checked`. The page-budget decision and Stage 5 remain.

## 1. What is here

| File | Purpose |
|---|---|
| [`contract.md`](contract.md) | Frozen Stage 4 scope, format decisions, verification standard, and access consequences |
| [`stage4-plan-and-handoff.md`](stage4-plan-and-handoff.md) | Original Stage 4 plan, current table status, and the Table 8 handoff |
| [`ledger.csv`](ledger.csv) | One record for every display row in the eight tables: 255 rows |
| `table-01.csv` … `table-08.csv` | Long-format cell records for each table; 594 benchmark cells seeded |
| `table-01-race-reference.csv` | 14 race/slavery cells from the former Table 1 design; reference only, not printed; Table 6 owns the series |
| [`exceptions.md`](exceptions.md) | Known discrepancies, access gaps, and decisions that must be resolved before a table is called drafted |
| [`checks.md`](checks.md) | Planned arithmetic and cross-table checks, with results recorded as they are run |

The ledger is complete. The cell files are deliberately partial: they contain the benchmark values stated in the Stage 3 outline, not the full matrix. Step 3 adds the remaining cells and replaces every `unverified` status with `verified` or a declared blocker.

## 2. Counts

| Table | Ledger rows | Printed rows | Drafted cells | Verified | n.a. | Other |
|---|---:|---:|---:|---:|---:|---:|
| **Table 1** | 41 | 41 | 178 | 166 | 12 | 0 |
| **Table 2** | 60 | 60 | 710 | 710 | 0 | 0 |
| **Table 3** | 13 | 13 | 113 | 101 | 6 | 6 not applicable |
| **Table 4** | 13 | 13 | 130 | 123 | 3 | 4 not applicable |
| **Table 5** | 42 | 41 | 246 | 244 | 2 | 1 reserve row |
| **Table 6** | 25 | 24 | 104 | 103 | 1 | 1 reserve row |
| **Table 7** | 38 | 38 | 191 | 147 | 44 | 0 |
| **Table 8** | 23 | 23 | 107 | 101 | 6 | 0 |
| **Total** | **255** | **254** | **1,779** | **1,695** | **74** | **10 not applicable; 2 reserve rows** |

Table 6's 25th ledger row is a reserve for the trade panel's one-row slack; it is not printed. The published row count is 254, inside the Stage 3 estimate of 254–260.

**Step 1 validation:** 255 ledger rows; 254 printed and one reserve; 1,280 seeded cells; no blank values; no duplicate `(row_id, column_id)` pairs; every seeded cell has a source key and locator; all 153 source keys resolve to definitions in the Stage 3 note list. The only ledger row without a source key is the Table 6 reserve, which is not printed.

**Step 2 pilot:** At the pilot, Table 3 had 113 cells, of which 100 were `verified`, 6 were `n_a`, 6 were `not_applicable`, and 1 was `unverified` (the Texas row note’s 1850 stock terms). The stock terms were later verified against 9 Stat. 446–47. The Table 3 draft and the Table 2 width proof are in `build/app-b-pilot.md` and `build/app-b-pilot.pdf`; the PDF is a 5-page Letter proof, with Table 3 on pages 1–3 including row notes and the Table 2 proof on pages 3–5. `build/` is gitignored, so the pilot is a review artifact, not a tracked manuscript file. Template decisions: eight-column Table 3 with letter-keyed row notes; an `.appendix-table` style at 8-point type, reduced padding, and row-level break avoidance, now added to `styles/pdf.css`; a ten-column packed Table 2 header; and Table 3’s ~2.5-page length accepted provisionally, to be reconciled at the full 20-page proof.

**Final assembly, November 24, 2026:** The appendix now has an unnumbered `## Note on the Tables` followed by eight numbered table sections. The Stage 3 production sections §1 “How Appendix B Works” and §10 “Cross-Table Rules and Production Record” are removed; the note “Used for” annotations were changed from the deleted subsection numbers to table and panel references. The body proof is 25 pages against the 20-page allowance; the combined note list adds 27 pages and is estimated separately, as the page metric requires. The duplicate-note filter `tools/dedupe-notes.lua` is wired into the EPUB, HTML, and print targets; it renders 3,355 note definitions once each and links repeats back to the first note. The full appendix proof is 52 pages, of which 25 are body and 27 are notes. The 25-page body is a five-page overrun awaiting a human decision on a revised allowance or the contract fallback cuts. Do not call the appendix `checked`.

**Step 3, Table 8:** Table 8 is drafted under §8 with 23 rows and 107 cells (101 `verified`, 6 `n_a`). Panel A prints seven selected TVA dams with river, state, construction and completion dates, purpose, and modern summer net dependable capacity; Wilson Dam, the three unprinted 1936-plan dams, the 1944 completion, and the TVA prose/Facts & Figures discrepancies are in the note. Panel B gives five June 30 CCC enrolled-strength values from *Statistical Abstract 1943*, Table 156; the camp-count benchmarks and the August 1935 peak are in the note, and no state CCC rows are printed. Panel C transcribes the 1940 Census of Agriculture national and Kansas/Oklahoma/Texas values, with inventory and harvest dates separated. Panel D uses Long and Siu (2018) for the 20-county population and the 1940 census and *Statistical Abstract 1946* for California; the 20-county totals are at p. 1007, and the California migration series is from Table 31, not the article. The table-plus-notes proof is three pages against the 1.75-page allowance, accepted provisionally; the table-only portion is about two pages.

**Step 3, Table 7:** Table 7 is drafted under §8 with 38 rows and 191 cells (147 `verified`, 44 `n_a`). Panel A combines HSUS Ea584–587 / Y 335–338 for 1789–1930 with OMB FY 2027 Tables 1.1, 1.2, and 7.1 for 1940–2024; the first row is the combined 1789–1791 account. Panel B uses HSUS Q 321–328 (1830 and 1860 road operated; 1900–1950 road owned), P 302 steel, Ba475 and BLS annual unemployment, CPI-U, Maddison 2023, and BEA NIPA Table 7.1. Panel C uses the WID 2026 public API (series `sptinc_p99p100_992_j`), Census H-4 Gini, HSUS D 951 union density, and BLS LNU01300000 participation. Panel D uses HSUS R 244–257 and R 224–231 newspapers, Editor & Publisher 2000, and HSUS R 1–16 / Census telephone series. The proof is three pages against the two-page allowance, accepted provisionally; WID access is resolved.

**Step 3, Table 6:** Table 6 is drafted under §7 with 24 printed rows and one reserve, 104 cells (103 `verified`, 1 `n_a`). Panel A is transcribed from Collins, Dunn, and Southey; Southey’s 1673 return was read at vol. 2, p. 104. Panel B combines HSUS A 1–5 and A 91–104 for total, Black, and enslaved counts; the 1800–1850 Black totals are summed from the male and female columns. Panel C uses the live SlaveVoyages estimates (12,521,354 embarked; 10,702,644 disembarked; 472,372 embarked and 388,744 disembarked for Mainland North America), with the earlier 472,381/388,747 figures in the note, and Pritchett’s Goldin and Tadman estimates. Panel D transcribes the Engerman Bb210 series and the Cc2 index. The proof is three pages against the two-page allowance, accepted provisionally.

**Step 3, Table 5:** Table 5 is drafted under §6 with 41 printed rows and one reserve (the 2020 foreign-born stock row), 246 cells (244 `verified`, 2 `n_a`). Panel A is transcribed from the 2022 and 2024 DHS Yearbook tables; Panel C prints selected quotas only for 1929; Panel D uses the 1850–1990 census stock and the 2010/2024 ACS 1-year estimates. The proof is three pages against the 2.5-page allowance, accepted provisionally.

**Step 3, Table 4:** Table 4 is drafted under §5 with 13 rows and 130 cells (123 `verified`, 4 `not_applicable`, 3 `n_a`). CRS RL32492, CRS RS22926, the August 31, 2021 DoD casualty status, Crawford Table 2, and Barceló et al. 2024 were checked. The table is three pages against the two-page allowance; the length is accepted provisionally. The 1902 Philippine report and Heitman note remain OCR/secondary-locator items.

**Step 3, Table 3:** Table 3 is drafted under §4 with 13 rows and 113 cells (101 `verified`, 6 `n_a`, 6 `not_applicable`). The Texas 1850 stock terms are verified against 9 Stat. 446–47 (GovInfo page 447). The table is eight columns with letter-keyed row notes; the proof is about 2.5 pages, accepted provisionally.

**Step 3, Table 2:** Table 2 is drafted under §3 with 60 rows and 710 cells. The cells are verified against the American Presidency Project compilation; HSUS Y 79–83, NARA, and FEC are the official cross-checks, and the row-level check remains for Stage 5. Popular-vote shares are printed without counts. The table is five pages against the four-page allowance; the length is accepted provisionally and will be reconciled at the full 20-page proof.

**Step 3, Table 1:** Table 1 is drafted in the appendix under its existing §2 heading. It has 178 cells: 166 `verified` and 12 `n_a`; all 41 rows are `verified`. Three design decisions are recorded: the White, Black, and enslaved columns are not printed in Table 1, because Table 6 owns race and legal status; 14 reference cells for those series are in `table-01-race-reference.csv`. Urban and regional counts are printed in thousands; shares are calculated from the underlying counts. The 1860 and 1900 regional counts are printed with a note and shares against the regional sum, because the HSUS retrospective regional series does not sum to the national census totals for those years. The Table 1 proof is three pages including notes, against the 2.5-page allowance. The appendix remains `researched` until Tables 2–8 are drafted.

## 3. Ledger schema

`ledger.csv` has one row per display row.

| Field | Meaning |
|---|---|
| `table_id` | `app-b-table-01` … `app-b-table-08` |
| `display` | `App. B, Table 1` … `App. B, Table 8` |
| `title` | Display title |
| `panel` | Panel letter, `A`–`E` |
| `row_id` | Stable row key, `t01-a-01` … `t08-d-05` |
| `row_label` | Printed row label, e.g. `1950`, `Northeast`, `2020 rank 1`, `June 30, 1935` |
| `period` | Observation year or period used in the table |
| `universe` | Geographic and population universe for the row |
| `source_keys` | Semicolon-separated note keys that support the row; the first is primary |
| `status` | `not_started`, `unverified`, `reserve` at Step 1; later `verified` |
| `blocker` | Named access or editorial blocker, if any |
| `note` | Row-specific caveat that must survive into the table note |

## 4. Cell schema

Each `table-0N.csv` is long format: one row per cell.

| Field | Meaning |
|---|---|
| `table_id`, `panel`, `row_id`, `row_label` | Link to the ledger row |
| `column_id` | Stable column key, e.g. `total`, `urban_share`, `winner_ev`, `cost_constant` |
| `column_label` | Printed column label |
| `value` | Source-stated value used for checking; may be a count, a range, a percentage, or a unit-bearing string such as `$101 million`. No blanks. |
| `display_value` | Value as it will print; use `n.a.` and `—` only where the convention applies |
| `unit` | `persons`, `percent`, `square miles`, `current dollars`, `constant dollars`, `acres`, etc. |
| `observation_year` | Observation year or period for the cell |
| `universe` | Geographic or population universe |
| `source_key` | Note key for the exact locator; may name more than one key |
| `locator` | Exact page, table, series, or document locator |
| `transformation` | `none`, `calculated`, `deflate`, `acres/640`, `sum`, etc. |
| `status` | Cell status; see §5 |
| `note` | Cell-specific caveat |

No cell may have an empty `value`. Use `n.a.` for not available and `—` for not applicable. A blank cell is a production error.

## 5. Status vocabulary

| Status | Meaning |
|---|---|
| `not_started` | Ledger row exists; no cell seeded yet |
| `unverified` | Benchmark seeded from the outline; not checked against the locator |
| `verified` | Checked against the exact locator in `locator` |
| `n_a` | Explicitly not available in the source |
| `not_applicable` | Explicitly not applicable; prints as `—` |
| `pending_image` | Page-image PDF not yet read or confirmed |
| `pending_paywall` | Subscription or registration barrier |
| `pending_print` | Print or archival item not consulted |
| `reserve` | Ledger row held for the trade panel's slack; not printed |

A `verified` cell with a secondary locator must say `as cited in …` in the source key or note. It verifies what the secondary work reports, not the unread original.

## 6. Step 3 workflow

1. Pick one table. Open its ledger rows and cell file.
2. Add every missing cell for every column and row. Do not add a column or row outside the contract.
3. Open the cited source and check the printed cell. Record the exact locator.
4. Set the cell to `verified`, `n_a`, or `not_applicable`. If access fails, set the blocker status and record it in `exceptions.md`.
5. When every cell in a row is resolved, set the ledger row to `verified`.
6. Draft the manuscript table from the CSV. Do not retype values by hand.
7. Run the checks in `checks.md` and record the result.

## 7. Source keys

The `source_key` values are the 153 note keys defined in the Stage 3 outline. They are stable and must not be renamed. A cell may cite more than one key; the first is the primary source. The manuscript table's source line and notes will use these keys, so a cell without a key is a blocker, not a formatting detail.

## 8. Conventions

- Percentages: one decimal unless the source reports more precision. A change in percentage points is not a percent change.
- Money: nominal dollars of the stated year; constant dollars only with the named index and base year.
- Dates: census date, calendar year, fiscal year, or observation year, as the source labels it.
- Geography: present-day U.S. boundaries unless the row says otherwise; historical rows give the boundaries in force.
- Race and status: keep the historical categories and explain them. Do not use “Black” and “enslaved” interchangeably.
- Rounding: follow the source. Do not force a column to add when the components are independently rounded.
- `(p)`: provisional or estimated value; define the flag in the table note.
- Cross-references: `App. B, Table 1`; `Ch. 12, §2.2`; no space after `§`.

## 9. Open items

See [`exceptions.md`](exceptions.md) for the full list. The main ones:

- **Table 7, Panel C:** WID access is resolved through the public API; the 2026 release gives the top-share column. WID remains a model vintage, so record the release and do not splice a different vintage.
- **Table 2, Panel B:** the 1828–1900 state-selection check depends on the American Presidency Project because CQ Press was not supplied.
- **Table 6, Panel A and C:** Southey’s 1673 page is now read at vol. 2, p. 104; Dunn 1969/1972 and Tadman remain second-hand, and the affected cells say “as cited in …” in the notes.
- **Table 1 and Table 6:** page-image cells (1950, 1860) still need confirmation from the image PDFs. The Table 8 1940 Agriculture and Population pages were read as images on November 24, 2026.
- **Map 26:** the 48-state CCC counts remain a Map 26 task, not a Table 8 column; collate them against Fechner’s *First Report* and NARA RG 35, Entry 3.
- **Page budget:** the body proof measures 25 pages against the 20-page allowance; the five-page overrun awaits a human decision on a revised allowance or the contract fallback cuts. The combined note list is 27 pages and is not counted against the text-page goal.
- **Stage 5:** evidence, quotation, cross-reference, visual, and rendering checks remain; the appendix is `drafted`, not `checked`. The duplicate-note rendering is fixed (EX-27 resolved).

## 10. Do not

- Do not edit `chapters/52-appendix-b.md` from these files automatically.
- Do not add a ninth table, a new panel, or a new display number.
- Do not change the universe, a row cap, or a closed series decision without changing the contract, the caption, the table notes, and the relevant resolved-check section together.
- Do not mark a table `drafted` while a printed cell is `unverified`, `pending_image`, `pending_paywall`, or `pending_print`.
- Do not treat a seeded benchmark as checked because it is in the CSV.

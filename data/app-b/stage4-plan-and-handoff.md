# Appendix B — Stage 4 plan and handoff

**Status:** Tables 1–7 drafted and committed; Table 8 is next. Appendix B remains `researched` until Table 8 is drafted. Last updated November 24, 2026.

**Purpose of this file:** preserve the original Stage 4 plan, the current state, and the working method so a fresh session can continue without the earlier chat context.

## 1. Current state

**HEAD:** the latest commit on `main`; the Table 7 commit is `afbd2a4` (“Draft Appendix B Table 7”).

| Commit | Work |
|---|---|
| `3756034` | Table 1 and the Step 0–3 production records |
| `d5a5a82` | Table 2 |
| `0947ff5` | Table 3 |
| `71f6052` | Table 4 |
| `56b8755` | Table 5 |
| `b8af27e` | Table 6 |
| `afbd2a4` | Table 7 |

| Display | Appendix section | Rows | Cells | Proof | Notes |
|---|---|---:|---:|---:|---|
| **Table 1** | §2 | 41 | 178 (166 verified, 12 n.a.) | 3 pp vs 2.5 | Race/slavery moved to Table 6; regional counts in thousands; 1860/1900 regional-sum note |
| **Table 2** | §3 | 60 | 710, all verified against the APP compilation | 5 pp vs 4 | Shares only, no counts; HSUS/NARA row-level cross-check remains for Stage 5 |
| **Table 3** | §4 | 13 | 113 (101 verified, 6 n.a., 6 not applicable) | 3 pp vs 2.5 | Texas 1850 stock terms verified against 9 Stat. 446–47 |
| **Table 4** | §5 | 13 | 130 (123 verified, 4 not applicable, 3 n.a.) | 3 pp vs 2 | CRS, DoD, Crawford verified |
| **Table 5** | §6 | 41 printed + 1 reserve | 246 (244 verified, 2 n.a.) | 3 pp vs 2.5 | 2020 foreign-born stock row reserved; ACS 5-year estimate not transcribed |
| **Table 6** | §7 | 24 printed + 1 reserve | 104 (103 verified, 1 n.a.) | 3 pp vs 2 | Southey vol. 2, p. 104; live SlaveVoyages U.S. imports 472,372/388,744; Dunn and Tadman as cited |
| **Table 7** | §8 | 38 | 191 (147 verified, 44 n.a.) | 3 pp vs 2 | WID 2026 API; HSUS/OMB/BLS/BEA/Census; 1789–1791 first row; debt and railroad definition breaks |

- The appendix is 16,566 words, 154 notes, 24 pipe tables. `python3 tools/check_book.py --strict chapters/52-appendix-b.md` passes with 0 errors and 0 warnings.
- The 20-page allowance is still the target. Tables 1–7 are all slightly over their individual allowances; the overruns were accepted provisionally and must be reconciled at the full 20-page proof.
- The table sections still use the Stage 3 numbering: §2 = Table 1, §3 = Table 2, §4 = Table 3, §5 = Table 4, §6 = Table 5, §7 = Table 6, §8 = Table 7, §9 = Table 8. §1 is “How Appendix B Works” and §10 is “Cross-Table Rules and Production Record.” The final pass will drop §1 and §10, add `## Note on the Tables`, and renumber Tables 1–8 as §1–§8.
- **Build blocker, EX-27:** Pandoc renders one note per reference, so a key used three times appears three times. The appendix has 154 definitions but hundreds of rendered references and an 83-page proof. Add a deduplication filter at Stage 7 before trusting any page measurement; do not delete repeated references to make the count fall.
- **Layout note:** in the full appendix proof, Table 7 Panel A splits after the 2024 row because the table starts mid-page. The table-only proof is three pages; the final layout needs a keep-together rule or a page break before large panels.

## 2. The original Stage 4 plan

### Step 0 — Freeze the drafting contract

- **Agent:** extract the eight-table contract from §§1–10; flag the open notes (`app-b-state-selection-check`, `app-b-map26-ccc-check`); list the format decisions and source-access consequences.
- **Human:** approve panel layout, heading scheme, the no-unverified-cells rule, the fallback cut order, the file location, and the source-access plan.
- **Gate:** written contract in the review log.

### Step 1 — Production files and row ledger

- **Agent:** create `data/app-b/` with the contract, ledger, eight cell CSVs, `README.md`, `exceptions.md`, and `checks.md`; seed the Stage 3 benchmarks as `unverified`.
- **Human:** approve the directory and CSV format.
- **Gate:** roughly 255 row records and every row has a source target.

### Step 2 — Pilot the format

- **Agent:** fully verify and draft Table 3 in a scratch copy; produce a 10-row Table 2 width proof.
- **Human:** review legibility, panel labels, captions, notes, and the Table 2 header.
- **Gate:** template approved.

### Step 3 — Draft the eight tables in display order

- **Agent, for each table:** verify or transcribe every cell; cross-foot; draft the table block; run the checker; update the ledger.
- **Human, in four review batches:** confirm the cells that cannot be machine-read; approve any value that changes a printed figure; approve any scope change.
- **Gate per table:** all cells resolved; table cross-foots; caption, definitions, source line, and notes present; checker clean.

### Step 4 — Reconcile across tables and against the chapters

- **Agent:** check the identities that tie the appendix together (1790, 1860, 1940, 1970, 2000, 2010, 2020; war costs; immigration; slavery; prices; areas); list every chapter reference to an Appendix B table and whether the printed table supports it.
- **Human:** decide whether to fix chapters now or log them for Stage 6. Recommendation: log only.
- **Gate:** no unresolved contradiction; an integration list exists.

### Step 5 — Convert the notes into the table note list

- **Agent:** map each note to a surviving reference; delete planning-only notes; add new notes; reorder by first reference; preserve full citation, locator, “Used for,” and limitations; ensure no note is unused.
- **Human:** spot-check 12–15 notes, especially paywalled/print sources.
- **Gate:** every note referenced, every reference defined, no `ibid.`, no nested references.

### Step 6 — Structural and arithmetic QA

- **Agent:** run the strict checker; run the checker tests; run the arithmetic and cross-table checks; record body words.
- **Human:** review the report and sign off residual warnings/blockers.
- **Gate:** zero errors/warnings, or every one declared.

### Step 7 — Typeset proof and page-budget decision

- **Agent:** build a PDF or table-only proof; measure pages per table, column widths, header repetition, overflow, and note length.
- **Human:** inspect at 8-point type; decide the fallback cuts if needed.
- **Gate:** tables fit 20 pages or approved cuts are applied; measured pages recorded.

### Step 8 — README and register; Stage 4 exit

- **Agent:** update the Appendix B status row and Draft status paragraph; update the eight register rows with final captions, source lines, rights, and status; reconcile page arithmetic; do not mark `checked`.
- **Human:** approve `researched` → `drafted`; schedule Stage 5.
- **Gate:** Stage 4 exit check in `AGENTS.md`.

## 3. Decisions and deviations already recorded

Read these before continuing:

- `contract.md` — panel layout (one pipe table per panel), temporary heading scheme, verification standard, fallback order, access consequences.
- `README.md` — counts, status vocabulary, Step 3 workflow.
- `exceptions.md` — all open/resolved items, especially:
  - **EX-04/EX-05:** Tadman is cited through Pritchett; Dunn 1969/1972 remain “as cited”; Southey’s 1673 return was read at vol. 2, p. 104.
  - **EX-17/EX-20:** Texas 1850 stock terms verified; Z 1–19 enslaved values corrected.
  - **EX-18:** Table 1’s 1860/1900 regional counts do not sum to national totals.
  - **EX-19:** Table 1 race/slavery columns dropped; Table 6 owns that series.
  - **EX-21:** Table 2 values verified against APP; HSUS/NARA/FEC row-level cross-check remains for Stage 5.
  - **EX-22/EX-23/EX-24/EX-26/EX-29:** Table 2, 4, 5, 6, and 7 page overruns accepted provisionally.
  - **EX-25:** SlaveVoyages Mainland North America totals changed between releases.
  - **EX-27:** the appendix proof duplicates notes on repeated references; fix the build before the page proof.
  - **EX-28:** Table 7 design corrections: 1789–1791 first row; public debt through 1930 and gross debt from 1940; road owned for 1900–1950; BLS annual series LNU04000000/LNU01300000; union-density denominator break; 1850 daily-newspaper row n.a.
- `checks.md` — per-table checks and result log.

### Key conventions learned

1. **Captions go after the table, inside the `.appendix-table` fenced div.**
   ```markdown
   ::: {.appendix-table}
   | ... |
   **Caption.** App. B, Table N, Panel A. ...
   :::
   ```
   The checker looks for `**Caption.**` within five lines after the table; a caption before the table is reported as uncaptioned.
2. **Use one pipe table per panel.** Do not use merged cells. Bold the leading cell of every body row.
3. **Use the `.appendix-table` CSS** in `styles/pdf.css` (8-point type, reduced padding, repeated header, row-level break avoidance). Without it, wide tables run six or more pages.
4. **Keep the Stage 3 section numbers for now.** The final renumbering to §1–§8 happens after Table 8. Do not renumber mid-stream; the checker expects sequential section numbers.
5. **Mark cells `verified` only against the exact locator.** For a secondary compilation, say “as cited in …” in the source line/note. Do not treat the Stage 3 benchmark as checked.
6. **Update the ledger and CSV together.** After a table is drafted, set the row statuses in `ledger.csv` and the cell statuses in `table-0N.csv`; update the counts in `README.md`.
7. **Normalize CSV line endings before committing:** `sed -i 's/\r$//' data/app-b/*.csv`.
8. **Commit after each table.** Use `git add README.md chapters/52-appendix-b.md data/app-b && git commit -m "Draft Appendix B Table N"`.
9. **Avoid broad year-based edits across panels.** A regex that matched `| **1860** |` once added a South Carolina note to Table 1’s rows. Always scope edits by panel/table.
10. **Watch for Vim swap files** in `chapters/`; do not delete them. The earlier session was closed cleanly.

## 4. Table 8 handoff

### Scope and rows

- **Table 8. Land Use, Public Works, and Settlement, 1930–1944.**
- **23 rows, 59 seeded cells (53 `unverified`, 6 `n.a.`).** This is a smaller table than Table 7, but most cells still need row-level verification.
- **Panel A (7):** TVA dams: Norris, Wheeler, Pickwick, Guntersville, Chickamauga, Watts Bar, Kentucky. Columns: dam; river; state; construction start; completion; purpose; capacity.
- **Panel B (5):** CCC enrollment, June 30, 1933, 1935, 1936, 1940, 1942. Columns: date; enrolled strength; source definition; note. No camp-count column, no state rows.
- **Panel C (6):** national 1930, 1935, 1940; Kansas, Oklahoma, Texas 1940. Columns: year; farms; land in farms; cropland harvested; unit; source.
- **Panel D (5):** Dust Bowl 20-county population 1930/1940/change; California in-migrants, out-migrants, net interstate migration. Columns: area; 1930; 1940; change; note.
- **Page allowance:** 1.75 pages; likely 2.5 at 8-point. Accept provisionally if needed and record an exception.

### Panel design (from the Stage 3 §9.2 outline)

- **A:** selected TVA dams, not the whole system. The note must cover Wilson Dam (acquired in 1933; built 1918–1925), the other three dams in the 1936 nine-dam plan (Hiwassee, Fort Loudoun, Fontana), the fact that Wheeler and Pickwick were already under construction when the plan was approved, and the statement that all nine plan dams were structurally complete by 1944. Capacity is modern summer net dependable capacity, not 1940s nameplate. Use the TVA Facts & Figures values where the page prose disagrees: Watts Bar 196, Chickamauga 142.
- **B:** five June 30 enrolled-strength values from *Statistical Abstract 1943*, Table 156: 279,722 (1933); 358,558 (1935); 321,243 (1936); 200,079 (1940); 42,315 (1942). The official monthly peak is 505,782 in August 1935, not 1936. Put the camp-count benchmarks (1,330 on June 29, 1933; about 2,650 established by 1935; 6,036 recorded sites) and the cumulative enrollment (about three million) in the note. Do not print a camp-count series or state rows.
- **C:** direct 1940 Census of Agriculture, Vol. III, Chapter I, Tables 4, 9, and 10. National 1940: 6,096,799 farms; 1,060,852,374 acres in farms; 321,242,430 acres harvested in 1939. 1935: 6,812,350; 1,054,515,111; 295,624,176 harvested in 1934. 1930: 6,288,648; 986,771,016; 359,242,091 harvested in 1929. Kansas 1940: 156,327 farms; 48,173,635 acres; 17,816,498 harvested in 1939. Oklahoma: 179,687; 34,803,317; 12,766,219. Texas: 418,002; 157,683,372; 26,044,008. Label the inventory dates (April 1, 1940; January 1, 1935; April 1, 1930) separately from the harvest years (1939, 1934, 1929).
- **D:** Long and Siu (2018), pp. 1002, 1007, and 1012. The 20 Soil Conservation Service counties in Colorado, Kansas, Oklahoma, and Texas fell from 120,859 in 1930 to 97,606 in 1940, a change of −23,253, or −19.2 percent. California 5,677,251 to 6,907,387, +1,230,136, or +21.7 percent. 1935–1940 California in-migrants 876,829, out-migrants 211,963, net interstate migration +664,866. The universe is persons age 5 and over in 1940; the figures are gross interstate moves and net interstate migration, not total population change. The residual +565,270 is not migration.

### Key values and checks

- **TVA dates:** Norris 1933–1936; Wheeler 1933–1936; Pickwick 1934–1938; Guntersville 1935–1939; Chickamauga 1936–1940; Watts Bar 1939–January 1942; Kentucky 1938–1944. Hiwassee 1936–1940; Fort Loudoun 1940–1943; Fontana 1942–1944. Wilson Dam 1918–1925 (lakeinfo says 1924), acquired 1933.
- **TVA capacity:** use Facts & Figures modern summer net dependable values; the page prose sometimes disagrees. Record both where they differ.
- **CCC:** 279,722; 358,558; 321,243; 200,079; 42,315. Peak 505,782 in August 1935. The NPS “1936” height is a fiscal-year label, not an August 1936 count.
- **Land use:** farms, land in farms, and cropland harvested are different measures. Do not add or reconcile them as if one were a subset that must sum.
- **Dust Bowl:** 120,859 − 97,606 = 23,253; 23,253 / 120,859 × 100 = 19.2. California 6,907,387 − 5,677,251 = 1,230,136; 876,829 − 211,963 = 664,866; 1,230,136 − 664,866 = 565,270. The residual is not net migration.
- **Universe:** 48-state continental total for 1940 and 1930; do not mix with 50-state retrospective totals.

### Sources and access

- **TVA:** “Building a Better Life for the Tennessee Valley,” the individual dam pages, and the lakeinfo page for Wilson. The TVA pages are institutional accounts; they do not measure distribution of benefits or environmental costs.
- ***Statistical Abstract 1943*:** Table 156, p. 157, for the five June 30 CCC values. NPS, NARA, PBS, and CCC Legacy supply camp-count context, not cells.
- **1940 Census of Agriculture:** direct Census Bureau PDF of Vol. III, Chapter I, Tables 4, 9, and 10 (pp. 34, 38, 40). Do not use the blocked NASS links.
- **1940 Census of Population:** Vol. 1, *Number of Inhabitants*, United States Summary, Table 3, pp. 14–15, for the continental total and California.
- ***Statistical Abstract 1946*:** Table 31, p. 32, reproducing *Internal Migration, 1935 to 1940: Color and Sex of Migrants*, for the California migration figures.
- **Long and Siu 2018:** *Journal of Economic History* 78, no. 4, pp. 1002, 1007, and 1012. The 2018 article confirms the working paper’s county totals and percentages.
- **Map 26:** the 48-state CCC counts stay in the map production CSV and must be collated against Fechner’s *First Report* and NARA RG 35, Entry 3. They are not Table 8 cells.

### Procedure

1. Read §9 in `chapters/52-appendix-b.md` and `data/app-b/table-08.csv`; note the 59 seeded cells and the 23 rows.
2. Verify or transcribe every cell panel by panel. Use the production CSV; do not rebuild from memory. Mark `verified`, `n_a`, or `not_applicable`.
3. Build `build/app-b-table-08.md` with four panels (A–D) and captions after each table inside `.appendix-table` divs. Render with:
   ```bash
   pandoc build/app-b-table-08.md --standalone --css=../styles/pdf.css \
     --metadata title='Table 8 proof' -o build/app-b-table-08.html
   weasyprint build/app-b-table-08.html build/app-b-table-08.pdf
   ```
4. Replace §9 in `chapters/52-appendix-b.md` with the draft. Keep the `## 9.` heading until the final renumbering. Do not leave unused note definitions: the checker reports `note-unused-definition`.
5. Run `python3 tools/check_book.py --strict chapters/52-appendix-b.md`. Expect 0 errors and 0 warnings; 154 notes remain unless a new note is needed.
6. Update `ledger.csv` (23 rows verified), `table-08.csv`, `README.md`, `contract.md`, `checks.md`, and `exceptions.md`.
7. Commit: `git add README.md chapters/52-appendix-b.md data/app-b && git commit -m "Draft Appendix B Table 8"`.

### Specific Table 8 traps

- **Do not add a camp-count column or state CCC rows.** The 48-state counts are a Map 26 task. The PBS August 1933 map is a secondary reproduction, and its round numbers look like authorized company allotments at about 200 men per camp, not enrolled strength.
- **Do not treat the NPS “1936” height as an August 1936 count.** The official monthly peak is August 1935, 505,782.
- **Do not present modern TVA summer net dependable capacity as 1940s installed capacity.** Label it modern and note the page-prose/Facts & Figures discrepancies.
- **Do not count Wilson Dam among the nine 1936-plan dams.** It is an acquired dam; the nine are Wheeler, Pickwick, Guntersville, Chickamauga, Hiwassee, Watts Bar, Fort Loudoun, Fontana, and Kentucky.
- **Do not treat 1940 farms and land in farms as the same observation date as 1939 cropland harvested.** The inventory dates and harvest years differ.
- **Do not compare the 1940 48-state total with a 50-state retrospective total.** Use 131,669,275 for 1940 and 122,775,046 for 1930.
- **Do not attribute all of California’s growth to the Dust Bowl.** Net interstate migration was 664,866 of a 1,230,136 increase; the residual 565,270 is natural increase, international migration, and coverage differences.
- **Do not use the PBS state counts as an official series.** They are for Map 26 verification only.

## 5. Remaining after Table 8

- **Final assembly:** drop §1 “How Appendix B Works” and §10 “Cross-Table Rules and Production Record,” add a reader-facing `## Note on the Tables`, renumber Tables 1–8 as §1–§8, reconcile the 20-page budget, update the README status to `drafted`, and run the full proof. Do not mark `checked`.
- **Build fix before the page proof:** EX-27, the duplicate-note rendering. Add a filter so each named key renders once with repeated references returning to the same note. Measure the appendix only after the fix.
- **Layout:** keep large panels together; the full proof currently splits Table 7 Panel A after the 2024 row.
- **Cross-table reconciliation:** check 1790, 1860, 1940, 1970, 2000, 2010, and 2020 identities across Tables 1–8; log chapter references for Stage 6.

## 6. Useful commands

```bash
# Structural check
python3 tools/check_book.py --strict chapters/52-appendix-b.md

# Section proof
pandoc build/app-b-table-08.md --standalone --css=../styles/pdf.css \
  --metadata title='Table 8 proof' -o build/app-b-table-08.html
weasyprint build/app-b-table-08.html build/app-b-table-08.pdf
pdfinfo build/app-b-table-08.pdf | grep Pages

# Normalize CSV line endings before commit
sed -i 's/\r$//' data/app-b/*.csv

# Commit
git add README.md chapters/52-appendix-b.md data/app-b
git commit -m "Draft Appendix B Table 8"
```

## 7. File map

| Path | Role |
|---|---|
| `chapters/52-appendix-b.md` | The draft; Tables 1–7 drafted under §§2–8, Table 8 still a Stage 3 specification under §9 |
| `data/app-b/contract.md` | Frozen decisions and verification standard |
| `data/app-b/README.md` | Counts, schemas, status, Step 3 workflow |
| `data/app-b/ledger.csv` | 255 display rows; current statuses and notes |
| `data/app-b/table-01.csv` … `08.csv` | Cell-level production records |
| `data/app-b/table-01-race-reference.csv` | 14 race/slavery cells moved out of Table 1; reference only |
| `data/app-b/checks.md` | Per-table checks and result log |
| `data/app-b/exceptions.md` | All open/resolved exceptions, including EX-25/26/27/28/29 |
| `styles/pdf.css` | `.appendix-table` compact table style |
| `README.md` | Book plan, Appendix B status row, page budget |
| `build/app-b-table-0N.md` / `.pdf` | Scratch proofs; `build/` is gitignored |

## 8. Immediate next action

Start with Table 8: open §9 and `table-08.csv`, verify the seven TVA rows, the five CCC values, the six land-use rows, and the five Dust Bowl rows, build the four-panel proof, splice it into §9, run the checker, update the records, and commit. Then the final assembly: drop the production sections, renumber Tables 1–8, fix the duplicate-note rendering, and measure the 20-page proof.

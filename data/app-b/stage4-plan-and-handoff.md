# Appendix B — Stage 4 plan and handoff

**Status:** Tables 1–6 drafted and committed; Table 7 is next. Appendix B remains `researched` until Tables 7–8 are drafted. Last updated November 24, 2026.

**Purpose of this file:** preserve the original Stage 4 plan, the current state, and the working method so a fresh session can continue without the earlier chat context.

## 1. Current state

**HEAD:** the latest commit on `main`; the Table 6 commit is `b8af27e` (“Draft Appendix B Table 6”).

| Commit | Work |
|---|---|
| `3756034` | Table 1 and the Step 0–3 production records |
| `d5a5a82` | Table 2 |
| `0947ff5` | Table 3 |
| `71f6052` | Table 4 |
| `56b8755` | Table 5 |
| `b8af27e` | Table 6 |

| Display | Appendix section | Rows | Cells | Proof | Notes |
|---|---|---:|---:|---:|---|
| **Table 1** | §2 | 41 | 178 (166 verified, 12 n.a.) | 3 pp vs 2.5 | Race/slavery moved to Table 6; regional counts in thousands; 1860/1900 regional-sum note |
| **Table 2** | §3 | 60 | 710, all verified against the APP compilation | 5 pp vs 4 | Shares only, no counts; HSUS/NARA row-level cross-check remains for Stage 5 |
| **Table 3** | §4 | 13 | 113 (101 verified, 6 n.a., 6 not applicable) | 3 pp vs 2.5 | Texas 1850 stock terms verified against 9 Stat. 446–47 |
| **Table 4** | §5 | 13 | 130 (123 verified, 4 not applicable, 3 n.a.) | 3 pp vs 2 | CRS, DoD, Crawford verified |
| **Table 5** | §6 | 41 printed + 1 reserve | 246 (244 verified, 2 n.a.) | 3 pp vs 2.5 | 2020 foreign-born stock row reserved; ACS 5-year estimate not transcribed |
| **Table 6** | §7 | 24 printed + 1 reserve | 104 (103 verified, 1 n.a.) | 3 pp vs 2 | Southey vol. 2, p. 104; live SlaveVoyages U.S. imports 472,372/388,744; Dunn and Tadman as cited |

- The appendix is 18,466 words, 154 notes, 20 pipe tables. `python3 tools/check_book.py --strict chapters/52-appendix-b.md` passes with 0 errors and 0 warnings.
- The 20-page allowance is still the target. Tables 1–6 are all slightly over their individual allowances; the overruns were accepted provisionally and must be reconciled at the full 20-page proof.
- The table sections still use the Stage 3 numbering: §2 = Table 1, §3 = Table 2, §4 = Table 3, §5 = Table 4, §6 = Table 5, §7 = Table 6, §8 = Table 7, §9 = Table 8. §1 is “How Appendix B Works” and §10 is “Cross-Table Rules and Production Record.” The final pass will drop §1 and §10, add `## Note on the Tables`, and renumber Tables 1–8 as §1–§8.
- **New build blocker, EX-27:** Pandoc renders one note per reference, so a key used three times appears three times. The appendix has 154 definitions but 279 rendered references and an 87-page proof. Add a deduplication filter at Stage 7 before trusting any page measurement; do not delete repeated references to make the count fall.

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
  - **EX-17/EX-20:** Texas 1850 stock terms verified; Z 1–19 enslaved values corrected (1780 575,420; 1770 459,822; 1760 325,806; 1750 236,420).
  - **EX-18:** Table 1’s 1860/1900 regional counts do not sum to national totals; shares use the regional sum.
  - **EX-19:** Table 1 race/slavery columns dropped; Table 6 owns that series.
  - **EX-21:** Table 2 values verified against the APP compilation; HSUS/NARA/FEC row-level cross-check remains for Stage 5.
  - **EX-22/EX-23/EX-24/EX-26:** Table 2, 4, 5, and 6 page overruns accepted provisionally.
  - **EX-25:** SlaveVoyages Mainland North America totals changed between releases: live 472,372/388,744; earlier 472,381/388,747. Table 6 prints the live values and notes the older ones.
  - **EX-27:** the appendix proof duplicates notes on repeated references; fix the build before the page proof.
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

## 4. Table 7 handoff

### Scope and rows

- **Table 7. Economic and Communications Benchmarks, 1790–2024.**
- **38 ledger rows, all printed.** The cell file has only 11 seeded cells (7 `n_a`, 4 `unverified`); 32 rows are `not_started`. This is the largest remaining transcription: roughly 190 cells across four panels.
- **Panel A (15):** public finance, 1790, 1800, 1820, 1840, 1860, 1880, 1900, 1920, 1930, 1940, 1950, 1970, 2000, 2020, 2024.
- **Panel B (9):** production, prices, and output, 1830, 1860, 1900, 1930, 1940, 1950, 1970, 2000, 2024.
- **Panel C (7):** distribution and labor, 1913, 1929, 1950, 1970, 2000, 2020, 2024.
- **Panel D (7):** communications, 1850, 1880, 1900, 1920, 1950, 1970, 2000.
- **Page allowance:** 2 pages; likely 3–4 at 8-point. Accept provisionally if needed and record an exception.

### Panel design (from the Stage 3 §8.2 outline)

- **A:** year; receipts; outlays; surplus or deficit; gross federal debt; receipts as % of GDP; outlays as % of GDP. Current dollars. Fiscal years, not calendar years. The percentage columns are `n.a.` before 1930.
- **B:** year; railroad miles operated; steel ingots; unemployment rate; CPI; real GDP per capita. Endpoints and `n.a.` rules: railroad mileage ends 1970; steel begins 1887 and ends 1960; unemployment begins 1890; CPI begins 1913. The 2020 row is dropped.
- **C:** year; top 1 percent pre-tax national income share; Gini index; union density; labor-force participation. Gini begins 1967; union density begins 1930; LFP begins 1950. `n.a.` before those years.
- **D:** year; daily newspapers; weekday circulation; telephones in service; households with telephone. Panel ends at 2000. Telephones in service ends 1970; household telephone begins 1960.

### Key values and checks (seeded)

- **Panel B unemployment:** 1900 5.00 percent; 1930 8.7; 1940 9.5. These are the Darby–Weir Ba475 values. Lebergott’s D 85–86 gives 1940 14.6; put that in the note, not the cell.
- **Panel D 2000:** 1,480 daily newspapers and 55,772,847 weekday circulation from *Editor & Publisher*; households with telephone 97.6 percent (100 − 2.4).
- **Panel D 2000:** telephones in service is `n.a.`; do not substitute the FCC line count.
- **Panel C:** Gini is `n.a.` for 1913, 1929, and 1950; union density and LFP are `n.a.` for 1913 and 1929.
- **Panel A:** the percentage columns are `n.a.` before 1930. Do not compute them from receipts and outlays.
- **Panel B:** steel is `n.a.` for 1830, 1860, 1970, 2000, and 2024; railroad mileage is `n.a.` after 1970; CPI is `n.a.` before 1913.

### Sources and access

- **OMB Historical Tables FY 2027:** Table 1.1 (receipts, outlays, deficits, 1789–2025), Table 1.2 (percentages of GDP, 1930–2025), Table 7.1 (federal debt, 1940–2025). FY 2024 and FY 2025 are actuals. Use Table 1.2 for the percentage columns; do not compute them from Table 1.1.
- **HSUS 1975:** Y 335–338 for 1789–1939 and Y 339–342 for 1929–1970; Q 321–328 and Q 284–312 for railroad mileage; P 302 for steel; E 135 for the 1967 = 100 CPI; D 927–969 for union density; R 224–231 and R 244–257 for newspapers; R 1–16 for telephones.
- **HSUS Millennial:** Ba475 for the Darby–Weir unemployment rate; Cc1–2 is not needed here.
- **BLS:** LNS14000000 for unemployment 1950–2024; CUUR0000SA0 for CPI-U 1930–2024; LNS11300000 for LFP 1950–2024; union membership data 1983–2025.
- **BEA:** NIPA Table 7.1 for real GDP per capita 1930–2024, chained 2017 dollars; cross-check FRED A939RX0Q048SBEA from 1947.
- **Maddison Project Database 2023:** 1830–1900, 2011 international dollars. It ends in 2022, so 2024 is BEA only.
- **WID:** top 1 percent pre-tax national income share, series `sptinc_p99p100_z`, one 2025/2026 vintage, 1913–2024. **Access is unresolved.** Test the public WID download first. If it fails, the options are a WID export, a documented scope change removing the column, or a declared blocker; do not substitute the 2022 PSZ appendix tables or splice vintages.
- **Census:** Historical Income Table H-4 for Gini, household money income, 1967–2024; do not use family Gini F-4.
- **Editor & Publisher:** 2001 *Year Book* for 2000; Pew’s 55,773,000 is a cross-check, not a second series.
- **Census housing:** “Historical Census of Housing Tables: Telephones” for 1960–2000.
- **CRS R47596:** union membership data 1930–1982, in addition to HSUS D 927–969.

### Procedure

1. Read §8 in `chapters/52-appendix-b.md` and `data/app-b/table-07.csv`; note the 11 seeded cells and the 32 `not_started` rows.
2. Resolve WID first. If the column cannot be sourced, stop and record the blocker; do not draft the table with an empty column.
3. Verify or transcribe every cell panel by panel. Use the production CSV; do not rebuild from memory. Mark `verified`, `n_a`, or `not_applicable`.
4. Build `build/app-b-table-07.md` with four panels (A–D) and captions after each table inside `.appendix-table` divs. Render with:
   ```bash
   pandoc build/app-b-table-07.md --standalone --css=../styles/pdf.css \
     --metadata title='Table 7 proof' -o build/app-b-table-07.html
   weasyprint build/app-b-table-07.html build/app-b-table-07.pdf
   ```
5. Replace §8 in `chapters/52-appendix-b.md` with the draft. Keep the `## 8.` heading until the final renumbering. Do not leave unused note definitions: the checker reports `note-unused-definition`.
6. Run `python3 tools/check_book.py --strict chapters/52-appendix-b.md`. Expect 0 errors and 0 warnings; 154 notes remain unless a new note is needed.
7. Update `ledger.csv` (38 rows verified), `table-07.csv`, `README.md`, `contract.md`, `checks.md`, and `exceptions.md`.
8. Commit: `git add README.md chapters/52-appendix-b.md data/app-b && git commit -m "Draft Appendix B Table 7"`.

### Specific Table 7 traps

- **WID is a hard blocker.** The outline forbids splicing the 2022 Piketty–Saez–Zucman appendix tables onto RealTimeInequality or a later vintage. One vintage only.
- **Do not average or splice Lebergott and Darby–Weir.** The cells use Ba475; Lebergott’s 14.6 percent for 1940 belongs in the note.
- **Do not mix CPI bases.** CPI-U 1982–84 = 100 from 1930; E 135 1967 = 100 in the note only.
- **Do not compare GDP levels across the 1900/1930 break.** Maddison 2011 international dollars for 1830–1900; BEA chained 2017 dollars for 1930–2024. Compare growth rates within each segment.
- **Do not use the family Gini F-4.** H-4 household money income only.
- **Do not use Pew’s post-2014 print-and-digital circulation series.** Panel D ends at 2000.
- **Do not use the FCC line count as “telephones in service.”** It counts incumbent and competitive local-exchange lines, interconnected VoIP, and mobile subscriptions.
- **Fiscal years are not calendar years.** Label the Panel A rows as fiscal years.
- **The 2024 output cell is BEA only.** Maddison ends in 2022.
- **No 2020 Panel B row.** The pandemic year is an outlier and is discussed in the chapters.

## 5. Remaining after Table 7

- **Table 8 (23 rows, 59 cells; 53 unverified, 6 n.a.):** TVA, CCC, 1940 land use, Dust Bowl population. Need TVA dam pages, Statistical Abstract 1943, 1940 Census of Agriculture/Population images, Long–Siu. Map 26’s 48-state CCC counts stay in the map production file, not Table 8.
- **Final assembly:** after Table 8, drop §1 “How Appendix B Works” and §10 “Cross-Table Rules and Production Record,” add a reader-facing `## Note on the Tables`, renumber Tables 1–8 as §1–§8, reconcile the 20-page budget, update the README status to `drafted`, and run the full proof. Do not mark `checked`.
- **Build fix before the page proof:** EX-27, the duplicate-note rendering. Add a filter so each named key renders once with repeated references returning to the same note. Measure the appendix only after the fix.

## 6. Useful commands

```bash
# Structural check
python3 tools/check_book.py --strict chapters/52-appendix-b.md

# Section proof
pandoc build/app-b-table-07.md --standalone --css=../styles/pdf.css \
  --metadata title='Table 7 proof' -o build/app-b-table-07.html
weasyprint build/app-b-table-07.html build/app-b-table-07.pdf
pdfinfo build/app-b-table-07.pdf | grep Pages

# Normalize CSV line endings before commit
sed -i 's/\r$//' data/app-b/*.csv

# Commit
git add README.md chapters/52-appendix-b.md data/app-b
git commit -m "Draft Appendix B Table 7"
```

## 7. File map

| Path | Role |
|---|---|
| `chapters/52-appendix-b.md` | The draft; Tables 1–6 drafted under §§2–7, Tables 7–8 still Stage 3 specifications under §§8–9 |
| `data/app-b/contract.md` | Frozen decisions and verification standard |
| `data/app-b/README.md` | Counts, schemas, status, Step 3 workflow |
| `data/app-b/ledger.csv` | 255 display rows; current statuses and notes |
| `data/app-b/table-01.csv` … `08.csv` | Cell-level production records |
| `data/app-b/table-01-race-reference.csv` | 14 race/slavery cells moved out of Table 1; reference only |
| `data/app-b/checks.md` | Per-table checks and result log |
| `data/app-b/exceptions.md` | All open/resolved exceptions, including EX-25/26/27 |
| `styles/pdf.css` | `.appendix-table` compact table style |
| `README.md` | Book plan, Appendix B status row, page budget |
| `build/app-b-table-0N.md` / `.pdf` | Scratch proofs; `build/` is gitignored |

## 8. Immediate next action

Start with Table 7: open §8 and `table-07.csv`, resolve the WID column first, then verify and transcribe the other panels, build the four-panel proof, splice it into §8, run the checker, update the records, and commit. Then Table 8, the duplicate-note build fix, and the final renumbering/20-page proof.

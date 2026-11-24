# Appendix B — Stage 4 plan and handoff

**Status:** Tables 1–5 drafted and committed; Table 6 is next. Appendix B remains `researched` until Tables 6–8 are drafted. Last updated November 24, 2026.

**Purpose of this file:** preserve the original Stage 4 plan, the current state, and the working method so a fresh session can continue without the earlier chat context.

## 1. Current state

**HEAD:** this handoff commit; the last table commit is `56b8755` (“Draft Appendix B Table 5”).

| Commit | Work |
|---|---|
| `3756034` | Table 1 and the Step 0–3 production records |
| `d5a5a82` | Table 2 |
| `0947ff5` | Table 3 |
| `71f6052` | Table 4 |
| `56b8755` | Table 5 |

| Display | Appendix section | Rows | Cells | Proof | Notes |
|---|---:|---:|---:|---:|---|
| **Table 1** | §2 | 41 | 178 (166 verified, 12 n.a.) | 3 pp vs 2.5 | Race/slavery moved to Table 6; regional counts in thousands; 1860/1900 regional-sum note |
| **Table 2** | §3 | 60 | 710, all verified against the APP compilation | 5 pp vs 4 | Shares only, no counts; HSUS/NARA row-level cross-check remains for Stage 5 |
| **Table 3** | §4 | 13 | 113 (101 verified, 6 n.a., 6 not applicable) | 3 pp vs 2.5 | Texas 1850 stock terms verified against 9 Stat. 446–47 |
| **Table 4** | §5 | 13 | 130 (123 verified, 4 not applicable, 3 n.a.) | 3 pp vs 2 | CRS, DoD, Crawford verified |
| **Table 5** | §6 | 41 printed + 1 reserve | 246 (244 verified, 2 n.a.) | 3 pp vs 2.5 | 2020 foreign-born stock row reserved; ACS 5-year estimate not transcribed |

- The appendix is 20,681 words, 154 notes, 16 pipe tables. `python3 tools/check_book.py --strict chapters/52-appendix-b.md` passes with 0 errors and 0 warnings.
- The 20-page allowance is still the target. Tables 1–5 are all slightly over their individual allowances; the overruns were accepted provisionally and must be reconciled at the full 20-page proof.
- The table sections still use the Stage 3 numbering: §2 = Table 1, §3 = Table 2, §4 = Table 3, §5 = Table 4, §6 = Table 5, §7 = Table 6, §8 = Table 7, §9 = Table 8. §1 is “How Appendix B Works” and §10 is “Cross-Table Rules and Production Record.” The final pass will drop §1 and §10, add `## Note on the Tables`, and renumber Tables 1–8 as §1–§8.

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
  - **EX-17/EX-20:** Texas 1850 stock terms verified; Z 1–19 enslaved values corrected (1780 575,420; 1770 459,822; 1760 325,806; 1750 236,420).
  - **EX-18:** Table 1’s 1860/1900 regional counts do not sum to national totals; shares use the regional sum.
  - **EX-19:** Table 1 race/slavery columns dropped; Table 6 owns that series.
  - **EX-21:** Table 2 values verified against the APP compilation; HSUS/NARA/FEC row-level cross-check remains for Stage 5.
  - **EX-22/EX-23:** Table 2 and Table 4 page overruns accepted provisionally.
  - **EX-24:** Table 5 2020 stock row reserved; three-page proof accepted provisionally.
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

## 4. Table 6 handoff

### Scope and rows

- **Table 6. Slavery, Coerced Movement, and Prices.**
- **25 ledger rows, 24 printed + 1 trade-panel reserve.**
  - **Panel A (3):** Barbados 1643; Barbados 1679/80; Jamaica 1673.
  - **Panel B (8):** 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860.
  - **Panel C (6 ledger / 5 printed):** transatlantic embarked 1501–1866; transatlantic disembarked; U.S. imports; domestic trade, Goldin 1790–1860; domestic trade, Tadman 1790–1860; reserve (not printed).
  - **Panel D (8):** 1804, 1810, 1820, 1830, 1840, 1850, 1860, 1861.
- **Cells:** 63 currently seeded — 62 `unverified`, 1 `n_a`. The reserve row has no cells.
- **Page allowance:** 2 pages; likely 2–3 pages at 8-point. Accept provisionally if needed and record an exception.

### Panel design (from the Stage 3 §7.2 outline)

- **A:** colony; year; White population; enslaved population; source type; notes.
- **B:** census year; total population; Black population; enslaved population; enslaved share of total; enslaved share of Black.
- **C:** series; period; estimate; unit; method; source. The unit for the domestic rows is “net forced migrants (not sales).”
- **D:** year; nominal price; real price in 1860 dollars; sample; notes.

### Key values and checks

- **1790:** 697,681 enslaved within 757,208 Black; 17.8% of 3,929,214; 92.1% of Black.
- **1800–1850:** 893,602; 1,191,362; 1,538,022; 2,009,043; 2,487,355; 3,204,313.
- **1860:** 3,953,760 enslaved within 4,441,830 Black; 12.6% of 31,443,321; 89.0% of Black. The 1860 census introduction prints 487,970 free “colored” and 4,441,730 total; the 100-person difference is a vintage difference.
- **Caribbean:** Barbados 1643 18,600 White / 6,400 enslaved; Barbados 1679/80 38,782 enslaved, White `n.a.`; Jamaica 1673 7,768 White / 9,504 enslaved.
- **Trade:** 12,521,354 embarked; about 10.7 million disembarked; U.S. imports 472,381 embarked / 388,747 disembarked; Goldin 835,000; Tadman 1,110,000. Goldin and Tadman are alternatives, not a range; Tadman is cited through Pritchett unless the book is read.
- **Prices:** nominal 700, 624, 875, 591, 773, 756, 1,513, 1,440; Cc2 index 142, 148, 141, 111, 104, 94, 100, 106; real 1860 dollars 493, 422, 621, 532, 743, 804, 1,513, 1,358.
- **Arithmetic:** 697,681 + 59,527 = 757,208; 3,953,760 + 488,070 = 4,441,830; 3,542,147 “black” + 411,613 “mulatto” = 3,953,760; nominal × 100 / Cc2 = real (rounded).

### Sources and access

- **HSUS Millennial** (user can supply): Bb209–214, Cc1–2; also Ba470–477. Record the release/access date.
- **HSUS 1975:** A 91–104 (race and enslaved totals), Z 1–19 (colonial totals; corrected values), Bb essay (if using the Millennial).
- **SlaveVoyages:** Estimates and Intra-American database pages.
- **Pritchett 2017** working paper; Tadman 1989 and Goldin via Pritchett.
- **Dunn 1969/1972 and Southey 1673:** print/archival pages not supplied. Use the exact page locators from the outline, or mark the affected cells `pending_print` and state “as cited in …”; do not present them as read.
- **1860 Census:** page images, pp. ix and 599; read as images.
- **ICPSR 7423 / Kotlikoff 1979:** alternatives, not cell sources; keep limitations.

### Procedure

1. Read the current Stage 3 §7 in `chapters/52-appendix-b.md` and `data/app-b/table-06.csv`; note the current values and statuses.
2. Verify or transcribe every cell. Use the production CSV; do not rebuild from memory. Mark `verified`, `n_a`, or `not_applicable`.
3. Build `build/app-b-table-06.md` with four panels (A–D) and captions after each table inside `.appendix-table` divs. Render with:
   ```bash
   pandoc build/app-b-table-06.md --standalone --css=../styles/pdf.css \
     --metadata title='Table 6 proof' -o build/app-b-table-06.html
   weasyprint build/app-b-table-06.html build/app-b-table-06.pdf
   ```
4. Replace §7 in `chapters/52-appendix-b.md` with the draft. Keep the `## 7.` heading until the final renumbering. Do not leave unused note definitions: the checker reports `note-unused-definition`.
5. Run `python3 tools/check_book.py --strict chapters/52-appendix-b.md`. Expect 0 errors and 0 warnings; 154 notes remain unless a new note is needed.
6. Update `ledger.csv` (24 printed rows verified; reserve stays `reserve`), `table-06.csv`, `README.md`, `contract.md`, `checks.md`, and `exceptions.md`.
7. Commit: `git add README.md chapters/52-appendix-b.md data/app-b && git commit -m "Draft Appendix B Table 6"`.

### Specific Table 6 traps

- The **1780/1770/1760/1750 enslaved values** were corrected in EX-20. Do not reintroduce 675,420/459,822/325,806 for 1780/1760/1750. Table 6 Panel B starts at 1790, but the source note and any colonial context must use the corrected values.
- **Do not add enslaved to Black**; the enslaved population is a subset of the Black population before 1865.
- **Do not use 305,326** as U.S. imports; that is the U.S.-flagged-vessel series.
- **Goldin and Tadman** are alternative estimates of net forced migrants, not a range and not sales counts.
- **Barbados 1679/80 White** is `n.a.`, not zero; the adjacent 21,725 (1676) and 19,568 (1684) values go in the note.
- **Prices** are the published Engerman Bb210 series, not a raw median from ICPSR 7423.
- The trade panel’s sixth ledger row is a reserve; do not print it.

## 5. Remaining after Table 6

- **Table 7 (38 rows, 11 cells: 7 n.a., 4 unverified):** economic and communications benchmarks. WID access is unresolved; HSUS Millennial is available; OMB/BLS/BEA/Maddison and Editor & Publisher. The top-share column cannot be drafted without a WID export or a documented scope change. The table is 38 rows and four panels; check the CSV and §8 outline.
- **Table 8 (23 rows, 59 cells; 53 unverified, 6 n.a.):** TVA, CCC, 1940 land use, Dust Bowl population. Need TVA dam pages, Statistical Abstract 1943, 1940 Census of Agriculture/Population images, Long–Siu. Map 26’s 48-state CCC counts stay in the map production file, not Table 8.
- **Final assembly:** after Table 8, drop §1 “How Appendix B Works” and §10 “Cross-Table Rules and Production Record,” add a reader-facing `## Note on the Tables`, renumber Tables 1–8 as §1–§8, reconcile the 20-page budget, update the README status to `drafted`, and run the full proof. Do not mark `checked`.

## 6. Useful commands

```bash
# Structural check
python3 tools/check_book.py --strict chapters/52-appendix-b.md

# Section proof
pandoc build/app-b-table-06.md --standalone --css=../styles/pdf.css \
  --metadata title='Table 6 proof' -o build/app-b-table-06.html
weasyprint build/app-b-table-06.html build/app-b-table-06.pdf
pdfinfo build/app-b-table-06.pdf | grep Pages

# Normalize CSV line endings before commit
sed -i 's/\r$//' data/app-b/*.csv

# Commit
git add README.md chapters/52-appendix-b.md data/app-b
git commit -m "Draft Appendix B Table 6"
```

## 7. File map

| Path | Role |
|---|---|
| `chapters/52-appendix-b.md` | The draft; Tables 1–5 drafted under §§2–6, Tables 6–8 still Stage 3 specifications under §§7–9 |
| `data/app-b/contract.md` | Frozen decisions and verification standard |
| `data/app-b/README.md` | Counts, schemas, status, Step 3 workflow |
| `data/app-b/ledger.csv` | 255 display rows; current statuses and notes |
| `data/app-b/table-01.csv` … `08.csv` | Cell-level production records |
| `data/app-b/table-01-race-reference.csv` | 14 race/slavery cells moved out of Table 1; reference only |
| `data/app-b/checks.md` | Per-table checks and result log |
| `data/app-b/exceptions.md` | All open/resolved exceptions |
| `styles/pdf.css` | `.appendix-table` compact table style |
| `README.md` | Book plan, Appendix B status row, page budget |
| `build/app-b-table-0N.md` / `.pdf` | Scratch proofs; `build/` is gitignored |

## 8. Immediate next action

Start with Table 6: open §7 and `table-06.csv`, verify the cells, build the four-panel proof, splice it into §7, run the checker, update the records, and commit. Then Table 7, Table 8, and the final renumbering/20-page proof.

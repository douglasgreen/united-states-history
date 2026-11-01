# Table Production and Data Guide

*A companion to the table register in [README.md](README.md) for “A Nation in Question: A History of the United States.”*

**Compiled:** November 1, 2026. **Scope:** the 80 published tables registered in `README.md`, plus the table-shaped drafts that are not published tables. **Authority:** `README.md` remains the canonical register and numbering authority. This guide is a derivative production worklist. If the two disagree, the README governs, and the discrepancy is recorded in §9. The guide records the state of the files on November 1, 2026; it is not itself a verification pass, and it does not certify any cell.

This guide is written for the person who has to gather the data, verify it, and set the table. It does not replace the chapter’s researched outline, the combined footnote list, or the README register. It tells you what each table is for, where it goes, which columns and rows it needs, what the draft currently contains, what must be checked, and how the finished table must look.

**Contents.** §1 How to use this guide · §2 The 80-table inventory · §3 Global production standard · §4 Master index · §5 Chapter data and comparison tables (13) · §6 Historiographical comparison tables (51) · §7 Appendix tables (16) · §8 Non-published table-shaped material · §9 Register discrepancies · §10 Research checklist by source family · §11 Sign-off checklist · §12 A note on authority.

## 1. How to use this guide

1. **Start with the master index in §4.** It lists all 80 published tables in book order with their planning IDs, display numbers, owners, exact locations, and status.
2. **Open the owning chapter or appendix before changing a table.** The draft table, its caption, its source line, and the surrounding argument are the local authority for that table’s job. This guide summarizes them but does not override them.
3. **Treat every value in a “draft values” block as unverified.** A value is publishable only after the source named in the chapter’s combined notes has been opened and the exact locator checked. “Planned” and “draft” are not publication states.
4. **Use the column specification, not the draft’s visual width, to decide what belongs in a cell.** The draft may be incomplete; the specification states the minimum content and the rules.
5. **Record every change in the owning file and in the README register.** A new row, a dropped row, a changed definition, or a new source is a substantive change. It reopens the chapter’s table check.
6. **Do not create a second numbering list.** Planning IDs such as `ch08-table-01` are for production. Readers see “Ch. 8, Table 1.” Appendix B panels keep one parent number; a panel is not a new table.

### Status vocabulary

| Status | Meaning for a table |
|---|---|
| **`planned`** | The table has a registered purpose, location, and scope, but no verified data or finished layout. |
| **`drafted`** | A complete draft table exists in the owning file, with caption and source line, but its cells have not been verified against the cited evidence. |
| **`verified`** | Every cell has been checked against a named source and locator; definitions, units, denominators, and rounding are stated; the caption and source line are final. |
| **`typeset`** | The table has been set in the book’s layout, inspected in proof, and reconciled with the page budget. |

The current manuscript is at `drafted` for the 13 chapter data tables and the 51 historiographical tables, and `planned` for the 16 appendix tables. One historiographical table, Ch. 49, Table 1, still has a placeholder row for the institutional-resilience position; it is a partial draft, not a finished one. No table in this repository is `verified` or `typeset`. The chapter files call these drafts “planned”; this guide uses `drafted` for the table block and `planned` for the data verification, because the distinction matters: the structure exists, the evidence does not yet.

## 2. The 80-table inventory

The README register counts **39 maps, nine figures, eight images, and 80 published tables**. “Published” here means the release plan’s count, not tables already in print; none of the 80 is verified or typeset. The 80 tables divide as follows:

| Group | Count | What it is | Where it lives |
|---|---:|---|---|
| **Chapter data and comparison tables** | 13 | Substantive tables inside narrative chapters: elections, resources, cases, casualties, treaties, quotas | Chapters 8, 19, 20, 22, 29, 30, 31, 32 |
| **Historiographical comparison tables** | 51 | One “map of positions” table per chapter, plus one in the Introduction | Introduction and Chapters 1–50, normally §6.4 or §7.4 |
| **Appendix tables** | 16 | Eight Appendix B datasets, one Appendix C gazetteer, seven Appendix D chronologies | Appendices B, C, D |
| **Total** | **80** | | |

The 51 historiographical tables are the Introduction’s Table 1 and one table in every numbered chapter. The display number is not always “Table 1”: eight chapters have earlier data tables, so their debate table is Table 2 or Table 3. The master index preserves the actual display numbers.

### What is in the files now

A direct scan of the 56 manuscript files on November 1, 2026, found **65 pipe-table blocks** outside the page-budget tables:

- **51 historiographical tables**, all with drafted rows, captions, source lines, alt text, and textual references.
- **13 registered chapter data tables**, all with drafted rows, captions, source lines, alt text, and textual references.
- **1 figure-backing table** in Chapter 9 (§1, “Draft Figure 1 data”), which is not a published table. It becomes Figure 1.
- **0 table blocks in Appendices A–E.** Appendix B is still a seed; Appendix C’s gazetteer is a list, not yet a table; Appendix D’s seven chronology blocks are still prose seeds.

The README’s older inventory of “81 pipe-table blocks” is a historical planning count, not the current file count. The six figure-backing tables named there (`ch16-figure-data`, `ch24-figure-data`, `ch26-figure-data`, `ch28-figure-data`, `ch33-figure-data`, `ch35-figure-data`) are not present as separate table blocks in the current chapter files. Their data must be rebuilt from the figures and production records. The three editorial tables (`app-b-editorial-crosswalk`, `app-c-editorial-concordance`, `app-c-editorial-figure-list`) are not published tables. Section 8 lists these non-published items.

## 3. Global production standard

Every published table in this book must satisfy the following rules, in addition to the evidence rules in `AGENTS.md` §§3–6.

### 3.1 Placement and numbering

- **Number within the owner.** Chapter tables use “Ch. 8, Table 1,” “Ch. 31, Table 2,” and so on. Appendix tables use “App. B, Table 1,” “App. D, Table 4.” The Introduction uses “Introduction, Table 1.”
- **One owner, one display number.** A table reproduced or referenced elsewhere keeps its owner and number. Do not renumber a table because it is mentioned in another chapter.
- **Place the table after the paragraph that introduces it.** The prose must refer to the table by number before the reader reaches it. A table without a textual reference is an orphan and fails the chapter check.
- **Keep the registered section location unless the chapter is restructured.** If the section moves, update the README register, the chapter’s textual reference, and any cross-reference in the same change.
- **Do not count planning tables.** The page-budget table at the top of each chapter is an unnumbered production table. It is not a published table and must not be counted, numbered, or captioned as one. The structural checker reports it as an uncaptioned planning table; that `INFO` is expected.

### 3.2 Markdown shape

```markdown
| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Row label** | Name, *Work* (year) | One-sentence claim. | One-sentence contribution. | One-sentence limitation. |
```

- Use a header row, a separator row, and body rows. No merged cells, nested tables, or multi-row headers.
- **Bold the leading cell of every body row.** Do not bold whole rows or whole paragraphs.
- Left-align text columns. Right-align numeric columns with `---:` in the separator. Do not center by default.
- Keep cells short. If a cell exceeds roughly 35 words, move the argument to prose or a table note. A five-column table with 50-word cells will not fit the trim size.
- Do not put footnote definitions or long citations inside cells. Use the chapter’s named note keys in the source line. If a draft cell contains a note marker such as `[^ch26-pfeifer-woodward]`, move it to the source line or to a table note keyed to the row; a published table should not read as a field of note markers.
- Do not use hard breaks, tabs, or non-breaking spaces inside cells. Use ordinary spaces.
- Use curly quotation marks and apostrophes, spaced em dashes, and en dashes for ranges. A hyphen is not a range.

### 3.3 Required apparatus

Each published table carries four elements after the table block:

1. **Caption.** `**Caption.** Table N. Title, date range, and unit/geography.` The caption must identify panels, observation dates, uncertainty, and definitions where they are not obvious.
2. **Source line.** `**Source line.** ... Status: ...` It names who compiled the table, the verified sources, the transformations, and the rights/credit status. Full bibliographic details live in the chapter’s combined notes; the source line carries the note keys.
3. **Alt text.** `**Alt text.** ...` One sentence describing the table’s structure and the pattern it shows. Do not repeat the caption or invent content. The current chapter drafts include alt text for every table; keep that convention.
4. **Textual reference.** `**Textual reference.** “...”` The exact sentence in the prose that sends the reader to the table. If the sentence changes, update this field.

The caption, source line, alt text, and textual reference are part of the table’s production record. A table without them is not finished, even if the cells are correct.

### 3.4 Data rules

- **Observation year is not publication year.** State the year or period the data describe. A 2024 Census Bureau release may report 2020 data; the table says 2020.
- **State units, denominators, and geography.** Persons, households, dollars, nominal or real, acres, square miles, percentages of what population, registered voters or voting-eligible population, states counted, boundaries used.
- **Distinguish stocks from flows.** Debt stock, annual revenue, cumulative service, peak strength, admissions, and foreign-born stock are not interchangeable.
- **Distinguish appropriations from expenditures and nominal from real.** If a cost is inflation-adjusted, name the index and base year. Do not mix series with different bases.
- **Do not derive a percentage across incompatible boundaries.** If the numerator and denominator use different geographies, races, or years, show the components and label the result as approximate, or omit the percentage.
- **Round consistently and say so.** If shares are rounded to one decimal and do not sum to 100, say that in a note.
- **“Not available” is a legitimate published value only when the table explains why.** A blank cell is not. A planning cell such as “not yet sourced” must be replaced before publication.
- **Do not combine estimates from different methods into a single total.** Show them side by side with method and scope, as Chapter 22’s mortality table does.
- **Do not treat a compiled table as a primary source.** The compilation is only as good as its underlying series. Cite the series, not the webpage that republished it.
- **Capitalize Black and White when referring to people**, including in table cells, captions, and alt text. Several drafts use lowercase “white” and “black”; correct them in the final pass. This is a house-style rule, not a change of meaning.

### 3.5 Evidence and rights

- Every row and every numeric cell needs a named citation note with an exact locator: page, table, document number, dataset variable, or timestamp.
- A citation to a work consulted only in review, excerpt, or publisher description must say so. Do not present a review’s paraphrase as the work’s argument.
- Original compilations are planned for the book’s own tables, but third-party data terms and copied artwork still need review. For images, permission and credit evidence are pending for each item. A table that reproduces a third-party table needs its own rights check.
- Do not invent a source, URL, page, dataset, or verification result. A link that opens is not proof that it supports the cell.

### 3.6 Sizing and typesetting

- The book’s trim size and text block are not yet measured in this repository. Until a representative table is typeset, treat every page allowance as provisional.
- A five-column historiographical table with 3–9 rows will likely require a full page at 8.5–9 pt, and a nine-row table may run longer. If it breaks across a page, repeat the header row; do not split a row.
- If a table cannot fit, shorten the cells. Do not delete a position merely to save space; the register’s row count is the analytical minimum.
- Inspect every table in proof for: header repetition, row splits, bold leading cells, numeric alignment, caption placement, source line, note keys, and the textual reference. A Markdown render is not a typeset proof.

## 4. Master index of published tables

The index is in book order: Introduction, Chapters 1–50, then Appendices B–D. “Location” is the section in the current manuscript. Where the README register gives a different section, both are shown and the discrepancy is flagged in §9. Status is the table block’s state, not the data’s.


| Display | Planning ID | Owner file | Exact location | Type | Title or subject | Status |
|---|---|---|---|---|---|---|
| **Introduction, Table 1** | `intro-table-01` | `chapters/00-introduction.md` | §6.5 Table 1 | Historiographical comparison | Schools, questions, and historical evidence | Drafted, unverified |
| **Ch. 1, Table 1** | `ch01-table-01` | `chapters/01-chapter-1.md` | §6.4 The map of positions | Historiographical comparison | Landscape management and ecological interpretation | Drafted, unverified |
| **Ch. 2, Table 1** | `ch02-table-01` | `chapters/02-chapter-2.md` | §6.4 The map of positions | Historiographical comparison | Exchange, disease, coercion, and demographic change | Drafted, unverified |
| **Ch. 3, Table 1** | `ch03-table-01` | `chapters/03-chapter-3.md` | §6.4 The map of positions | Historiographical comparison | Indigenous agency and the contact framework | Drafted, unverified |
| **Ch. 4, Table 1** | `ch04-table-01` | `chapters/04-chapter-4.md` | §6.4 The map of positions | Historiographical comparison | Religion, commerce, freedom, and colonial labor | Drafted, unverified |
| **Ch. 5, Table 1** | `ch05-table-01` | `chapters/05-chapter-5.md` | §6.4 The map of positions | Historiographical comparison | Origins of racial slavery | Drafted, unverified |
| **Ch. 6, Table 1** | `ch06-table-01` | `chapters/06-chapter-6.md` | §6.4 The map of positions | Historiographical comparison | War, alliance, and the imperial turn | Drafted, unverified |
| **Ch. 7, Table 1** | `ch07-table-01` | `chapters/07-chapter-7.md` | §7.4 The map of positions | Historiographical comparison | Deference, conflict, and colonial culture | Drafted, unverified |
| **Ch. 8, Table 1** | `ch08-table-01` | `chapters/08-chapter-8.md` | §1.3, “The demographic imbalance and what it meant,” under “Draft Table 1” | Chapter data/comparison | New France and the British colonies compared, about 1755 | Drafted, unverified |
| **Ch. 8, Table 2** | `ch08-table-02` | `chapters/08-chapter-8.md` | §5.1, “The Peace of Paris and the reshuffling of empires,” under “Draft Table 2” | Chapter data/comparison | The 1763 territorial settlement in North America | Drafted, unverified |
| **Ch. 8, Table 3** | `ch08-table-03` | `chapters/08-chapter-8.md` | §6.4 The map of positions | Historiographical comparison | Imperial victory and independence’s contingency | Drafted, unverified |
| **Ch. 9, Table 1** | `ch09-table-01` | `chapters/09-chapter-9.md` | §6.4 The map of positions | Historiographical comparison | Ideology, interests, and imperial resistance | Drafted, unverified |
| **Ch. 10, Table 1** | `ch10-table-01` | `chapters/10-chapter-10.md` | §7.4 The map of positions | Historiographical comparison | The decision for independence | Drafted, unverified |
| **Ch. 11, Table 1** | `ch11-table-01` | `chapters/11-chapter-11.md` | §7.4 The map of positions | Historiographical comparison | Revolution, civil war, and world war | Drafted, unverified |
| **Ch. 12, Table 1** | `ch12-table-01` | `chapters/12-chapter-12.md` | §7.4 The map of positions | Historiographical comparison | The Constitution’s interests and powers | Drafted, unverified |
| **Ch. 13, Table 1** | `ch13-table-01` | `chapters/13-chapter-13.md` | §7.4 The map of positions | Historiographical comparison | Party, fiscal authority, and consolidation | Drafted, unverified |
| **Ch. 14, Table 1** | `ch14-table-01` | `chapters/14-chapter-14.md` | §6.4 The map of positions | Historiographical comparison | Jeffersonian restraint and expansion | Drafted, unverified |
| **Ch. 15, Table 1** | `ch15-table-01` | `chapters/15-chapter-15.md` | §6.4 The map of positions | Historiographical comparison | The Market Revolution | Drafted, unverified |
| **Ch. 16, Table 1** | `ch16-table-01` | `chapters/16-chapter-16.md` | §6.4 The map of positions | Historiographical comparison | Democracy, class, and exclusion | Drafted, unverified |
| **Ch. 17, Table 1** | `ch17-table-01` | `chapters/17-chapter-17.md` | §6.4 The map of positions | Historiographical comparison | Removal, sovereignty, and borderlands | Drafted, unverified |
| **Ch. 18, Table 1** | `ch18-table-01` | `chapters/18-chapter-18.md` | §6.4 The map of positions | Historiographical comparison | Expansion, slavery, and conquest | Drafted, unverified |
| **Ch. 19, Table 1** | `ch19-table-01` | `chapters/19-chapter-19.md` | §2.1, “Table 1: selected fugitive cases, 1851–1854” | Chapter data/comparison | Selected fugitive cases under the Fugitive Slave Act of 1850, 1851–1854 | Drafted, unverified |
| **Ch. 19, Table 2** | `ch19-table-02` | `chapters/19-chapter-19.md` | §3.4, “Table 2: the election of 1856” | Chapter data/comparison | The presidential election of 1856: candidates, popular votes, and electoral votes | Drafted, unverified |
| **Ch. 19, Table 3** | `ch19-table-03` | `chapters/19-chapter-19.md` | §6.4 The map of positions | Historiographical comparison | Sectional conflict and contingency | Drafted, unverified |
| **Ch. 20, Table 1** | `ch20-table-01` | `chapters/20-chapter-20.md` | §1.3, “Table 1: the election of 1860” | Chapter data/comparison | The presidential election of 1860: candidates, reported popular votes, shares, and electoral votes | Drafted, unverified |
| **Ch. 20, Table 2** | `ch20-table-02` | `chapters/20-chapter-20.md` | §5.1, “Table 2: resources at the war’s outset” | Chapter data/comparison | Resources at the war’s outset: explicit Union and Confederate geography, 1860–61 | Drafted, unverified |
| **Ch. 20, Table 3** | `ch20-table-03` | `chapters/20-chapter-20.md` | §6.4 The map of positions | Historiographical comparison | Secession and slaveholding state-building | Drafted, unverified |
| **Ch. 21, Table 1** | `ch21-table-01` | `chapters/21-chapter-21.md` | §7.4 The map of positions | Historiographical comparison | Emancipation and the war’s transformation | Drafted, unverified |
| **Ch. 22, Table 1** | `ch22-table-01` | `chapters/22-chapter-22.md` | §3.3, “The measure: the election of 1864” | Chapter data/comparison | The election of 1864: national versus soldier vote | Drafted, unverified |
| **Ch. 22, Table 2** | `ch22-table-02` | `chapters/22-chapter-22.md` | §4.4, “The measure: the mortality estimates” | Chapter data/comparison | Civil War mortality estimates: methods, scope, and uncertainty | Drafted, unverified |
| **Ch. 22, Table 3** | `ch22-table-03` | `chapters/22-chapter-22.md` | §6.4 The map of positions | Historiographical comparison | Victory, revolution, and state-building | Drafted, unverified |
| **Ch. 23, Table 1** | `ch23-table-01` | `chapters/23-chapter-23.md` | §7.4 The map of positions | Historiographical comparison | Reconstruction and counterrevolution | Drafted, unverified |
| **Ch. 24, Table 1** | `ch24-table-01` | `chapters/24-chapter-24.md` | §6.4 The map of positions | Historiographical comparison | Management, political economy, and labor | Drafted, unverified |
| **Ch. 25, Table 1** | `ch25-table-01` | `chapters/25-chapter-25.md` | §6.4 The map of positions | Historiographical comparison | Frontier versus conquest | Drafted, unverified |
| **Ch. 26, Table 1** | `ch26-table-01` | `chapters/26-chapter-26.md` | §6.4 The map of positions | Historiographical comparison | Making and enforcing Jim Crow | Drafted, unverified |
| **Ch. 27, Table 1** | `ch27-table-01` | `chapters/27-chapter-27.md` | §6.4 The map of positions | Historiographical comparison | Populism, reform, and empire | Drafted, unverified |
| **Ch. 28, Table 1** | `ch28-table-01` | `chapters/28-chapter-28.md` | §6.4 The map of positions | Historiographical comparison | Mass culture and hierarchy | Drafted, unverified |
| **Ch. 29, Table 1** | `ch29-table-01` | `chapters/29-chapter-29.md` | §4.3, “The election of 1912” | Chapter data/comparison | The election of 1912: candidates, reported popular vote and share, and electoral votes | Drafted, unverified |
| **Ch. 29, Table 2** | `ch29-table-02` | `chapters/29-chapter-29.md` | §6.4 The map of positions | Historiographical comparison | Progressive reform and its limits | Drafted, unverified |
| **Ch. 30, Table 1** | `ch30-table-01` | `chapters/30-chapter-30.md` | §1.4, “Table 1 and Map 23: the instruments, 1901–1917” | Chapter data/comparison | Instruments of Caribbean control, 1901–1917: territory, instrument and date, what the United States gained, and the legal form | Drafted, unverified |
| **Ch. 30, Table 2** | `ch30-table-02` | `chapters/30-chapter-30.md` | §6.4 The map of positions | Historiographical comparison | Informal empire and intervention | Drafted, unverified |
| **Ch. 31, Table 1** | `ch31-table-01` | `chapters/31-chapter-31.md` | §2.4, “Map 24 and Table 1: the AEF in France and its cost” | Chapter data/comparison | AEF personnel and casualties, 1917–1919: the size of the force, its deaths by cause, its combat days, and the cost of the Meuse-Argonne | Drafted, unverified |
| **Ch. 31, Table 2** | `ch31-table-02` | `chapters/31-chapter-31.md` | §5.3, “Table 2: the Senate votes” (README register says §5.4 — see §9) | Chapter data/comparison | Senate votes on the Treaty of Versailles: the three roll calls of 1919–20 and their failure to reach the constitutional two-thirds | Drafted, unverified |
| **Ch. 31, Table 3** | `ch31-table-03` | `chapters/31-chapter-31.md` | §6.4 The map of positions | Historiographical comparison | Wartime state and democratic coercion | Drafted, unverified |
| **Ch. 32, Table 1** | `ch32-table-01` | `chapters/32-chapter-32.md` | §4.2, “Table 1: the quota systems compared” | Chapter data/comparison | Immigration quota systems, 1921–1929: the shift from a 1910-based 3 percent quota to a 1924 interim formula and the 1929 national-origins quotas, with the exclusions each imposed | Drafted, unverified |
| **Ch. 32, Table 2** | `ch32-table-02` | `chapters/32-chapter-32.md` | §6.4 The map of positions | Historiographical comparison | Modernity, prosperity, and belonging | Drafted, unverified |
| **Ch. 33, Table 1** | `ch33-table-01` | `chapters/33-chapter-33.md` | §6.4 The map of positions | Historiographical comparison | Causes and transmission of depression | Drafted, unverified |
| **Ch. 34, Table 1** | `ch34-table-01` | `chapters/34-chapter-34.md` | §6.4 The map of positions | Historiographical comparison | New Deal transformation and exclusions | Drafted, unverified |
| **Ch. 35, Table 1** | `ch35-table-01` | `chapters/35-chapter-35.md` | §6.4 The map of positions | Historiographical comparison | Neutrality, intervention, and choice | Drafted, unverified |
| **Ch. 36, Table 1** | `ch36-table-01` | `chapters/36-chapter-36.md` | §6.4 The map of positions | Historiographical comparison | Coalition, citizenship, and the war’s endings | Drafted, unverified |
| **Ch. 37, Table 1** | `ch37-table-01` | `chapters/37-chapter-37.md` | §6.4 The map of positions | Historiographical comparison | Cold War origins and domestic consequences | Drafted, unverified |
| **Ch. 38, Table 1** | `ch38-table-01` | `chapters/38-chapter-38.md` | §6.4 The map of positions | Historiographical comparison | Affluence, conformity, and resistance | Drafted, unverified |
| **Ch. 39, Table 1** | `ch39-table-01` | `chapters/39-chapter-39.md` | §7.4 The map of positions | Historiographical comparison | Movement strategy, rights, and economic justice | Drafted, unverified |
| **Ch. 40, Table 1** | `ch40-table-01` | `chapters/40-chapter-40.md` | §6.4 The map of positions | Historiographical comparison | Great Society ambition and constraint | Drafted, unverified |
| **Ch. 41, Table 1** | `ch41-table-01` | `chapters/41-chapter-41.md` | §6.4 The map of positions | Historiographical comparison | Containment and Vietnam escalation | Drafted, unverified |
| **Ch. 42, Table 1** | `ch42-table-01` | `chapters/42-chapter-42.md` | §6.4 The map of positions | Historiographical comparison | Liberal continuity and political realignment | Drafted, unverified |
| **Ch. 43, Table 1** | `ch43-table-01` | `chapters/43-chapter-43.md` | §6.4 The map of positions | Historiographical comparison | Seventies crisis and institutional change | Drafted, unverified |
| **Ch. 44, Table 1** | `ch44-table-01` | `chapters/44-chapter-44.md` | §6.4 The map of positions | Historiographical comparison | Conservatism and the Cold War’s ending | Drafted, unverified |
| **Ch. 45, Table 1** | `ch45-table-01` | `chapters/45-chapter-45.md` | §6.4 The map of positions | Historiographical comparison | Globalization, growth, and distribution | Drafted, unverified |
| **Ch. 46, Table 1** | `ch46-table-01` | `chapters/46-chapter-46.md` | §6.4 The map of positions | Historiographical comparison | Emergency, security, and constitutional power | Drafted, unverified |
| **Ch. 47, Table 1** | `ch47-table-01` | `chapters/47-chapter-47.md` | §6.4 The map of positions | Historiographical comparison | Recovery, reform, and polarization | Drafted, unverified |
| **Ch. 48, Table 1** | `ch48-table-01` | `chapters/48-chapter-48.md` | §7.4 The map of positions | Historiographical comparison | Populism and institutional erosion | Drafted, unverified |
| **Ch. 49, Table 1** | `ch49-table-01` | `chapters/49-chapter-49.md` | §6.4 The map of positions | Historiographical comparison | Competing explanations of the unsettled present | Drafted, unverified |
| **Ch. 50, Table 1** | `ch50-table-01` | `chapters/50-chapter-50.md` | §6.4 The map of positions | Historiographical comparison | Usable past, exceptionalism, and unfinished settlement | Drafted, unverified |
| **App. B, Table 1** | `app-b-table-01` | `chapters/52-appendix-b.md` | First dataset; §B.1 | Appendix dataset | Population and urbanization, 1630–2020 | Planned, no data |
| **App. B, Table 2** | `app-b-table-02` | `chapters/52-appendix-b.md` | Second dataset; §B.2 | Appendix dataset | Presidential elections, 1789–2024 | Planned, no data |
| **App. B, Table 3** | `app-b-table-03` | `chapters/52-appendix-b.md` | Third dataset; §B.3 | Appendix dataset | Territory and treaty instruments, 1763–1917 | Planned, no data |
| **App. B, Table 4** | `app-b-table-04` | `chapters/52-appendix-b.md` | Fourth dataset; §B.4 | Appendix dataset | War, mobilization, and cost: selected conflicts through 2021 | Planned, no data |
| **App. B, Table 5** | `app-b-table-05` | `chapters/52-appendix-b.md` | Fifth dataset; §B.5 | Appendix dataset | Immigration and quotas, 1820–2020, with separately labeled colonial context | Planned, no data |
| **App. B, Table 6** | `app-b-table-06` | `chapters/52-appendix-b.md` | Sixth dataset; §B.6 | Appendix dataset | Enslavement and coerced movement: Caribbean benchmarks, the U.S. census, and trade and price estimates | Planned, no data |
| **App. B, Table 7** | `app-b-table-07` | `chapters/52-appendix-b.md` | Seventh dataset; §B.7 | Appendix dataset | Economic and communications benchmarks, 1790–2024 where series permit | Planned, no data |
| **App. B, Table 8** | `app-b-table-08` | `chapters/52-appendix-b.md` | Eighth dataset; §B.8 | Appendix dataset | Land use, public works, and settlement, 1930–1940 | Planned, no data |
| **App. C, Table 1** | `app-c-table-01` | `chapters/53-appendix-c.md` | Gazetteer; §C.2 | Appendix dataset | Gazetteer of historical and present place names | Planned, no data |
| **App. D, Table 1** | `app-d-table-01` | `chapters/54-appendix-d.md` | §D.1 | Appendix chronology | Deep past–1606 | Planned, no data |
| **App. D, Table 2** | `app-d-table-02` | `chapters/54-appendix-d.md` | §D.2 | Appendix chronology | 1607–1699 | Planned, no data |
| **App. D, Table 3** | `app-d-table-03` | `chapters/54-appendix-d.md` | §D.3 | Appendix chronology | 1700–1799 | Planned, no data |
| **App. D, Table 4** | `app-d-table-04` | `chapters/54-appendix-d.md` | §D.4 | Appendix chronology | 1800–1899 | Planned, no data |
| **App. D, Table 5** | `app-d-table-05` | `chapters/54-appendix-d.md` | §D.5 | Appendix chronology | 1900–1945 | Planned, no data |
| **App. D, Table 6** | `app-d-table-06` | `chapters/54-appendix-d.md` | §D.6 | Appendix chronology | 1946–2000 | Planned, no data |
| **App. D, Table 7** | `app-d-table-07` | `chapters/54-appendix-d.md` | §D.7 | Appendix chronology | 2001–October 29, 2026 | Planned, no data |

*Count check: 51 historiographical + 13 chapter data/comparison + 16 appendix = 80 published tables. The Introduction is counted in the 51; the 13 data tables are counted in the chapters; the 16 appendix tables are 8 + 1 + 7.*

*Location note: the chapter locations are actual headings in the current files. The Appendix B, C, and D locations are planned section labels because those appendix files are still Stage 2 seeds; they will become actual headings when the tables are built.*

---

## 5. Chapter data and comparison tables (13)

These are the substantive tables inside narrative chapters. Each entry gives the exact location, the analytical job, the column specification, the draft rows, the required apparatus, and the verification cautions. The draft table block is reproduced so you can see the current cell content; it is not a verified table.

### 5.1 Ch. 8, Table 1 — `ch08-table-01`

**Owner and location.** `chapters/08-chapter-8.md`, §1.3, “The demographic imbalance and what it meant,” under “Draft Table 1”. **Display number:** Ch. 8, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare New France and the British colonies on the eve of the Seven Years’ War across population, settlement, land tenure, religion, economy, Indigenous relations, and military capacity. The table’s job is to make the asymmetry a problem both sides had to solve, not a guaranteed British victory.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Dimension** | The seven comparison categories. Use exactly these labels, in this order: Population; Settlement pattern; Land tenure; Religion; Economy; Indigenous relations; Military capacity. |
| **New France (about 1755)** | One to three sentences or a short numeric phrase per category. State whether a figure is a colonist count, a militia count, a regular-soldier count, or an estimate. Do not mix Acadian, Canadien, and Louisiana populations into one total without labeling the components. |
| **The British colonies (about 1755)** | The parallel content for the thirteen colonies. Name the population base (White and Black, free and enslaved) and the military definition (regulars, provincial troops, militia). Do not use “British North America” as a synonym for the thirteen colonies. |

**Row grain.** Seven body rows, one per dimension. No totals row; the categories are not additive.

**Draft values (verify every cell before publication).**

| Dimension | New France (about 1755) | The British colonies (about 1755) |
|---|---|---|
| **Population** | About 55,000 Canadiens, 10,000 Acadians, and about 4,000 Louisiana settlers; estimates range to 75,000–90,000 colonists | About 1.5 million people in the thirteen colonies, combining White and Black populations; roughly 1.17 million in 1750 |
| **Settlement pattern** | Concentrated along the St. Lawrence and a few posts; a vast interior held by trade and alliance | A dense Atlantic seaboard and growing piedmont, with expanding ports and cities |
| **Land tenure** | Seigneurial grants held of the crown, with habitants paying dues | Freehold, headright, charter, and proprietary tenure varying by colony |
| **Religion** | An established Catholic church with public authority in parishes, schools, and hospitals | Multiple Protestant establishments and a range of tolerated and dissenting faiths |
| **Economy** | Fur trade, missions, and provisions, oriented to the St. Lawrence and the interior | Staple agriculture, commerce, shipping, and a growing internal market |
| **Indigenous relations** | Alliance, gift diplomacy, and kinship in a Great Lakes “middle ground” | Treaties, land purchases, and the Covenant Chain, alongside settler expansion |
| **Military capacity** | A small regular force plus militia; peak of about 10,000 regulars and 15,000 militia in 1757 | About 46,500 regulars at peak strength in 1758, plus provincial troops raised by the colonies |

**Required caption.** Table 1. New France and the British colonies compared, about 1755.

**Source line (current draft; update the status when verified).** Drafted for this volume from the sources named in the combined notes; the population estimates are compiled totals and must be reconciled with Appendix B, Table 1. Status: `planned`; the New France and military figures require verification against the cited works and additional colonial records.[^ch08-check-table1][^ch08-pop-hs][^ch08-newfrance-wiki][^ch08-french-indian-wiki]

**Required alt text.** A seven-row table comparing New France and the British colonies around 1755 on population, settlement pattern, land tenure, religion, economy, Indigenous relations, and military capacity.

**Textual reference.** “Table 1 presents the comparison.”

**Cautions and limitations.** The population estimates are compiled totals, not a single census. The New France side combines about 55,000 Canadiens, 10,000 Acadians, and about 4,000 Louisiana settlers, with estimates ranging to 75,000–90,000 colonists; the British side is about 1.5 million in the thirteen colonies, roughly 1.17 million in 1750. Those are different geographies and dates. The military figures (about 10,000 regulars and 15,000 militia in 1757; about 46,500 British regulars at peak in 1758) are peak-strength figures, not cumulative service. Reconcile the population cells with App. B, Table 1 and state the observation year in the caption.

---

### 5.2 Ch. 8, Table 2 — `ch08-table-02`

**Owner and location.** `chapters/08-chapter-8.md`, §5.1, “The Peace of Paris and the reshuffling of empires,” under “Draft Table 2”. **Display number:** Ch. 8, Table 2. **Status:** drafted, unverified.

**Purpose.** Set out the 1763 settlement by instrument, distinguishing the public Treaty of Paris from the secret Treaty of Fontainebleau and separating European cessions from Native title. The table should show that the peace reassigned claims without settling who controlled the interior.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Territory or claim** | The named territory or claim. Use the eighteenth-century name and add the present-day region in parentheses where helpful. Do not use a modern state name as if it were the diplomatic unit. |
| **From** | The ceding or transferring power. For Native land, write “Not ceded by the Native nations,” not a European power. |
| **To** | The receiving power or status. For exchanged islands, write “Exchanged” or “Returned or retained,” not a single recipient. |
| **Instrument and date** | The treaty, proclamation, or instrument and its date. Distinguish Fontainebleau (November 3, 1762) from Paris (February 10, 1763) and the Royal Proclamation (October 7, 1763). |

**Row grain.** Six body rows: Canada and the interior east of the Mississippi; Louisiana west of the Mississippi; Florida; Caribbean conquests; fishing and island rights; the interior “Indian reserve.”

**Draft values (verify every cell before publication).**

| Territory or claim | From | To | Instrument and date |
|---|---|---|---|
| **Canada and the interior east of the Mississippi** | France | Great Britain | Treaty of Paris, February 10, 1763 |
| **Louisiana west of the Mississippi** | France | Spain | Treaty of Fontainebleau, November 3, 1762; acknowledged in the 1763 settlement |
| **Florida** | Spain | Great Britain | Treaty of Paris, February 10, 1763 |
| **Caribbean conquests** | Exchanged | Returned or retained | Treaty of Paris, February 10, 1763; Guadeloupe and Martinique returned to France |
| **Fishing and island rights** | Retained by France | Saint Pierre and Miquelon and fishing rights in the Gulf of St. Lawrence | Treaty of Paris, February 10, 1763 |
| **The interior “Indian reserve”** | Not ceded by the Native nations | Reserved to them under British sovereignty | Royal Proclamation, October 7, 1763 |

**Required caption.** Table 2. The 1763 territorial settlement in North America.

**Source line (current draft; update the status when verified).** Drafted for this volume from the Treaty of Paris, the Treaty of Fontainebleau, and the Royal Proclamation, as transcribed by the Avalon Project, with the territorial and treaty series to be reconciled with Appendix B, Table 3. Status: `planned`; the Fontainebleau instrument and the exact bounds require verification against authoritative editions and Appendix B.[^ch08-check-table2][^ch08-paris-avalon][^ch08-proc-avalon]

**Required alt text.** A six-row table listing the 1763 territorial settlement by territory, the ceding power, the receiving power, and the governing instrument and date.

**Textual reference.** “Table 2 lays out the settlement.”

**Cautions and limitations.** Do not attribute Native lands to any European power as if the nations had ceded them. The Fontainebleau instrument is secret and its exact bounds and acknowledgment require verification against authoritative editions. “Caribbean conquests” is an exchange, not a simple cession. The Royal Proclamation is a unilateral British instrument, not a Native cession. Reconcile the territorial series with App. B, Table 3.

---

### 5.3 Ch. 19, Table 1 — `ch19-table-01`

**Owner and location.** `chapters/19-chapter-19.md`, §2.1, “Table 1: selected fugitive cases, 1851–1854”. **Display number:** Ch. 19, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six well-documented fugitive cases to show how enforcement, local vigilance, and federal preparation produced different outcomes. The table makes the law’s costs visible and supports the chapter’s claim that the settlement of 1850 was unenforceable without coercion.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Case** | The named case or the person at its center. Use the form the chapter uses; for the Christiana Resistance, name the event rather than a single defendant. |
| **Date and place** | The date and city or county. If the legal proceedings ran over weeks, give the range and the place of the decisive hearing. |
| **Claimant** | The person or state claiming the fugitive. If the record does not identify the claimant, write “not identified in the consulted record,” not a guess. |
| **Forum and outcome** | The commissioner, court, or warrant; the result (rescued, remanded, acquitted, killed). Name the commissioner only when the record supports it. |

**Row grain.** Six body rows: Shadrach Minkins; Thomas Sims; Christiana Resistance; Jerry Rescue; Joshua Glover; Anthony Burns.

**Draft values (verify every cell before publication).**

| Case | Date and place | Claimant | Forum and outcome |
|---|---|---|---|
| **Shadrach Minkins** | February 15, 1851; Boston | Virginia claimant | Federal commissioner; rescued by a crowd |
| **Thomas Sims** | April 1851; Boston | James Potter of Georgia | Commissioner George Ticknor Curtis; remanded |
| **Christiana Resistance** | September 11, 1851; Lancaster County, Pennsylvania | Edward Gorsuch of Maryland | Federal warrant; resistance; Gorsuch killed; Castner Hanway acquitted of treason |
| **Jerry Rescue** | October 1, 1851; Syracuse, New York | Missouri claimant | Commissioner Joseph Sabine; rescued by a crowd |
| **Joshua Glover** | March 1854; Racine and Milwaukee, Wisconsin | Missouri claimant | Federal warrant; rescued by a Milwaukee crowd |
| **Anthony Burns** | May–June 1854; Boston | Charles F. Suttle of Virginia | Commissioner Edward G. Loring; remanded |

**Required caption.** Table 1. Selected fugitive cases under the Fugitive Slave Act of 1850, 1851–1854.

**Source line (current draft; update the status when verified).** Draft for this volume from the cited court, archive, and institutional records; full citations in the combined notes. Status: `planned`. Each row’s date, venue, claimed owner, and outcome must be verified against the direct record before publication; the Glover and Christiana entries presently rest on institutional summaries.[^ch19-check-tables][^ch19-ev-burns][^ch19-nps-sims][^ch19-glover][^ch19-christiana-society]

**Required alt text.** A table of six fugitive cases from 1851 to 1854, each row listing the accused person, the date and place, the claimed enslaver or claimant, the legal forum, and the outcome.

**Textual reference.** “Table 1 lists the cases that made the Fugitive Slave Act a national drama.”

**Cautions and limitations.** Each row’s date, venue, claimant, and outcome must be verified against the direct court or archive record. The Glover and Christiana entries presently rest on institutional summaries. Do not treat “rescued” or “remanded” as a verdict on the law’s legitimacy; the table records outcomes, not merits. Do not add a case merely because it is dramatic; the six are selected for documentation and contrast.

---

### 5.4 Ch. 19, Table 2 — `ch19-table-02`

**Owner and location.** `chapters/19-chapter-19.md`, §3.4, “Table 2: the election of 1856”. **Display number:** Ch. 19, Table 2. **Status:** drafted, unverified.

**Purpose.** Present the 1856 result to show the sectional realignment: a Democrat won the presidency while a new Republican Party carried most of the North. The table supports the chapter’s claim that the party system was reorganizing on sectional lines.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Candidate** | Full name as it appears on the ticket. Do not use a nickname alone. |
| **Party** | The ticket’s name: Democratic; Republican; Whig-American. If a state fusion ticket existed, note it below the table rather than inventing a national party. |
| **Popular votes** | Reported national popular votes. Use one compilation consistently; do not mix state and national totals. |
| **Share** | Popular-vote percentage, rounded to one decimal. State the denominator (total reported presidential popular votes). |
| **Electoral votes** | Electoral votes won. State the total electoral vote and the majority needed in a note. |

**Row grain.** Three body rows: James Buchanan; John C. Frémont; Millard Fillmore.

**Draft values (verify every cell before publication).**

| Candidate | Party | Popular votes | Share | Electoral votes |
|---|---|---|---:|---:|
| **James Buchanan** | Democratic | 1,836,072 | 45.3% | 174 |
| **John C. Frémont** | Republican | 1,342,345 | 33.1% | 114 |
| **Millard Fillmore** | Whig-American | 873,053 | 21.6% | 8 |

**Required caption.** Table 2. The presidential election of 1856: candidates, popular votes, and electoral votes.

**Source line (current draft; update the status when verified).** Drawn for this volume from the American Presidency Project’s 1856 state returns; full citation in the combined notes. Status: `planned`. Verify the state totals against the official returns and Appendix B, Table 2 before publication.[^ch19-election-1856][^ch19-check-tables]

**Required alt text.** A three-row table comparing Buchanan’s Democratic ticket, Frémont’s Republican ticket, and Fillmore’s Whig-American ticket, with popular votes, popular-vote shares, and electoral votes.

**Textual reference.** “Table 2 shows the 1856 result that confirmed the sectional realignment.”

**Cautions and limitations.** The returns are the American Presidency Project’s compiled state series; percentages are rounded; Buchanan won less than a majority. Verify the state totals against the official returns and App. B, Table 2 before publication. Do not infer individual voter motives from state totals. If a fourth ticket received votes, add a note; do not silently omit it. The draft alt text refers to “electoral-vote shares,” a column the table does not have; the corrected alt text above matches the five actual columns.

---

### 5.5 Ch. 20, Table 1 — `ch20-table-01`

**Owner and location.** `chapters/20-chapter-20.md`, §1.3, “Table 1: the election of 1860”. **Display number:** Ch. 20, Table 1. **Status:** drafted, unverified.

**Purpose.** Present the four-way 1860 result to show how Lincoln won a decisive electoral majority with well under half the popular vote. The table also makes the split electors and South Carolina’s legislative choice visible instead of hiding them in a national total.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Candidate** | Full name. For Lincoln, use “Abraham Lincoln”; for Douglas, “Stephen A. Douglas.” |
| **Ticket** | The ticket’s name: Republican; Northern Democratic; Southern Democratic; Constitutional Union. Do not label all four “Democratic” or “Republican” without the regional qualifier. |
| **Reported popular votes** | Reported national popular votes. Name the compilation in the source line. |
| **Share** | Popular-vote percentage, rounded to one decimal. State the denominator. |
| **Electoral votes** | Electoral votes won. Add table notes for New Jersey’s split electors and South Carolina’s legislative choice. |

**Row grain.** Four body rows: Abraham Lincoln; Stephen A. Douglas; John C. Breckinridge; John Bell.

**Draft values (verify every cell before publication).**

| Candidate | Ticket | Reported popular votes | Share | Electoral votes |
|---|---|---:|---:|---:|
| **Abraham Lincoln** | Republican | 1,867,198 | 39.8% | 180 |
| **Stephen A. Douglas** | Northern Democratic | 1,379,434 | 29.4% | 12 |
| **John C. Breckinridge** | Southern Democratic | 854,248 | 18.2% | 72 |
| **John Bell** | Constitutional Union | 591,658 | 12.6% | 39 |

**Required caption.** Table 1. The presidential election of 1860: candidates, reported popular votes, shares, and electoral votes.

**Source line (current draft; update the status when verified).** Drawn for this volume from the American Presidency Project’s 1860 state returns, cross-checked against the National Archives electoral-college result; full citations in the combined notes. Status: `planned`. Reported national totals vary among compilations and the popular-vote shares are rounded; verify against the official state returns and Appendix B, Table 2 before publication.[^ch20-app-election-1860][^ch20-archives-electoral-1860][^ch20-check-tables]

**Required alt text.** A four-row table comparing the Republican, Northern Democratic, Southern Democratic, and Constitutional Union tickets of 1860, each row listing the candidate, the ticket, reported popular votes, the popular-vote share, and the electoral votes won.

**Textual reference.** “Table 1 shows the four-way result that made Lincoln president without a single slave state.”

**Cautions and limitations.** Reported national totals vary: the American Presidency Project gives Lincoln 1,867,198; the AHA chronology gives 1,866,452. Shares are rounded. New Jersey split its electors, and South Carolina’s legislature chose electors. Do not present a single national total as settled or hide the split in a footnote. Verify against official state returns and App. B, Table 2.

---

### 5.6 Ch. 20, Table 2 — `ch20-table-02`

**Owner and location.** `chapters/20-chapter-20.md`, §5.1, “Table 2: resources at the war’s outset”. **Display number:** Ch. 20, Table 2. **Status:** drafted, unverified.

**Purpose.** Compare Union and Confederate resources at the war’s outset, with the states counted made explicit, to show the asymmetry without treating it as destiny. The table is also a warning against the loose “North–South” shorthand.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Resource, 1860–61** | The resource category. Use exactly: Total population; Enslaved people; Males of military age, 18–45; Share of manufacturing output; Share of railroad mileage; Share of banks. |
| **Union (loyal states)** | The figure for the states that remained loyal, defined in a note. State whether the count includes the border slave states and their enslaved populations. |
| **Confederacy (11 seceded states)** | The figure for the eleven seceded states, defined in a note. Do not use “the South” as a synonym. |
| **Definition and source** | The definition, observation year, denominator, and source for the row. This column is not optional; it is what makes the comparison honest. |

**Row grain.** Six body rows, one per resource category.

**Draft values (verify every cell before publication).**

| Resource, 1860–61 | Union (loyal states) | Confederacy (11 seceded states) | Definition and source |
|---|---|---|---|
| **Total population** | approximately 23 million | approximately 9 million | States counted as loyal or seceded; 1860 census base; NPS synthesis |
| **Enslaved people** | not separately stated here | approximately 3.5 million | Enslaved people within the Confederacy’s 9 million; 1860 census |
| **Males of military age, 18–45** | approximately 3.5 million | approximately 1 million | NPS synthesis; eligibility rules in prose |
| **Share of manufacturing output** | 90 percent from northern states | remainder | North–South regional measure, not identical to Union–Confederate |
| **Share of railroad mileage** | approximately 71 percent | approximately 29 percent | NPS synthesis; regional and dated |
| **Share of banks** | approximately 87 percent | approximately 13 percent | NPS synthesis; regional and dated |

**Required caption.** Table 2. Resources at the war’s outset: explicit Union and Confederate geography, 1860–61.

**Source line (current draft; update the status when verified).** Drawn for this volume from the National Park Service synthesis, the 1860 census, and the cited scholarship; full citations in the combined notes, with underlying series promised to Appendix B, Tables 1, 4, and 7. Status: `planned`. The columns must be defined by the states counted; the “North–South” regional percentages are not identical to the Union–Confederate state sets; no cell may be published without a stated observation year and denominator.[^ch20-nps-industry-economy][^ch20-census-1860][^ch20-check-tables]

**Required alt text.** A six-row table comparing Union and Confederate resources at the war’s outset, listing total population, enslaved people, males of military age, share of manufacturing output, share of railroad mileage, and share of banks, with a definition and source column.

**Textual reference.** “Table 2 compares the two sides’ resources at the war’s outset, with the states counted made explicit.”

**Cautions and limitations.** The National Park Service’s “North” and “South” are regional categories that do not correspond exactly to the Union and the Confederacy. The Union population included enslaved people in the loyal border states; the Confederacy’s nine million included about 3.5 million enslaved people and about four million free White women. No cell may be published without a stated observation year and denominator. Reconcile with App. B, Tables 1, 4, and 7. Do not compute a “resource ratio” from categories with different bases.

---

### 5.7 Ch. 22, Table 1 — `ch22-table-01`

**Owner and location.** `chapters/22-chapter-22.md`, §3.3, “The measure: the election of 1864”. **Display number:** Ch. 22, Table 1. **Status:** drafted, unverified.

**Purpose.** Distinguish the national popular vote from the Union soldier vote in 1864, and show Lincoln’s electoral mandate alongside the closeness of the popular contest. The table supports the chapter’s argument that the election gave Lincoln a mandate while revealing how close the political contest was.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Candidate (party)** | Candidate and party/ticket. Use “National Union” for Lincoln’s 1864 ticket and “Democratic” for McClellan. |
| **Electoral votes** | Electoral votes won. State the total in a note. |
| **Popular votes** | Reported national popular votes. Name the compilation; totals vary slightly. |
| **Share** | Popular-vote percentage, rounded to one decimal. State the denominator. |
| **Soldier vote** | The soldier-vote count and share, with the denominator. If a candidate’s soldier vote is not separated in the source, write “not separated in the consulted source” and explain; do not estimate it from the national total. |

**Row grain.** Three body rows: Abraham Lincoln (National Union); George B. McClellan (Democratic); Scattering.

**Draft values (verify every cell before publication).**

| Candidate (party) | Electoral votes | Popular votes | Share | Soldier vote |
|---|---|---|---|---|
| **Abraham Lincoln (National Union)** | 212 | 2,220,846 | 55.1% | 30,503 of 40,247 (75.8%) |
| **George B. McClellan (Democratic)** | 21 | 1,809,445 | 44.9% | Not separated in the consulted source; reconcile before publication |
| **Scattering** | 0 | — | — | 543 of 40,247 (1.3%) |

**Required caption.** Table 1. The election of 1864: national versus soldier vote.

**Source line (current draft; update the status when verified).** Drawn for this volume from the American Presidency Project’s compiled returns and the American Battlefield Trust’s account of the soldiers’ vote; full citations in the combined notes. Reported popular-vote totals vary slightly among compilations, the shares are rounded, and McClellan’s soldier-vote total is not given by the consulted account and must be reconciled before publication. The popular-vote series should be cross-checked against Appendix B, Table 2. Status: `planned`.[^ch22-app-1864][^ch22-battlefields-election][^ch22-check-tables]

**Required alt text.** A three-row table comparing the 1864 candidates by electoral votes, national popular votes and share, and the Union soldier vote, showing Lincoln’s 212 electoral votes and 55.1 percent against McClellan’s 21 electoral votes and 44.9 percent, with a soldier-vote column that is complete only for Lincoln.

**Textual reference.** “Table 1 distinguishes the national vote from the soldier vote.”

**Cautions and limitations.** Popular-vote totals vary slightly among compilations; shares are rounded. McClellan’s soldier-vote total is not given by the consulted account and must be reconciled before publication. The “Scattering” row is incomplete. Cross-check App. B, Table 2. Do not present the soldier vote as a representative sample of the army.

---

### 5.8 Ch. 22, Table 2 — `ch22-table-02`

**Owner and location.** `chapters/22-chapter-22.md`, §4.4, “The measure: the mortality estimates”. **Display number:** Ch. 22, Table 2. **Status:** drafted, unverified.

**Purpose.** Compare the conventional Civil War death count, Hacker’s census-based estimate, and the 2024 full-count estimate, with method, scope, and uncertainty. The table’s job is to show why responsible estimates differ, not to crown a new official number.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Estimate** | The estimate and its date/author. Put the number first, then the source label in parentheses. |
| **Method and data** | The method and the data it uses: mortality rates applied to a count; census sex-differential on a sample; full-count census with migration adjustment. |
| **What it counts** | The population and deaths counted: Union and Confederate military deaths; excess wartime deaths of military-age native-born White males; excess deaths including foreign-born and Black Union soldiers. |
| **Uncertainty and limits** | The range, sampling error, coverage gaps, and known biases. Do not reduce this to “approximate.” |

**Row grain.** Three body rows: 618,222 (conventional; Livermore, 1900); about 750,000 (Hacker, 2011); about 698,000 (Barceló and others, 2024).

**Draft values (verify every cell before publication).**

| Estimate | Method and data | What it counts | Uncertainty and limits |
|---|---|---|---|
| **618,222 (conventional; Livermore, 1900)** | Union Army mortality rates applied to a rough count of Confederate soldiers | Combined Union and Confederate military deaths | Widely treated as an undercount because Confederate records are incomplete |
| **About 750,000 (Hacker, 2011)** | Census sex-differential method on a 1% sample of the 1850–1880 censuses | Excess wartime deaths of military-age native-born white males, adjusted | Sampling error; range of roughly 650,000 to 850,000 |
| **About 698,000 (Barceló and others, 2024)** | Full-count census records with a migration-adjusted comparison | Excess deaths; about 496,000 native-born white males plus foreign-born and 36,000 Black Union soldiers | Bounds of roughly 647,000 to 749,000; frontier-state estimates unreliable |

**Required caption.** Table 2. Civil War mortality estimates: methods, scope, and uncertainty.

**Source line (current draft; update the status when verified).** Drawn for this volume from the *Proceedings of the National Academy of Sciences* study by Barceló, Jensen, Peisakhin, and Zhai (2024) and the works it cites; full citations in the combined notes. The estimates rest on different methods, populations, and geographies and are not interchangeable; the table should be cross-checked against Appendix B, Table 4. Status: `planned`.[^ch22-pnas-mortality][^ch22-check-tables]

**Required alt text.** A three-row table comparing the conventional 618,222 figure, Hacker’s roughly 750,000 figure, and the 2024 full-count estimate of about 698,000, each row stating the method and data, the population and deaths counted, and the uncertainty or range.

**Textual reference.** “Table 2 compares the conventional count, Hacker’s census-based estimate, and the 2024 full-count estimate.”

**Cautions and limitations.** The estimates rest on different methods, populations, and geographies and are not interchangeable. 618,222 is widely treated as an undercount because Confederate records are incomplete; Hacker’s range is roughly 650,000–850,000; the 2024 estimate’s bounds are roughly 647,000–749,000, with frontier-state estimates unreliable. Do not present any figure as a new official count. Cross-check App. B, Table 4.

---

### 5.9 Ch. 29, Table 1 — `ch29-table-01`

**Owner and location.** `chapters/29-chapter-29.md`, §4.3, “The election of 1912”. **Display number:** Ch. 29, Table 1. **Status:** drafted, unverified.

**Purpose.** Present the 1912 result with running mates, popular vote, share, and electoral votes, so readers can see Wilson’s decisive electoral margin alongside his 41.8 percent plurality. The table supports the chapter’s warning against treating the plurality as a mandate.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Candidate** | Candidate and party in parentheses. Use “Woodrow Wilson (Democratic),” “Theodore Roosevelt (Progressive),” “William Howard Taft (Republican),” “Eugene V. Debs (Socialist).” |
| **Running mate** | Full name. Do not omit a running mate because the ticket won no electors. |
| **Reported popular vote** | Reported national popular vote. Name the compilation. |
| **Share** | Popular-vote percentage, rounded to one decimal. State the denominator and note that shares do not sum to 100. |
| **Electoral votes** | Electoral votes won. Add a note for California’s split (11 Roosevelt, 2 Wilson). |

**Row grain.** Four body rows: Wilson; Roosevelt; Taft; Debs.

**Draft values (verify every cell before publication).**

| Candidate | Running mate | Reported popular vote | Share | Electoral votes |
|---|---|---:|---:|---:|
| **Woodrow Wilson (Democratic)** | Thomas R. Marshall | 6,294,327 | 41.8% | 435 |
| **Theodore Roosevelt (Progressive)** | Hiram Johnson | 4,120,207 | 27.4% | 88 |
| **William Howard Taft (Republican)** | Nicholas Butler | 3,486,343 | 23.2% | 8 |
| **Eugene V. Debs (Socialist)** | Emil Seidel | 900,370 | 6.0% | 0 |

**Required caption.** Table 1. The election of 1912: candidates, reported popular vote and share, and electoral votes.

**Source line (current draft; update the status when verified).** Drawn for this volume from the American Presidency Project’s state-by-state returns and the National Archives electoral tally, cross-checked against Teaching American History’s compilation; full citations in the combined notes. Reported shares are rounded to one decimal place and do not sum to 100 percent because of minor-party and write-in votes. California split its 13 electoral votes, 11 for Roosevelt and 2 for Wilson. Status: `planned`.[^ch29-app-1912][^ch29-archives-1912][^ch29-tah-1912][^ch29-check-table1]

**Required alt text.** A four-row table listing the 1912 presidential candidates Woodrow Wilson, Theodore Roosevelt, William Howard Taft, and Eugene V. Debs with their running mates, reported popular votes, popular-vote shares, and electoral votes, showing Wilson’s 435 electoral votes against Roosevelt’s 88, Taft’s 8, and Debs’s none.

**Textual reference.** “Table 1 gives each candidate’s running mate, reported popular vote, share, and electoral votes.”

**Cautions and limitations.** Shares are rounded to one decimal and do not sum to 100 because of minor-party and write-in votes. California split its 13 electoral votes. The combined Roosevelt–Taft vote is a majority; the table should make that visible without adding a “combined” row that double-counts. Verify against App. B, Table 2 and official state returns.

---

### 5.10 Ch. 30, Table 1 — `ch30-table-01`

**Owner and location.** `chapters/30-chapter-30.md`, §1.4, “Table 1 and Map 23: the instruments, 1901–1917”. **Display number:** Ch. 30, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare the instruments of U.S. control in the Caribbean and Central America, 1901–1917, to show that annexation was rare while leases, receiverships, occupations, and treaty concessions were common. The table carries the chapter’s argument about “empire without formal annexation.”

**Columns.**

| Column | Required content and rules |
|---|---|
| **Territory** | The territory or country. Use the period name and the present name where they differ. |
| **Instrument and date** | The treaty, amendment, intervention, or occupation and its date. If the arrangement ran over years, give the start date and the end date in parentheses. |
| **What the United States gained** | The specific right, base, revenue control, or occupation. Do not write “control” without saying what was controlled. |
| **Legal form** | Protectorate; receivership; occupation; treaty concession; lease; intervention. Use one of these labels, and explain mixed forms in a note. |

**Row grain.** Five body rows: Cuba; Dominican Republic; Nicaragua; Haiti; Panama.

**Draft values (verify every cell before publication).**

| Territory | Instrument and date | What the United States gained | Legal form |
|---|---|---|---|
| **Cuba** | Platt Amendment, 1901; permanent treaty, May 22, 1903; interventions 1906, 1912, 1917, 1920 | Right to intervene in Cuban affairs; lease for a naval base at Guantánamo Bay | Protectorate |
| **Dominican Republic** | Customs receivership, 1905; treaty, 1907; military government, 1916–1924 | Administration of customs revenues to pay foreign creditors; later direct military rule | Receivership, then occupation |
| **Nicaragua** | Marine intervention, 1912; Bryan–Chamorro Treaty, signed August 5, 1914 | Option to build an interoceanic canal; 99-year lease of the Corn Islands; right to a naval base on the Gulf of Fonseca | Intervention and treaty concession |
| **Haiti** | Marine occupation from July 1915; Haitian-American Treaty, 1915 | Control of Haitian finances and the gendarmerie; right to intervene | Occupation and treaty |
| **Panama** | Hay–Bunau-Varilla Treaty, November 18, 1903 | Canal zone, with the rights of a sovereign within it; guarantee of Panamanian independence; rights to naval and coaling stations | Treaty grant of zone |

**Required caption.** Table 1. Instruments of Caribbean control, 1901–1917: territory, instrument and date, what the United States gained, and the legal form of the arrangement.

**Source line (current draft; update the status when verified).** Drawn for this volume from the Platt Amendment transcript at the National Archives, the Department of State histories of the Dominican Republic and Haiti, the Bryan–Chamorro Treaty summary in *Foreign Relations of the United States*, and the Hay–Bunau-Varilla Treaty text at the Avalon Project; full citations in the combined notes. Dates are instrument or occupation dates, not endpoints; the Dominican occupation is shown to its 1924 end for clarity. Status: `planned`.[^ch30-platt-amendment][^ch30-state-dr][^ch30-state-haiti][^ch30-frus-bryan-chamorro][^ch30-hay-bunau-varilla][^ch30-check-table1]

**Required alt text.** A five-row table listing Cuba, the Dominican Republic, Nicaragua, Haiti, and Panama, with each territory’s instrument and date, what the United States gained, and the legal form of the arrangement, showing that annexation was rare and that leases, receiverships, and occupations were common.

**Textual reference.** “Table 1 gives each territory, its instrument and date, what the United States gained, and the legal form of the arrangement.”

**Cautions and limitations.** Dates are instrument or occupation dates, not endpoints; the Dominican occupation is shown to its 1924 end for clarity. Legal forms are not equivalent acquisitions. Do not color the whole basin as a single sovereignty or use “annexation” for a lease. Verify the Platt Amendment, the Bryan–Chamorro Treaty, the Hay–Bunau-Varilla Treaty, and the State Department histories.

---

### 5.11 Ch. 31, Table 1 — `ch31-table-01`

**Owner and location.** `chapters/31-chapter-31.md`, §2.4, “Map 24 and Table 1: the AEF in France and its cost”. **Display number:** Ch. 31, Table 1. **Status:** drafted, unverified.

**Purpose.** Present AEF personnel and casualty series for 1917–1919, with observation periods and service definitions, to show the scale of the force, its deaths by cause, and the cost of the Meuse-Argonne. The table supports the chapter’s claim that a nation that entered late and fought briefly still paid a price near the worst of any campaign.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Category** | The series label. Use exactly: Army, Navy, and Marine forces; Total deaths, all causes; Battle deaths; Non-combat deaths; Sick and wounded; AEF days in combat; Meuse-Argonne participants; Meuse-Argonne killed in action; Meuse-Argonne total casualties; Registered for the draft; Conscripted share of those who served. |
| **Figure** | The number or range. Include the unit (persons, days, percent) in the cell or the category label. |
| **Period** | The observation period, not the publication date. Use month/day/year where known. |
| **Definition and source** | The service definition, counting rule, and source. Each row states its own definition; do not assume Army, Navy, and Marine categories are comparable. |

**Row grain.** Eleven body rows, one per category.

**Draft values (verify every cell before publication).**

| Category | Figure | Period | Definition and source |
|---|---|---|---|
| **Army, Navy, and Marine forces** | 4.7 million | April 1, 1917–December 31, 1918 | Total serving: Army about 4.1 million, Navy about 600,000; Department of Defense official figures as reported by Byerly |
| **Total deaths, all causes** | 116,516 | April 1, 1917–December 31, 1918 | Army, Navy, and Marine deaths, including 479 soldiers and 675 at sea; Byerly |
| **Battle deaths** | 53,402 | April 1, 1917–December 31, 1918 | Deaths in combat or from wounds; Byerly |
| **Non-combat deaths** | 63,114 | April 1, 1917–December 31, 1918 | Disease and other causes, largely influenza; Byerly |
| **Sick and wounded** | about 320,000 | April 1, 1917–December 31, 1918 | AEF casualties treated; Byerly |
| **AEF days in combat** | about 200 | April 25–November 11, 1918 | Continuous combat period; Byerly |
| **Meuse-Argonne participants** | over 1 million | September 26–November 11, 1918 | Largest AEF operation; National Archives |
| **Meuse-Argonne killed in action** | over 26,000 | September 26–November 11, 1918 | National Archives |
| **Meuse-Argonne total casualties** | over 120,000 | September 26–November 11, 1918 | National Archives |
| **Registered for the draft** | about 24 million | 1917–18 | National Archives |
| **Conscripted share of those who served** | more than half | 1917–18 | National Archives |

**Required caption.** Table 1. AEF personnel and casualties, 1917–1919: the size of the force, its deaths by cause, its combat days, and the cost of the Meuse-Argonne.

**Source line (current draft; update the status when verified).** Drawn for this volume from the National Archives account of the Meuse-Argonne Offensive, the National Archives history of the selective-service lottery, and Carol R. Byerly’s “War Losses (USA)” in the 1914-1918-Online encyclopedia citing Department of Defense figures; full citations in the combined notes. Dates are observation periods, not endpoints. The service definitions differ among sources, and each row states its own. Status: `planned`.[^ch31-byerly-losses][^ch31-nara-meuse-argonne][^ch31-selective-service][^ch31-check-table1]

**Required alt text.** An eleven-row table giving the number of Americans who served, total deaths, battle and non-combat deaths, the sick and wounded, the AEF’s combat days, the Meuse-Argonne’s participants and losses, and the draft registrations, each with its observation period, definition, and source.

**Textual reference.** “Table 1 gives the personnel and casualty series, the observation period, the service definitions, and the source for each figure.”

**Cautions and limitations.** Dates are observation periods, not endpoints. Service definitions differ among sources. The 116,516 total includes 53,402 battle deaths and 63,114 non-combat deaths; the “sick and wounded” figure is about 320,000. Do not combine Army, Navy, and Marine categories without saying so. Cross-check App. B, Table 4. Do not add a “total casualties” row that double-counts the killed and wounded.

---

### 5.12 Ch. 31, Table 2 — `ch31-table-02`

**Owner and location.** `chapters/31-chapter-31.md`, §5.3, “Table 2: the Senate votes” (README register says §5.4 — see §9). **Display number:** Ch. 31, Table 2. **Status:** drafted, unverified.

**Purpose.** Present the three Senate roll calls on the Treaty of Versailles to show that the treaty failed not once but three times and that the two-thirds threshold, not a simple majority, was decisive. The table supports the chapter’s claim about the constitutional obstacle.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Date** | The roll-call date. If two votes occurred on the same day, repeat the date in both rows and distinguish them in “Question put.” |
| **Question put** | The version of the treaty or the procedural question: ratification with the fourteen Lodge reservations; ratification without amendments or reservations; ratification with revised reservations. |
| **Yes** | Yes votes. Use the official roll call, not a newspaper summary. |
| **No** | No votes. Use the official roll call. |
| **Result** | Rejected or adopted; the threshold; whether the vote was a majority but short of two-thirds. Do not write “failed” without saying which threshold failed. |

**Row grain.** Three body rows: November 19, 1919, with reservations; November 19, 1919, without amendments; March 19, 1920, with revised reservations.

**Draft values (verify every cell before publication).**

| Date | Question put | Yes | No | Result |
|---|---|---|---|---|
| **November 19, 1919** | Ratification with the fourteen Lodge reservations | 39 | 55 | Rejected; short of two-thirds |
| **November 19, 1919** | Ratification without amendments or reservations | 38 | 53 | Rejected; short of two-thirds |
| **March 19, 1920** | Ratification with reservations, revised | 49 | 35 | Rejected; a majority, short of two-thirds |

**Required caption.** Table 2. Senate votes on the Treaty of Versailles: the three roll calls of 1919–20 and their failure to reach the constitutional two-thirds.

**Source line (current draft; update the status when verified).** Drawn for this volume from the U.S. Capitol Visitor Center account of the November 1919 votes, the Department of State’s *Foreign Relations* narrative of the March 1920 vote, and the Senate’s own history of the treaty’s rejection; the direct roll calls must be supplied from the *Congressional Record* or the roll-call databases before publication. Status: `planned`.[^ch31-capitol-senate-votes][^ch31-state-gov-peace][^ch31-state-versailles][^ch31-voteview-1919][^ch31-check-table2]

**Required alt text.** A three-row table listing the November 19, 1919, vote with the Lodge reservations, the November 19, 1919, vote without amendments, and the March 19, 1920, vote with revised reservations, with each vote count and a note that all three fell short of two-thirds.

**Textual reference.** “Table 2 gives each vote’s date, the version of the treaty or the question put, the vote, the two-thirds threshold, and the source roll calls.”

**Cautions and limitations.** The published tallies (39–55, 38–53, 49–35) must be reconciled with the direct Congressional Record roll calls. The question of whether the second vote followed on the same day remains open. State the two-thirds threshold and attendance. Do not describe the 49–35 vote as a defeat for lack of a majority; it was a majority short of two-thirds.

---

### 5.13 Ch. 32, Table 1 — `ch32-table-01`

**Owner and location.** `chapters/32-chapter-32.md`, §4.2, “Table 1: the quota systems compared”. **Display number:** Ch. 32, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare the 1921, 1924 interim, and 1929 national-origins quota systems by basis, ceiling, exclusions, and enforcement, to show the shift from a labor-supply policy to a racial-composition policy. The table supports the chapter’s argument about the decade’s turn in immigration policy.

**Columns.**

| Column | Required content and rules |
|---|---|
| **System** | The statute or regime: Emergency Quota Act, 1921; Johnson–Reed Act, 1924 (interim formula); National origins system, 1929 onward; Enforcement institutions after 1924. |
| **Basis of quota** | The census base and percentage, or the national-origins computation. Distinguish the 1910 census base (1921) from the 1890 base (1924 interim) and the 1790 national-origins computation (1929). |
| **Annual ceiling** | The approximate annual ceiling and its unit. State whether the figure is the worldwide quota, the Eastern Hemisphere quota, or a sum of country quotas. |
| **Principal exclusions** | The main racial, nationality, and procedural exclusions. This is a summary, not a complete legal list; say so. |
| **Source** | The statute, quota schedule, or official history. Use a short source label in the cell and the full citation in the combined notes. |

**Row grain.** Four body rows: 1921 Act; 1924 interim formula; 1929 national-origins system; post-1924 enforcement institutions.

**Draft values (verify every cell before publication).**

| System | Basis of quota | Annual ceiling | Principal exclusions | Source |
|---|---|---|---|---|
| **Emergency Quota Act, 1921** | 3 percent of the foreign-born of each nationality in the 1910 census | about 350,000 | No quotas for the Western Hemisphere; 1917 literacy test and Asiatic Barred Zone continue | State Dept; NPS |
| **Johnson–Reed Act, 1924 (interim formula)** | 2 percent of the foreign-born of each nationality in the 1890 census | about 165,000 by the interim formula | Aliens ineligible for citizenship by race or nationality (most Asians); no Western Hemisphere quotas | State Dept |
| **National origins system, 1929 onward** | National origins of the whole population as of 1790, as computed under the 1924 act | about 150,000 | Same racial exclusions; Western Hemisphere still unrestricted | State Dept; USCIS |
| **Enforcement institutions after 1924** | Visa system; consular issuance; Border Patrol | not applicable | Illegal entry and smuggling enforcement; deportation | USCIS |

**Required caption.** Table 1. Immigration quota systems, 1921–1929: the shift from a 1910-based 3 percent quota to a 1924 interim formula and the 1929 national-origins quotas, with the exclusions each imposed.

**Source line (current draft; update the status when verified).** Drawn for this volume from the Department of State’s Office of the Historian account of the 1924 act, the National Park Service account of the closing of the open door, and the Department of Homeland Security’s USCIS agency history; the immigration series is cross-checked against Appendix B, Table 5. The interim 1924 quota and the final national-origins figures must be reconciled against the actual quota schedules before publication. Status: `planned`.[^ch32-state-immigration][^ch32-nps-immigration][^ch32-uscis-restriction][^ch32-check-table1]

**Required alt text.** A four-row table comparing the 1921 Emergency Quota Act, the 1924 interim formula, the 1929 national-origins quotas, and the post-1924 enforcement institutions, each with its basis, annual ceiling, principal exclusions, and source.

**Textual reference.** “Table 1 compares the 1921 and 1924 systems by basis, annual ceiling, and exclusion.”

**Cautions and limitations.** The 1924 interim formula and the 1929 national-origins figures must be reconciled against the actual quota schedules. The ceilings are approximate and changed within years. Western Hemisphere quotas were absent, but other bars applied. “Principal exclusions” is not a complete legal list. Cross-check App. B, Table 5. Do not present the 1924 interim ceiling as the final national-origins ceiling.

---

## 6. Historiographical comparison tables (51)

The Introduction and every numbered chapter have one “map of positions” table. These are the book’s most numerous tables and the easiest to fake: a row can look like a summary of a historian’s argument while resting on a review, a publisher’s description, or another scholar’s citation. The rule is simple: **a row exists only for a position the chapter actually discusses, and every claim in it must be checked against the named work.**

### 6.1 The standard five-column schema

All 51 tables use the same five columns. Two tables (the Introduction and Chapter 1) head the second column “Historians and works”; the other 49 head it “Voices, historians, and works.” Do not change the header without changing the register.

| Column | Required content | Rules |
|---|---|---|
| **Position** | A short label for the interpretive position, in bold. | One to four words. Do not use a historian’s name as the label unless the position is genuinely eponymous. Do not call every row a “school” if it is a single argument. |
| **Voices, historians, and works** | The named people and works that carry the position, with dates. | Include primary voices where the debate includes them (for example, Las Casas in Ch. 2, Franklin in Ch. 7, Haudenosaunee accounts in Ch. 3). Use italics for books and quotation marks for articles, speeches, and short documents. Do not list a work you have not identified; do not list a review as the work. |
| **Core claim** | The position’s strongest one-sentence claim. | 15–30 words. State the claim as its proponents would state it, not as a caricature. No “they believed” without evidence. |
| **Strongest contribution** | What the position explains that its rivals do not. | One sentence. This is not faint praise and not a summary of the book’s topic; it is the analytical gain. |
| **Limitation** | The strongest criticism of the position. | One sentence. Distinguish an empirical error, a scope limit, and a conceptual blind spot. Do not knock down a straw man; do not make the limitation a moral verdict. |

**Row order.** Use the order in the draft unless the chapter’s debate has a clear chronological or logical sequence. If you reorder, update the section introduction and the textual reference. **Row count.** Three to nine. Do not add a token opposing view to fill a shape; do not delete a position the chapter actually argues against.

**No “winner” column.** The chapter prose makes the judgment. The table’s job is to make the positions comparable, not to score them.

**Note markers in the draft blocks.** Several draft tables carry `[^key]` markers inside cells. That is a drafting convenience, not the final format. Move each marker to the source line or to a table note keyed to the row before publication. The source line may carry a cluster of note keys; the cells should carry the argument.

### 6.2 The tables

#### Introduction, Table 1 — `intro-table-01`

**Owner and location.** `chapters/00-introduction.md`, §6.5 Table 1. **Display number:** Introduction, Table 1. **Status:** drafted, unverified.

**Purpose.** Make the book’s method visible: five schools have asked different questions of the American past, and the Introduction’s synthesis borrows from several without adopting any one as the answer. The table is a map of those choices for readers, not a ranking.

**Columns.** Position; Historians and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Historians and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Progressive political economy** | Frederick Jackson Turner, “The Significance of the Frontier in American History” (1893); Charles A. Beard, *An Economic Interpretation of the Constitution of the United States* (1913) | American democracy and the Constitution were shaped by westward expansion and conflicts over economic interest. | Put land, class, and power at the center; made conflict historical. | Treated the frontier as empty and inevitable; reduced politics to interest. |
| **Consensus/liberal** | Richard Hofstadter, *The American Political Tradition* (1948); critique of the Progressive historians in *The Progressive Historians* (1968) | American politics has rested on a shared liberal framework; conflict occurs within narrow bounds. | Explained stability and the durability of institutions. | Underestimated slavery, dispossession, and coercion; treated a national consensus as universal. |
| **Conflict/social history** | Eric Foner, *Reconstruction* (1988); Jacquelyn Dowd Hall, “The Long Civil Rights Movement and the Political Uses of the Past” (2005) | History from below; race, labor, and grassroots movements drive change; emancipation and civil rights are unfinished. | Restored agency, violence, and the long arc of struggle. | Fragmented the national story; the state and political economy sometimes disappeared. |
| **Sovereignty, race, gender, environment** | Roxanne Dunbar-Ortiz, *An Indigenous Peoples’ History of the United States* (2014); Richard White, *The Middle Ground* (1991); William Cronon, *Nature’s Metropolis* (1991) | Conquest, Indigenous political orders, gender, and ecology are constitutive, not peripheral. | Reframed the nation as a settler-colonial and ecological project. | Synthesis can flatten regional variation; “settler colonialism” can become a single explanatory key. |
| **Transnational/critical political economy** | New History of Capitalism (Sven Beckert, *Empire of Cotton*; Edward Baptist, *The Half Has Never Been Told*); critique by Alan L. Olmstead and Paul W. Rhode (2018) | Slavery and cotton were central to industrial capitalism; the economy was built through global flows of capital, labor, and violence. | Connected domestic inequality to global markets and coerced labor. | Definitional and quantitative disputes; can reduce slavery to a factor of production. |

**Required caption.** Table 1. Schools, questions, and historical evidence.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; each row requires verification against the cited work before publication.

**Required alt text.** A five-row table comparing Progressive political economy, consensus/liberal, conflict/social history, sovereignty/race/gender/environment, and transnational/critical political economy approaches to U.S. history. Each row lists representative historians and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares five positions that have shaped the history of the United States. The rows are tools for comparison, not teams to join.”

**Cautions and limitations.** The rows compress whole bodies of work into a few sentences. Beard’s economic interpretation, Hofstadter’s consensus argument, Foner’s Reconstruction synthesis, Dunbar-Ortiz’s Indigenous history, and the New History of Capitalism are not interchangeable with the labels. Verify each claim against the named work and its critics. The “limitation” column must state the strongest criticism, not a straw man. The Introduction’s table is the one place where a school may be represented by a programmatic work rather than the author’s whole corpus; say so in the source line.

---

#### Ch. 1, Table 1 — `ch01-table-01`

**Owner and location.** `chapters/01-chapter-1.md`, §6.4 The map of positions. **Display number:** Ch. 1, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare three ways of interpreting the precontact continent: a humanized landscape, an Ecological Indian critique, and regional empirical caution. The table should let readers see why the same evidence supports different emphases on management, conservation, and local contingency.

**Columns.** Position; Historians and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Historians and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Humanized landscape** | William M. Denevan, “The Pristine Myth” (1992); Charles C. Mann, *1491* (2005) | Indigenous peoples modified environments across the hemisphere; the “pristine” continent is largely a post-contact illusion. | Reframed the continent as inhabited, managed, and historically dynamic; connected demography, land use, and ecology. | Continental synthesis can flatten regional variation; population estimates are contested; Mann’s account is journalistic, and Denevan himself criticized its overstatements. |
| **Ecological Indian critique** | Shepard Krech III, *The Ecological Indian* (1999); critique by Adrian Tanner (2001) | Indigenous peoples were not uniformly conservationist; their environmental behavior varied and sometimes wasted or depleted resources. | Tested a romantic stereotype against empirical cases; insisted on historical context and cultural diversity. | Can treat a stereotype as a single testable claim; judges behavior by Western conservation premises; case selection and evidence are disputed. |
| **Regional empirical caution** | Bradley T. Lepper on Serpent Mound (2020); James A. Tainter on Cahokia (2019); Todd Surovell and colleagues on Monte Verde (2026) | Dates, causes, and site histories are local and contested; grand narratives often outrun stratigraphy and chronology. | Demands precise dating, explicit methods, and falsifiable claims; corrects overreach. | Can fragment the continental story; technical disputes may obscure lived experience; a caution is not a full interpretation. |

**Required caption.** Table 1. Landscape management and ecological interpretation.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; each row requires verification against the cited work before publication.[^ch01-check-table]

**Required alt text.** A three-row table comparing the humanized-landscape position, the Ecological Indian critique, and regional empirical caution. Each row lists representative historians and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares three positions that organize the debate over landscape management and ecological interpretation.”

**Cautions and limitations.** Denevan criticized Mann’s overstatement; Krech is a corrective to a stereotype, not a denial of Indigenous management; Lepper, Tainter, and Surovell are site-specific. Do not turn any row into a continental law. Mann’s book is a journalistic synthesis, not a primary authority. The “regional empirical caution” row is a method, not a full interpretation; do not present it as the chapter’s winner.

---

#### Ch. 2, Table 1 — `ch02-table-01`

**Owner and location.** `chapters/02-chapter-2.md`, §6.4 The map of positions. **Display number:** Ch. 2, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four explanations of the demographic catastrophe: virgin-soil disease, syndemic and colonial conditions, conquest and coercion, and a regional disease-centered synthesis. The table’s job is to show that the disagreement is about mechanism and weight, not whether disease mattered.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Virgin-soil exchange** | Alfred W. Crosby, *The Columbian Exchange* (1972) and “Virgin Soil Epidemics” (1976) | Old World pathogens struck populations with no prior exposure, and the resulting mortality was catastrophic. | Explained the speed and scale of the catastrophe and connected disease to the wider biological exchange. | The “virgin soil” label can become a monocausal “no immunity” slogan; Crosby himself stressed malnutrition and social chaos, and regional variation complicates the model. |
| **Syndemic and colonial critique** | David S. Jones, “Virgin Soils Revisited” (2003); Suzanne Austin Alchon, *A Pest in the Land* (2003); Paul Kelton, *Epidemics and Enslavement* (2007) | Mortality arose from the interaction of novel pathogens with warfare, forced labor, hunger, displacement, and the collapse of care. | Explains why the same pathogen produced different outcomes and why some populations failed to recover. | The relative weight of biological and social factors is difficult to quantify; the approach can understate the real immunological vulnerability of isolated populations. |
| **Conquest and coercion** | Bartolomé de las Casas, *A Short Account* (1552); Andrés Reséndez, *The Other Slavery* (2016) | Violence, enslavement, and forced labor were central to the catastrophe, not incidental to it. | Restores Indigenous enslavement and coercion to the center of the story and corrects a purely biological account. | Can make disease seem secondary when it was demonstrably lethal; the sources for Indigenous slavery are uneven, and the numbers are contested. |
| **Regional and disease-centered synthesis** | Linda A. Newson, “The Demographic Collapse of Native Peoples of the Americas” (1993); Noble David Cook, *Born to Die* (1998) | Depopulation and recovery varied by region, ecology, and colonial policy; epidemic disease was a principal agent, but its effects were shaped by local conditions. | Demands precise denominators, regional comparison, and attention to recovery as well as collapse. | Technical and fragmentary; the sources do not support a single hemispheric figure, and some regional estimates remain speculative. |

**Required caption.** Table 1. Exchange, disease, coercion, and demographic change.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; each row requires verification against the cited work before publication.[^ch02-check-table]

**Required alt text.** A four-row table comparing virgin-soil exchange, syndemic and colonial critique, conquest and coercion, and regional and disease-centered synthesis. Each row lists representative voices, historians, and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares four positions that organize the debate over exchange, disease, coercion, and demographic change.”

**Cautions and limitations.** Crosby stressed malnutrition and social chaos, not a simple “no immunity” slogan; Jones, Alchon, and Kelton emphasize interaction and coercion; Cook and Newson insist on regional variation. Do not present a single hemispheric death percentage as settled. The “conquest and coercion” row must not make disease seem incidental; the “virgin-soil” row must not make coercion seem incidental.

---

#### Ch. 3, Table 1 — `ch03-table-01`

**Owner and location.** `chapters/03-chapter-3.md`, §6.4 The map of positions. **Display number:** Ch. 3, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four frameworks for Indigenous agency and the contact period: the middle ground, Indigenous-centered history, Indigenous power, and sovereignty/living treaty. The table should clarify what each framework can explain and where its evidence and geography limit it.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Middle ground** | Richard White, *The Middle Ground* (1991) and “Creative Misunderstandings and New Understandings” (2006) | In conditions of rough balance and mutual need, peoples built a workable world through creative misunderstanding and mediation rather than through conquest alone. | Explains accommodation, alliance, and the making of new cultural forms without denying violence. | The durable “space” fit the Great Lakes and the French alliance; it did not arise everywhere, and it can understate English settler expansion, which sought land rather than mediation. |
| **Indigenous-centered history** | Daniel K. Richter, *Facing East from Indian Country* (2001); James H. Merrell, *The Indians’ New World* (1989) | Early America should be seen from Native ground, with Native people as the subjects of the story, not the objects of European expansion. | Restores Native perspectives, choices, and continuities and reframes colonization as something Native people experienced and shaped. | The written record is largely European, so the method must infer Native views from mediated sources; it can be read as underplaying epidemic and demographic catastrophe. |
| **Indigenous power** | Pekka Hämäläinen, *The Comanche Empire* (2008) and *Lakota America* (2019) | Native nations could build empires and dominate regions, controlling trade, diplomacy, and violence on their own terms. | Shows Native power and expansion, not only decline, and treats Native polities as strategic actors. | Its cases are later and Western; it does not describe the eastern woodlands of this chapter, and “empire” as a model is contested. |
| **Sovereignty and living treaty** | Haudenosaunee, Wendat, and Caddo nation accounts; Smithsonian NMAI, *Haudenosaunee Guide for Educators* | Native nations hold their own law, government, and treaty relationships, which remain living and binding. | Presents Native political institutions and treaty claims in Native terms and as continuous into the present. | It is a claim of sovereignty and memory, not a neutral chronicle; scholars must distinguish the tradition’s authority from a documentary date. |

**Required caption.** Table 1. Indigenous agency and the contact framework.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works and nation sources named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; the Richter, Merrell, Hämäläinen, and White book entries were consulted through reviews, samples, or the 2006 article rather than read in full, and each row requires verification against the cited work before publication.[^ch03-check-table][^ch03-check-sources]

**Required alt text.** A four-row table comparing the middle ground, Indigenous-centered history, Indigenous power, and sovereignty and living treaty. Each row lists representative voices, historians, and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares four positions that organize the debate over Indigenous agency and the framework of contact.”

**Cautions and limitations.** White’s middle ground is regionally bounded; Hämäläinen’s cases are later and western; Richter and Merrell work from mediated European records; the sovereignty row rests on nation accounts and memory, not a documentary date. Distinguish a tradition’s authority from a documentary claim. Do not use “Indigenous agency” as a slogan that erases the catastrophic loss of life.

---

#### Ch. 4, Table 1 — `ch04-table-01`

**Owner and location.** `chapters/04-chapter-4.md`, §6.4 The map of positions. **Display number:** Ch. 4, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of colonial origins: Puritan intellectual history, commercial and economic interpretation, freedom and slavery in Virginia, and social/legal revisionism. The table should show how religion, profit, labor, and law each become the center of a different account.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Puritan intellectual history** | Perry Miller, *The New England Mind: The Seventeenth Century* (1939) and *Errand into the Wilderness* (1956) | The puritans carried a coherent religious worldview, and ideas — covenant, conversion, declension — were the mainspring of New England’s history. | Takes puritan thought seriously as a system of ideas and founded the intellectual history of early America. | Describes mainly the clergy and church members, and can underplay the unconverted majority, women, Native people, the enslaved, and the economy. |
| **Commercial and economic interpretation** | Virginia Company records and the tobacco trade; Bernard Bailyn, *The New England Merchants in the Seventeenth Century* (1955) | The colonies were commercial ventures; trade, land, credit, and labor demand, not doctrine alone, drove settlement and expansion. | Explains Virginia’s tobacco economy, the headright system, and New England’s fishing and trade, and connects American colonies to Atlantic markets. | Can reduce religious commitment to disguised economic interest, and treats the two colonies through one economic lens. |
| **Freedom and slavery in Virginia** | Edmund S. Morgan, *American Slavery, American Freedom: The Ordeal of Colonial Virginia* (1975) and “Slavery and Freedom: The American Paradox” (1972) | Virginia’s White liberty was built alongside and on the coercion of first servants and then enslaved Africans; freedom and slavery developed together. | Links labor, race, and freedom and gives the Chesapeake’s social order a single explanatory frame. | A Virginia-centered thesis; it understates New England, depends on a contested chronology of racial slavery, and is questioned for its account of elite concessions. |
| **Social and legal revisionism** | New England town studies and critics of Miller; Kathleen M. Brown, *Good Wives, Nasty Wenches, and Anxious Patriarchs* (1996) | Colonial societies were divided by class, gender, and race; law and social practice, not one “mind” or market, made their orders. | Restores conflict, gender, and the legal making of racial and gendered hierarchy. | Fragmented and often local; it can lose the broad comparison among colonies that this chapter needs. |

**Required caption.** Table 1. Religion, commerce, freedom, and colonial labor.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; the Miller, Bailyn, and Brown works and the town studies were not read in full for this outline and each row requires verification against the cited work before publication.[^ch04-check-table][^ch04-check-sources]

**Required alt text.** A four-row table comparing puritan intellectual history, commercial and economic interpretation, freedom and slavery in Virginia, and social and legal revisionism. Each row lists representative voices and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares four positions that organize the debate over religion, commerce, freedom, and colonial labor.”

**Cautions and limitations.** Miller wrote mainly about clergy and church members; Bailyn’s merchants are not the whole colonial economy; Morgan’s thesis is Virginia-centered and depends on a contested chronology; Brown and the town studies restore gender and conflict but can fragment the comparison. Do not reduce belief to interest or interest to belief. The “commercial” row is not a claim that every colonist was a merchant.

---

#### Ch. 5, Table 1 — `ch05-table-01`

**Owner and location.** `chapters/05-chapter-5.md`, §6.4 The map of positions. **Display number:** Ch. 5, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four explanations of how racial slavery took shape: class and deliberate choice, culture and the “unthinking decision,” gender and law, and gradualist/legal skepticism. The table should make the chronology and the causal weight of law, labor, and culture visible.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Class and deliberate choice** | Edmund S. Morgan, *American Slavery, American Freedom: The Ordeal of Colonial Virginia* (1975) | After Bacon’s Rebellion, Virginia’s elite chose racial slavery to divide poor Whites from Africans and to secure a permanent labor force. | Connects labor, race, and White liberty, and gives the turn to slavery a political motive grounded in a documented crisis. | A Virginia-centered and largely economic-political thesis; the chronology of the servant-to-slave shift is contested, and it underplays the Caribbean and gender. |
| **Culture and the “unthinking decision”** | Winthrop D. Jordan, *White Over Black: American Attitudes toward the Negro, 1550–1812* (1968) | English attitudes toward Africans and Blackness were deep and prior; enslavement was an “unthinking decision” shaped by culture, not a single deliberate plan. | Takes the cultural and psychological roots of racial ideology seriously and grounds them in early Atlantic sources. | Critics argue it understates law, labor demand, and the deliberate statutory construction of hereditary status. |
| **Gender, law, and patriarchy** | Kathleen M. Brown, *Good Wives, Nasty Wenches, and Anxious Patriarchs: Gender, Race, and Power in Colonial Virginia* (1996) | Racial slavery cannot be understood without gender; the labor and reproductive roles of women, and the laws governing them, made race and slavery together. | Explains why statutes such as the 1662 maternal-status act focused on mothers, and restores women to the center of the story. | A Virginia study; it addresses gender more fully than the Caribbean or the Middle Colonies, and its framework is less economic. |
| **Gradualist and legal-skeptical** | Oscar and Mary F. Handlin, “Origins of the Southern Labor System,” *William and Mary Quarterly* 7 (1950); Warren M. Billings, “The Cases of Fernando and Elizabeth Key,” *WMQ* 30 (1973) | Racial slavery emerged gradually from the decay of servitude; there was no single deliberate turn, and status cases such as Elizabeth Key’s show it was still contested into the 1650s–60s. | Forces attention to the blurry line between servant and slave and to the case-by-case making of status. | Its chronology has been largely rejected; it can understate the role of race and the deliberateness of later statutes. |

**Required caption.** Table 1. Origins of racial slavery.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Morgan, Jordan, and Brown were consulted through reference summaries, publisher descriptions, and reviews, and the Handlin, Billings, and related works were not read for this outline. Each row requires verification against the cited work before publication.[^ch05-check-table][^ch05-check-sources]

**Required alt text.** A four-row table comparing class-and-deliberate-choice, culture-and-unthinking-decision, gender-and-law, and gradualist interpretations of the origins of racial slavery. Each row lists representative historians and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares four positions that organize the debate over the origins of racial slavery.”

**Cautions and limitations.** Morgan’s post-Bacon’s Rebellion chronology is contested; Jordan’s “unthinking decision” has been criticized for understating law and labor; Brown is a Virginia study; the Handlins’ gradualist chronology has been largely rejected, but their attention to the servant–slave boundary remains useful. Do not present 1662 as a single origin point. The “gradualist” row is not a denial that racial slavery existed.

---

#### Ch. 6, Table 1 — `ch06-table-01`

**Owner and location.** `chapters/06-chapter-6.md`, §6.4 The map of positions. **Display number:** Ch. 6, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of war, alliance, and the imperial turn: the middle ground, its limits, language and identity, and Native enslavement as a system. The table should connect Indigenous diplomacy, colonial violence, and the making of empire.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Accommodation and the middle ground** | Richard White, *The Middle Ground: Indians, Empires, and Republics in the Great Lakes Region, 1650–1815* (1991) | Europeans and Indians built a shared world of meaning and exchange in the Great Lakes; accommodation, not simple conquest, organized the encounter until the nineteenth century. | Restored Indigenous agency and showed that colonial relations were negotiated and mutually intelligible rather than unilateral. | The model was built for one region and one period; extending it to New England, the Chesapeake, or the Southwest flattens places where power ran differently. |
| **The limits of the middle ground** | Andrew Lipman, “No More Middle Grounds?” *Reviews in American History* 44 (2016); Heidi Bohaker, Brett Rushforth, and Robert Morrissey on the Great Lakes | The middle ground was place-specific and did not name the whole of European–Indigenous relations; “middle grounds” are now hard to find, and the term has been overextended. | Forces attention to where accommodation failed and to the regions where Native and European worlds pulled apart. | A critical and largely historiographical position; it says less about how to narrate the places where accommodation did occur. |
| **Language, identity, and the meaning of war** | Jill Lepore, *The Name of War: King Philip’s War and the Origins of American Identity* (1998) | The English fought Metacom’s War partly to secure their own identity; the war’s meanings were made in the colonists’ language, and the survivors’ accounts reveal as much about the English as about the fighting. | Reads a one-sided archive against itself and treats the language of war as evidence, not decoration. | A New England study centered on English sources; it must be paired with work on Native and Spanish archives to cover the chapter’s full scope. |
| **Native enslavement as a system** | Margaret Ellen Newell, *Brethren by Nature* (2015); Linford D. Fisher, “‘Why shall wee have peace to bee made slaves’” (2017) | Native enslavement was systematic, entwined with African slavery, and central to colonial growth; ambiguity in law let servitude harden into heritable slavery. | Documents the scale and machinery of Native slavery and reads slavery as an instrument of war. | Newell’s footnoting is uneven at points, and Fisher’s figures are estimates; the totals require care. |

**Required caption.** Table 1. War, alliance, and the imperial turn.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; White and Lepore were consulted through a publisher description and a publisher-authorized excerpt, and Newell and Fisher through a published review, a university news account, and a journal abstract, not read in full. Each row requires verification against the cited work before publication.[^ch06-check-table][^ch06-check-sources]

**Required alt text.** A four-row table comparing accommodation-and-the-middle-ground, the-limits-of-the-middle-ground, language-and-identity, and Native-enslavement-as-a-system interpretations of the wars and the imperial turn. Each row lists representative historians and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares four positions that organize the debate over the wars and the imperial turn.”

**Cautions and limitations.** White’s model was built for the Great Lakes; Lipman and others question its extension; Lepore reads English sources and must be paired with Native and Spanish archives; Newell’s footnoting is uneven and Fisher’s figures are estimates. Do not let “middle ground” become a synonym for all contact. The Native-enslavement row is not a minor theme; it is a system with its own law and economy.

---

#### Ch. 7, Table 1 — `ch07-table-01`

**Owner and location.** `chapters/07-chapter-7.md`, §7.4 The map of positions. **Display number:** Ch. 7, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare five positions on colonial society: deference, class formation, revival as transformation, revival as invention or conservatism, and print/Enlightenment public. The table should show how historians disagree about how much ordinary people challenged authority before the Revolution.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Deference and the provincial order** | Richard L. Bushman, *King and People in Provincial Massachusetts* (1985); Charles S. Sydnor, *Gentlemen Freeholders* (1952) | Colonial politics ran on deference: ordinary people looked to their social betters for leadership, and monarchy supplied a whole culture of authority. | Explains how political and religious authority actually worked in provincial society, and takes the period’s own idioms seriously. | Written largely from the top down; it can understate conflict from below and the pressure that migration and revival put on the norm. |
| **Class formation and popular politics** | Gary B. Nash, *The Urban Crucible* (1979); Rhys Isaac, *The Transformation of Virginia, 1740–1790* (1982) | Seaport and backcountry society became more stratified, and the laboring classes developed a political consciousness before the Revolution. | Restores inequality and conflict to the center of colonial history and connects social change to the coming Revolution. | It risks reading later class politics back into an earlier century and leans on records that over-represent the towns. |
| **Revival as transformation** | Harry S. Stout, *The New England Soul* (1986); Alan Heimert, *Religion and the American Mind* (1966) | The awakenings transformed and democratized communication and faith, helping to prepare a new popular politics. | Takes religion seriously as a public and political force rather than a private enthusiasm. | It can overstate the radical effect of revivals that also divided and disciplined their converts. |
| **Revival as invention or conservatism** | Jon Butler, “Enthusiasm Described and Decried: The Great Awakening as Interpretive Fiction,” *Journal of American History* 69 (1982–83); Christine Leigh Heyrman, *Commerce and Culture* (1984); Frank Lambert, *Inventing the “Great Awakening”* (1999) | The “Great Awakening” was a category historians and revivalists created; the revivals were less coordinated and more conservative than the label implies. | Forces precision about what was new and cautions against treating a retrospective label as an event. | It can understate the real, connected revivalism that contemporaries did experience and report. |
| **Print, Enlightenment, and the public** | Benjamin Franklin, the *Pennsylvania Gazette* and *Poor Richard* (1729–1758); Michael Warner, *The Letters of the Republic* (1990) | A print public and a pragmatic Enlightenment grew in the colonies, carried by printers, newspapers, and voluntary projects. | Shows how ideas and news circulated across colonies and how print made a shared audience. | The public it describes was small, male, propertied, and entangled with slavery and commerce. |

**Required caption.** Table 1. Deference, class, revival, and the colonial Enlightenment.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Bushman and Nash were consulted through publisher descriptions, and Butler, Heyrman, Stout, Heimert, Lambert, Isaac, and Warner through an institutional synthesis or discovery, not read in full. Each row requires verification against the cited work before publication.[^ch07-check-table][^ch07-check-sources]

**Required alt text.** A five-row table comparing deference-and-the-provincial-order, class-formation-and-popular-politics, revival-as-transformation, revival-as-invention-or-conservatism, and print-Enlightenment-and-the-public interpretations of colonial society. Each row lists representative historians and works, the position’s core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares five positions that organize the debate over colonial society.”

**Cautions and limitations.** Bushman and Sydnor write from the top down; Nash and Isaac can read later class politics backward; Stout and Heimert may overstate revival’s radical effect; Butler calls the “Great Awakening” an interpretive fiction; the print public was small, male, propertied, and entangled with slavery. Do not let either the elite or the crowd stand in for everyone.

---

#### Ch. 8, Table 3 — `ch08-table-03`

**Owner and location.** `chapters/08-chapter-8.md`, §6.4 The map of positions. **Display number:** Ch. 8, Table 3. **Status:** drafted, unverified.

**Purpose.** Compare four positions on the Seven Years’ War: imperial contingency, the middle ground and Indigenous agency, imperial/fiscal interpretation, and the war as a global/Atlantic event. The table should show how the same war becomes a different event depending on the frame.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Imperial-war contingency** | Fred Anderson, *Crucible of War* (2000) | The Seven Years’ War decisively shaped American history, and its consequences, including the road to Revolution, were unintended and contingent. | Restores the war to the center of early American history and refuses to read independence back into it. | Its imperial focus can still make the Revolution the destination and underplay Native and colonial worlds on their own terms. |
| **The middle ground and Indigenous agency** | Richard White, *The Middle Ground* (1991); Colin Calloway, *The Scratch of a Pen* (2006) | In the Great Lakes and interior, Native nations and empires accommodated each other, and the nations shaped the war and the 1763 settlement as independent actors. | Puts Native decisions at the center and explains how a small French colony held a large interior. | The middle-ground model is bounded to a region and period and can understate violence and coercion. |
| **Imperial and fiscal interpretation** | The imperial school of British colonial history and the postwar reform narrative; secondary syntheses of the debt crisis | The war’s cost created the fiscal problem that drove imperial reform and colonial resistance, making the war the hinge of the imperial crisis. | Connects the war directly to the politics of the 1760s and supplies the evidence of debt and reform. | Can reduce a global and Indigenous conflict to a budget problem and assume the Revolution followed. |
| **The war as a global and Atlantic event** | Recent global histories of the Seven Years’ War; the imperial historians of the British Empire | The American fighting was one theater of a world war whose peace was negotiated across Europe, the Caribbean, and India. | Frames the settlement as a global bargain and explains Britain’s choices about which conquests to keep. | Can let the global frame overshadow the continental and Indigenous histories that this chapter centers. |

**Required caption.** Table 3. Imperial victory and the contingency of independence.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Anderson and Calloway were consulted through a magazine appreciation, a publisher description, and a scholarly review, and White through an author description and a National Park Service synthesis, not read in full. Each row requires verification against the cited work before publication.[^ch08-check-table3][^ch08-check-sources]

**Required alt text.** A four-row table comparing imperial-war-contingency, middle-ground-and-Indigenous-agency, imperial-and-fiscal, and global-and-Atlantic interpretations of the Seven Years’ War, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 3 compares the positions that organize the debate over the war and its consequences.”

**Cautions and limitations.** Anderson’s imperial focus can still make the Revolution the destination; White’s middle ground is regionally bounded; the fiscal row can reduce a global and Indigenous conflict to a budget problem; the global row can overshadow the continental and Indigenous histories. Do not treat British victory as inevitable or as a mere prelude to independence.

---

#### Ch. 9, Table 1 — `ch09-table-01`

**Owner and location.** `chapters/09-chapter-9.md`, §6.4 The map of positions. **Display number:** Ch. 9, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four explanations of imperial resistance: radical-Whig ideology, constitutional principle, social and economic change, and parliamentary sovereignty. The table should distinguish what each position says about motive, coordination, and the meaning of the crisis.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Ideology and the radical-Whig tradition** | Bernard Bailyn, *The Ideological Origins of the American Revolution* (1967) | The colonists interpreted the measures through an absorbed opposition ideology that read power as a conspiracy against liberty, and ideas propelled the Revolution. | Restores the pamphlet argument to the center and explains how disparate grievances cohered into a constitutional case. | Its focus on pamphlets and leaders can underplay popular action, material grievance, and the interests of non-elite colonists. |
| **Constitutional principle and English liberties** | Edmund S. and Helen M. Morgan, *The Stamp Act Crisis* (1953) | The resistance was a principled defense of English constitutional rights, especially consent to taxation, pressed through assemblies and congresses. | Provides the fullest account of the Stamp Act crisis and takes the patriots’ legal argument seriously. | Can treat the constitutional argument as settled and underweight popular violence and social conflict. |
| **Social and economic change** | Gary B. Nash, *The Urban Crucible* (1979); the older Progressive economic interpretation | The Revolution grew out of the economic transformation of the port cities, where inequality and class conflict created popular politics. | Explains the urban base of resistance and the radicalism of Boston in particular. | Can reduce an imperial and constitutional conflict to class interest and read the Revolution backward from its outcome. |
| **Parliamentary sovereignty and virtual representation** | Soame Jenyns, *The Objections to the Taxation of our American Colonies* (1765); Thomas Hutchinson; the imperial and fiscal interpretation | Parliament was supreme within the empire, the colonies were represented virtually, and the measures were a reasonable sharing of the cost of the war. | States the strongest contemporary defense of parliamentary authority and explains the ministry’s motives on its own terms. | Virtual representation convinced few colonists, and the position can dismiss the colonists’ objections as faction without answering them. |

**Required caption.** Table 1. Ideology, interests, and imperial resistance.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Bailyn, Morgan, and Nash were consulted through the Pulitzer spotlight, a scholarly forum and a book review, and a retrospective essay rather than read in full, and Jenyns was consulted in a course transcription. Each row requires verification against the cited work before publication.[^ch09-check-table][^ch09-check-sources]

**Required alt text.** A four-row table comparing ideology, constitutional principle, social-and-economic, and parliamentary-sovereignty interpretations of the imperial crisis, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the crisis.”

**Cautions and limitations.** Bailyn denies that social and economic conflict by itself explains the Revolution; Morgan reads resistance as constitutional principle; Nash locates it in port-city inequality; Hutchinson and Jenyns state the imperial case from within America. Do not collapse ideology, interest, and constitutional argument into one cause. The “parliamentary sovereignty” row is a serious constitutional position, not a caricature of tyranny.

---

#### Ch. 10, Table 1 — `ch10-table-01`

**Owner and location.** `chapters/10-chapter-10.md`, §7.4 The map of positions. **Display number:** Ch. 10, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare five interpretations of the decision for independence: ideology, popular action, the Declaration as practical politics, radical social transformation, and imperial sovereignty. The table should show how the same decision looks from the committee room, the street, and Whitehall.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Ideology and the radical-Whig tradition** | Bernard Bailyn, *The Ideological Origins of the American Revolution* (1967) | The colonists interpreted British measures through an absorbed opposition ideology that read power as a conspiracy against liberty, and ideas propelled the move to independence. | Restores the pamphlet argument to the center and explains how scattered grievances became a constitutional case for separation. | Its focus on pamphlets and leaders can underplay popular action, material grievance, and the interests of non-elite colonists. |
| **The people from below** | Gary B. Nash, *The Unknown American Revolution* (2005); *The Urban Crucible* (1979) | Ordinary people — artisans, farmers, mariners, enslaved and free people of African descent, Native peoples, and women — made the Revolution, and independence was not inevitable. | Recovers the agency of people usually left out and explains the popular energy behind resistance. | Can underweight the constitutional argument and the decisions of Congress; the evidence for popular intentions is uneven. |
| **The Declaration as practical politics** | Pauline Maier, *American Scripture* (1997) | The Declaration was one of many “other declarations,” written by practical politicians for specific audiences, not a timeless statement of national creed. | Situates the Declaration in the profusion of local and state declarations and disciplines later veneration of the text. | Its focus on the Declaration can treat the decision for independence as more settled than it was in early 1776. |
| **Radical social transformation** | Gordon S. Wood, *The Radicalism of the American Revolution* (1992) | The Revolution destroyed a hierarchical, monarchical society and created a democratic one, a change more radical than the colonists intended. | Explains why the Revolution mattered beyond the war and the founding documents. | Measures the Revolution by its social consequences and can read the outcome backward from what followed. |
| **Imperial sovereignty and rebellion** | George III’s Proclamation of Rebellion (1775); the parliamentary and Loyalist case; Lord North’s ministry | Parliament was supreme in the empire, the colonies were in rebellion, and force was the lawful answer to unlawful combinations. | States the imperial case on its own terms and explains why London saw conciliation as surrender. | Dismissed colonial claims as faction and could not offer terms the colonists would accept short of independence. |

**Required caption.** Table 1. Ideology, popular action, and the decision for independence.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Bailyn, Nash, Maier, and Wood were consulted through a museum reflection, two scholarly reviews, a Library of Congress report, and a university interview rather than read in full. Each row requires verification against the cited work before publication.[^ch10-check-table][^ch10-check-sources]

**Required alt text.** A five-row table comparing ideological, social-from-below, practical-politics, radical-transformation, and imperial-sovereignty interpretations of the decision for independence, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the decision for independence.”

**Cautions and limitations.** Bailyn, Nash, Maier, and Wood were consulted only through reviews, reflections, or interviews; the Declaration’s drafting and signing sequence remains open. Do not attribute a unified “colonial mind” to a divided population. The “radical social transformation” row must not claim that independence was a social revolution in the modern sense without evidence.

---

#### Ch. 11, Table 1 — `ch11-table-01`

**Owner and location.** `chapters/11-chapter-11.md`, §7.4 The map of positions. **Display number:** Ch. 11, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare five ways of framing the War for Independence: revolution, civil war, world war, dispossession, and the British imperial view. The table should make clear that the war’s meaning changes with the frame, not that one frame is simply correct.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **War as revolution** | Charles Royster, *A Revolutionary People at War* (1979); John Shy, *A People Numerous and Armed* (1976) | The war tested and reshaped American society; the ideals of virtue and freedom clashed with the demands of a standing army, and war and society shaped each other. | Takes the Continental Army’s experience and the political culture of service seriously, and explains why the war mattered beyond the battlefield. | Can treat the army as the center of the Revolution and underweight the Loyalist, Native, and enslaved people outside it. |
| **War as civil war** | Maya Jasanoff, *Liberty’s Exiles* (2011); the New York confiscation records | The Revolution was a civil war that divided communities, families, and nations; Loyalists were coerced, dispossessed, and exiled. | Recovers the losers and the internal violence, and explains the Loyalist diaspora that reshaped the British Empire. | Its focus on Loyalists can leave the political argument over independence in the background. |
| **War as world war** | Piers Mackesy, *The War for America, 1775–1783* (1964); Andrew Jackson O’Shaughnessy, *The Men Who Lost America* (2013); the National Archives | The American war was one theater in a global imperial conflict, and Britain’s able commanders lost a war that could not be won as fought. | Restores Britain, France, Spain, and the Netherlands to the story and explains the alliance that made Yorktown possible. | A global frame can underplay local allegiance, Native nations, and the experience of ordinary Americans. |
| **War as dispossession** | Colin Calloway, *The American Revolution in Indian Country* (1995); Alan Taylor, *American Revolutions* (2016) | Native nations and enslaved people were central actors, and the Revolution’s liberty for some rested on the dispossession of others. | Places Indigenous and enslaved people at the center and connects the war to continental expansion. | A continental frame can diffuse attention from the thirteen colonies’ politics and the decision for independence. |
| **The British imperial view** | George III’s government, Lord North’s ministry, and the Howe brothers; the Loyalist case | Parliament was supreme, the rebellion was unlawful, and force was the proper answer, though Britain preferred to restore rather than conquer. | States the imperial case on its own terms and explains why London pursued conciliation and force at once. | Underestimated American and French resolve and could not offer terms the rebels would accept short of independence. |

**Required caption.** Table 1. Revolution, civil war, and world war: interpreting the War for Independence.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Royster, Shy, Mackesy, O’Shaughnessy, Jr., and Taylor were consulted through reviews and institutional summaries rather than read in full, and Calloway remains unread. Each row requires verification against the cited work before publication.[^ch11-check-table][^ch11-check-sources]

**Required alt text.** A five-row table comparing revolution, civil-war, world-war, dispossession, and British-imperial interpretations of the War for Independence, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over what kind of war this was.”

**Cautions and limitations.** The Brooklyn and Yorktown strength and casualty figures remain open; the number of enslaved people who escaped to the British is contested; Royster, Shy, Mackesy, O’Shaughnessy, and Taylor were consulted only through reviews or summaries. Do not use “civil war” to flatten the war’s international and Indigenous dimensions. The British imperial row is not a Loyalist apology; it is a strategic perspective.

---

#### Ch. 12, Table 1 — `ch12-table-01`

**Owner and location.** `chapters/12-chapter-12.md`, §7.4 The map of positions. **Display number:** Ch. 12, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six interpretations of the Constitution: Beardian economic interest, critical-period crisis, revisionist refutation, democratic participation, slavery-centered, and slavery’s ambiguity. The table should show how the same text supports different accounts of interest, ideas, and exclusion.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Economic interest (Beardian)** | Charles A. Beard, *An Economic Interpretation of the Constitution of the United States* (1913); Robert A. McGuire and later statistical work | The Constitution was framed by holders of personal property, especially public securities, to protect their interests and to check debtor-majority politics. | Puts the debt question and material interest at the center and forces the Constitution to be explained rather than merely praised. | Beard’s evidence and categories have been shown inaccurate, and the reading can reduce ideas and institutions to class interest. |
| **Critical-period crisis (Whig and ideational)** | John Fiske, *The Critical Period of American History* (1888); Gordon S. Wood, *Power and Liberty* (2021) | The 1780s were a genuine crisis of debt, commerce, diplomacy, and disorder, and the Constitution answered a real institutional failure. | Explains why so many changed their minds and why the change was radical rather than incremental. | Can overstate the crisis; Jensen and others showed the decade had growth and political vitality. |
| **Revisionist refutation** | Robert E. Brown, *Charles Beard and the Constitution* (1956); Forrest McDonald, *We the People* (1958) | Beard misread the framers’ and ratifiers’ interests; there were many interests, and the Constitution cannot be reduced to bondholders’ self-interest. | Grounds the debate in systematic evidence and restores ideas and bargaining. | Its own categories and its dismissal of economic questions have themselves been revised. |
| **Democratic participation (neo-Progressive)** | Jackson Turner Main, *The Antifederalists* (1961); Merrill Jensen, *The New Nation* (1950) | The contest was a political struggle over power and the meaning of the Revolution, and the Antifederalists were critics of distant, consolidated government, not merely debtors. | Restores the losers and shows that ratification was not a foregone conclusion. | Can romanticize the Antifederalists and understate their own exclusions of the enslaved, Native nations, and women. |
| **Slavery-centered** | Staughton Lynd (1967); Paul Finkelman (1987); David Waldstreicher, *Slavery’s Constitution* (2009) | The three-fifths, fugitive-slave, and slave-trade clauses protected slavery and built slaveholding power into national institutions. | Makes slavery central to the founding and to the meaning of “we the people.” | Can read the framers’ avoidance of the word as either concealment or antislavery ambiguity, a disputed point. |
| **Slavery’s ambiguity (“no property in man”)** | Sean Wilentz, *No Property in Man* (2018) | The Constitution never recognized property in human beings, and that omission gave later antislavery politics a constitutional foothold. | Takes the text’s silences seriously and connects the founding to emancipation. | Critics reply that the document safeguarded slaveholder power regardless of its silence. |

**Required caption.** Table 1. The Constitution’s interests and powers: interpreting the founding.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Beard, Brown, McDonald, Main, Jensen, Lynd, Finkelman, Waldstreicher, and Wilentz were consulted only through reviews, excerpts, and secondary summaries rather than read in full. Each row requires verification against the cited work before publication.[^ch12-check-table][^ch12-check-sources]

**Required alt text.** A six-row table comparing economic-interest, critical-period, revisionist, democratic-participation, slavery-centered, and slavery-ambiguity interpretations of the Constitution, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the Constitution’s interests and powers.”

**Cautions and limitations.** Beard, Brown, McDonald, Main, Jensen, Lynd, Finkelman, Waldstreicher, and Wilentz were consulted only through reviews, excerpts, or secondary summaries; Madison’s notes and the Documentary History are not yet read. Do not treat “economic interest” or “slavery” as a single explanation. The “slavery’s ambiguity” row is a position, not a compromise between the others.

---

#### Ch. 13, Table 1 — `ch13-table-01`

**Owner and location.** `chapters/13-chapter-13.md`, §7.4 The map of positions. **Display number:** Ch. 13, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six interpretations of the 1790s: economic interest, political synthesis, republican ideology, liberal capitalism, democracy and its limits, and dispossession/slavery. The table should connect fiscal policy, party formation, and the exclusions that made the new republic.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Economic interest (Beardian)** | Charles A. Beard, *Economic Origins of Jeffersonian Democracy* (1915) | The Federalist–Republican struggle was a conflict between agrarianism and fluid capital, and the fiscal program served a monied interest. | Puts material interest and the debt question at the center and forces the program to be explained rather than praised. | Beard’s categories and evidence have been heavily revised, and the reading can reduce ideas and institutions to class interest. |
| **Political synthesis (Federalist era)** | Stanley Elkins and Eric McKitrick, *The Age of Federalism* (1993) | The 1790s were a contest over the meaning of the Revolution, shaped by political ideas and by the Federalists’ own political misjudgment. | Gives the decade a coherent political narrative and treats both parties as serious actors. | Can overstate the Federalists’ distinctiveness and understate economic and social conflict. |
| **Republican ideology (republican synthesis)** | Lance Banning, *The Jeffersonian Persuasion* (1978); Drew McCoy; Bernard Bailyn | The Republicans opposed a corrupt, consolidated government in the name of a classical republican tradition and the memory of 1776. | Explains the language of the opposition and its fear of power. | Critics argue it understates the Republicans’ commercial and liberal commitments and their own exclusions. |
| **Liberal capitalism** | Joyce Appleby, *Capitalism and a New Social Order* (1984) | The Republicans were the party of a new liberal, commercial society, not of classical virtue. | Reclaims the era’s economic optimism and challenges the republican synthesis. | Can minimize the persistence of republican language and the depth of the slavery and dispossession questions. |
| **Democracy and its limits** | Gordon S. Wood, *Empire of Liberty* (2009); critics Nancy Isenberg and John L. Brooke | The era brought egalitarian democracy for ordinary White men and a new commercial society. | Connects the 1790s to the broad democratization of American life. | Its consensus frame homogenizes Americans and marginalizes women, slavery, and dispossession. |
| **Dispossession and slavery** | Colin G. Calloway, *The Victory with No Name* (2015); Alan Taylor, *American Revolutions* (2016); Claudio Saunt, *Unworthy Republic* (2020) | National consolidation and the fiscal-military state were built on Native dispossession and the defense of slavery. | Restores the western war and slavery to the center of the 1790s. | Can understate the domestic political contest and the genuine appeal of the fiscal program. |

**Required caption.** Table 1. Party, fiscal authority, and consolidation: interpreting the 1790s.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Beard, Banning, McCoy, Bailyn, Appleby, Calloway, Taylor, and Saunt were consulted only through reviews, excerpts, and secondary summaries rather than read in full. Each row requires verification against the cited work before publication.[^ch13-check-table][^ch13-check-sources]

**Required alt text.** A six-row table comparing economic-interest, political-synthesis, republican-ideology, liberal-capitalist, democracy-and-limits, and dispossession-and-slavery interpretations of the 1790s, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the fiscal program, party, and consolidation.”

**Cautions and limitations.** The $54 million versus $77 million debt discrepancy, the 1796 electoral totals, and the St. Clair casualty figures remain open; Beard, Elkins–McKitrick, Banning, McCoy, Bailyn, Appleby, Calloway, Taylor, and Saunt were consulted only through reviews or summaries. Do not let the Hamiltonian financial story stand in for the whole decade. The “dispossession and slavery” row is not a later add-on; it is constitutive of the period.

---

#### Ch. 14, Table 1 — `ch14-table-01`

**Owner and location.** `chapters/14-chapter-14.md`, §6.4 The map of positions. **Display number:** Ch. 14, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six interpretations of Jeffersonian expansion and the War of 1812: restraint, empire of liberty, a second war of independence, the war as expansion, strategic failure, and dispossession/slavery. The table should show how foreign policy, territorial expansion, and slavery are weighted differently.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Jeffersonian restraint** | Thomas Jefferson and Albert Gallatin; Dumas Malone, *Jefferson and His Time*; Merrill D. Peterson, *Thomas Jefferson and the New Nation* | The administration pursued a principled program of economy, tax repeal, debt reduction, and a small military, and expanded only when the national interest required it. | Takes the language and the choices of the Republicans seriously and explains the appeal of a frugal republic. | Can treat the program’s coercive instruments—the embargo, the war, the acquisition of Louisiana—as exceptions rather than as the logic of expansion. |
| **Empire of liberty** | Gordon S. Wood, *Empire of Liberty*; Peter S. Onuf, *Jefferson’s Empire* | The central project was the extension of republican self-government across the continent, which reconciled liberty with expansion. | Connects limited-government ideology to continental empire and gives the era a coherent shape. | Can make expansion look consensual and understate the coercion, dispossession, and slavery that financed it. |
| **A second war of independence** | Popular memory and older nationalist scholarship; Donald R. Hickey’s ambivalent reading | The War of 1812 vindicated American sovereignty, secured the republic’s standing, and produced a lasting national identity. | Explains why the war mattered to Americans even when the treaty conceded nothing. | The concrete gains were few; the treaty said nothing about impressment, and the “victory” was assembled from the timing of the news. |
| **The war as expansion** | The War Hawks Henry Clay and John C. Calhoun; Reginald Horsman and Alan Taylor on the West and the war | The war aimed at Canada and at the destruction of Native power, opening western land to settlement and slavery. | Puts land, the West, and Indigenous dispossession at the center of a war usually remembered for sailors’ rights. | Not all Republicans were War Hawks, and Madison sought to avoid war even as he asked for it. |
| **Strategic failure (“Mr. Madison’s War”)** | The Federalist critique and the Hartford Convention report; Henry Adams’s ironic account | The war was poorly fought, politically divisive, and achieved none of its stated aims; the peace was a stalemate. | Measures the gap between war aims and results and recovers the seriousness of the opposition. | Reads the war with hindsight and can underestimate the real diplomatic and psychological gains that followed. |
| **Dispossession and slavery** | Alan Taylor; Claudio Saunt on removal and the cotton frontier; the treaty’s own clauses on slaves and Native rights | The expansion of the era rested on Native dispossession and the extension of slavery, and the state built to secure “liberty” secured both. | Restores the people the empire displaced and enslaved to the center of the story. | Risks reading later developments—Missouri, removal—back into a period whose outcomes were still contested. |

**Required caption.** Table 1. Jeffersonian restraint, expansion, and the War of 1812: interpreting 1801–1815.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Malone, Peterson, Wood, Onuf, Horsman, Taylor, and Saunt were consulted only through publisher descriptions, reviews, or institutional summaries rather than read in full. Each row requires verification against the cited work before publication.[^ch14-check-table][^ch14-check-sources]

**Required alt text.** A six-row table comparing Jeffersonian-restraint, empire-of-liberty, second-war-of-independence, war-as-expansion, strategic-failure, and dispossession-and-slavery interpretations of 1801–1815, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over Jeffersonian restraint, continental expansion, and the meaning of the War of 1812.”

**Cautions and limitations.** The walk-versus-horse inauguration story, the Tecumseh speech’s provenance, the peace-medal engraver, and the Tippecanoe/New Orleans casualty figures remain open. Do not equate “empire of liberty” with a coherent policy; Jefferson’s restraint and expansion were in tension. The “strategic failure” row is a judgment about the war’s conduct, not a denial of its consequences.

---

#### Ch. 15, Table 1 — `ch15-table-01`

**Owner and location.** `chapters/15-chapter-15.md`, §6.4 The map of positions. **Display number:** Ch. 15, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare five interpretations of the Market Revolution: capitalist transformation, opportunity and communication, gradual and regional change, slavery at the center of capitalism, and households/gender. The table should show how the same decades look from the factory, the farm, the slave plantation, and the household.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Capitalist transformation** | Charles Sellers, *The Market Revolution* (1991) | Establishing capitalist hegemony over economy, politics, and culture between 1815 and 1846 was the era’s defining event, imposed on a largely subsistence farm population. | Gives the period a single, powerful structure and takes the coercion in the transition seriously. | Can flatten regional difference and treat market participation as uniformly coerced. |
| **Opportunity and communication** | Daniel Walker Howe, *What Hath God Wrought* (2007) | Market relations were earlier than Sellers allows; most farm families welcomed larger markets, and the telegraph, post, and press defined the age. | Recovers the agency and the gains of ordinary participants and corrects an over-tragic reading. | Can understate the coercion and the losses that fell on the least powerful. |
| **Gradual and regional change** | Daniel Feller; John Lauritz Larson, *The Market Revolution in America*; Winifred Barr Rothenberg; Christopher Clark | The transition was slower, more local, and less total than the word “revolution” implies. | Insists on evidence and on the persistence of older practices. | Risks losing the forest of national connection in the trees of local variation. |
| **Slavery at the center of capitalism** | Walter Johnson, *Soul by Soul*; Edward E. Baptist, *The Half Has Never Been Told*; Seth Rockman, *Scraping By*; Sven Beckert, *Empire of Cotton* | Enslaved labor and the credit built on it were not adjacent to American capitalism but central to it. | Puts the internal slave trade and the factorage system at the middle of the story. | Debated in its strongest claims and sometimes reads later outcomes back into the 1820s and 1830s. |
| **Households and gender** | Catharine Beecher; Nancy F. Cott, *The Bonds of Womanhood*; Jeanne Boydston, *Home and Work*; Mary P. Ryan, *Cradle of the Middle Class* | The reorganization of household work and the ideology of separate spheres were part of the market’s making, not a refuge from it. | Connects the market to daily life and to the making of gender roles. | Can generalize from middle-class New England to a much more varied country. |

**Required caption.** Table 1. The Market Revolution: interpreting economic change, 1790s–1840s.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Sellers, Howe, Feller, Larson, Rothenberg, Clark, Johnson, Baptist, Rockman, Beckert, Cott, Boydston, and Ryan were consulted only through reviews, institutional summaries, or excerpts rather than read in full. Each row requires verification against the cited work before publication.[^ch15-check-table][^ch15-check-sources]

**Required alt text.** A five-row table comparing capitalist-transformation, opportunity-and-communication, gradual-and-regional, slavery-at-the-center, and households-and-gender interpretations of the Market Revolution, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the Market Revolution, its timing, its beneficiaries, and its relationship to slavery.”

**Cautions and limitations.** The factor’s account page, the Noah’s Ark flotilla anecdote, the “daughters of freemen” wording, and the seventy-three-hour week remain open; Sellers, Howe, Feller, Larson, Rothenberg, Clark, Johnson, Baptist, Rockman, Beckert, Cott, Boydston, Ryan, and Woodman were consulted only through reviews or summaries. Do not treat the market as a single national experience. The “slavery at the center” row is not a claim that every northern worker was a slave.

---

#### Ch. 16, Table 1 — `ch16-table-01`

**Owner and location.** `chapters/16-chapter-16.md`, §6.4 The map of positions. **Display number:** Ch. 16, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare seven interpretations of Jacksonian democracy: class conflict from below, entrepreneurs against elites, nostalgic restoration, ethnocultural and quantitative analysis, stratification and inequality, labor/party/class, and White supremacy/dispossession. The table should make the debate over who benefited from democratization explicit.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Class conflict from below** | Arthur M. Schlesinger Jr., *The Age of Jackson* (1945) | Jacksonian democracy was a coalition of farmers and laborers, East, West, and South, against Eastern capitalist privilege. | Gives the era a clear social base and takes the economic grievances of ordinary people seriously. | Can overstate popular protest and understate the racial and gender limits of the coalition. |
| **Entrepreneurs against elites** | Richard Hofstadter, “Andrew Jackson” (1948); Bray Hammond (1957) | Jacksonians were rising entrepreneurs attacking monopolistic privilege to open their own road, not champions of those below them. | Explains the anti-bank, anti-charter politics as self-interest rather than egalitarianism. | Can reduce a mass movement to elite ambition and miss the popular mobilization. |
| **Nostalgic restoration** | Marvin Meyers, *The Jacksonian Persuasion* (1957) | Jackson and his followers yearned to restore an imagined agrarian, republican past. | Recovers the period’s ideas and its misgivings about the emerging industrial order. | Risks treating rhetoric as motive and the past it invoked as real. |
| **Ethnocultural and quantitative** | Lee Benson, *The Concept of Jacksonian Democracy* (1961) | Religion and ethnicity, more than class, determined party divisions; an egalitarian spirit extended beyond the Democrats. | Brings voting data and a genuinely new method to the study of politics. | Can dissolve class and slavery into an “Age of Egalitarianism” both parties shared. |
| **Stratification and inequality** | Edward Pessen, *Jacksonian America* (1969) | The democratic rhetoric of the age disguised an increasingly stratified society with growing inequality. | Tests the egalitarian claim against social structure and finds it wanting. | Can understate the real changes in participation and party organization. |
| **Labor, party, and class** | Sean Wilentz, *Chants Democratic* (1984), *The Rise of American Democracy* (2005); John Ashworth; Harry Watson | Party politics reflected a broad struggle over opportunity and the reach of capitalist power. | Connects politics to the market revolution and to working-class identity. | Can read later democratic outcomes back into the 1830s. |
| **White supremacy and dispossession** | Michael Rogin, *Fathers and Children* (1975); Alexander Saxton, *The Rise and Fall of the White Republic* (1990); Daniel Walker Howe, *What Hath God Wrought* (2007) | The Jacksonians advanced White male supremacy, protected slavery, and built democracy on racial exclusion and dispossession. | Puts removal, slavery, and racial exclusion at the center of the age. | Its strongest claims are debated, and it can understate the era’s genuine democratizing changes. |

**Required caption.** Table 1. Democracy, class, and exclusion: interpreting Jacksonian democracy, 1815–1840.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Schlesinger, Hofstadter, Hammond, Meyers, Benson, Pessen, Wilentz, Ashworth, Watson, Rogin, Saxton, Howe, and Remini were consulted only through a textbook historiography survey rather than read in full. Each row requires verification against the cited work before publication.[^ch16-check-table][^ch16-check-sources]

**Required alt text.** A seven-row table comparing class-conflict, entrepreneurial, nostalgic-restoration, ethnocultural, stratification, labor-party-class, and white-supremacy interpretations of Jacksonian democracy, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over Jacksonian democracy, its beneficiaries, and its relationship to exclusion.”

**Cautions and limitations.** Franchise dates and contractions (New York 1826, Pennsylvania 1838), the 1824 popular-vote series, and turnout denominators remain open. Do not equate expanded White male suffrage with democracy for all; the White supremacy/dispossession row is essential, not an add-on. The “ethnocultural” row is a method as well as a position; do not reduce it to a single election.

---

#### Ch. 17, Table 1 — `ch17-table-01`

**Owner and location.** `chapters/17-chapter-17.md`, §6.4 The map of positions. **Display number:** Ch. 17, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of removal: benevolent necessity and the vanishing people, federal deportation and capitalist dispossession, Indigenous nation-building and legal resistance, and borderlands Indigenous power. The table should show how the same policy looks from Washington, from the nations, and from the borderlands.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Benevolent necessity and the vanishing people** | Andrew Jackson’s Second Annual Message (1830); the policy’s defenders; older nationalist histories | Removal was a humane measure that saved a people who could not survive beside Whites, and it was inevitable. | States the policy’s own justification, which the chapter must confront rather than caricature. | Contradicted by the Cherokee constitution, the *Cherokee Phoenix*, the *Worcester* ruling, and the record of resistance; treats a choice as fate. |
| **Federal deportation and capitalist dispossession** | Claudio Saunt, *Unworthy Republic* (2020); Elliott West | Removal was a centrally planned, funded, and administered deportation, tied to the expansion of land, cotton, and slavery, and it was not inevitable. | Puts federal agency, finance, and racial capitalism at the center and recovers contingency. | Its sharpest claims about scale and intent are debated; “deportation” is a strong reframing to test against period usage. |
| **Indigenous nation-building and legal resistance** | Theda Perdue and Michael D. Green, *The Cherokee Nation and the Trail of Tears* (2007); Cherokee Nation institutional history; Tim Alan Garrison on *Worcester* | The Cherokee built a modern nation and resisted through law, press, and diplomacy; removal was contested within the nation and sovereignty survived it. | Centers Cherokee agency, institutions, and survival rather than treating the nation only as a victim. | Can understate the coercion and death at the center of the story; the Cherokee case is not the whole of removal. |
| **Borderlands Indigenous power** | Pekka Hämäläinen, *The Comanche Empire* (2008); Brian DeLay, *War of a Thousand Deserts* (2008); the Handbook of Texas Comanche entry | On the Southern Plains and the Mexican North, Comanche and allied nations exercised real power that shaped the region and the U.S.-Mexican conflict. | Restores Native power and turns the borderlands into a subject rather than a backdrop. | The “empire” framing is contested, and Comanche power did not prevent eventual conquest. |

**Required caption.** Table 1. Removal, sovereignty, and borderlands: interpreting dispossession and survival, 1820–1848.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Saunt was consulted through a scholarly review that quotes the book, and Perdue and Green, Hämäläinen, and DeLay were discovered but not read in full. Each row requires verification against the cited work before publication.[^ch17-check-table][^ch17-check-sources]

**Required alt text.** A four-row table comparing benevolent-necessity, federal-deportation, Indigenous-sovereignty, and borderlands-power interpretations of removal and the borderlands, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over removal, sovereignty, and the borderlands.”

**Cautions and limitations.** The number removed (about 50,000 versus 100,000 versus Saunt’s “nearly eighty thousand”) and the Cherokee death toll remain open; Saunt was consulted through a review, and Perdue–Green, Hämäläinen, and DeLay remain unread. Do not use “removal” as a single event or a single death toll. The “benevolent necessity” row must state the position fairly before the chapter refutes it.

---

#### Ch. 18, Table 1 — `ch18-table-01`

**Owner and location.** `chapters/18-chapter-18.md`, §6.4 The map of positions. **Display number:** Ch. 18, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of the Mexican-American War: democratic opportunity and the mission of self-government, slaveholding strategy and the Slave Power, conquest/race and the price, and contingency/“Mr. Polk’s War.” The table should show how the war’s causes and meaning change with the frame.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Democratic opportunity and the mission of self-government** | John L. O’Sullivan, “Annexation” (1845); Albert K. Weinberg, *Manifest Destiny* (1935); Frederick Merk, *Manifest Destiny and Mission in American History* (1963) | Expansion extended republican self-government and liberty across the continent; a broad popular “mission” outlasted the failed program of “destiny.” | Takes the era’s own civic language seriously and shows the democratic content of expansionist argument. | Confuses a claim of consent with consent itself; leaves out the enslaved, the conquered, and the dispossessed. |
| **Slaveholding strategy and the Slave Power** | Ulysses S. Grant, *Personal Memoirs* (1885); Frederick Douglass, *North Star* (1848); John Quincy Adams; later “Slave Power” scholarship | Annexation and war were a scheme to extend slavery and add slave states, and northerners came to see them that way. | Connects the war to slavery’s political economy and to the sectional crisis it produced. | The strongest “conspiracy” form overstates a unified plan; California entered free, and Polk’s own priority was California. |
| **Conquest, race, and the price** | Reginald Horsman, *Race and Manifest Destiny* (1981); Amy S. Greenberg, *A Wicked War* (2012); Paul Foos, *A Short, Offhand, Killing Affair* (2002); Timothy J. Henderson, *A Glorious Defeat* (2007) | A war of conquest legitimated by racial Anglo-Saxonism, with a heavy human cost borne by Mexicans, volunteers, and the conquered. | Recovers the ideology, the violence, and the Mexican and dissenting perspectives. | Can flatten the variety of American motives and treat the outcome as foreordained. |
| **Contingency and “Mr. Polk’s War”** | Daniel Walker Howe, *What Hath God Wrought* (2007); John H. Schroeder, *Mr. Polk’s War* (1973); Anders Stephanson, *Manifest Destiny* (1995); David M. Pletcher, *The Diplomacy of Annexation* (1973) | There was no overwhelming popular demand; the war was Polk’s contingent decision, forced on a divided nation. | Restores agency, contingency, and the depth of opposition. | Can understate structural forces — slavery, land hunger, and racial ideology. |

**Required caption.** Table 1. Expansion, slavery, and conquest: interpreting the Mexican-American War, 1844–1850.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Merk, Weinberg, Stephanson, Horsman, Greenberg, Foos, Henderson, Howe, Schroeder, and Pletcher were discovered through bibliographies and descriptions but not read in full for this outline, and each row requires verification against the cited work before publication.[^ch18-check-table][^ch18-check-sources]

**Required alt text.** A four-row table comparing democratic-opportunity, slaveholding-strategy, conquest-and-race, and contingency interpretations of the Mexican-American War, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over expansion, slavery, and conquest.”

**Cautions and limitations.** The Senate ratification vote (34–14 versus 38–14), the Thornton casualty figures, the Mexican death toll, and Emerson’s exact wording remain open. Do not let the domestic political story erase Mexican agency or the war’s imperial character. The “democratic opportunity” row is a period argument, not a endorsement of the war.

---

#### Ch. 19, Table 3 — `ch19-table-03`

**Owner and location.** `chapters/19-chapter-19.md`, §6.4 The map of positions. **Display number:** Ch. 19, Table 3. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of the sectional crisis: fundamental conflict, party collapse and contingency, the slaveholders’ offensive, and a synthesis of slavery amid contingency. The table should show how structure and choice are weighted differently.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Fundamental conflict** | Edward L. Ayers, “What Caused the Civil War?” (2005), summarizing the “fundamentalist” school; the slavery-centered tradition that runs through David M. Potter, *The Impending Crisis* (1976) | Slavery and free labor were intrinsically opposed, so a clash was all but inevitable. | Names slavery as the central and unbridgeable issue and refuses to explain the war away. | Can make the outcome automatic and obscure the choices, timing, and near-misses. |
| **Party collapse and contingency** | Michael F. Holt, *The Political Crisis of the 1850s* (1978); Marc Egnal, *Clash of Extremes* (2009) | The breakdown of the national two-party system, driven by economic change, made Americans perceive internal enemies; the war was contingent on that breakdown. | Restores contingency, party mechanics, and structural depth; explains the realignment. | Can understate slavery’s moral and political force and treat sectionalism as an effect of economics. |
| **Slaveholders’ offensive** | William W. Freehling, *The Road to Disunion*, vol. 2 (2007); Charles B. Dew, *Apostles of Disunion* (2001); the “Slave Power” tradition | A proslavery, expansionist movement drove the crisis, and secessionists built support by warning of emancipation and racial equality. | Recovers the slaveholders’ agency and the racial logic of disunion; takes southern arguments seriously. | Stressing a unified “Slave Power” can flatten the South’s internal divisions and disagreement. |
| **Synthesis: slavery amid contingency** | David M. Potter, *The Impending Crisis, 1848–1861* (completed by Don E. Fehrenbacher, 1976) | Slavery pervaded every aspect of the sectional conflict, but the crisis unfolded through specific, contingent political decisions and failures. | Holds structure and contingency together; remains the standard account. | Its very balance can understate the militancy of the enslaved and free Black actors who forced the issue. |

**Required caption.** Table 3. Slavery, party politics, and contingency: interpreting the coming of the Civil War, 1850–1859.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Potter, Holt, Egnal, Dew, and Freehling were discovered through a scholarly reading guide and were not read in full for this outline, and each row requires verification against the cited work before publication.[^ch19-check-tables][^ch19-check-sources]

**Required alt text.** A four-row table comparing fundamental-conflict, party-collapse-and-contingency, slaveholders’-offensive, and synthesis interpretations of the coming of the Civil War, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 3 compares the positions that organize the debate over slavery, party politics, and the coming of the Civil War.”

**Cautions and limitations.** Potter, Holt, Egnal, Dew, and Freehling were discovered through a reading guide and read only in summary; the Lecompton and English bill votes and the Glover and Minkins case details rest on summaries. Do not turn contingency into randomness or slavery into the only cause. The “party collapse” row is not a claim that the parties were the only thing that mattered.

---

#### Ch. 20, Table 3 — `ch20-table-03`

**Owner and location.** `chapters/20-chapter-20.md`, §6.4 The map of positions. **Display number:** Ch. 20, Table 3. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of secession: revolution for slavery, the counterrevolution of slavery, the explicit cause in the commissioners’ rhetoric, and contingency amid slavery. The table should distinguish the deep cause, the immediate trigger, and the choice to leave.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Revolution for slavery** | The secessionists’ own language: the *Charleston Mercury*, November 3, 1860; Alexander H. Stephens’s Cornerstone Speech, March 21, 1861 | Secession was a revolution — a break with the old government to secure slavery and racial subordination. | Takes the actors’ self-description seriously and refuses to sanitize it. | “Revolution” can obscure that the aim was to preserve, not extend, an existing hierarchy. |
| **The counterrevolution of slavery** | Manisha Sinha, *The Counterrevolution of Slavery* (2000) | Secession was a conservative movement by a slaveholding elite to protect slavery and white supremacy, not to advance liberty. | Reframes secession as reaction against democratic and antislavery politics. | Focused on South Carolina; its elite-centered account can understate popular support. |
| **Apostles of disunion: the explicit cause** | Charles B. Dew, *Apostles of Disunion* (2001); the state declarations of causes | The secession commissioners argued openly that slavery and racial inequality were the cause. | Uses the secessionists’ own words to answer the “states’ rights” apologia. | Concentrates on the commissioners and the elite; may understate divisions within the South. |
| **Contingency amid slavery** | William W. Freehling, *The Road to Disunion*, vol. 2 (2007); David M. Potter, *The Impending Crisis* (1976); Michael F. Holt, *The Political Crisis of the 1850s* (1978) | Slavery was central, but disunion was contested and its timing contingent on specific political and military choices. | Restores the South’s internal divisions and the contingency of the Sumter decision. | Can seem to dilute slavery’s centrality or the secessionists’ own stated purpose. |

**Required caption.** Table 3. Revolution, counterrevolution, and slaveholding state-building: interpreting secession and the coming of the war, 1860–61.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; Dew and Freehling were consulted only through reviews, Sinha through a book description and a blocked review, and McCurry, Potter, and Holt through a publisher description and summaries, so each row requires verification against the cited work before publication.[^ch20-check-tables][^ch20-check-sources]

**Required alt text.** A four-row table comparing the revolution-for-slavery, counterrevolution-of-slavery, apostles-of-disunion, and contingency-amid-slavery interpretations of secession and the coming of the war, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 3 compares the positions that organize the debate over secession and the coming of the war.”

**Cautions and limitations.** Dew and Freehling were consulted only through reviews; Sinha through a blocked review and a book description; McCurry, Potter, and Holt through a publisher description and summaries. The Mississippi declaration and the Georgia and Texas texts remain open. Do not use “states’ rights” as an explanation without showing what the states said they were protecting.

---

#### Ch. 21, Table 1 — `ch21-table-01`

**Owner and location.** `chapters/21-chapter-21.md`, §7.4 The map of positions. **Display number:** Ch. 21, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of emancipation: federal action, self-emancipation from below, military necessity and hard war, and the second American Revolution. The table should show how agency, law, and military contingency are distributed across the explanations.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Federal action: Lincoln, Congress, and party** | James M. McPherson, “Who Freed the Slaves?” (1997); Eric Foner, *The Fiery Trial* (2010) | Emancipation came from political leadership and federal power: Lincoln, Congress, and the Republican Party ended slavery. | Takes constitutional authority, statecraft, and the wartime state seriously. | Can understate the enslaved people whose flight forced the issue. |
| **Self-emancipation from below** | David W. Blight, *A Slave No More* (2007); Ira Berlin, “Who Freed the Slaves?” (1997); Barbara J. Fields, “Who Freed the Slaves?” (1990); David Williams, *I Freed Myself* (2014) | Enslaved people freed themselves by fleeing, laboring, and serving, and the proclamation ratified a process already underway. | Centers Black agency and refuses a gift-from-above story. | Can understate the federal and military conditions that made escape and service possible. |
| **Military necessity and hard war** | The Emancipation Proclamation’s own language (“a fit and necessary war measure”); Mark E. Neely Jr., *The Civil War and the Limits of Destruction* (2007) | Emancipation served military needs, and the war’s destructiveness was real but more limited than its reputation suggests. | Connects emancipation to the conduct of the war and asks how hard it truly was. | “Necessity” can reduce a moral revolution to tactics, and the limits thesis is contested. |
| **The second American Revolution** | James M. McPherson, *Abraham Lincoln and the Second American Revolution* (1991) | The war remade the nation’s constitutional and social order, with emancipation at its center. | Links emancipation to a durable transformation of the state and citizenship. | “Revolution” can overstate rupture and understate the persistence of racial hierarchy. |

**Required caption.** Table 1. Emancipation and the war’s transformation: interpreting who freed the slaves and how the war changed, 1861–63.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Status: `planned`; McPherson’s “Who Freed the Slaves?,” Berlin’s essay, Fields’s essay, and Williams’s book were consulted only through reviews, descriptions, or citations in other scholarship, and Foner and Neely through publisher descriptions and a scholarly review, so each row requires verification against the cited work before publication.[^ch21-check-table][^ch21-check-sources]

**Required alt text.** A four-row table comparing the federal-action, self-emancipation, military-necessity, and second-American-Revolution interpretations of emancipation and the war’s transformation, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over emancipation and the war’s transformation.”

**Cautions and limitations.** McPherson’s “Who Freed the Slaves?”, Berlin, Fields, Williams, Foner, and Neely were consulted only through reviews, descriptions, or citations; the Douglass epigraph’s original print source and the Pryor photograph dates remain open. Do not make emancipation a single actor’s gift or a purely bottom-up event. The “military necessity” row is not a claim that emancipation was only a tactic.

---

#### Ch. 22, Table 3 — `ch22-table-03`

**Owner and location.** `chapters/22-chapter-22.md`, §6.4 The map of positions. **Display number:** Ch. 22, Table 3. **Status:** drafted, unverified.

**Purpose.** Compare three interpretations of Union victory: the second American Revolution, state-building, and restoration with the limits of change. The table should weigh transformation against continuity in the war’s outcome.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Second American Revolution** | James M. McPherson, *Abraham Lincoln and the Second American Revolution* (1991); Eric Foner, *The Second Founding* (2019) | The war remade the constitutional and social order, with emancipation at its center. | Takes the constitutional revolution and the new citizenship seriously. | “Revolution” can overstate rupture and understate the persistence of racial hierarchy. |
| **State-building** | Richard Franklin Bensel, *Yankee Leviathan* (1991) | The war and Reconstruction built new central state authority in finance, military organization, and administration. | Explains the durable federal capacities the war created. | Can understate how much of the new state receded and how unevenly it reached the South. |
| **Restoration and the limits of change** | The Dunning School and its Lost Cause foundations, as described by Eric Foner; David W. Blight, *Race and Reunion* (2001) | Union victory restored the old Union and the amendments’ promise was quickly contained, while reunion restored a white republic. | Directs attention to the swift reconstruction of the old racial order after 1865. | As a determinist thesis it can understate Black political action and the amendments’ later force. |

**Required caption.** Table 3. Victory, revolution, and state-building: interpreting what the Union’s victory meant.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The works were consulted at the level noted in the combined notes, and each row requires verification against the cited work before publication. Status: `planned`.[^ch22-foner-second-founding][^ch22-mcpherson-second-revolution][^ch22-bensel-yankee-leviathan][^ch22-check-tables]

**Required alt text.** A three-row table comparing the second-American-Revolution, state-building, and restoration interpretations of Union victory, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 3 compares the positions that organize the debate over what victory meant.”

**Cautions and limitations.** The mortality methods (618,222; Hacker’s roughly 750,000; the 2024 full-count 698,000) are not interchangeable; McClellan’s soldier-vote total is not separated in the consulted source; the 1864 popular-vote totals vary. Do not present any mortality estimate as a new official count. The “restoration” row is not a denial that the war changed the Constitution.

---

#### Ch. 23, Table 1 — `ch23-table-01`

**Owner and location.** `chapters/23-chapter-23.md`, §7.4 The map of positions. **Display number:** Ch. 23, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of Reconstruction: a democratic experiment, a second founding and revolution, an occupation with limits, and counterrevolution and redemption. The table should show how historians weigh Black political agency, federal power, and White violence.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Democratic experiment** | W. E. B. Du Bois, *Black Reconstruction in America* (1935) | Reconstruction was a genuine attempt at interracial democracy, and the enslaved had already struck for freedom by withdrawing their labor. | Restores Black agency, political economy, and the era’s democratic aspiration to the center of the story. | The “general strike” thesis and the account of Reconstruction governments have been qualified and debated. |
| **Second founding and revolution** | Eric Foner, *Reconstruction: America’s Unfinished Revolution, 1863–1877* (1988); *The Second Founding* (2019) | The war and Reconstruction produced a constitutional and political revolution in citizenship and federal power that was then reversed. | Synthesizes the amendments, national politics, and freedpeople’s agency into a coherent account. | “Revolution” can understate the counterrevolution’s success and the persistence of racial hierarchy. |
| **Occupation and its limits** | Accounts of Reconstruction as military occupation; Richard Franklin Bensel, *Yankee Leviathan* (1991) | Reconstruction rested on too few troops and transient northern will, and its federal state-building reached the South unevenly. | Explains why enforcement receded and local power reasserted itself. | “Occupation” misdescribes a program also built by southern Unionists, Black voters, and elected state governments. |
| **Counterrevolution and redemption** | The Dunning School and its Lost Cause foundations, as described by W. E. B. Du Bois and Eric Foner; David W. Blight, *Race and Reunion* (2001) | White paramilitary violence and northern retreat restored a White republic and suppressed the emancipationist promise. | Directs attention to organized violence and the swift reconstruction of the old racial order. | As a determinist thesis it can understate Black political action and the amendments’ later force. |

**Required caption.** Table 1. Reconstruction and counterrevolution: interpreting what the era was.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The works were consulted at the level noted in the combined notes, and each row requires verification against the cited work before publication. Status: `planned`.[^ch23-aaihs-dubois][^ch23-foner-second-founding][^ch23-foner-reconstruction][^ch23-bensel-yankee-leviathan][^ch23-blight-race-reunion][^ch23-check-table]

**Required alt text.** A four-row table comparing the democratic-experiment, second-founding, occupation, and counterrevolution interpretations of Reconstruction, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over what Reconstruction was.”

**Cautions and limitations.** The Black officeholder counts (about 1,500 versus about 2,000), the Memphis and New Orleans casualty figures, the Colfax death toll, and the amendment-ratification chronology remain open; Du Bois, Foner, Bensel, and Blight were consulted only through secondary summaries. Do not let “failure” or “unfinished revolution” become a verdict that erases Black political life. The “occupation” row is a metaphor as well as a policy description; define it.

---

#### Ch. 24, Table 1 — `ch24-table-01`

**Owner and location.** `chapters/24-chapter-24.md`, §6.4 The map of positions. **Display number:** Ch. 24, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare four interpretations of the second industrial revolution: managerial enterprise, political economy and the state, labor and the great upheaval, and corporate capitalism and the law. The table should show how technology, state action, labor conflict, and law each become the center of a different account.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Managerial enterprise** | Alfred D. Chandler Jr., *The Visible Hand* (1977) | Large firms and salaried managers coordinated production and distribution more efficiently than markets, so the visible hand of management replaced the invisible hand of market forces. | Explains the internal logic and cost advantages of the modern corporation across railroads, steel, and distribution. | Can understate public subsidy, coercion, and labor conflict, and it treats efficiency as the main cause of concentration. |
| **Political economy and the state** | Richard White, *The Republic for Which It Stands* (2017) | Corporate power was built with the state: land grants, tariffs, courts, and coercion organized the Gilded Age economy and its exclusions. | Restores law, subsidy, and the state to the center, and connects industrial change to race, immigration, and the West. | A broad synthesis; the relative weight of state action and market efficiency is not settled by the framework alone. |
| **Labor and the great upheaval** | David Montgomery, *The Fall of the House of Labor* (1987); Herbert G. Gutman, *Work, Culture, and Society in Industrializing America* (1976) | Workers built their own organizations and a republican politics, and the era’s strikes and defeats reconstructed workplace authority. | Treats workers as historical actors and explains what the defeats of 1892 and 1894 closed off. | The works were not consulted for this outline; their arguments must be verified against the texts before publication. |
| **Corporate capitalism and the law** | Martin J. Sklar, *The Corporate Reconstruction of American Capitalism, 1890–1916* (1988); William G. Roy, *Socializing Capital* (1997) | The corporation was a legal and governmental creation, and antitrust was a reordering of property rights rather than an attack on business. | Explains how law made the corporation and how regulation became a form of governance. | The works were not consulted for this outline; their arguments must be verified against the texts before publication. |

**Required caption.** Table 1. Management, political economy, and labor: interpreting the second industrial revolution.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Only Chandler and White were consulted at the level noted in the combined notes; the labor and law rows name works that remain unread and must be verified before publication. Status: `planned`.[^ch24-chandler-visible-hand][^ch24-white-republic][^ch24-check-sources][^ch24-check-table]

**Required alt text.** A four-row table comparing the managerial-enterprise, political-economy, labor, and corporate-law interpretations of the second industrial revolution, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over how the second industrial revolution built corporate power.”

**Cautions and limitations.** The New York-specific witnesses for the standard-time scene, the number of local times before 1883, and the rail/steel/urban series remain open; the cited inequality figures for the 1870s–90s lack a settled source. Do not treat “managerial revolution” as a complete explanation of industrial power. The “labor” row must not reduce the upheaval to a single strike.

---

#### Ch. 25, Table 1 — `ch25-table-01`

**Owner and location.** `chapters/25-chapter-25.md`, §6.4 The map of positions. **Display number:** Ch. 25, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare five interpretations of the American West: the frontier thesis, conquest and New Western history, political economy and the federal West, hydraulic empire and environmental limits, and Indigenous power. The table should show how the same region becomes a process, a conquest, a federal project, an ecological system, or a set of Native polities.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Frontier thesis** | Frederick Jackson Turner, “The Significance of the Frontier in American History” (1893) | The existence of an area of free land, its recession, and westward settlement explain American development; the frontier produced individualism and democracy. | Gave the West a central place in national history and named a real process of settlement and institutional change. | Treats Indigenous nations as obstacles to civilization, takes “free land” as empty, and declares the frontier closed in 1890 as if conflict had ended. |
| **Conquest and New Western history** | Patricia Nelson Limerick, *The Legacy of Conquest* (1987); with William Cronon, *Nature’s Metropolis* (1991), and Elliott West | The West is a place and not a process; conquest — of Indigenous nations, Mexicans, and others — is its organizing fact, and its legacy persists. | Restores Indigenous, Mexican, Chinese, and Black people to the story and treats conquest as serious as slavery. | A broad synthesis; it can underplay the weight of federal policy and of environmental constraint, and it leaves the meaning of “conquest” for non-Indigenous settlers open. |
| **Political economy and the federal West** | Richard White, *“It’s Your Misfortune and None of My Own”* (1991) | The West was made by federal power, corporate capital, and diverse labor; it is a region shaped by the state and by the market, not a folk process. | Puts law, subsidy, and the state at the center and connects the West to national industrial development. | A survey; the relative weight of the federal state and of local actors is not settled by the framework alone. |
| **Hydraulic empire and environmental limits** | Donald Worster, *Rivers of Empire* (1985) | Aridity made the West dependent on federally built water systems, producing a “hydraulic empire” and concentrated power. | Explains how aridity and irrigation structured western society and politics. | The thesis is strongest for the arid far West and does not fit the humid eastern margin; the work was consulted only through reviews for this outline. |
| **Indigenous power** | Pekka Hämäläinen, *The Comanche Empire* (2008) and *Lakota America* (2019) | Indigenous nations such as the Comanche and Lakota built empires and shaped the colonial order rather than merely resisting it. | Restores Indigenous nations as powerful historical actors and rewrites the chronology of western power. | The “empire” framework is debated; the works were consulted only through reviews and descriptions for this outline. |

**Required caption.** Table 1. Frontier versus conquest: interpreting the American West.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Turner and Limerick were consulted at the level noted in the combined notes; White, Worster, and Hämäläinen remain unread and must be verified before publication. Status: `planned`.[^ch25-tah-turner][^ch25-archive-limerick][^ch25-white-misfortune][^ch25-worster-rivers][^ch25-hamalainen-lakota][^ch25-check-sources][^ch25-check-table]

**Required alt text.** A five-row table comparing the frontier-thesis, conquest, political-economy, environmental-limits, and Indigenous-power interpretations of the American West, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over how the American West should be explained.”

**Cautions and limitations.** The Sitting Bull epigraph lacks a dated period source; the Limerick quotation needs collation; the 1868 treaty cession clause needs collation; the 1889 land-run and Exoduster figures rest on summaries. Do not use “frontier” as a neutral synonym for the West. The “Indigenous power” row is not a claim that Native nations were never defeated.

---

#### Ch. 26, Table 1 — `ch26-table-01`

**Owner and location.** `chapters/26-chapter-26.md`, §6.4 The map of positions. **Display number:** Ch. 26, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six interpretations of Jim Crow: Woodward’s timing thesis, class conflict and the Populist scapegoat, elite state-building, culture and gender, violence and the state, and Black agency and resistance. The table should show how the segregation order was made, enforced, and contested.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Woodward’s timing thesis** | C. Vann Woodward, *The Strange Career of Jim Crow* (1955; 2002 commemorative ed.) | Rigid, statutory segregation was not an age-old southern tradition but a product of the 1890s, after a period of fluid race relations and White dissent. | Made segregation a historical problem with a timeline and showed that the racial order was contingent, not natural. | Its critics found segregation already present before the 1890s and argued it underplayed customary practice and treated Black Southerners as objects rather than subjects.[^ch26-pfeifer-woodward] |
| **Class conflict and the Populist scapegoat** | Woodward; with Thomas E. Watson as the emblem | The order rose as White conservatives and former Populists turned on their Black allies and used White supremacy to reunite estranged White classes. | Connects the timing of segregation to the politics of the 1890s and to the collapse of interracial agrarian politics. | The Watson case shows the turn was real but uneven; the thesis can make Black voters the occasion for White conflict rather than actors in it.[^ch26-woodward-summary][^ch26-nge-watson] |
| **Elite state-building** | J. Morgan Kousser, *The Shaping of Southern Politics* (1974); Donald G. Nieman | Disfranchisement was a deliberate project of political elites who chose facially neutral devices to remove the most opponents at the least cost to their own coalition. | Explains the specific choice of mechanisms and links them to party strategy and apportionment. | A top-down account; it can slight rural organization, violence, and the role of registrars in local enforcement.[^ch26-history-disfranchise] |
| **Culture and gender** | Glenda Elizabeth Gilmore; Grace Elizabeth Hale; Joel Williamson | Segregation was made through ideas about White womanhood, Black masculinity, and urban space, not by law alone. | Explains the sexualized rhetoric of lynching and the popular culture of separation. | Strongest for the urban South and the early twentieth century; the works were consulted only through a review for this outline. |
| **Violence and the state** | Michael J. Pfeifer, *Rough Justice*; W. Fitzhugh Brundage | Lynching was a form of rough justice embedded in local order, and formal segregation and “legal lynchings” followed as White elites sought orderly racial control. | Treats racial violence as structured and historically specific rather than as random savagery. | Emphasizes local and urban dynamics; it must be balanced against the state constitutional and economic evidence.[^ch26-pfeifer-woodward] |
| **Black agency and resistance** | Ida B. Wells; W. E. B. Du Bois; Paula Giddings; Shawn Leigh Alexander | Black Southerners fought the new order through investigation, journalism, organization, and law, and their choices shaped its history. | Restores Black actors as subjects and explains how the order was contested from the start. | The sources survive unevenly, and the chapter must name the silence where no voice is recorded.[^ch26-durocher-wells][^ch26-dubois-souls] |

**Required caption.** Table 1. Making and enforcing Jim Crow: positions on the making of the southern racial order.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Woodward and Watson were consulted at the level noted in the combined notes; Kousser, Nieman, Gilmore, Hale, Williamson, Pfeifer’s *Rough Justice*, Brundage, Giddings, and Alexander remain unread and must be verified before publication. Status: `planned`.[^ch26-woodward-summary][^ch26-pfeifer-woodward][^ch26-nge-watson][^ch26-durocher-wells][^ch26-dubois-souls][^ch26-check-sources][^ch26-check-table]

**Required alt text.** A six-row table comparing the Woodward timing thesis, the class-conflict and Populist-scapegoat interpretation, the elite state-building interpretation, the culture-and-gender interpretation, the violence-and-the-state interpretation, and the Black agency and resistance interpretation of the making of the southern racial order, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over how the making and enforcement of Jim Crow should be explained.”

**Cautions and limitations.** The Vardaman declaration’s attribution, the Woodward epigraph and page numbers, the 1875 Mississippi Plan death toll, the registration series, the Nieman percentages, the Kousser poll-tax figure, and the Wilmington death toll remain open. Do not treat Jim Crow as a single law or a single moment. The “Black agency” row is not a claim that resistance was always successful.

---

#### Ch. 27, Table 1 — `ch27-table-01`

**Owner and location.** `chapters/27-chapter-27.md`, §6.4 The map of positions. **Display number:** Ch. 27, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare seven interpretations of populism and empire: status anxiety, democratic promise, modernizing politics, economic expansion and the Open Door, strategy and sea power, race/civilization/manhood, and decision/contingency. The table should connect the 1890s domestic crisis to the turn abroad.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Status anxiety and the agrarian myth** | Richard Hofstadter, *The Age of Reform* (1955) | Populism was a backward-looking protest by producers losing status in modernization, moved more by myth and conspiracy than by economics. | Made Populist ideology a serious historical problem and connected the rhetoric of producer grievance to later paranoid politics. | Critics found the Populists forward-looking and programmatic, and argued Hofstadter ignored the Omaha Platform and the Alliance’s economic experience.[^ch27-hofstadter][^ch27-hofstadter-wiki] |
| **Democratic promise and movement culture** | Lawrence Goodwyn, *Democratic Promise* (1976) and *The Populist Moment* (1978) | The Alliance’s cooperatives created a self-generated democratic culture, and Populism was an expansive, creative movement for a democratized industrial order. | Restored the cooperative movement and the Populists’ own goals to the center and showed the party grew out of economic experience. | Can romanticize the movement; the Alliance excluded Black farmers and its southern wing would not defend Black political rights.[^ch27-hofstadter][^ch27-colored-farmers] |
| **Modernizing, commercially engaged politics** | Michael Kazin, *The Populist Persuasion* (1995); Charles Postel, *The Populist Vision* (2007) | The Populists were connected to the wider world and proposed modern solutions to modern problems rather than a return to a vanished past. | Explains the movement’s breadth and its place in a long tradition of producer politics. | The tradition’s later uses can obscure the movement’s own racial and sectional limits.[^ch27-hofstadter][^ch27-colored-farmers] |
| **Economic expansion and the Open Door** | William Appleman Williams; Walter LaFeber, *The New Empire* (1963) | The search for markets and outlets for surplus production drove expansion, and 1898 was continuous with a long economic expansion rather than an aberration. | Connects the agrarian crisis and the business search for markets to the decision for empire and explains the Open Door. | Can make the outcome look foreordained and understates strategic, ideological, and contingent factors.[^ch27-empire-debate][^ch27-open-door] |
| **Strategy, sea power, and the “large policy”** | Alfred Thayer Mahan; Henry Cabot Lodge; Theodore Roosevelt | Naval power, coaling stations, and the defense of a projected canal made the Philippines and Hawaii strategically necessary. | Explains the timing and geography of the acquisitions and the role of the Navy’s advocates. | The “large policy” advocates did not alone decide; McKinley made the decision, and the argument explains intention better than outcome.[^ch27-empire-debate][^ch27-tnsr] |
| **Race, civilization, and manhood** | Rudyard Kipling, “The White Man’s Burden” (1899); Gail Bederman, *Manliness and Civilization* (1995) | Empire was justified as a civilizing duty of a superior race and as a proving ground for a vigorous manhood. | Explains the language of the debate — “the white man’s burden,” “benevolent assimilation,” “criminal aggression” — and the gendered rhetoric of empire. | Does not by itself explain the decision; Bederman and the poem’s reception were consulted only through summaries and must be read directly. |
| **Decision and contingency** | John Offner; the Texas National Security Review account of McKinley’s decision | McKinley chose annexation incrementally, with incomplete information, and the “inevitable” empire was the product of a specific decision. | Explains why the Philippines were taken despite the absence of a plan and restores agency to the decision. | Concentrates on the decision-maker and can slight the structural forces that made annexation thinkable.[^ch27-tnsr][^ch27-empire-debate] |

**Required caption.** Table 1. Populism, reform, and empire: positions on the movements of the 1890s and the turn to empire.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Hofstadter, Goodwyn, Kazin, Postel, Williams, LaFeber, Mahan, Lodge, Roosevelt, Offner, and Bederman were consulted at the level noted in the combined notes; Williams, LaFeber, Mahan’s writings, Offner, and Bederman remain unread and must be verified before publication. Status: `planned`.[^ch27-hofstadter][^ch27-hofstadter-wiki][^ch27-empire-debate][^ch27-tnsr][^ch27-open-door][^ch27-colored-farmers][^ch27-check-sources][^ch27-check-table]

**Required alt text.** A seven-row table comparing the status-anxiety and agrarian-myth interpretation, the democratic-promise and movement-culture interpretation, the modernizing-politics interpretation, the economic-expansion and Open Door interpretation, the strategy and sea-power interpretation, the race and civilization and manhood interpretation, and the decision and contingency interpretation of Populism, reform, and empire, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over Populism, reform, and empire.”

**Cautions and limitations.** The Bryan speech transcript, Kipling’s McClure’s text, the Beveridge and Hofstadter epigraphs, and the Omaha Platform need collation; the 1896 popular-vote totals, the Maine casualty counts, and the Philippine war death estimates remain open. Do not reduce populism to status anxiety or empire to a single economic motive. The “race, civilization, and manhood” row is not a decorative add-on; it is a causal argument.

---

#### Ch. 28, Table 1 — `ch28-table-01`

**Owner and location.** `chapters/28-chapter-28.md`, §6.4 The map of positions. **Display number:** Ch. 28, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare seven interpretations of 1890s culture: sacralization and cultural hierarchy, commercial leisure and working women’s agency, the new mass audience, incorporation and the culture of capitalism, antimodernism, the print marketplace, and racial/eugenic classification. The table should show how culture, commerce, and hierarchy interacted.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Sacralization and cultural hierarchy** | Lawrence W. Levine, *Highbrow/Lowbrow* (1988) | A shared nineteenth-century culture split into high and low as art was “sacralized” and removed from popular life. | Shows that hierarchy was made, not natural, and connects the era’s institutions to the loss of a common culture. | A national synthesis can understate the regional, racial, and working-class audiences that did not share the culture it describes.[^ch28-levine] |
| **Commercial leisure and working women’s agency** | Kathy Peiss, *Cheap Amusements* (1986); Roy Rosenzweig, *Eight Hours for What We Will* (1983) | Working people, and especially young women, used commercial amusements to build their own social worlds and identities. | Restores audiences and consumers as actors rather than victims of the culture industry. | Concentrates on a few cities and may understate the producers’ power to set the terms.[^ch28-peiss] |
| **Amusement and the new mass audience** | John F. Kasson, *Amusing the Million* (1978) | Coney Island’s parks knitted a heterogeneous crowd into a new mass audience and expressed the era’s break with Victorian order. | Reads commercial amusement as a sign of a cultural order in transition. | Treats the park as representative and can romanticize the crowd’s freedom.[^ch28-kasson] |
| **Incorporation and the culture of capitalism** | Alan Trachtenberg, *The Incorporation of America* (1982) | The Gilded Age incorporated culture along with the economy, reorganizing work, space, and meaning under corporate power. | Connects the era’s cultural forms to the political economy rather than treating them as decoration. | Can make the outcome too coherent and leave less room for contest and reversal.[^ch28-trachtenberg] |
| **Antimodernism and the search for authenticity** | T. J. Jackson Lears, *No Place of Grace* (1981) | Middle- and upper-class Americans answered corporate modernity with antimodernism that soothed rather than resisted it. | Explains why intense cultural protest could accommodate people to the new order. | Its subjects are elite and its “therapeutic” reading may understate genuine alternatives.[^ch28-lears] |
| **The print marketplace and its readers** | Richard Ohmann, *Selling Culture* (1996); Christopher Wilson, *The Labor of Words* (1985) | The cheap magazine was a business that built a national audience and a professional class of writers. | Shows how advertising, distribution, and authorship produced the mass reading public. | Focuses on the producers and the text more than on how readers used them.[^ch28-ohmann] |
| **Racial and eugenic classification** | Frederick L. Hoffman, *Race Traits* (1896); W. E. B. Du Bois, review (1897); Stephen Jay Gould, *The Mismeasure of Man* (1981) | The era’s sciences ranked peoples as a way of explaining inequality and justifying exclusion. | Centres race and shows that the ranking was a project of the sciences, not an outside intrusion. | Hoffman is a source and an object of study; Gould is a later critic and must not stand in for the 1890s debate.[^ch28-hoffman-jstor][^ch28-dubois-hoffman][^ch28-gould] |

**Required caption.** Table 1. Mass culture and hierarchy: positions on the culture of the American 1890s.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Levine, Peiss, Kasson, and Trachtenberg were consulted at the level noted in the combined notes; Lears, Ohmann, Wilson, Rosenzweig, and Gould were consulted only through publisher or reference descriptions and must be read before publication. Status: `planned`.[^ch28-check-sources][^ch28-check-table]

**Required alt text.** A seven-row table comparing the sacralization and cultural-hierarchy interpretation, the commercial-leisure and working-women’s-agency interpretation, the new-mass-audience interpretation, the incorporation-and-capitalism interpretation, the antimodernism interpretation, the print-marketplace interpretation, and the racial-and-eugenic-classification interpretation of the culture of the American 1890s, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over mass culture and cultural hierarchy.”

**Cautions and limitations.** The Comstock Act, Veblen, Levine, Howells, James, Rauschenbusch, and Brownie advertising quotations need collation; the newspaper and telephone series and denominators remain open; the 1897 catalogue facsimile’s rights are unresolved. Do not treat mass culture as either pure democratization or pure manipulation. The “racial and eugenic classification” row is part of the culture, not a separate topic.

---

#### Ch. 29, Table 2 — `ch29-table-02`

**Owner and location.** `chapters/29-chapter-29.md`, §6.4 The map of positions. **Display number:** Ch. 29, Table 2. **Status:** drafted, unverified.

**Purpose.** Compare seven interpretations of Progressivism: status anxiety, organizational synthesis, corporate regulation and the triumph of conservatism, grassroots and urban-working-class democracy, transatlantic reform networks, a progressive social movement, and illiberal reform. The table should make the debate over who drove reform and whom it excluded explicit.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Status anxiety and the producer ethic** | Richard Hofstadter, *The Age of Reform* (1955) | Reformers were old-stock middle-class people whose status was slipping, and their moral politics reflected a psychological rather than an economic discontent. | Explains the era’s moral fervor and its distance from class interest. | Its psychological reading can understate the material grievances and the working-class participation that other scholars document.[^ch29-glencoe-historians] |
| **Organizational synthesis and the search for order** | Robert H. Wiebe, *The Search for Order, 1877–1920* (1967) | A new professional middle class built national institutions to bring order to a society whose economy had outgrown its local institutions. | Connects reform to bureaucratic modernization rather than to moral impulse alone. | Its functionalism can make the outcome seem inevitable and leave less room for contingency and conflict.[^ch29-tyrrell-wiebe][^ch29-glencoe-historians] |
| **Corporate regulation and the triumph of conservatism** | Gabriel Kolko, *The Triumph of Conservatism* (1963); Martin J. Sklar, *The Corporate Reconstruction of American Capitalism* (1988) | Regulation was sought and shaped by corporate leaders to stabilize competition, not won from them by the public. | Exposes the interests behind reform and tests its rhetoric against its results. | Can overstate business control and understate the popular pressure that made regulation politically possible.[^ch29-glencoe-historians] |
| **Grassroots and urban-working-class democracy** | David P. Thelen, *The New Citizenship* (1972); J. Joseph Huthmacher (1962); John Buenker, *Urban Liberalism and Progressive Reform* (1973) | Reform drew on a broad coalition of ordinary citizens, including immigrants and urban workers, against corporate privilege. | Restores working-class and urban actors as makers of reform. | Concentrates on particular states and cities and can understate the top-down character of many measures.[^ch29-glencoe-historians] |
| **Transatlantic reform networks** | Daniel T. Rodgers, *Atlantic Crossings* (1998) | American reform was one part of a transatlantic traffic in social policy, not a purely national invention. | Situates reform in a wider world of ideas and institutions. | Can blur the distinctively American racial and federal context of the reforms.[^ch29-check-debate-works] |
| **A progressive social movement** | Michael McGerr, *A Fierce Discontent* (2003) | A middle-class movement set out to remake American society and, in falling short, shaped the political attitudes of the century that followed. | Treats reform as a coherent movement with a lasting cultural legacy. | Its focus on the middle class can slight the workers, immigrants, and Black reformers who joined or resisted the movement.[^ch29-mcgerr] |
| **Illiberal reform: race, eugenics, and exclusion** | Thomas C. Leonard, *Illiberal Reformers* (2016) | The economic progressives’ reform agenda rested on eugenic and racial assumptions that made exclusion central to the movement, not incidental to it. | Takes the exclusions seriously as a product of reform’s own logic. | Its focus on the economists can understate the reformers who opposed racism and the Black reformers who pressed their own claims.[^ch29-check-debate-works] |

**Required caption.** Table 2. Progressive reform and its limits: positions on the Progressive movement.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The Hofstadter, Wiebe, Kolko, Sklar, Thelen, Huthmacher, and Buenker positions were consulted through the McGraw-Hill companion summary and the Tyrrell retrospective on Wiebe; McGerr was consulted through a study-guide reproduction; and Rodgers and Leonard were discovered through publisher and review descriptions and not yet read. Status: `planned`.[^ch29-glencoe-historians][^ch29-tyrrell-wiebe][^ch29-mcgerr][^ch29-check-debate-works][^ch29-check-sources]

**Required alt text.** A seven-row table comparing the status-anxiety interpretation, the organizational-synthesis interpretation, the corporate-regulation interpretation, the grassroots-democracy interpretation, the transatlantic-networks interpretation, the progressive-social-movement interpretation, and the illiberal-reform interpretation of the Progressive movement, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 2 compares the positions that organize the debate over Progressive reform and its limits.”

**Cautions and limitations.** The Roosevelt, Progressive-platform, and McGerr epigraphs, the Sinclair/Dunne/muckrake quotations, and the Muller opinion need collation; the 1912 figures, the Triangle death-count range, and the conservation acreage need reconciliation. Do not equate reform with democracy; the illiberal row is part of the story. The “social movement” row is a later analytical frame; do not project it onto every reformer.

---

#### Ch. 30, Table 2 — `ch30-table-02`

**Owner and location.** `chapters/30-chapter-30.md`, §6.4 The map of positions. **Display number:** Ch. 30, Table 2. **Status:** drafted, unverified.

**Purpose.** Compare nine positions on American power abroad and the decision for war: aberration, economic Open Door imperialism, Caribbean hegemony, the promotional state and informal empire, ideology and racial hierarchy, gender and manhood, continuity and connection, German actions, and economic tilt. The table should show that the debate is about the mix of motives, not a single switch.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Aberration** | Samuel Flagg Bemis (1936) | Overseas colonization, especially of the Philippines, departed from American tradition and overextended the nation’s resources. | Focuses on the policy’s costs and its distance from continental precedent. | Its “aberration” frame can understate the continuities of conquest and the durability of overseas rule.[^ch30-shibusawa] |
| **Economic Open Door imperialism** | William Appleman Williams, *The Tragedy of American Diplomacy* (1959); Walter LaFeber, *The New Empire* (1963) | The search for markets, expressed in the Open Door policy, drove expansion and shaped foreign relations after 1900. | Connects diplomacy to the industrial economy and to a strategy of informal control. | Can make economic interest the master key and slight ideology, security, and contingency.[^ch30-williams-tragedy][^ch30-lafeber-new-empire] |
| **Caribbean hegemony** | David Healy, *Drive to Hegemony* (1988) | The United States built a regional hegemony in the Caribbean basin through a mix of instruments, with strategic and commercial motives intertwined. | Integrates the piecemeal Caribbean interventions into a single regional policy. | A regional focus can underplay the Pacific and the European war decision.[^ch30-healy-drive] |
| **Promotional state and informal empire** | Emily S. Rosenberg, *Spreading the American Dream* (1982) | Government worked with private business and cultural agencies to expand American economic and cultural influence from the 1890s onward. | Shows how formal and informal power worked together rather than in sequence. | Can blur coercion and persuasion when measuring influence.[^ch30-rosenberg-dream] |
| **Ideology and racial hierarchy** | Michael H. Hunt, *Ideology and U.S. Foreign Policy* (1987) | A durable ideology of national mission and racial hierarchy shaped how Americans understood other peoples and justified intervention. | Restores ideas and race to the center of diplomatic history. | Can underweight material and strategic interests in particular decisions.[^ch30-hunt-ideology] |
| **Gender and manhood** | Kristin L. Hoganson, *Fighting for American Manhood* (1998); Gail Bederman, *Manhood and “Civilization”* (1995) | Ideas about manhood and civilization helped provoke and sustain the imperial wars and interventions. | Reveals the cultural fuel of empire that interest-based accounts miss. | Focused on the 1890s wars and may travel less well to the neutrality years.[^ch30-hoganson-bederman] |
| **Continuity and connection** | Paul A. Kramer, “Power and Connection” (2011) | U.S. empire is best studied as a connected history of power across metropole and colony, not as an aberration or a single economic logic. | Offers a synthetic frame that holds formal and informal empire together. | Its breadth can make particular episodes harder to adjudicate.[^ch30-kramer-imperial] |
| **German actions forced the decision** | Office of the Historian, *U.S. Entry into World War I* | German violations of neutral rights, especially unrestricted submarine warfare and the Zimmermann Telegram, made entry necessary by 1917. | Documents the sequence and the documents that moved Congress. | An official account can understate the Allied tilt and the dissent at home.[^ch30-state-wwi] |
| **Economic tilt and the drift to war** | Charles A. Beard, *The Devil Theory of War* (1936) | Neutral rights became a rationale for protecting the loans and trade that tied the United States to the Allies. | Forces attention to the material stake in an Allied victory. | Can understate genuine outrage at submarine warfare and Wilson’s own reasoning.[^ch30-beard-devil][^ch30-cfr-lafollette] |

**Required caption.** Table 2. Informal empire and intervention: positions on American power abroad and the decision for war.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The essay by Naoko Shibusawa was read in full for the aberration, economic, ideological, and gender positions; the works by Williams, LaFeber, Healy, Rosenberg, Hunt, Hoganson, Bederman, Kramer, and Beard were discovered through reviews, descriptions, and citations and were not read in full. Status: `planned`.[^ch30-shibusawa][^ch30-williams-tragedy][^ch30-lafeber-new-empire][^ch30-healy-drive][^ch30-rosenberg-dream][^ch30-hunt-ideology][^ch30-hoganson-bederman][^ch30-kramer-imperial][^ch30-beard-devil][^ch30-state-wwi][^ch30-check-debate-works]

**Required alt text.** A nine-row table comparing the aberration, economic Open Door, Caribbean hegemony, promotional state, ideology and racial hierarchy, gender and manhood, continuity and connection, German-actions, and economic-tilt interpretations of American power abroad, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 2 compares the positions that organize the debate over informal empire and intervention.”

**Cautions and limitations.** The La Follette quotation, the Roosevelt 1904 message, the Lusitania death toll (1,195 including 123 Americans versus 1,198 including 128), the Veracruz and Columbus casualty figures, and the Bryan–Chamorro terms remain open. Do not use “isolationism” or “empire” as undifferentiated labels. The “German actions” and “economic tilt” rows are explanations of the decision for war, not full accounts of the era.

---

#### Ch. 31, Table 3 — `ch31-table-03`

**Owner and location.** `chapters/31-chapter-31.md`, §6.4 The map of positions. **Display number:** Ch. 31, Table 3. **Status:** drafted, unverified.

**Purpose.** Compare nine positions on total mobilization: the war welfare state, improvisation and dissolution, popular coercion, civil liberties and the state, race and the war for democracy, suffrage as culmination, suffrage memory and exclusion, treaty failure as Wilson’s rigidity, and treaty failure as constitutional threshold. The table should connect the war’s domestic transformation to its international failure.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **War welfare state** | Ronald Schaffer, *America in the Great War* (1991) | The war built a durable “war welfare state” that took responsibility for soldiers, veterans, and the economy and set precedents for later federal action. | Connects mobilization, benefits, and administration into a single account of state growth. | May overstate durability when the wartime agencies were largely dismantled after 1918.[^ch31-schaffer-welfare-state] |
| **Improvised and dissolved** | David M. Kennedy, *Over Here* (1980) | The mobilization was improvised and administered unevenly, and much of the war state was dismantled after the armistice. | Shows the gap between the announced program and the actual administration. | A focus on the war years can underplay the capacities and expectations that survived.[^ch31-kennedy-over-here] |
| **Popular coercion** | Christopher Capozzola, *Uncle Sam Wants You* (2008) | Wartime loyalty was enforced by citizens as a matter of civic obligation, not only by federal officials, and this obligation outlasted the war. | Restores ordinary people to the history of wartime repression. | Blurs the line between state action and private violence if not carefully drawn.[^ch31-capozzola-unc-sam] |
| **Civil liberties and the state** | Paul L. Murphy, *World War I and the Origin of Civil Liberties in the United States* (1979) | The war’s repression provoked the modern civil-liberties movement as much as it crushed dissent. | Explains how resistance to the Sedition Act produced lasting organizations and arguments. | Can read later civil-liberties institutions back into wartime actors.[^ch31-murphy-civil-liberties] |
| **Race and the war for democracy** | Adriane Lentz-Smith, *Freedom Struggles* (2009); Chad Williams, *Torchbearers of Democracy* (2010) | Black soldiers and communities used the war’s rhetoric of democracy to press claims at home, even as the army and the state enforced the color line. | Puts Black agency and the wartime contradiction at the center of the war’s meaning. | The South’s violence and the limits of wartime gains can be understated if the focus stays on assertion.[^ch31-lentz-smith][^ch31-williams-torchbearers] |
| **Suffrage as culmination** | Carrie Chapman Catt’s “winning plan,” as described in the National Archives account | The Nineteenth Amendment crowned decades of coordinated state and federal campaigning and completed the enfranchisement of women. | Captures the movement’s organization and the amendment’s achievement. | Can underplay the movement’s racial exclusions and the amendment’s limited reach.[^ch31-nara-19th-amendment][^ch31-tetrault-suffrage] |
| **Suffrage memory and exclusion** | Lisa Tetrault, *The Myth of Seneca Falls* (2014) | The standard suffrage story simplifies a movement that was divided and exclusionary, and the amendment’s constitutional meaning remained contested. | Restores conflict and exclusion to the history of the amendment. | Can make the amendment’s real enfranchisement of millions of women seem merely rhetorical.[^ch31-tetrault-myth][^ch31-tetrault-suffrage] |
| **Treaty failure as Wilson’s rigidity** | U.S. Senate, “Senate Rejects the Treaty of Versailles” | Wilson’s refusal to accept reservations and his insistence on the League as written made ratification impossible. | Documents the personal and procedural collapse of the ratification fight. | Can underplay Republican partisanship and the institutional two-thirds barrier.[^ch31-state-versailles] |
| **Treaty failure as constitutional threshold** | U.S. Capitol Visitor Center; Department of State *Foreign Relations* | The decisive obstacle was the two-thirds requirement, which repeated majorities could not meet. | Isolates the institutional rule that decided the outcome. | Explains the arithmetic but not the politics that produced the votes.[^ch31-capitol-senate-votes][^ch31-state-gov-peace] |

**Required caption.** Table 3. Wartime state and democratic coercion: positions on what total mobilization did to the American state and to democratic citizenship.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The National Archives, U.S. Senate, U.S. Capitol Visitor Center, and Department of State sources were read for this outline; the works by Schaffer, Kennedy, Capozzola, Murphy, Lentz-Smith, Williams, and Tetrault were discovered through bibliographies and descriptions and were not read in full. Status: `planned`.[^ch31-schaffer-welfare-state][^ch31-kennedy-over-here][^ch31-capozzola-unc-sam][^ch31-murphy-civil-liberties][^ch31-lentz-smith][^ch31-williams-torchbearers][^ch31-tetrault-myth][^ch31-state-versailles][^ch31-capitol-senate-votes][^ch31-state-gov-peace][^ch31-check-debate-works]

**Required alt text.** A nine-row table comparing the war-welfare-state, improvised-mobilization, popular-coercion, civil-liberties, race-and-democracy, suffrage-as-culmination, suffrage-memory, Wilsonian-rigidity, and constitutional-threshold interpretations of the wartime state, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 3 compares the positions that organize the debate over the wartime state and democratic coercion.”

**Cautions and limitations.** The Wilson, Debs, and Tetrault epigraphs need collation; the Senate vote tallies (39–55, 38–53, 49–35) and the dating of the second vote need direct Congressional Record roll calls; the Committee on Public Information figures need archival records. Do not treat the treaty’s defeat as a single-cause story. The suffrage rows must distinguish the Nineteenth Amendment from the persistence of state-level exclusion.

---

#### Ch. 32, Table 2 — `ch32-table-02`

**Owner and location.** `chapters/32-chapter-32.md`, §6.4 The map of positions. **Display number:** Ch. 32, Table 2. **Status:** drafted, unverified.

**Purpose.** Compare eight positions on the 1920s: culture war, modern temper, discontented America, nativism as the through-line, the Harlem Renaissance as Black modernity, the transnational New Negro, uneven prosperity, and regulation and the new state. The table should show how the decade’s prosperity, culture, and exclusion fit together.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Culture war** | William E. Leuchtenburg, *The Perils of Prosperity* (1958) | The decade was a contest between an emerging modern, urban culture and a defensive traditionalism. | Frames the decade as a conflict of values with lasting political stakes. | Can reduce political economy and race to a clash of cultures.[^ch32-leuchtenburg-perils] |
| **Modern temper** | Lynn Dumenil, *The Modern Temper* (1995) | Mass culture, consumerism, and the new middle class were the decade’s central integrative forces. | Puts consumption and popular culture at the center of the analysis. | Can underplay the coercion and exclusion built into the same culture.[^ch32-dumenil-modern-temper] |
| **Discontented America** | David Goldberg, *Discontented America* (1999) | The 1920s were a distinctive postwar period of reaction, restriction, and political economy, not merely a culture war. | Restores politics, policy, and nativism to the decade’s history. | Can understate the genuine cultural creativity of the same years.[^ch32-goldberg-discontented] |
| **Nativism as the through-line** | John Higham, *Strangers in the Land* (1955) | Immigration restriction and racial nativism were the decade’s defining political achievements. | Explains the quota acts and the Klan as one movement. | A focus on restriction can slight Black and labor history.[^ch32-higham-strangers] |
| **Harlem Renaissance as Black modernity** | Nathan Huggins, *Harlem Renaissance* (1971); David Levering Lewis, *When Harlem Was in Vogue* (1981) | The Renaissance was a self-conscious Black modernism that redefined American culture. | Establishes Black artists and intellectuals as central, not marginal, to the decade. | Class and patronage limits can be underplayed.[^ch32-huggins-harlem][^ch32-lewis-when-harlem] |
| **Transnational New Negro** | Brent Hayes Edwards, *The Practice of Diaspora* (2003) | Black internationalism and diaspora networks shaped the Renaissance and Garveyism alike. | Connects Harlem to the Caribbean, Africa, and Europe. | Can underplay local, city-level political struggles.[^ch32-edwards-diaspora] |
| **Uneven prosperity** | Agricultural and economic histories of the farm depression | The decade’s prosperity was regional and sectoral, and agriculture suffered throughout. | Explains the rural distress that preceded the Depression. | A sectoral focus can obscure the decade’s new mass consumption.[^ch32-coolidge-mcnary][^ch32-digitalhistory-consumer] |
| **Regulation and the new state** | Histories of broadcasting and the Radio Act (FCC; Library of Congress) | The decade created the institutions of federal broadcast regulation that governed the medium for decades. | Shows how a new technology produced a new federal capacity. | Can make regulation seem more coherent than its crowding-driven origins.[^ch32-fcc-radio][^ch32-loc-law-radio] |

**Required caption.** Table 2. Modernity, prosperity, and belonging: positions on what the 1920s did to American culture, economy, and membership.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The Federal Communications Commission, the Library of Congress, and the Coolidge Foundation sources were read for this outline; the works by Leuchtenburg, Dumenil, Goldberg, Higham, Huggins, Lewis, and Edwards were discovered through bibliographies, descriptions, or reviews and were not read in full. Status: `planned`.[^ch32-check-table2][^ch32-check-debate-works]

**Required alt text.** An eight-row table comparing the culture-war, modern-temper, discontented-America, nativism, Harlem-Renaissance, transnational-New-Negro, uneven-prosperity, and broadcast-regulation interpretations of the 1920s, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 2 compares the positions that organize the debate over modernity, prosperity, and belonging in the 1920s.”

**Cautions and limitations.** The Harding, Hughes, and Zeitz epigraphs need collation; the 1924 interim quota and 1929 national-origins figures need the actual quota schedules; the Klan membership, Tulsa death toll, farm figures, and Mellon tax rates rest on summaries. Do not let the “Roaring Twenties” label erase rural distress or racial violence. The “Harlem Renaissance” row must not treat Black cultural production as a decorative accompaniment to White modernity.

---

#### Ch. 33, Table 1 — `ch33-table-01`

**Owner and location.** `chapters/33-chapter-33.md`, §6.4 The map of positions. **Display number:** Ch. 33, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare eight explanations of the Depression: monetary contraction, spending collapse, gold-standard transmission, international leadership vacuum, financial frictions, structural inequality, policy failure, and regime uncertainty. The table should show how the same contraction becomes a different catastrophe depending on the mechanism.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Monetary contraction** | Milton Friedman and Anna Schwartz, *A Monetary History of the United States* (1963) and *The Great Contraction, 1929–1933* (1965) | The Federal Reserve’s failure to prevent bank failures and the collapse of the money stock caused and deepened the Depression. | Explains the depth and length and the counterfactual role of the central bank. | Can treat the money stock as more exogenous than the evidence allows and underplay nonmonetary channels.[^ch33-frh-great-depression] |
| **Spending collapse** | Peter Temin, *Did Monetary Forces Cause the Great Depression?* (1976); Christina Romer, “The Great Crash and the Onset of the Great Depression” (1990) | The initial downturn came from a fall in autonomous spending and a crash-induced collapse in purchases of durable goods; money responded. | Grounds the onset in the real economy and household behavior. | Struggles to explain the Depression’s depth and international synchronicity.[^ch33-frh-crash][^ch33-check-debate-works] |
| **Gold-standard transmission** | Barry Eichengreen, *Golden Fetters* (1992); Barry Eichengreen and Peter Temin, “The Gold Standard and the Great Depression” (2000) | Adherence to the interwar gold standard and the gold-standard mentality transmitted deflation and paralyzed policy; countries leaving gold recovered first. | Explains the worldwide reach and the timing of recovery. | Can make policy ideas the main actor and underplay domestic banking structure.[^ch33-eichengreen-temin] |
| **International leadership vacuum** | Charles Kindleberger, *The World in Depression, 1929–1939* (1973) | With Britain unable and the United States unwilling to act as international lender and stabilizer, the system had no leader to halt the slide. | Explains the failure of international coordination, including the London conference of 1933. | Hegemonic-stability logic can be deterministic and hard to test.[^ch33-kindlberger-cepr][^ch33-state-gold] |
| **Financial frictions** | Ben Bernanke, “Nonmonetary Effects of the Financial Crisis…” (1983); Charles Calomiris and Joseph Mason (2003); Gary Richardson | Bank failures destroyed credit information and intermediation, suppressing output beyond the money-supply effect. | Links banking structure to real output; regional evidence from Fed district borders. | Distinguishing illiquidity from insolvency remains contested.[^ch33-frh-banking-panics] |
| **Structural inequality** | John Kenneth Galbraith, *The Great Crash 1929* (1955); later underconsumption accounts | A maldistribution of income left consumption unable to absorb productive capacity; the boom made the economy fragile. | Connects the 1920s boom’s unevenness to the collapse. | Inequality alone did not set the timing, and underconsumption is hard to test.[^ch33-pew-inequality][^ch33-check-inequality] |
| **Policy failure** | Herbert Hoover’s voluntarism; the Federal Reserve’s real-bills doctrine; balanced-budget orthodoxy | Leaders applied a framework that made them act late and sometimes perversely — the 1931 rate rise, the 1932 tax increase. | Identifies specific decisions with measurable harm. | Risk of retrospective blame that underplays structural constraints.[^ch33-hoover-archives][^ch33-oertx-hoover] |
| **Regime uncertainty** | Robert Higgs; Amity Shlaes, *The Forgotten Man* (2007) | Uncertainty created by the New Deal discouraged investment and prolonged the recovery. | Focuses attention on investment and expectations. | Addresses the recovery after 1933, not the 1929–33 collapse it is often asked to explain.[^ch33-smiley-econlib][^ch33-check-debate-works] |

**Required caption.** Table 1. Causes and transmission of depression: positions on why a contraction became a catastrophe.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The Federal Reserve, Federal Deposit Insurance Corporation, Department of State, and Federal Reserve Bank of St. Louis sources were read for this outline; the works by Friedman and Schwartz, Temin, Eichengreen, Kindleberger, Bernanke, Calomiris and Mason, Richardson, Galbraith, Higgs, and Shlaes were identified through those sources and their bibliographies and were not read in full. Status: `planned`.[^ch33-check-table1][^ch33-check-debate-works]

**Required alt text.** An eight-row table comparing the monetary-contraction, spending-collapse, gold-standard, international-leadership, financial-frictions, structural-inequality, policy-failure, and regime-uncertainty interpretations of the Great Depression, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the causes and transmission of the Depression.”

**Cautions and limitations.** The Hoover, Bernanke, and Eichengreen–Temin epigraphs need collation; the unemployment (Lebergott/Darby), foreclosure, income-share, and bank-suspension figures rest on summaries; Friedman–Schwartz, Temin, Eichengreen, Kindleberger, Bernanke, Calomiris–Mason, Richardson, Galbraith, Higgs, and Shlaes were not read in full. Do not present one mechanism as the consensus. The “regime uncertainty” row is a hypothesis about expectations, not a measured quantity.

---

#### Ch. 34, Table 1 — `ch34-table-01`

**Owner and location.** `chapters/34-chapter-34.md`, §6.4 The map of positions. **Display number:** Ch. 34, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare eight interpretations of the New Deal: incomplete revolution, liberal state-building, capitalism preserved, racial exclusion, administrative feasibility, gendered two-track welfare, labor power from below, and business and the associational state. The table should weigh transformation, preservation, and exclusion together.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Incomplete revolution** | William E. Leuchtenburg, *Franklin D. Roosevelt and the New Deal, 1932–1940* (1963) | The New Deal transformed federal responsibility but stopped short of a full redistribution of power and income. | Captures the scale of change and its limits in one frame. | Can make the New Deal’s incompleteness a matter of will rather than structure.[^ch34-leuchtenburg] |
| **Liberal state-building** | Alan Brinkley, *The End of Reform* (1995); Theda Skocpol, *Protecting Soldiers and Mothers* (1992) | The New Deal built durable federal institutional capacity and redefined the public responsibilities of the state. | Explains why the institutions outlasted the political coalition that created them. | Can underplay how narrowly the new capacity was distributed.[^ch34-brinkley][^ch34-skocpol] |
| **Capitalism preserved** | Barton J. Bernstein, “The New Deal: The Conservative Achievements of Liberal Reform” (1968) | The New Deal stabilized and reorganized capitalism without transferring power or wealth. | Takes seriously the interests the settlement protected. | Can flatten genuine gains in security and rights into mere stabilization.[^ch34-bernstein] |
| **Racial exclusion** | Ira Katznelson, *When Affirmative Action Was White* (2005); the scholars surveyed in DeWitt (2010), among them Robert Lieberman | Southern power shaped the occupational exclusions so that social provision entrenched a racial gap. | Puts race at the center of program design, not at its margins. | Intent is inferred; administrative explanations remain possible for parts of the record.[^ch34-katznelson][^ch34-dewitt-exclusions] |
| **Administrative feasibility** | Larry DeWitt, “The Decision to Exclude Agricultural and Domestic Workers…” (2010) | The exclusions followed from the difficulty of collecting payroll taxes from farm and domestic work, not from racial motive. | Grounds the exclusions in the mechanics of tax administration. | May underplay the racial effects and the southern political context.[^ch34-dewitt-exclusions] |
| **Gendered two-track welfare** | Linda Gordon, *Pitied but Not Entitled* (1994); Theda Skocpol, *Protecting Soldiers and Mothers* (1992) | Insurance for (mostly male) workers and stigmatized assistance for mothers created a stratified welfare state. | Explains the durable split between “social insurance” and “welfare.” | Can treat the 1935 design as more settled than the contested record shows.[^ch34-gordon-welfare][^ch34-skocpol] |
| **Labor power from below** | Lizabeth Cohen, *Making a New Deal* (1990); Nelson Lichtenstein, *State of the Union* (2002) | Workers’ own institutions and mobilization, more than federal law alone, produced the labor settlement. | Restores agency to the people the New Deal governed. | Can underplay the state’s role in protecting and then containing unions.[^ch34-cohen][^ch34-lichtenstein] |
| **Business and the associational state** | Colin Gordon, *New Deals* (1994); Frances Fox Piven and Richard A. Cloward, *Poor People’s Movements* (1977) | Business interests shaped the recovery institutions, while disruptive protest from below forced relief and reform. | Connects policy design to both organized capital and organized pressure. | The two claims pull in different directions and need separate testing.[^ch34-colin-gordon][^ch34-piven-cloward] |

**Required caption.** Table 1. New Deal transformation and exclusions: positions on what the New Deal built and whom it protected.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The Social Security Administration’s and Federal Reserve’s records and the primary statutes named in the notes were read for this outline; the works by Leuchtenburg, Bernstein, Brinkley, Skocpol, Gordon, Cohen, Lichtenstein, Colin Gordon, and Piven and Cloward were identified through catalogs, publisher descriptions, or teaching summaries and were not read in full. Status: `planned`.[^ch34-check-table1][^ch34-check-debate-works]

**Required alt text.** An eight-row table comparing the incomplete-revolution, liberal-state-building, capitalism-preserved, racial-exclusion, administrative-feasibility, gendered-two-track-welfare, labor-power-from-below, and business-and-protest interpretations of the New Deal, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the New Deal’s transformation and its exclusions.”

**Cautions and limitations.** The Roosevelt, Long, and Katznelson epigraphs need collation; the Social Security exclusions’ parallel Title II definition and the $3,000 cap need checking; the CCC, TVA, and Dust Bowl figures rest on summaries; the Memorial Day Massacre counts need the La Follette Committee records. Do not treat the New Deal as a single program or a single verdict. The “capitalism preserved” row is not a claim that nothing changed.

---

#### Ch. 35, Table 1 — `ch35-table-01`

**Owner and location.** `chapters/35-chapter-35.md`, §6.4 The map of positions. **Display number:** Ch. 35, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare seven positions on how the United States entered the Second World War: revisionist back door, orthodox response to aggression, reluctant belligerent, political contest, strategic manager, economic conflict in the Pacific, and escalation/synthesis. The table should show how agency, economics, and strategy are weighted.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Revisionist: the back door to war** | Charles A. Beard, *President Roosevelt and the Coming of the War, 1941* (1948) | Roosevelt moved the country from neutrality to armed intervention behind the appearance of neutrality, without a candid case to the public. | Takes the gap between Roosevelt’s public posture and his private steps seriously and reads the records closely. | Attributes a single intention and can treat preparation as proof of a plan to provoke attack.[^ch35-beard] |
| **Orthodox: response to aggression** | William L. Langer and S. Everett Gleason, *The Challenge to Isolation* (1952) and *The Undeclared War* (1953) | Roosevelt responded to Axis aggression, moving only as far as events and public opinion allowed. | Integrates diplomacy and strategy across the Atlantic and the Pacific. | Can make Roosevelt’s choices appear the only responsible ones.[^ch35-langer-gleason] |
| **Reluctant belligerent** | Robert A. Divine, *The Reluctant Belligerent* (1965) | Roosevelt advanced aid cautiously because public opinion constrained him; entry followed Japanese and German decisions. | Foregrounds domestic opinion as a real limit on policy. | Can understate Roosevelt’s own initiative and the effect of his measures on Axis choices.[^ch35-divine] |
| **Political contest** | Wayne S. Cole, *Roosevelt and the Isolationists* (1983) | The outcome turned on an organized contest between Roosevelt and a durable isolationist coalition. | Restores the isolationists as serious actors with arguments. | Focuses on the American arena and can underweight foreign decisions.[^ch35-cole] |
| **Strategic manager** | Waldo Heinrichs, *Threshold of War* (1988) | Roosevelt acted as a global strategic manager, balancing Europe-first priorities and the Pacific crisis in 1941. | Shows the summer and fall of 1941 as an integrated strategic problem. | Can make the policy more coherent than the record shows.[^ch35-heinrichs] |
| **Economic conflict in the Pacific** | Michael A. Barnhart, *Japan Prepares for Total War* (1987) | Japan’s resource dependence and the American embargo made war a calculated response to economic strangulation. | Connects the sanctions to Japan’s decision for war. | Explains Japan’s choice more than Washington’s and can make the embargo a sufficient cause.[^ch35-barnhart] |
| **Escalation and synthesis** | David M. Kennedy, *Freedom from Fear* (1999) | The two powers stepped through escalating moves that provoked but failed to restrain each other. | Holds structure and contingency together in one frame. | A synthesis, not a source of new archival evidence on the entry decision.[^ch35-kennedy] |

**Required caption.** Table 1. Neutrality, intervention, and choice: positions on how the United States entered the Second World War.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The primary statutes, addresses, and official accounts named in the notes were read for this outline; the works by Beard, Langer and Gleason, Divine, Cole, Heinrichs, Barnhart, and Kennedy were identified through catalogs, publisher descriptions, or another work’s citation and were not read in full. Status: `planned`.[^ch35-check-table1][^ch35-check-debate-works]

**Required alt text.** A seven-row table comparing the revisionist, orthodox, reluctant-belligerent, political-contest, strategic-manager, economic-conflict, and escalation interpretations of the American entry into the Second World War, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over how the United States entered the Second World War.”

**Cautions and limitations.** The domestic reaction to the Chicago address has no consulted source; no 1939–41 polling series was consulted, so the public-choice debate is under-sourced; the Japanese decision-making side rests on American accounts; the Reuben James death toll and the December 1941 roll calls need direct sources. Do not treat Pearl Harbor as the inevitable result of a single policy. The “revisionist” row must be stated fairly before it is criticized.

---

#### Ch. 36, Table 1 — `ch36-table-01`

**Owner and location.** `chapters/36-chapter-36.md`, §6.4 The map of positions. **Display number:** Ch. 36, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare eight positions on the Second World War’s strategy, exclusions, and endings: military necessity in the Pacific, atomic diplomacy, Soviet entry, coalition bargaining, race war, mobilization as political economy, the “good war” questioned, and abandonment of the Jews. The table should connect battlefield decisions, coalition politics, and the war’s moral costs.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Military necessity in the Pacific** | Henry L. Stimson, “The Decision to Use the Atomic Bomb,” *Harper’s* (1947); Harry S. Truman | The bombs ended the war quickly and avoided an invasion of Japan that would have cost hundreds of thousands of lives. | Takes the projected invasion casualties and the decision-makers’ reasoning seriously. | Reads decisions after the fact and can treat the bomb as the only alternative.[^ch36-stinson] |
| **Atomic diplomacy** | Gar Alperovitz, *Atomic Diplomacy* (1965) and *The Decision to Use the Atomic Bomb* (1995) | Japan was near defeat, and the bomb was used partly to end the war before the Soviet Union could claim a share of the victory in Asia. | Reads the timing of the bombings against the diplomacy of the Soviet entry. | Can attribute a single motive and discount the invasion’s projected cost.[^ch36-alperovitz] |
| **Soviet entry decisive** | Tsuyoshi Hasegawa, *Racing the Enemy* (2005) | The Soviet declaration of war on August 8, 1945 played the greater role in Japan’s surrender; the bombs’ effect has been overstated. | Uses Japanese and Soviet sources and re-centers the surrender decision. | Contested by historians who read the imperial records differently.[^ch36-hasegawa] |
| **Coalition bargaining** | Mark A. Stoler, *Allies and Adversaries* (2000) | Strategy emerged from bargaining among allies, and the Joint Chiefs became a major instrument of American foreign policy. | Integrates military strategy with alliance politics and civil–military relations. | Focuses on the Anglo-American chiefs and underweights other allies.[^ch36-stoler] |
| **Race war** | John W. Dower, *War Without Mercy* (1986) | The Pacific war was a race war, and racial ideology shaped combat, atrocity, and memory on both sides. | Links battlefront conduct to home-front racism and to the incarceration. | Explains the Pacific better than the war against Germany.[^ch36-dower] |
| **Mobilization as political economy** | David M. Kennedy, *Freedom from Fear* (1999) | American war production was a negotiated mobilization whose distribution of gains and costs shaped the postwar order. | Holds economic, social, and political change in one frame. | A synthesis, not a source of new production records.[^ch36-kennedy] |
| **The “good war” questioned** | Studs Terkel, *“The Good War”* (1984) | The remembered “good war” was a partial memory that obscured the war’s exclusions, its violence, and the experience of the defeated. | Restores ordinary and dissenting voices to the war’s history. | Oral history is retrospective testimony and not a measure of wartime opinion.[^ch36-terkel] |
| **Abandonment of the Jews** | David S. Wyman, *The Abandonment of the Jews* (1984) | American officials knew enough to act and chose not to divert resources to rescue European Jews. | Establishes the timing and limits of American rescue policy. | Can treat feasibility as established when it was contested at the time.[^ch36-wyman] |

**Required caption.** Table 1. Coalition, citizenship, and the war’s endings: positions on the Second World War’s strategy, its exclusions, and its endings.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The primary documents, official accounts, and commission report named in the notes were read for this outline; the works by Stimson, Alperovitz, Hasegawa, Stoler, Dower, Kennedy, Terkel, and Wyman were identified through catalogs, publisher descriptions, reviews, or another work’s citation and were not read in full. Status: `planned`.[^ch36-check-table1][^ch36-check-debate-works]

**Required alt text.** An eight-row table comparing the military-necessity, atomic-diplomacy, Soviet-entry, coalition-bargaining, race-war, mobilization, “good-war,” and abandonment interpretations of the Second World War’s strategy, exclusions, and endings, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the war’s coalition, its exclusions, and its endings.”

**Cautions and limitations.** The Roosevelt cable, the commission phrase, the Jackson dissent, and the Churchill speech need collation; reconcile the 122,000/120,000 incarceration figures and the about 12,000/about 78,000 questionnaire counts; global mortality estimates remain method-dependent. Do not use “military necessity” as a self-validating claim. The “abandonment of the Jews” row is a body of scholarship, not a rhetorical accusation.

---

#### Ch. 37, Table 1 — `ch37-table-01`

**Owner and location.** `chapters/37-chapter-37.md`, §6.4 The map of positions. **Display number:** Ch. 37, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare nine positions on Cold War origins and domestic consequences: orthodox, realist leadership, Open Door revisionism, atomic diplomacy, post-revisionist synthesis, national security, new Cold War history, Korea as civil war, and domestic anticommunism. The table should connect the international and domestic Cold Wars.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Orthodox** | Herbert Feis, *Churchill, Roosevelt, Stalin* (1957); Thomas A. Bailey | Soviet expansion and broken wartime agreements caused the Cold War; American policy was a defensive response. | Establishes the sequence of broken agreements and the Soviet consolidation of Eastern Europe. | Reads American motives as defensive and discounts American power.[^ch37-orthodox-works] |
| **Realist leadership** | Arthur Schlesinger Jr., “Origins of the Cold War” (1967) | The conflict arose from two universalist powers meeting in a European power vacuum. | Centers the structural vacuum left by the war. | Treats Soviet and American aims as symmetrical.[^ch37-orthodox-works] |
| **Open Door revisionism** | William Appleman Williams, *The Tragedy of American Diplomacy* (1959); Walter LaFeber, *America, Russia, and the Cold War* (1967) | American capitalism’s need for markets and the Open Door drove expansion and confrontation. | Connects foreign policy to political economy. | Can make economics the single cause.[^ch37-revisionist-works] |
| **Atomic diplomacy** | Gar Alperovitz, *Atomic Diplomacy* (1965) | The bomb and the atomic monopoly were used as leverage against the Soviet Union. | Reads the bomb’s timing against the diplomacy of 1945. | Attributes a single motive and is contested.[^ch37-revisionist-works] |
| **Post-revisionist synthesis** | John Lewis Gaddis, *The United States and the Origins of the Cold War, 1941–1947* (1972) | Neither side bore sole responsibility; security dilemmas and misperception mattered. | Balances documentation from both sides. | Critics call it a return to orthodoxy.[^ch37-postrevisionist-works] |
| **National security** | Melvyn P. Leffler, *A Preponderance of Power* (1992) | American leaders pursued a preponderance of power to protect security and an Open Door world order. | Integrates security, economics, and ideology. | Focuses on elites and underweights allies and the third world.[^ch37-postrevisionist-works] |
| **New Cold War history** | Odd Arne Westad, *The Cold War: A World History* (2017); Vladislav Zubok and Constantine Pleshakov, *Inside the Kremlin’s Cold War* (1996) | The conflict was global, and Soviet and third-world actors had their own agency and ideologies. | Uses post-1991 archives and decenters the United States. | The global frame can underweight the American domestic story.[^ch37-newhistory-works] |
| **Korea as civil war** | Bruce Cumings, *The Origins of the Korean War* (1981, 1990) | The Korean War was rooted in Korean politics and society, not only superpower rivalry. | Recovers Korean agency and the war’s civil dimension. | Contested on the attribution of North Korean and Chinese decisions.[^ch37-newhistory-works] |
| **Domestic anticommunism** | Ellen Schrecker, *Many Are the Crimes* (1998); David Caute, *The Great Fear* (1978) | Anticommunism was a broad system of domestic repression with lasting costs. | Documents the scope and machinery of the loyalty-security state. | Can treat “the state” as more unified than it was.[^ch37-domestic-works] |

**Required caption.** Table 1. Cold War origins and domestic consequences: positions on why the alliance broke down and what containment cost at home.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The primary documents and institutional accounts named in the notes were read for this outline; the scholarly works by Feis, Bailey, Schlesinger, Williams, LaFeber, Alperovitz, Gaddis, Leffler, Westad, Zubok and Pleshakov, Cumings, Schrecker, and Caute were identified through catalogs, publisher descriptions, reviews, or another work’s citation and were not read in full. Status: `planned`.[^ch37-check-table1][^ch37-check-debate-works]

**Required alt text.** A nine-row table comparing the orthodox, realist, Open Door revisionist, atomic-diplomacy, post-revisionist, national-security, new-Cold-War-history, Korea-as-civil-war, and domestic-anticommunism interpretations of the Cold War’s origins and domestic consequences, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the origins of the Cold War and its domestic consequences.”

**Cautions and limitations.** The Churchill, Truman, and Williams epigraphs need collation; the Long Telegram and the “X” article need collation against FRUS and Foreign Affairs; the loyalty-program screening figures rest on a Truman Library teaching page; Korean casualty figures conflict. Do not treat the Cold War as a single American project or a single Soviet one. The “Korea as civil war” row is not a claim that the United States was irrelevant.

---

#### Ch. 38, Table 1 — `ch38-table-01`

**Owner and location.** `chapters/38-chapter-38.md`, §6.4 The map of positions. **Display number:** Ch. 38, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare eight positions on the 1950s: affluent-society critique, consensus and conformity, domestic containment, the myth of the 1950s family, the consumers’ republic, Cold War civil rights, the long civil rights movement, and the origins of the urban crisis. The table should show how prosperity, conformity, and resistance coexisted.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Affluent-society critique** | John Kenneth Galbraith, *The Affluent Society* (1958) | Private abundance coexisted with neglected public needs; wants were created by the process that satisfied them. | Names the imbalance between private goods and public provision. | A period argument, not a measured finding; its forecasts are contestable.[^ch38-galbraith] |
| **Consensus and conformity** | William H. Whyte, *The Organization Man* (1956); David Riesman, *The Lonely Crowd* (1950); C. Wright Mills, *White Collar* (1951) | The decade produced “other-directed,” organization-shaped conformity. | Captures the cultural anxiety of the new middle class. | Draws on an elite, largely White sample and can overstate uniformity.[^ch38-affluent-works] |
| **Domestic containment** | Elaine Tyler May, *Homeward Bound* (1988) | Cold War anxiety was channeled into the contained nuclear family. | Links foreign policy to domestic gender norms. | Centers the Cold War as cause and can underweight economic and racial forces.[^ch38-exclusion-works] |
| **The myth of the 1950s family** | Stephanie Coontz, *The Way We Never Were* (1992) | The golden-age family is a nostalgic invention; the 1950s were exceptional. | Uses demographic evidence to dismantle a durable myth. | Can flatten real gains and real variety within the decade.[^ch38-coontz] |
| **Consumers’ republic** | Lizabeth Cohen, *A Consumers’ Republic* (2003) | Mass consumption became the basis of citizenship and of exclusion. | Connects prosperity to belonging and to segregation. | A large synthesis; specific local claims need their own evidence.[^ch38-exclusion-works] |
| **Cold War civil rights** | Mary L. Dudziak, *Cold War Civil Rights* (2000) | International criticism pressured federal civil rights reform but confined it to formal equality. | Puts American race relations in a global frame. | Can underweight Black activism and domestic politics.[^ch38-dudziak] |
| **Long civil rights movement** | Jacquelyn Dowd Hall, “The Long Civil Rights Movement” (2005) | The movement predates 1954–55 and extends beyond legal rights. | Widens the chronology and the demands at stake. | Can blur the distinctiveness of the mid-1950s turning points.[^ch38-exclusion-works] |
| **Origins of the urban crisis** | Thomas J. Sugrue, *The Origins of the Urban Crisis* (1996) | Deindustrialization and housing discrimination, not the 1960s riots, produced the urban crisis. | Moves the causal clock back to the 1940s and 1950s. | A single-city study whose generalization must be argued.[^ch38-exclusion-works] |

**Required caption.** Table 1. Affluence, conformity, and resistance: positions on whether the 1950s are best understood as a period of prosperity and consensus or of exclusion and incipient revolt.

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The primary documents and institutional accounts named in the notes were read for this outline; the scholarly works by Galbraith, Whyte, Riesman, Mills, May, Cohen, Dudziak, Hall, and Sugrue were identified through catalogs, publisher descriptions, reviews, or another work’s citation and were not read in full. Status: `planned`.[^ch38-check-table1][^ch38-check-debate-works]

**Required alt text.** An eight-row table comparing the affluent-society, consensus-and-conformity, domestic-containment, myth-of-the-1950s-family, consumers’-republic, Cold-War-civil-rights, long-civil-rights-movement, and origins-of-the-urban-crisis interpretations of the 1950s, each listing representative historians and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over affluence, conformity, and resistance.”

**Cautions and limitations.** The Levittown lease clause and the 1949 Levitt statement are quoted at second hand; the 1960 Levittown population figures conflict; the television diffusion series conflict across sources; the women’s labor-force figure needs BLS/Census reconciliation. Do not let the suburban image stand in for the whole decade. The “long civil rights movement” row is a periodization argument, not a claim that nothing changed in 1954.

---

#### Ch. 39, Table 1 — `ch39-table-01`

**Owner and location.** `chapters/39-chapter-39.md`, §7.4 The map of positions. **Display number:** Ch. 39, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare eight positions on the civil rights revolution: from protest to politics, nonviolent direct action, Black Power, the local organizing tradition, the long civil rights movement, the critique of the long movement, federal partnership and surveillance, and courts and social change. The table should show how strategy, state action, and periodization are debated.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **From protest to politics** | Bayard Rustin, “From Protest to Politics” (1965) | Legal and protest gains must be translated into organized political and economic power. | Links civil rights to economic justice and to electoral strategy. | Assumes a coalition that was already fracturing. [^ch39-rustin-1965] |
| **Nonviolent direct action** | Martin Luther King Jr., “Letter from Birmingham Jail” (1963) and the Poor People’s Campaign (1967–68) | Organized nonviolent pressure creates a crisis that forces negotiation; economic security is the final goal. | Joins moral appeal to enforceable law. | Criticized as too slow and as depending on federal goodwill. [^ch39-letter-birmingham][^ch39-poor-peoples-king] |
| **Black Power** | Stokely Carmichael (Kwame Ture), Greenwood speech (1966); Carmichael and Charles V. Hamilton, *Black Power* (1967) | Black self-determination requires independent political, economic, and cultural power. | Names the limits of integration and the demand for power. | The slogan’s meaning was unstable and was used to justify a federal retreat. [^ch39-carmichael-power][^ch39-carmichael-blackpast] |
| **Local organizing tradition** | Charles M. Payne, *I’ve Got the Light of Freedom* (1995); Aldon D. Morris, *The Origins of the Civil Rights Movement* (1984) | The movement was built by local networks, institutions, and organizers, not only national leaders. | Recovers the work of ordinary people and local leaders. | Can underweight national politics and media. [^ch39-organizing-works] |
| **The long civil rights movement** | Jacquelyn Dowd Hall, “The Long Civil Rights Movement and the Political Uses of the Past” (2005) | The movement began in the 1930s–40s and continued past 1965, aiming at economic as well as legal change. | Exposes the narrow “classical” frame. | Can blur distinct phases and root the movement too broadly. [^ch39-hall-jstor] |
| **Critique of the long movement** | Sundiata Keita Cha-Jua and Clarence Lang, “The ‘Long Movement’ as Vampire” (2007) | The long-movement frame commits temporal and spatial fallacies and flattens the mid-century movement’s specificity. | Insists on periodization and context. | Risks restoring the very “classical” canon it criticizes. [^ch39-chajua-lang] |
| **Federal partnership and surveillance** | David J. Garrow, *Bearing the Cross* (1986); Kenneth O’Reilly, *Racial Matters* (1989); FBI records | The federal government was both ally and surveillant; COINTELPRO targeted King and the movement. | Documents state repression alongside reform. | A national-security lens can displace movement agency. [^ch39-fbi-king][^ch39-surveillance-works] |
| **Courts and social change** | Gerald N. Rosenberg, *The Hollow Hope* (1991), against the view that *Brown* and the courts catalyzed the movement | Court decisions rarely produce social change without political mobilization. | Presses what law alone accomplished. | Contested among legal historians and can understate law’s agenda-setting role. [^ch39-courts-works] |

**Required caption.** Table 1. Movement strategy, rights, and economic justice: positions on what the civil rights revolution accomplished and what remained beyond enforceable rights.[^ch39-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The primary and institutional accounts named in the notes were read for this outline; the scholarly works by Payne, Morris, Hall, Cha-Jua and Lang, Garrow, O’Reilly, and Rosenberg were identified through bibliographic records, abstracts, or another work’s citation and were not read in full. Status: `planned`.[^ch39-check-table1][^ch39-check-debate-works]

**Required alt text.** An eight-row table comparing the protest-to-politics, nonviolent-direct-action, Black-Power, local-organizing, long-civil-rights-movement, critique-of-the-long-movement, federal-partnership-and-surveillance, and courts-and-social-change interpretations of the civil rights revolution, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over movement strategy, rights, and economic justice.”

**Cautions and limitations.** The King epigraph and “Letter from Birmingham Jail” quotations need collation; Carmichael’s Greenwood quotation and the National Archives case-file account need a contemporaneous transcript; Hall’s epigraph needs the published article; no specific Louisiana literacy test has been identified. Do not use “the movement” as a single actor or a single timeline. The “federal partnership and surveillance” row holds two things together; do not split them into a hero and a villain.

---

#### Ch. 40, Table 1 — `ch40-table-01`

**Owner and location.** `chapters/40-chapter-40.md`, §6.4 The map of positions. **Display number:** Ch. 40, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on the Great Society: completion of New Deal liberalism, policy design and “maximum feasible misunderstanding,” grassroots pressure and movement-driven reform, racial hierarchy and the two-tier welfare state, the unraveling and backlash, and conservative critique of government failure. The table should weigh ambition, design, and constraint.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Completion of New Deal liberalism** | Joshua Zeitz, *Building the Great Society* (2018); Julian E. Zelizer, *The Fierce Urgency of Now* (2015) | The Great Society was a moderate, incremental completion of the New Deal and Fair Deal, and it worked. | Restores the programs’ design and the political skill behind them. | Can underweight the racial and structural limits the programs left. [^ch40-zeitz][^ch40-zelizer] |
| **Policy design and “maximum feasible misunderstanding”** | Daniel Patrick Moynihan, *Maximum Feasible Misunderstanding* (1969); Peter Marris and Martin Rein, *Dilemmas of Social Reform* (1967) | The antipoverty programs failed because social-science theory was imposed without clear goals or administrative capacity. | Presses the distance between intent and implementation. | Can blame theory for failures that were also political and fiscal. [^ch40-moynihan-max] |
| **Grassroots pressure and movement-driven reform** | Julian E. Zelizer, *The Fierce Urgency of Now* (2015); movement records | The legislation was shaped by organized demands from below as much as by presidential initiative. | Recovers the role of movements and Congress. | Can understate Johnson’s legislative role and the 1964 mandate. [^ch40-zelizer] |
| **Racial hierarchy and the two-tier welfare state** | Jill Quadagno, *The Color of Welfare* (1994) | Racism divided the welfare state into a universal social insurance tier and a stigmatized means-tested tier. | Explains why some programs became durable and others politically vulnerable. | A race-centered account can underweight class and federalism. [^ch40-quadagno] |
| **The unraveling and the backlash** | Allen J. Matusow, *The Unraveling of America* (1984); Thomas J. Sugrue, *The Origins of the Urban Crisis* (1996) | Liberal reform and urban racial conflict together produced the backlash that ended the reform era. | Connects domestic reform to the politics of neighborhood and race. | A backlash frame can treat voters’ motives as settled. [^ch40-matusow][^ch40-sugrue] |
| **Conservative critique of government failure** | Amity Shlaes, *Great Society: A New History* (2019), as reviewed by Fred Siegel | The programs expanded government, fed inflation, and failed on their own terms. | Forces the question of what the programs actually accomplished. | A polemical frame can dismiss durable gains such as Medicare. [^ch40-shlaes-siegel] |

**Required caption.** Table 1. Great Society ambition and constraint: positions on what the federal rights and social programs of 1961–68 accomplished and what limited them.[^ch40-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Zeitz’s argument was read through the *Politico Magazine* adaptation, and Shlaes’s argument through Fred Siegel’s review; Zelizer, Quadagno, Matusow, Sugrue, Moynihan, and Marris and Rein were identified through bibliographic records or publisher descriptions and were not read in full. Status: `planned`.[^ch40-check-table1][^ch40-check-debate-works]

**Required alt text.** A six-row table comparing the completion-of-New-Deal, policy-design, grassroots-pressure, racial-hierarchy, unraveling-and-backlash, and conservative-critique interpretations of the Great Society, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the Great Society’s ambition and its constraints.”

**Cautions and limitations.** The Shlaes and Zeitz epigraphs need collation; the ESEA signing date (April 9, 11, or 12, 1965) and the Truman Medicare card fields need collation; the 1966 seat counts rest on a center essay; the poverty, Head Start, education, and Medicare figures rest on institutional summaries. Do not treat the Great Society as a single legislative moment. The “conservative critique” row is not a caricature; state its strongest version.

---

#### Ch. 41, Table 1 — `ch41-table-01`

**Owner and location.** `chapters/41-chapter-41.md`, §6.4 The map of positions. **Display number:** Ch. 41, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on Vietnam: Cold War consensus and the quagmire, the war was chosen, bureaucratic failure and dereliction, Vietnamese and international agency, revisionism and the missed victory, and the war the soldiers fought. The table should show how the same escalation looks from Washington, Hanoi, and the ground.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Cold War consensus and the quagmire** | George C. Herring, *America’s Longest War* (1979; 6th ed. 2019) | The United States stumbled into a war it could not win, driven by containment and credibility. | Establishes the policy’s incremental logic and its costs. | Can understate the choices that were made and the alternatives available. [^ch41-herring] |
| **The war was chosen** | Fredrik Logevall, *Choosing War* (1999) | Leaders had viable alternatives in 1964–65 and chose escalation despite them. | Restores contingency and the record of dissent. | A choice model can underweight the political cost of withdrawal. [^ch41-logevall] |
| **Bureaucratic failure and dereliction** | H.R. McMaster, *Dereliction of Duty* (1997) | The Joint Chiefs and civilian leaders failed to debate honestly, producing decisions by default. | Presses the distance between advice and decision. | Focuses on Washington and can underweight Vietnamese agency. [^ch41-mcmaster] |
| **Vietnamese and international agency** | Lien-Hang T. Nguyen, *Hanoi’s War* (2012); Pierre Asselin, *Hanoi’s Road to the Vietnam War* (2013) | Hanoi pursued its own strategy and made its own choices, often against its patrons’ advice. | Corrects the American-centered frame. | Vietnamese archival access remains partial and uneven. [^ch41-nguyen-hanoi][^ch41-asselin] |
| **Revisionism and the missed victory** | Mark Moyar, *Triumph Forsaken* (2006) | Diem was a viable ally and the war was winnable; the 1963 coup was the decisive mistake. | Forces the question of what “winning” would have required. | A polemical frame can stretch the evidence, as reviewers have charged. [^ch41-moyar] |
| **The war the soldiers fought** | Christian G. Appy, *Working-Class War* (1993) | The war was fought chiefly by poor and working-class Americans who had little say in it. | Recovers the social composition and experience of the force. | A social-history focus can underweight strategy and diplomacy. [^ch41-appy] |

**Required caption.** Table 1. Containment and Vietnam escalation: positions on why the United States escalated and why it could not resolve the war.[^ch41-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Herring, Logevall, McMaster, Moyar, Nguyen, Asselin, and Appy were identified through publisher, library, and review records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch41-check-table1][^ch41-check-debate-works]

**Required alt text.** A six-row table comparing the Cold-War-consensus, chosen-war, bureaucratic-failure, Vietnamese-agency, revisionist, and soldiers’-war interpretations of the Vietnam escalation, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over containment and escalation.”

**Cautions and limitations.** The Hồ Chí Minh and Logevall epigraphs need collation; the American share of French war costs, Rolling Thunder tonnage, body-count and draft figures, Gallup question wording, and My Lai estimates rest on institutional pages or second-hand citations. Do not use “quagmire” as a substitute for showing decisions. The “missed victory” row is a serious revisionist argument; do not dismiss it with casualties alone.

---

#### Ch. 42, Table 1 — `ch42-table-01`

**Owner and location.** `chapters/42-chapter-42.md`, §6.4 The map of positions. **Display number:** Ch. 42, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on 1968–74: backlash and realignment, liberal continuity, the grassroots rights revolution, the suburban “silent majority,” the seventies as structural pivot, and dealignment and an unstable party system. The table should show whether the period realigned American politics or left it unsettled.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Backlash and realignment** | Rick Perlstein, *Nixonland* (2008); Thomas Byrne Edsall with Mary D. Edsall, *Chain Reaction* (1991) | The movements and the racial and cultural conflicts of the 1960s produced a durable conservative majority that Nixon assembled and that outlived him. | Recovers the political work of coalition-building and the centrality of race and culture. [^ch42-perlstein-nixonland][^ch42-edsall-chain] | Can infer a durable majority from election outcomes and understate dealignment and instability. [^ch42-burnham-dealignment] |
| **Liberal continuity** | Joan Hoff, *Nixon Reconsidered* (1994) | Nixon governed within and even extended the New Deal order; the administrative state grew rather than shrank. | Establishes the domestic record that the resignation overshadowed. [^ch42-hoff-nixon] | Can understate the era’s economic and ideological rupture. [^ch42-fraser-gerstle] |
| **Grassroots rights revolution** | John D. Skrentny, *The Minority Rights Revolution* (2002) | The era’s defining change was the expansion of rights for minorities, women, and others, driven by social movements and administrative decisions. | Centers the movements and the policy machinery they moved. [^ch42-skrentny-rights] | A rights-centered account can underweight the backlash the expansion provoked. [^ch42-edsall-chain] |
| **Suburban “silent majority”** | Matthew D. Lassiter, *The Silent Majority* (2006); Kevin M. Kruse, *White Flight* (2005) | The decisive politics of the era took place in suburbs and metropolitan areas, where race, taxes, and neighborhood were fused. | Locates the era’s politics at the level where it was lived. [^ch42-lassiter-silent][^ch42-kruse-whiteflight] | Metropolitan accounts can underweight national coalition and foreign policy. [^ch42-perlstein-nixonland] |
| **The seventies as structural pivot** | Bruce J. Schulman, *The Seventies* (2001); Steve Fraser and Gary Gerstle, eds., *The Rise and Fall of the New Deal Order* (1989) | The end of the postwar boom and the rupture of the New Deal order — not the movements alone — set the political direction of the decades that followed. | Connects political change to economic structure. [^ch42-schulman-seventies][^ch42-fraser-gerstle] | Structural accounts can underweight the contingency of elections and scandals. [^ch42-nara-watergate] |
| **Dealignment and an unstable party system** | Walter Dean Burnham, *Critical Elections and the Mainsprings of American Politics* (1970) | The old party system was coming apart rather than re-forming; volatility, falling turnout, and divided government were the era’s real pattern. | Presses the evidence against a clean realignment story. [^ch42-burnham-dealignment] | Can understate the durable conservative turn that followed 1980. [^ch42-perlstein-nixonland] |

**Required caption.** Table 1. Liberal continuity and political realignment: positions on whether 1968–74 realigned American politics or left it unsettled.[^ch42-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Perlstein, Edsall and Edsall, Hoff, Skrentny, Lassiter, Kruse, Schulman, Fraser and Gerstle, and Burnham were identified through publisher, library, and review records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch42-check-table1][^ch42-check-debate-works]

**Required alt text.** A six-row table comparing the backlash-and-realignment, liberal-continuity, grassroots-rights, suburban-silent-majority, structural-pivot, and dealignment interpretations of American politics in 1968–74, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over liberal continuity and political realignment.”

**Cautions and limitations.** The Nixon and DeLarverie epigraphs need collation; the Perlstein epigraph must be replaced or collated; the Clean Air Act signing date, the Cambodian incursion authorization date, the “smoking gun” tape date, the 1972 popular-vote totals, the War Powers Resolution enactment date, and the Alcatraz occupation dates rest on institutional pages or second-hand citations. Do not infer individual voter movement from aggregate returns. The “silent majority” row is a political rhetoric as well as an electoral coalition; distinguish them.

---

#### Ch. 43, Table 1 — `ch43-table-01`

**Owner and location.** `chapters/43-chapter-43.md`, §6.4 The map of positions. **Display number:** Ch. 43, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on the 1970s: decline and “malaise,” structural pivot, the market turn, working-class rupture, the rise of the right and the taxpayer, and global/contingent change. The table should show how economic shocks, political realignment, and institutional change are connected.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Decline and “malaise”** | Jimmy Carter’s July 15, 1979, address; Christopher Lasch, *The Culture of Narcissism* (1979) | The decade was a crisis of confidence and a loss of national purpose rooted in culture and institutions. [^ch43-carter-confidence][^ch43-lasch-narcissism] | Names the subjective and institutional dimensions of the period. [^ch43-carter-confidence] | Can mistake an elite diagnosis for a national mood and understate structural causes. [^ch43-check-debate-works] |
| **Structural pivot** | Bruce J. Schulman, *The Seventies* (2001); Judith Stein, *Pivotal Decade* (2010) | The end of the postwar boom and the New Deal order, not a mood, set the decades that followed. [^ch43-schulman-seventies][^ch43-stein-pivotal] | Connects political change to economic structure. [^ch43-stein-pivotal] | Can understate contingency and the role of ideas and movements. [^ch43-falwell-pbs] |
| **Market turn and the rediscovery of the market** | Daniel T. Rodgers, *Age of Fracture* (2011); Daniel Stedman Jones, *Masters of the Universe* (2012) | The era’s decisive change was intellectual and institutional: a turn toward markets, choice, and deregulation. [^ch43-rodgers-fracture][^ch43-stedman-jones-masters] | Explains the ideological groundwork for later policy. [^ch43-rodgers-fracture] | Can overstate the coherence of “neoliberalism” and understate what did not change. [^ch43-check-debate-works] |
| **Working-class rupture** | Jefferson Cowie, *Stayin’ Alive* (2010); Steve Fraser and Gary Gerstle, eds., *The Rise and Fall of the New Deal Order* (1989) | Deindustrialization and the breakup of the labor-capital compact divided the Democratic coalition and remade politics. [^ch43-cowie-stayinalive][^ch43-fraser-gerstle-43] | Centers work, class, and the geography of deindustrialization. [^ch43-cowie-stayinalive] | Can underweight race, gender, and the rights realignment. [^ch43-loc-era] |
| **The rise of the right and the taxpayer** | Thomas Byrne Edsall with Mary D. Edsall, *Chain Reaction* (1991); Lisa McGirr, *Suburban Warriors* (2001) | Conservative organization around taxes, race, and family values built a durable movement before 1980. [^ch43-edsall-chain-43][^ch43-mcgirr-suburban] | Recovers grassroots conservative agency. [^ch43-mcgirr-suburban] | Can understate the role of economic shock and the movement’s limited reach. [^ch43-fed-oil1979] |
| **Global and contingent** | Thomas Borstelmann, *The 1970s: A New Global History* (2012) | The decade’s outcomes were shaped by oil, empire, and transnational forces as much as by American choices. [^ch43-borstelmann-1970s] | Restores the international frame. [^ch43-borstelmann-1970s] | Can dissolve American agency into structure. [^ch43-check-debate-works] |

**Required caption.** Table 1. Seventies crisis and institutional change: positions on whether the decade was a decline, a structural pivot, a market turn, a working-class rupture, a conservative groundswell, or a global transformation.[^ch43-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Schulman, Stein, Rodgers, Stedman Jones, Cowie, Fraser and Gerstle, Edsall and Edsall, McGirr, Borstelmann, and Lasch were identified through publisher, library, and course records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch43-check-table1][^ch43-check-debate-works]

**Required alt text.** A six-row table comparing the decline-and-malaise, structural-pivot, market-turn, working-class-rupture, rise-of-the-right-and-taxpayer, and global-and-contingent interpretations of the American 1970s, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the Seventies crisis and institutional change.”

**Cautions and limitations.** The Carter, Falwell, and Schulman epigraphs need collation; the Schulman sentence is a paraphrase to replace or drop; the Camp David treaty signing date, the “Ford to City: Drop Dead” headline date, and the unsupported 150-word Proposition 13 claim need resolution; the productivity, oil, and inflation figures rest on institutional summaries. Do not reduce the decade to “malaise.” The “working-class rupture” row is not a claim that all White workers left the Democratic Party.

---

#### Ch. 44, Table 1 — `ch44-table-01`

**Owner and location.** `chapters/44-chapter-44.md`, §6.4 The map of positions. **Display number:** Ch. 44, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on the Reagan era and the end of the Cold War: conservative realignment, institutional continuity, Reagan won the Cold War, internal Soviet collapse, Gorbachev’s agency, and multiple causation and the era’s costs. The table should separate domestic realignment from the international ending.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Conservative realignment** | Sean Wilentz, *The Age of Reagan* (2008); Kevin P. Phillips, *The Emerging Republican Majority* (1969); Thomas Byrne Edsall with Mary D. Edsall, *Chain Reaction* (1991); Lisa McGirr, *Suburban Warriors* (2001) | 1980 marked the start of a durable conservative era in national politics, built on a movement that predated it. [^ch44-wilentz-age-reagan][^ch44-edsall-chain-reaction][^ch44-mcgirr-suburban] | Takes electoral change and grassroots conservative agency seriously. [^ch44-mcgirr-suburban] | Can overstate durability and understate what did not change. [^ch44-schwab-illusion] |
| **Institutional continuity** | Larry M. Schwab, *The Illusion of a Conservative Reagan Revolution* (1991); Gil Troy, *The Reagan Revolution: A Very Short Introduction* (2009) | The Reagan years changed rhetoric and some policy but left much of the New Deal institutional order intact. [^ch44-schwab-illusion][^ch44-troy-reagan-revolution] | Tests the revolution’s claims against policy outcomes and continuity. [^ch44-schwab-illusion] | Can understate the long-run shift in tax, regulatory, and judicial policy. [^ch44-wilentz-age-reagan] |
| **Reagan won the Cold War** | Peter Schweizer, *Victory* (1994); Paul Kengor, *The Crusader* (2006) | Reagan’s buildup, SDI, and Reagan Doctrine exhausted the Soviet Union and forced Gorbachev to accommodate. [^ch44-schweizer-victory][^ch44-kengor-crusader] | Explains the timing of the accommodation and the ideological dimension. [^ch44-kengor-crusader] | Overstates Reagan’s specific contribution; SDI was not technically viable. [^ch44-gaddis-coldwar] |
| **Internal Soviet collapse** | John Lewis Gaddis, *The Cold War: A New History* (2005); Vladislav Zubok, *A Failed Empire* (2007); Stephen Kotkin, *Armageddon Averted* (2001) | The Soviet collapse was primarily the product of internal structural failures that predated the Reagan buildup. [^ch44-gaddis-coldwar][^ch44-zubok-failed-empire][^ch44-kotkin-armageddon] | Rests on Soviet archival evidence and explains why the collapse came from within. [^ch44-zubok-failed-empire] | Can make the collapse seem inevitable and understate choices. [^ch44-brown-gorbachev-factor] |
| **Gorbachev’s agency** | Archie Brown, *The Gorbachev Factor* (1996) | The peaceful end was primarily the product of Gorbachev’s decisions not to use force and to accept change. [^ch44-brown-gorbachev-factor] | Takes political agency seriously and explains the form of the ending. [^ch44-brown-gorbachev-factor] | Risks a “great man” account that underweights structure. [^ch44-kotkin-armageddon] |
| **Multiple causation and the era’s costs** | John Lewis Gaddis, *The Cold War: A New History* (2005); Elizabeth Hinton, *From the War on Poverty to the War on Crime* (2016); Jennifer Brier, *Infectious Ideas* (2009) | The Cold War ended through the interaction of structure, pressure, and choice, and the era’s domestic costs fell unevenly on the poor, the ill, and the incarcerated. [^ch44-gaddis-coldwar][^ch44-hinton-war-on-poverty][^ch44-brier-infectious-ideas] | Rejects single-cause accounts and restores the era’s social costs. [^ch44-brier-infectious-ideas] | The synthesis can flatten real differences among the causal accounts. [^ch44-explaininghistory-coldwar] |

**Required caption.** Table 1. Conservatism and the Cold War’s ending: positions on whether 1980 began a durable realignment or a limited change, and on whether the Cold War ended through American pressure, Soviet collapse, Gorbachev’s choices, or their interaction.[^ch44-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Wilentz, Phillips, Edsall and Edsall, McGirr, Schwab, Troy, Schweizer, Kengor, Gaddis, Zubok, Kotkin, Brown, Hinton, and Brier were identified through publisher and library records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch44-check-table1][^ch44-check-debate-works]

**Required alt text.** A six-row table comparing the conservative-realignment, institutional-continuity, Reagan-won-the-Cold-War, internal-Soviet-collapse, Gorbachev’s-agency, and multiple-causation positions on the Reagan era and the Cold War’s ending, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over conservatism and the Cold War’s ending.”

**Cautions and limitations.** The Reagan, Gorbachev, and Gaddis epigraphs need collation; the hostage-release terms, the 1988 “read my lips” pledge and 1990 reversal, the Libya strike details, the 1983 Soviet early-warning episode, the 1986 Iran funding figures, and the quilt-panel identifier and rights remain open. Do not assign the Soviet collapse to a single actor. The “Reagan won” and “internal collapse” rows are not symmetrical; each has a different evidentiary burden.

---

#### Ch. 45, Table 1 — `ch45-table-01`

**Owner and location.** `chapters/45-chapter-45.md`, §6.4 The map of positions. **Display number:** Ch. 45, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare five positions on globalization: broadly shared growth, concentrated losses, a winner-take-all distribution, institutions rather than trade explaining the divide, and the end of history and its critics. The table should connect economic integration to distribution and political confidence.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Globalization delivered broadly shared growth** | Congressional Research Service, *The North American Free Trade Agreement (NAFTA)*, R42965 (2017); Peterson Institute analyses of NAFTA | Trade and investment integration lowered prices, expanded exports, and raised aggregate output without large net American job losses. [^ch45-nafta-crs][^ch45-piie-nafta] | Takes aggregate gains and consumer benefits seriously and uses trade data. [^ch45-nafta-crs] | Can understate concentrated displacement and regional effects. [^ch45-epi-nafta] |
| **Globalization produced concentrated losses** | Economic Policy Institute, “The high price of ‘free’ trade” (2003) and related briefs | The agreements accelerated the relocation of manufacturing and produced large net job losses concentrated in specific industries and communities. [^ch45-epi-nafta] | Restores the displaced workers and regions the aggregate figures omit. [^ch45-epi-nafta] | Attribution to trade alone is contested; other forces also moved jobs. [^ch45-piie-nafta] |
| **A winner-take-all distribution** | Congressional Budget Office, *Trends in the Distribution of Household Income Between 1979 and 2007* (2011); Center on Budget and Policy Priorities analyses | The gains of the expansion flowed disproportionately to the top of the distribution, widening inequality across the period. [^ch45-cbo-distribution][^ch45-cbpp-2003] | Uses consistent tax and transfer series over a long period. [^ch45-cbo-distribution] | Long periods can obscure late-decade gains at the bottom. [^ch45-census-income-1999] |
| **Institutions, not trade, explain the divide** | Joseph E. Stiglitz, *The Roaring Nineties* (2003); Dani Rodrik, *Has Globalization Gone Too Far?* (1997) | Labor-market institutions, tax policy, and financial deregulation did more than trade to widen the distribution. [^ch45-check-debate-works] | Separates trade from the domestic policy choices that shaped its effects. | The works were identified through records and were not read in full for this outline; verify before publication. [^ch45-check-debate-works] |
| **The end of history and its critics** | Francis Fukuyama, “The End of History?” (1989); critics including Samuel P. Huntington, “The Clash of Civilizations?” (1993) | Liberal democracy was the endpoint of ideological evolution; critics argued that cultural and religious conflict, not convergence, would define the era. [^ch45-fukuyama-1989][^ch45-check-debate-works] | Frames the decade’s largest question about the post-Cold War order. [^ch45-fukuyama-1989] | The decade’s conflicts and inequality can be read against the proposition. [^ch45-nsarchive-rwanda] |

**Required caption.** Table 1. Globalization, growth, and distribution: positions on whether the decade’s integration and expansion were broadly shared, on how much trade caused the losses it produced, and on whether liberal democracy had reached its endpoint.[^ch45-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. The Economic Policy Institute, Peterson Institute, Stiglitz, Rodrik, and Huntington works were identified through search results, publisher, or library records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch45-check-table1][^ch45-check-debate-works]

**Required alt text.** A five-row table comparing the broadly-shared-growth, concentrated-losses, winner-take-all, institutions-explain-the-divide, and end-of-history positions on the 1990s economy, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over globalization, growth, and distribution.”

**Cautions and limitations.** The Clinton, Perot, and Fukuyama epigraphs need collation; the exact venue of the 1992 address, the Perot wording, the Nasdaq peak and decline, the health-care reform record, the 1994 budget-confrontation sequence, and the 2000 popular-vote totals remain open. Do not treat “globalization” as a single policy or a single outcome. The “end of history” row is an intellectual position, not an economic finding.

---

#### Ch. 46, Table 1 — `ch46-table-01`

**Owner and location.** `chapters/46-chapter-46.md`, §6.4 The map of positions. **Display number:** Ch. 46, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on the post-9/11 response: the emergency required a war and broad authority, the response endangered the liberties it claimed to defend, the Iraq war followed from ideology and credibility rather than imminent threat, the war rested on claims the evidence did not support, detention and interrogation became a war on American values, and the collapse was avoidable and systemic. The table should connect security policy, law, and the financial crisis.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **The emergency required a war and broad authority** | George W. Bush, September 20, 2001, address; administration legal memoranda | The attacks were an act of war, and preventing a second attack justified military force, expanded surveillance, and coercive interrogation. [^ch46-bush-joint-address-2001] | Takes the novelty and scale of the threat seriously and states the security case plainly. [^ch46-bush-joint-address-2001] | Can understate the legal costs and the evidence that the interrogation program’s intelligence claims were overstated. [^ch46-ssci-2014] |
| **The response endangered the liberties it claimed to defend** | Russ Feingold, Senate statement, October 25, 2001; ACLU, “Surveillance Under the USA/PATRIOT Act” | Emergency powers, and especially the expanded records authority, reversed checks and balances and made the war winnable at home only by not sacrificing constitutional rights. [^ch46-feingold-2001][^ch46-patriot-aclu] | Restores the civil-liberties stakes and reads the statutory text closely. [^ch46-patriot-aclu] | Can understate the genuine intelligence needs and the courts’ later role. [^ch46-check-debate-works] |
| **The Iraq war followed from ideology and credibility, not imminent threat** | Melvyn P. Leffler, *Confronting Saddam Hussein* (2023); critics of the administration’s case | Bush went to war to enforce disarmament and preserve American credibility after September 11, not because Iraq posed an imminent threat. [^ch46-leffler-2023] | Situates the decision in the president’s own reasoning and the post-9/11 context. | Leffler was identified through reviews and was not read in full for this outline; verify before publication. [^ch46-leffler-2023] |
| **The war rested on claims the evidence did not support** | Iraq Survey Group (Duelfer report, 2004); Colin Powell’s later assessment | Iraq had destroyed its stockpiles; the administration’s public case for war was not supported by the evidence found. [^ch46-duelfer-report][^ch46-powell-un-2003] | Grounds the judgment in the post-invasion findings rather than in retrospective opinion. [^ch46-duelfer-report] | The finding describes the weapons, not the intentions of the decision-makers. [^ch46-check-debate-works] |
| **Detention and interrogation became a war on American values** | Jane Mayer, *The Dark Side* (2008); Senate Select Committee on Intelligence study (2014) | The administration adopted a deliberate program of coercive interrogation and rendition that violated law and damaged the nation’s standing. [^ch46-ssci-2014][^ch46-hrw-abu-ghraib] | Documents the program and connects policy to outcome. [^ch46-ssci-2014] | The report carries minority views, and the legal characterization is contested. [^ch46-ssci-2014] |
| **The collapse was avoidable and systemic** | Financial Crisis Inquiry Commission, *The Financial Crisis Inquiry Report* (2011); Ben S. Bernanke (2010) | The crisis resulted from failures of regulation, governance, and risk management and from structural vulnerabilities, not from any single cause. [^ch46-fcic-report][^ch46-bernanke-2010] | Separates triggers from vulnerabilities and uses the official record. [^ch46-bernanke-2010] | The commission’s conclusions are contested by a dissenting minority. [^ch46-check-debate-works] |

**Required caption.** Table 1. Emergency, security, and constitutional power: positions on whether the post-9/11 response was a necessary defense, a threat to liberty, a war built on unsupported claims, or a systemic failure of regulation.[^ch46-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Leffler and Mayer were identified through reviews, publisher, or library records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch46-check-table1][^ch46-check-debate-works]

**Required alt text.** A six-row table comparing the war-and-broad-authority, endangered-liberties, ideology-and-credibility, unsupported-case, war-on-values, and systemic-collapse positions on the post-9/11 emergency, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over emergency, security, and constitutional power.”

**Cautions and limitations.** The Bush, Feingold, and planned historian epigraphs need collation; the 9/11 toll components, the evacuation total, the Senate Iraq vote, the surge troop figures, the war-cost and civilian-casualty estimates, and the Katrina toll need source reconciliation. Do not use “war on terror” as a single policy or a single period. The “systemic collapse” row concerns the financial crisis as well as the war; keep the two mechanisms distinct.

---

#### Ch. 47, Table 1 — `ch47-table-01`

**Owner and location.** `chapters/47-chapter-47.md`, §6.4 The map of positions. **Display number:** Ch. 47, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on the Obama era: crisis management prevented a second Depression, the response was too small and too kind to finance, the era was defined by racialized reaction, organized opposition remade the Republican Party, movement pressure from below drove the rights gains, and asymmetric polarization and institutional veto. The table should connect recovery policy, social movements, and polarization.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Crisis management prevented a second Depression** | Obama administration Council of Economic Advisers; Congressional Budget Office; Alan S. Blinder and Mark Zandi | The stimulus, the auto rescue, and the financial reform raised output and employment above what they would otherwise have been and stabilized the system. [^ch47-cbo-arra-impact] | Takes the scale of the emergency seriously and uses model-based counterfactuals openly. [^ch47-cbo-arra-impact] | The counterfactual cannot be observed, and the estimates depend on the model and its assumptions. [^ch47-check-numbers][^ch47-check-debate-works] |
| **The response was too small, too slow, and too kind to finance** | Paul Krugman and other Keynesian critics; Economic Policy Institute analyses | The stimulus was undersized relative to the output gap, and the recovery’s slowness reflected political choices as much as economic limits. [^ch47-census-income-2016] | Connects the policy design to the household experience of the recovery. [^ch47-census-income-2016] | Identified for this outline through commentary and summaries; verify the specific estimates before use. [^ch47-check-debate-works] |
| **The era was defined by racialized reaction** | Michael Tesler, *Post-Racial or Most-Racial?* (2016) | Obama’s presidency made racial considerations more, not less, central to White Americans’ political attitudes. [^ch47-tesler-2016] | Grounds the polarization argument in survey evidence rather than anecdote. [^ch47-tesler-2016] | Tesler was identified through the publisher and reviews and not read in full; survey trends do not establish individual motives. [^ch47-tesler-2016] |
| **Organized opposition remade the Republican Party** | Theda Skocpol and Vanessa Williamson, *The Tea Party and the Remaking of Republican Conservatism* (2012) | The Tea Party was a grassroots reaction by older middle-class conservatives that pulled the Republican Party rightward and reshaped primaries. [^ch47-skocpol-williamson-2012] | Shows how movement energy translated into party change. [^ch47-skocpol-williamson-2012] | Focuses on one movement and period; read in summary for this outline, so verify before use. [^ch47-check-debate-works] |
| **Movement pressure from below drove the rights gains** | Keeanga-Yamahtta Taylor, *From #BlackLivesMatter to Black Liberation* (2016); organizers’ accounts | The rights and policing struggles were forced by organized movements, not granted by courts or presidents alone. [^ch47-taylor-2016] | Restores the agency of the movements and names structural racism. [^ch47-taylor-2016] | An engaged account; balance it against the legal and policy record. [^ch47-check-debate-works] |
| **Asymmetric polarization and institutional veto** | Thomas E. Mann and Norman J. Ornstein, *It’s Even Worse Than It Looks* (2012) | The gridlock of the period followed from asymmetric party polarization colliding with a constitutional system of veto points, not from a pox on both parties. [^ch47-skocpol-williamson-2012] | Connects procedural rules and party behavior to legislative outcomes. [^ch47-skocpol-williamson-2012] | The thesis was identified through reviews and summaries and not read in full; verify before use. [^ch47-check-debate-works] |

**Required caption.** Table 1. Renewal, constraint, and reaction in the Obama era: positions on whether the period was effective crisis management, an undersized and uneven recovery, racialized reaction, party realignment, movement-driven change, or asymmetric polarization.[^ch47-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Tesler, Taylor, Skocpol and Williamson, and Mann and Ornstein were identified through publisher and review records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch47-check-table1][^ch47-check-debate-works]

**Required alt text.** A six-row table comparing the crisis-management, undersized-recovery, racialized-reaction, party-realignment, movement-driven, and asymmetric-polarization positions on the Obama era, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over renewal, constraint, and reaction in the Obama era.”

**Cautions and limitations.** The Obama, McConnell, and Tesler epigraphs need collation; the 2008 exit-poll shares, the 2010 seat change, the CBO stimulus-impact report, the Benghazi Accountability Review Board, and the stimulus, auto-rescue, gun-vote, and cloture claims need source reconciliation. Do not treat the era as a single referendum on the president. The “racialized reaction” row is a body of evidence about attitudes and coalition change, not a claim that every critic was racist.

---

#### Ch. 48, Table 1 — `ch48-table-01`

**Owner and location.** `chapters/48-chapter-48.md`, §7.4 The map of positions. **Display number:** Ch. 48, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six positions on the populist turn of 2015–2021: economic dislocation and the trade shock, status threat and cultural backlash, place-based resentment and party decline, media and information disorder, institutional erosion and democratic norms, and comparative populism. The table should show how economic, cultural, and institutional explanations compete.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Economic dislocation and the trade shock** | David Autor, David Dorn, Gordon Hanson, and Kaveh Majlesi, “Importing Political Polarization?” (2020) | Local exposure to Chinese import competition depressed manufacturing employment and shifted affected districts toward the Republican Party and more extreme candidates. [^ch48-autor-2020] | Uses a quasi-experimental measure of trade exposure and links it to electoral outcomes. [^ch48-autor-2020] | An ecological finding about districts cannot establish any individual voter’s motive. [^ch48-check-debate-works] |
| **Status threat and cultural backlash** | Diana C. Mutz, “Status threat, not economic hardship” (2018); Pippa Norris and Ronald Inglehart, *Cultural Backlash* (2019) | Status threat and a cultural backlash among older social conservatives, not personal economic hardship, drove support for the populist candidate. [^ch48-mutz-2018] | Grounds the explanation in panel and survey evidence rather than aggregate geography. [^ch48-mutz-2018] | Survey measures of status threat are contested, and Mutz’s article was identified through its abstract and reviews and not read in full. [^ch48-check-debate-works] |
| **Place-based resentment and party decline** | Katherine J. Cramer, *The Politics of Resentment* (2016); Sam Rosenfeld, *The Polarizers* (2018) | Resentment rooted in rural place and a long polarization of the parties, not a single election, produced the turn. [^ch48-cramer-2016] | Restores the local and institutional texture that national accounts miss. [^ch48-cramer-2016] | Cramer’s fieldwork precedes 2016 and Rosenfeld was identified through publisher and review records and not read in full. [^ch48-check-debate-works] |
| **Media and information disorder** | Yochai Benkler, Robert Faris, and Hal Roberts, *Network Propaganda* (2018) | A distinct right-wing media ecosystem, rather than symmetric failure, produced the period’s asymmetric misinformation. [^ch48-benkler-2018] | Connects media structure to the spread of specific false claims. [^ch48-benkler-2018] | Focuses on one ecosystem and period, and was read only in summary for this outline. [^ch48-check-debate-works] |
| **Institutional erosion and democratic norms** | Steven Levitsky and Daniel Ziblatt, *How Democracies Die* (2018) | Elected leaders erode democracy slowly by breaking the norms of mutual toleration and institutional forbearance. [^ch48-levitsky-ziblatt-2018] | Names the informal norms that formal rules leave unprotected. [^ch48-levitsky-ziblatt-2018] | A comparative framework read here through reviews and summaries; it can understate institutional resilience. [^ch48-check-debate-works] |
| **Comparative populism** | Jan-Werner Müller, *What Is Populism?* (2016); Michael Kazin, *The Populist Persuasion* (rev. ed., 2017) | Populism is a thin-centered claim of a pure people against corrupt elites, and the American version belongs to a long persuasion. [^ch48-muller-2016] | Supplies a comparative definition the American case can be tested against. [^ch48-muller-2016] | Definitions vary across the literature, and both works were identified through descriptions and not read in full. [^ch48-check-debate-works] |

**Required caption.** Table 1. Populism and institutional erosion: positions on what drove the populist turn of 2015–2021 and how it bore on American institutions.[^ch48-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Mutz, Norris and Inglehart, Cramer, Rosenfeld, Benkler, Levitsky and Ziblatt, Müller, and Kazin were identified through publisher, review, or catalog records and were not read in full for this outline; supply page locators or mark the rows unverified before publication. Status: `planned`.[^ch48-check-table1][^ch48-check-debate-works]

**Required alt text.** A six-row table comparing the economic-dislocation, status-threat, place-based, media, institutional-erosion, and comparative-populism positions on the 2015–2021 turn, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over populism and institutional erosion.”

**Cautions and limitations.** The Trump, Clinton, and planned Kazin epigraphs need collation; the 2016 and 2020 popular-vote compilations, the Mueller report’s executive-summary sentences, the second impeachment resolution and both Senate acquittal roll calls, the family-separation count, and the January 6 prosecution counts need source reconciliation. Do not infer motive from a county-level vote shift. The “media and information disorder” row is not a single-platform story.

---

#### Ch. 49, Table 1 — `ch49-table-01`

**Owner and location.** `chapters/49-chapter-49.md`, §6.4 The map of positions. **Display number:** Ch. 49, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare six explanations of the unsettled present: democratic backsliding and norm erosion, institutional resilience and constitutional hardball, economic dislocation and the trade shock, status threat and cultural backlash, place-based resentment and coalition change, and comparative populism and the thin center. The table should make the book’s provisional judgment about 2021–2026 explicit without pretending the outcome is settled.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **Democratic backsliding and norm erosion** | Steven Levitsky and Daniel Ziblatt, *How Democracies Die* (2018) and *Tyranny of the Minority* (2023) | Elected leaders erode democracy slowly by breaking mutual toleration and institutional forbearance, and the American case fits a comparative pattern. [^ch49-levitsky-ziblatt-2018][^ch49-levitsky-ziblatt-2023] | Names the informal norms that formal rules leave unprotected and connects the American case to others. [^ch49-levitsky-ziblatt-2018] | A comparative framework can understate the courts, elections, and bureaucracy that checked the period; both works were identified through publisher and review records and not read in full. [^ch49-check-debate-works] |
| **Institutional resilience and constitutional hardball** | [A named constitutional scholar, identified work] | The period’s conflicts were ordinary constitutional hardball among parties, and the institutions held; the danger is overstated. [^ch49-check-debate-works] | Takes the courts’, elections’, and agencies’ actual record seriously. [^ch49-check-debate-works] | A planned position; the named work is not yet identified or read, so the row must be sourced or marked unverified. [^ch49-check-debate-works] |
| **Economic dislocation and the trade shock** | David Autor, David Dorn, Gordon Hanson, and Kaveh Majlesi, “Importing Political Polarization?” (2020) | Local exposure to Chinese import competition shifted affected districts toward more extreme candidates and the Republican Party. [^ch49-autor-2020] | Links a quasi-experimental measure of trade exposure to electoral outcomes. [^ch49-autor-2020] | An ecological finding about districts cannot establish any individual voter’s motive; identified through the journal record and not read in full. [^ch49-check-debate-works] |
| **Status threat and cultural backlash** | Diana C. Mutz, “Status threat, not economic hardship” (2018) | Changes in financial well-being had little effect on individual vote choice while measures of status threat did. [^ch49-mutz-2018] | Grounds the explanation in panel and survey evidence rather than aggregate geography. [^ch49-mutz-2018] | Survey measures of status threat are contested, and the article was identified through its abstract and not read in full. [^ch49-check-debate-works] |
| **Place-based resentment and coalition change** | Katherine J. Cramer, *The Politics of Resentment* (2016) | Resentment rooted in rural place and a perceived urban disregard, compounding long-run party change, produced the turn. [^ch49-cramer-2016] | Restores the local texture that national accounts miss. [^ch49-cramer-2016] | The fieldwork precedes 2016, and the book was identified through publisher and review records and not read in full. [^ch49-check-debate-works] |
| **Comparative populism and the thin center** | Jan-Werner Müller, *What Is Populism?* (2016) | Populism is a thin-centered claim of a pure people against corrupt elites, which the American case can be tested against. [^ch49-muller-2016] | Supplies a comparative definition rather than a label. [^ch49-muller-2016] | Definitions vary across the literature, and the work was identified through publisher and review records and not read in full. [^ch49-check-debate-works] |

**Required caption.** Table 1. Competing explanations of the unsettled present: positions on what the period 2021–October 2026 showed about American democracy, political economy, and coalition change.[^ch49-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Levitsky and Ziblatt, Autor, Dorn, Hanson, and Majlesi, Mutz, Cramer, and Müller were identified through publisher, review, or catalog records and were not read in full for this outline; the institutional-resilience row has no identified work yet, so it must be sourced or marked unverified before publication. Status: `planned`.[^ch49-check-table1][^ch49-check-debate-works]

**Required alt text.** A six-row table comparing the democratic-backsliding, institutional-resilience, economic-dislocation, status-threat, place-based, and comparative-populism positions on the period, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over the unsettled present.”

**Cautions and limitations.** The Dobbs epigraph, the planned 2025 inaugural epigraph, and the planned historian epigraph need collation; the 2022 and 2024 returns, the tariff timeline and the February 20, 2026, Learning Resources ruling, the One Big Beautiful Bill Act, the DOGE order and audit, the removal statistics, the deployment orders and 2026 ruling, the shutdown and protest records, the Afghanistan after-action review, and the Ukraine, Gaza, and Iran records need source reconciliation. Every 2025–26 claim remains a research task until checked against a dated record. Do not turn the table into a prediction of the November 2026 election.

---

#### Ch. 50, Table 1 — `ch50-table-01`

**Owner and location.** `chapters/50-chapter-50.md`, §6.4 The map of positions. **Display number:** Ch. 50, Table 1. **Status:** drafted, unverified.

**Purpose.** Compare five positions on the usable past: American exceptionalism, the critique of exceptionalism, declension and renewal, unfinished democratization, and competing uses of the national history. The table should let the conclusion weigh what the past can and cannot authorize.

**Columns.** Position; Voices, historians, and works; Core claim; Strongest contribution; Limitation. The full schema is defined in §6.1.

**Draft row values (the current table block; verify every claim).**

| Position | Voices, historians, and works | Core claim | Strongest contribution | Limitation |
|---|---|---|---|---|
| **American exceptionalism** | Seymour Martin Lipset, *American Exceptionalism: A Double-Edged Sword* (1996); Alexis de Tocqueville, *Democracy in America* (1835–40) | The United States occupies a distinctive position in a matrix of values — different, not simply better — shaped by its founding creed, its religiosity, and the absence of a mass socialist movement. [^ch50-lipset-1996] | Names the distinctive features a comparative history must explain rather than assume. [^ch50-lipset-1996] | “Exceptionalism” can slip from a description into a boast or a category that blocks comparison; Lipset was identified through a review and publisher record and not read in full. [^ch50-check-debate-works] |
| **The critique of exceptionalism** | Harold Hongju Koh, “On American Exceptionalism” (2003) | Exceptionalism has two faces — a readiness to set the world to rights and a readiness to exempt the United States from the rules — and the second face is a danger, not a destiny. [^ch50-koh-2003] | Separates a defensible distinctiveness from an exemption from law. [^ch50-koh-2003] | A legal argument about foreign policy, and the article was identified through its record and not read in full; it does not by itself explain domestic inequality. [^ch50-check-debate-works] |
| **Declension and renewal** | Samuel P. Huntington, “The U.S.—Decline or Renewal?” (1988); Paul Kennedy, *The Rise and Fall of the Great Powers* (1987) | The United States has passed through repeated waves of declinism; the real test of a great power is its ability to renew, so decline is a choice as much as a fate. [^ch50-huntington-1988][^ch50-kennedy-1987] | Treats decline as an argument to be tested, not a mood, and supplies a comparative frame. [^ch50-huntington-1988] | A 1988 framing written before the Cold War’s end; Kennedy was identified through Huntington’s article and a catalog record and not read in full. [^ch50-check-debate-works] |
| **Unfinished democratization** | Abraham Lincoln, Gettysburg Address (1863); Eric Foner, *Reconstruction: America’s Unfinished Revolution* (1988) and *The Second Founding* (2019) | The nation’s founding promise is realized only through an “unfinished work” that each generation must carry on; emancipation and Reconstruction were a second founding that remains incomplete. [^ch50-gettysburg-ncc][^ch50-foner-reconstruction][^ch50-foner-second-founding] | Explains both real progress and real reversal without equating the nation with either its promise or its crimes. [^ch50-gettysburg-ncc] | “Unfinished” can become an alibi that defers judgment or implies an inevitable completion; Foner’s books were identified through reviews and records and not read in full. [^ch50-check-debate-works] |
| **Competing uses of the national history** | Jill Lepore, *These Truths* (2018); The 1619 Project (2019); the President’s Advisory 1776 Commission, *The 1776 Report* (2021); Jacquelyn Dowd Hall, “The Long Civil Rights Movement and the Political Uses of the Past” (2005) | A nation founded on a contradiction will argue forever over the meaning of its history; public accounts of the past — 1619, 1776, the 250th anniversary — are themselves historical evidence. [^ch50-lepore-these-truths][^ch50-project-1619][^ch50-report-1776][^ch50-hall-2005] | Treats memory and commemoration as evidence, connecting historiography to public life. [^ch50-archives-foundation-2026] | The contest can flatten into two camps; Hall’s article and the 1776 Report’s criticisms were not read in full, and the AHA statement is access-blocked. [^ch50-check-debate-works][^ch50-aha-1776] |

**Required caption.** Table 1. Usable past, exceptionalism, and unfinished settlement: positions on whether the American past yields a usable guide, a unique national trajectory, a pattern of decline, an incomplete democratization, or a permanent contest over memory.[^ch50-check-table1]

**Source line (current draft; update the status when verified).** Drawn for this volume from the works named; full citations in the combined notes. Positions are analytical summaries, not quotations. Lipset, Koh, Kennedy, Foner’s two books, and Hall were identified through publisher, review, catalog, or journal records and were not read in full for this outline; the 1776 Report was read in part, and the AHA statement is access-blocked. Every row must be verified against the cited work or marked unverified before publication. Status: `planned`.[^ch50-check-table1][^ch50-check-debate-works]

**Required alt text.** A five-row table comparing the exceptionalism, anti-exceptionalism, declension-and-renewal, unfinished-democratization, and competing-uses-of-history positions on the American past, each listing representative voices and works, the core claim, its strongest contribution, and its limitation.

**Textual reference.** “Table 1 compares the positions that organize the debate over a usable past, American exceptionalism, and unfinished settlement.”

**Cautions and limitations.** The Declaration, Douglass, and Lepore epigraphs need collation; the Douglass 1852 pamphlet, the full Lepore text, the full 1776 Report, and the 1619 Project issue remain unread; the American Historical Association statement is access-blocked. Do not turn the table into a verdict on the present or a prediction of the 2026 election. The “competing uses” row is about public history, not a license to treat all uses as equally supported.

---

## 7. Appendix tables (16)

The appendix tables are reference infrastructure, not narrative. They have no roadmap, summary, or study questions; they do have captions, source lines, definitions, and one combined footnote list per appendix. Appendix B’s eight datasets are the largest research task in the book. Each is a parent table with labeled panels; a panel is not a new table number.

### 7.1 Appendix B. Tables and Data (8)

#### 7.1.1 App. B, Table 1 — `app-b-table-01`

**Owner and location.** `chapters/52-appendix-b.md`, First dataset; §B.1. **Display number:** App. B, Table 1. **Status:** planned; no dataset exists.

**Purpose.** Give readers a compact, bounded series for population and urbanization from the colonial estimates to the 2020 census, with regional and city comparisons, so chapters can cite a consistent reference point without implying that colonial estimates and modern censuses are the same kind of count.

**Format.** One parent table with four labeled panels (A–D). A panel is not a new table number. Use a repeated header for each panel and a panel label in the first column or as a spanning caption line above the header. If the typeset page cannot hold four panels, break the table at a panel boundary and repeat “App. B, Table 1 (continued)” — do not assign a new number.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **A. Colonial and early national estimates, 1630–1790** | Panel A has its own header: Year \| Scope \| Total population \| White \| Black (enslaved) \| Black (free) \| Indigenous population (separate estimate) \| Urban share \| Source and definition. |
| **Year** | Observation year, not publication year. Use benchmark years, not every year. |
| **Scope** | The geographic and political unit: “British mainland colonies,” “United States,” or a named region. Do not compare a colonial estimate for the seaboard with a census total for the present-day United States without saying so. |
| **Total population** | The estimate or count. State whether it includes Native Americans and whether it includes enslaved people. |
| **White; Black (enslaved); Black (free)** | The available components. If a component is not available for a year, write “not available” and explain; do not leave a blank or infer it by subtraction unless the source does the subtraction. |
| **Indigenous population (separate estimate)** | A separate estimate, not a census category. Label the source and method. Do not add it to the colonial total without saying that the total excludes or includes it. |
| **Urban share** | The share living in places defined as urban in that year. State the threshold and the source. Do not project the modern 2,500-person threshold backward without saying so. |
| **B. Census population, 1790–2020** | Panel B has its own header: Census year \| Total \| White \| Black \| Native American / Alaska Native \| Asian / Native Hawaiian / Pacific Islander \| Some other race \| Two or more races \| Hispanic (any race) \| Urban population \| Urban share \| Scope and notes \| Source. |
| **Census year** | The decennial census year. Use benchmark years in the printed table: 1790, 1800, 1820, 1840, 1860, 1880, 1900, 1920, 1940, 1960, 1980, 2000, 2010, 2020. The full decennial series may live in the production dataset. |
| **Race columns** | Use the census categories for that year, not a single modern scheme. Before 1850, “Black” may include enslaved and free; before 1890, Native Americans were not consistently enumerated; “Asian” and “Pacific Islander” categories change; “Two or more races” begins in 2000. State the category definition in a note. |
| **Hispanic (any race)** | Ethnicity, not a race. Do not add Hispanic to the race columns to produce a total. The census treats Hispanic origin separately. |
| **Urban population and share** | Use the census urban definition for that year. The definition changed in 1910, 1950, 2000, and later; state the threshold and whether urbanized areas or places are used. |
| **C. Regional shares, selected years** | Panel C has its own header: Year \| Northeast \| Midwest \| South \| West \| Source and definition. Use 1790, 1860, 1900, 1950, 2000, 2020. State the Census region boundaries used in each year; the South and West definitions changed with territory and statehood. |
| **D. Largest cities, selected years** | Panel D has its own header: Year \| Rank \| City \| Population \| Source and definition. Use 1790, 1850, 1900, 1950, 2000, 2020. Use the census place definition and note municipal annexations; a modern city boundary is not the historical city. |

**Row grain and required rows.** Panel A: 1630, 1650, 1700, 1750, 1770, 1790. Panel B: the benchmark years listed above. Panel C: the six benchmark years. Panel D: the top five cities in each benchmark year, or the top three if space is tight; state the rank rule.

**Values to gather.** No values are supplied by this guide. The manuscript’s draft anchors are: about 1.17 million people in the British colonies in 1750 (Ch. 8, Table 1); 31,443,321 people in the United States in 1860, including 3,953,760 enslaved people (Ch. 20, Table 2). Both are draft values to verify against the census and the historical series, not settled numbers. The 1790 census total and the 2020 apportionment count must come from the Census Bureau’s own tables. Colonial estimates must come from a named historical series (for example, McCusker and Menard) and be labeled as estimates with a range.

**Cautions and limitations.** This is not one continuous series. Colonial estimates are not censuses; the census undercounts Native Americans, enslaved people, immigrants, and the poor; race categories changed repeatedly; Hispanic origin is separate from race; urban definitions changed; regional boundaries changed; city boundaries annexed. Do not compute a 1630–2020 growth rate from mixed estimates, and do not present a single “U.S. population” for 1630. Every panel needs its own definition note.

---

#### 7.1.2 App. B, Table 2 — `app-b-table-02`

**Owner and location.** `chapters/52-appendix-b.md`, Second dataset; §B.2. **Display number:** App. B, Table 2. **Status:** planned; no dataset exists.

**Purpose.** Provide a compact election reference that distinguishes electoral votes from reported popular votes and turnout, and refuses to invent a national popular vote before meaningful coverage exists. The table should let chapters compare elections without turning every contest into a presidential mandate.

**Format.** One parent table with two panels and a turnout note. Panel A: one row per election, 1789–2024. Panel B: multi-candidate elections where a third ticket won electoral votes or a substantial popular-vote share (at minimum 1860, 1912, 1968, 1992, 2000, 2016, 2024; add others if the chapter uses them). Use a repeated header.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **A. Election summary** | Year \| Winner \| Party \| Winner electoral votes \| Runner-up \| Runner-up electoral votes \| Other electoral votes \| Winner popular votes \| Winner popular-vote share \| Total reported popular vote \| Turnout (%) \| Turnout denominator \| Notes and source. |
| **Year** | Election year. Do not use the inauguration year. |
| **Winner; Party** | The winning candidate and party. For elections decided in the House (1800, 1824), say so in Notes. |
| **Winner electoral votes; Runner-up electoral votes; Other electoral votes** | Electoral votes. “Other” is the sum of all remaining tickets; do not assign them to the runner-up. State the total electoral vote and the majority needed in a note. |
| **Winner popular votes; Winner popular-vote share** | Reported national popular votes and share. For 1789–1823, write “n/a — no national popular vote” and explain that electors were chosen by state legislatures or by limited franchises. Do not fill the cell with a state total or a guess. |
| **Total reported popular vote** | The sum of the reported candidate totals. State whether it includes third-party and write-in votes. |
| **Turnout (%)** | Votes cast divided by the stated denominator. Do not mix ballots cast, total presidential votes, and valid votes without saying which. |
| **Turnout denominator** | Voting-eligible population, voting-age population, or another named series. Name the source (Census, McDonald, Burnham, state records). The denominator is not interchangeable across series. |
| **B. Multi-candidate elections** | Year \| Candidate \| Party \| Popular votes \| Popular-vote share \| Electoral votes \| Notes and source. Include every ticket that won electoral votes and every ticket above the chapter’s stated threshold. Do not include a candidate who was not on the ballot in enough states to affect the result without saying so. |

**Row grain and required rows.** Panel A: every presidential election from 1789 through 2024 (60 elections). Panel B: at least 1860, 1912, 1968, 1992, 2000, 2016, and 2024; add 1824, 1856, 1892, 1912, 1924, 1948, 1968, 1980, 1992, 1996, and 2000 if the chapter discusses them.

**Values to gather.** The chapter data tables supply verified-to-be-checked anchors for 1856 (Ch. 19, Table 2), 1860 (Ch. 20, Table 1), 1864 (Ch. 22, Table 1), and 1912 (Ch. 29, Table 1). Do not copy those cells into Appendix B until the same source and rounding rule have been reconciled. For 1789–1823, the required value is often “no national popular vote,” not a number. For 2024, use the official state canvasses and the Electoral College result; do not use a media call.

**Cautions and limitations.** The Electoral College is not a national popular vote. State legislatures chose electors in several states before 1824; South Carolina used a legislative choice until 1860; some states had restricted franchises. The winners in 1876, 1888, 2000, and 2016 lost the popular vote; the table must show both facts without treating either as a anomaly. Turnout denominators vary widely and change the percentage; never compare a VAP rate with a VEP rate without saying so. Popular-vote totals are revised after canvasses; state the version date.

---

#### 7.1.3 App. B, Table 3 — `app-b-table-03`

**Owner and location.** `chapters/52-appendix-b.md`, Third dataset; §B.3. **Display number:** App. B, Table 3. **Status:** planned; no dataset exists.

**Purpose.** Set out territorial acquisitions and cessions with the instrument, date, area, and nominal cost, distinguishing sovereignty, control, and Native title. The table should show that the United States expanded through several legal forms, not one simple process of “settlement.”

**Format.** One parent table, one row per transaction or instrument. If the table is too wide, split into Panel A (continental acquisitions, 1763–1867) and Panel B (overseas and Caribbean, 1898–1917), with the same columns. A panel is not a new number.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **Sequence** | A short ordinal or date order. Use the instrument date, not the date the territory was organized. |
| **Territory or region** | The named territory or region. Use the period name and add the present-day name in parentheses. |
| **Transaction** | Purchase; cession by treaty; annexation by joint resolution; lease; occupation; boundary settlement; exchange. Do not use “acquisition” for a lease. |
| **From; To** | The transferring and receiving sovereign or claimant. For Native land, write “Native nations” and explain that a European cession did not extinguish Native title. |
| **Instrument** | The treaty, joint resolution, convention, or statute. Give the short name and the citation (for example, Treaty of Paris, 1783; Louisiana Purchase Treaty, 1803). |
| **Signed; Effective** | The date signed and the date the instrument took effect or was ratified. If they differ, show both. |
| **Area (sq mi); Area (km²)** | The area, with the source and whether it is land area, total area, or claimed area. Do not compute a total from incompatible figures. If the source gives only one unit, convert with a stated factor or leave the other blank with a note. |
| **Nominal cost; Currency and units** | The nominal price and the currency/units of the day. Do not inflation-adjust in this column. If the cost includes assumed claims or debts, say so in Cost basis. |
| **Cost basis** | What the price covered: purchase price; assumed claims; boundary commission; lease payments; no payment. Distinguish a purchase price from a total cost. |
| **Sovereignty and control** | Sovereignty; control; lease; occupation; protectorate; Native title not extinguished. Use one or two labels and explain mixed arrangements. |
| **Notes and source** | The source, the treaty article or statute section, and any definitional caveat. |

**Row grain and required rows.** Required rows: 1763 Treaty of Paris (context, not a U.S. acquisition); 1783 Treaty of Paris (independence and boundaries); 1803 Louisiana Purchase; 1819 Adams–Onís Treaty (Florida); 1845 Texas annexation; 1846 Oregon Treaty; 1848 Treaty of Guadalupe Hidalgo; 1853 Gadsden Purchase; 1867 Alaska purchase; 1898 Hawaii annexation; 1898 Treaty of Paris (Puerto Rico, Guam, Philippines); 1899 Samoa partition; 1903 Hay–Bunau-Varilla Treaty (Canal Zone grant); 1917 Danish West Indies purchase. Add the 1850 Clayton–Bulwer Treaty or the 1842 Webster–Ashburton Treaty only if the chapter uses them as boundary instruments, not as acquisitions.

**Values to gather.** Area and cost values must come from the treaty text, the Statutes at Large, or a named reference series. The Louisiana price was 15 million dollars; the Florida transaction involved assumed claims of about 5 million dollars; the Mexican Cession included 15 million dollars plus assumed claims; the Gadsden Purchase was 10 million dollars; Alaska was 7.2 million dollars; the Danish West Indies was 25 million dollars. These are nominal values of the day and must be verified against the instrument before publication. Do not add them into a single “cost of empire” total.

**Cautions and limitations.** Area figures vary by source and by whether water, claims, or Native homelands are included. Nominal costs are not comparable across centuries. A European cession did not extinguish Native title; the table must not imply that Native nations were parties to every instrument. “Sovereignty,” “control,” and “lease” are different legal forms. The 1898 settlement included territories with different constitutional status; do not color them all as states-in-waiting.

---

#### 7.1.4 App. B, Table 4 — `app-b-table-04`

**Owner and location.** `chapters/52-appendix-b.md`, Fourth dataset; §B.4. **Display number:** App. B, Table 4. **Status:** planned; no dataset exists.

**Purpose.** Provide comparable war-mobilization and cost benchmarks with explicit definitions, so chapters do not mix peak strength, cumulative service, battle deaths, all-cause deaths, appropriations, and expenditures. The table should make the human and fiscal cost comparable only where the definitions permit.

**Format.** One parent table, one row per conflict, with a separate row for the Confederacy in the Civil War. If the cost columns are too wide, use Panel A (mobilization and mortality) and Panel B (cost), with the same conflict rows and a repeated header.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **Conflict** | The war or intervention. Use the name the book uses, with dates. |
| **Dates** | Start and end years, or the U.S. involvement period if different. State the difference in a note. |
| **U.S. side / belligerent** | The United States and its allies/co-belligerents, or the opposing side for the Civil War. Do not use “America” for one side in a civil war. |
| **U.S. service members** | Cumulative inductions/enlistments or peak strength — state which. Do not mix the two. For the Civil War, give Union and Confederate separately. |
| **Battle deaths** | Deaths in combat or from wounds, with the source’s definition. Do not include disease deaths. |
| **Other deaths** | Disease, accident, imprisonment, and other non-battle deaths, where the source separates them. |
| **Total deaths** | Battle plus other deaths, only when the components use the same population and period. If the source gives a total without components, say so. |
| **Wounded** | Wounded, with the definition (treated, hospitalized, unique persons). Do not add wounded to deaths to produce “casualties” unless the source does. |
| **Opposing deaths** | Confederate or enemy deaths, only where a source gives a comparable figure. Do not estimate by ratio. |
| **Direct federal cost (nominal)** | Appropriations or expenditures — state which. Give the currency and the period. Do not mix war costs with veterans’ benefits, interest, or later reconstruction costs unless the column label says so. |
| **Cost period** | The years the cost covers. A war’s cost may continue after the fighting. |
| **Cost basis** | Appropriations; expenditures; obligations; estimated; nominal; constant dollars with base year. Do not compare a nominal figure with a constant-dollar figure. |
| **Notes and source** | The source series, the definition, and the main uncertainty. |

**Row grain and required rows.** Required rows: Revolutionary War (1775–1783); War of 1812 (1812–1815); Mexican-American War (1846–1848); Civil War, Union (1861–1865); Civil War, Confederacy (1861–1865); Spanish-American War (1898); World War I (1917–1918); World War II (1941–1945); Korean War (1950–1953); Vietnam War (1964–1973, with the 1955–1975 advisory period noted); Gulf War (1990–1991); Afghanistan (2001–2021); Iraq (2003–2011, with the later anti-ISIS period noted separately if included).

**Values to gather.** Use the official Defense Casualty Analysis System for modern conflicts; the National Archives and the Official Records for the Civil War; the American Battle Monuments Commission for World War I and II; and a named cost series (CBO, OMB, Congressional Research Service) for dollars. The Civil War mortality row must choose one of the estimates in Ch. 22, Table 2, or show them side by side; do not create a new total. World War I: 116,516 total deaths, including 53,402 battle and 63,114 non-combat. These are draft anchors, not settled values.

**Cautions and limitations.** Definitions are the main hazard. “Service members” can mean peak strength, cumulative inductions, or registered personnel; “deaths” can mean battle deaths, all-cause deaths, or excess deaths; “cost” can mean appropriations, expenditures, or a modeled long-term cost. The Civil War estimates differ by method (618,222 conventional; about 750,000 Hacker; about 698,000 in 2024) and are not interchangeable. Confederate records are incomplete. Do not add veterans’ benefits, interest, or reconstruction to a war-cost column without a separate label. Do not compare nominal dollars across centuries without a price index and base year.

---

#### 7.1.5 App. B, Table 5 — `app-b-table-05`

**Owner and location.** `chapters/52-appendix-b.md`, Fifth dataset; §B.5. **Display number:** App. B, Table 5. **Status:** planned; no dataset exists.

**Purpose.** Present immigration admissions by decade and origin, foreign-born stock, and the 1921, 1924, and 1929 quota systems, while keeping admissions, net migration, foreign-born stock, and unauthorized population distinct. The table should support the chapters’ arguments about belonging and exclusion without turning four different measures into one.

**Format.** One parent table with three panels: A (admissions by decade and origin), B (foreign-born stock and share), C (quota systems). Use a repeated header for each panel. The colonial context is a labeled note or a short pre-1820 panel, not a row in the 1820–2020 series.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **A. Admissions by decade** | Decade \| Total admissions \| Europe \| Asia \| Americas \| Africa \| Oceania \| Not specified \| Source and definition. Use fiscal decades or calendar decades consistently; state which. |
| **Total admissions** | Legal permanent resident admissions, not net migration, not foreign-born stock, not unauthorized population. |
| **Region columns** | The region of birth or last residence, as the source defines it. Do not use “continent” categories that change across series without a note. |
| **Not specified** | A residual category, not a guess. If the source does not provide a regional breakdown for a decade, write “not available.” |
| **B. Foreign-born stock** | Census year \| Foreign-born population \| Foreign-born share of total population \| Source and definition. Use 1850–2020; the census did not ask a consistent nativity question before 1850. |
| **C. Quota systems** | System \| Year \| Basis of quota \| Annual ceiling \| Selected country quotas \| Principal exclusions \| Source. Rows: 1921 Emergency Quota Act; 1924 Johnson–Reed interim formula; 1929 national-origins system. |
| **Selected country quotas** | Use a consistent set of countries across the three systems (for example, United Kingdom, Ireland, Germany, Italy, Russia/Poland, China, Japan, Mexico, Canada). State the quota year and whether the figure is a country maximum or an allocated number. Do not imply that the Western Hemisphere was subject to the same quota. |

**Row grain and required rows.** Panel A: decades from 1820–1829 through 2010–2019, plus 2020–2024 if the source permits; before 1820, a labeled colonial note, not a row. Panel B: 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020. Panel C: 1921, 1924, 1929.

**Values to gather.** Use the Yearbook of Immigration Statistics and the Census Bureau’s foreign-born tables. The 1921 ceiling is about 350,000; the 1924 interim ceiling is about 165,000; the 1929 national-origins ceiling is about 150,000. These are approximate and must be reconciled against the actual quota schedules. Do not use a single “immigration” number that mixes admissions and foreign-born stock.

**Cautions and limitations.** Admissions are legal permanent residents, by fiscal year; net migration includes emigration and is usually a residual estimate; foreign-born stock is a census count; unauthorized population is a separate estimate with its own method. Before 1820 there were no federal admission statistics; the colonial context must be labeled as context, not comparable data. Region categories change; “Asia” may include the Middle East or not; “Americas” may include Canada and Latin America or only Latin America. Quota ceilings changed within years and did not apply to the Western Hemisphere. Do not treat a quota as the actual number admitted.

---

#### 7.1.6 App. B, Table 6 — `app-b-table-06`

**Owner and location.** `chapters/52-appendix-b.md`, Sixth dataset; §B.6. **Display number:** App. B, Table 6. **Status:** planned; no dataset exists.

**Purpose.** Separate the enslaved population census, the Atlantic slave trade, the domestic trade, and price benchmarks, so no single series is mistaken for another. The table should show the scale of enslavement and coerced movement without pretending that a database of voyages is a census of people.

**Format.** One parent table with four panels: A (17th-century Caribbean benchmarks), B (U.S. enslaved population, 1790–1860), C (trade estimates), D (price benchmarks). Use a repeated header and a panel label. Do not combine the panels into a single total.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **A. Caribbean benchmarks** | Colony or place \| Year \| Enslaved population \| Total population \| Enslaved share \| Source and definition. Use named colonies and benchmark years; do not generalize “the Caribbean.” |
| **B. U.S. enslaved population** | Census year \| Enslaved population \| Total population \| Enslaved share \| Free Black population \| Scope (states/territories) \| Source. Use 1790–1860 decennial years. |
| **C. Trade estimates** | Series \| Period \| Estimate \| Range \| Definition \| Source. Rows: transatlantic disembarkations to mainland North America; domestic trade; illegal importations after 1808. Do not use the transatlantic database as a domestic-trade census. |
| **D. Price benchmarks** | Year \| Place \| Category \| Nominal price \| Currency \| Source. Use named categories (for example, prime field hand, skilled artisan, child) and named markets; a price sample is not an average. |

**Row grain and required rows.** Panel A: at least Barbados, Jamaica, and Saint-Domingue (or another named colony) at two or three 17th-century benchmark years. Panel B: 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860. Panel C: transatlantic to mainland North America, 1600–1860; domestic trade, 1790–1860; illegal importations, 1808–1860. Panel D: at least two markets and two periods (for example, Virginia and New Orleans, 1790s and 1850s).

**Values to gather.** Use the 1790–1860 census schedules for Panel B; SlaveVoyages for the transatlantic series; a named scholarly estimate for the domestic trade (Tadman, Fogel–Engerman, Baptist, or Johnson) and state its method; and named probate, auction, or newspaper records for prices. The manuscript’s draft anchor is 3,953,760 enslaved people in 1860 (Ch. 20, Table 2), which must be verified against the printed census. Do not invent a domestic-trade total or average price.

**Cautions and limitations.** The census undercounts enslaved people; the Three-Fifths Clause is a representation rule, not a population count; “Black” and “mulatto” categories changed; the transatlantic database counts voyages and embarked/disembarked people, not the resident population; domestic-trade estimates vary widely and use different definitions; price samples are not averages and may not be comparable across places and categories. Caribbean benchmarks are not U.S. data. Do not add the panels into a single “slaves imported” total.

---

#### 7.1.7 App. B, Table 7 — `app-b-table-07`

**Owner and location.** `chapters/52-appendix-b.md`, Seventh dataset; §B.7. **Display number:** App. B, Table 7. **Status:** planned; no dataset exists.

**Purpose.** Provide a labeled set of economic and communications benchmarks, with breaks and definitions, so chapters can compare public finance, production, labor, inequality, and communications without implying one continuous series. The table should make the breaks visible rather than smooth them away.

**Format.** One parent table with six panels: A (public finance), B (production and infrastructure), C (labor and prices), D (inequality), E (communications), F (regional employment). Use a repeated header for each panel. Do not merge panels into a single wide table; the definitions differ.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **A. Public finance** | Year \| Federal debt (nominal) \| GDP (nominal) \| Debt/GDP \| Federal receipts \| Federal outlays \| Surplus or deficit \| Price index and base \| Source. State whether debt is gross or net, and whether receipts/outlays are fiscal years. |
| **B. Production and infrastructure** | Year \| Railroad mileage \| Steel production (tons) \| Manufacturing output index \| Urban share \| Source. State the rail network definition (first main track? all track?), the steel product, and the output index base. |
| **C. Labor and prices** | Year \| Unemployment rate \| Labor force \| Union density \| CPI or price index \| Real GDP per capita \| Source. Name the unemployment series (Lebergott, Darby, BLS) and the price base. |
| **D. Inequality** | Year \| Top 1% share \| Top 10% share \| Gini \| Source. Name the series (Piketty–Saez, Census, or another) and whether the unit is family, household, or individual; pre-tax or post-tax; including or excluding capital gains. |
| **E. Communications** | Year \| Daily newspapers \| Newspaper circulation \| Circulation per capita \| Telephones \| Telephones per 1,000 \| Source. State missing years; do not interpolate without saying so. |
| **F. Regional employment** | Year \| Region \| Total employment \| Manufacturing employment \| Change from prior benchmark \| Source. State the region definitions and whether the change is absolute or percentage. |

**Row grain and required rows.** Panel A: benchmark years 1790, 1800, 1820, 1840, 1860, 1880, 1900, 1920, 1930, 1940, 1950, 1960, 1980, 2000, 2020, 2024 where available. Panel B: 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1970, 2000, 2020. Panel C: 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2024. Panel D: 1913, 1929, 1945, 1960, 1980, 2000, 2020. Panel E: 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020. Panel F: 1969, 1979, 1990, 2000, 2010, 2019.

**Values to gather.** Use the Treasury’s historical debt tables, BEA GDP series, Census historical statistics, BLS labor series, Piketty–Saez inequality tables, and the Census/Ayer newspaper and telephone series. Do not copy a number from a secondary chart without the underlying series. The manuscript’s draft anchors (for example, the $54 million versus $77 million debt discrepancy in Ch. 13) are unresolved and must not be entered as settled values.

**Cautions and limitations.** This is a set of panels, not one series. Nominal and real dollars are not comparable; GDP series are revised; the unemployment rate has multiple historical series; union density has different denominators; inequality series differ by unit, tax treatment, and capital gains; newspaper and telephone counts have missing years and changing definitions; regional employment boundaries change. State every break. Do not compute a 1790–2024 growth rate from mixed series or imply that all measures share one base year.

---

#### 7.1.8 App. B, Table 8 — `app-b-table-08`

**Owner and location.** `chapters/52-appendix-b.md`, Eighth dataset; §B.8. **Display number:** App. B, Table 8. **Status:** planned; no dataset exists.

**Purpose.** Provide bounded land-use, public-works, and settlement data for 1930–1940, tied to Map 26, without promising continental environmental series the evidence cannot support. The table should show what the New Deal built and where, and what the drought and migration did to land and people.

**Format.** One parent table with four panels: A (TVA projects), B (CCC camps), C (land use and drought), D (settlement and migration). Use a repeated header. Do not add bison, forest, carbon-dioxide, or extreme-weather series; those are prose topics, not appendix datasets.

**Columns and panels.**

| Column or panel | Required content and rules |
|---|---|
| **A. TVA projects** | Project \| State and county \| Coordinates (lat, long) \| Type (dam, reservoir, power plant, navigation) \| Construction dates \| Capacity (MW) \| Land acquired (acres) \| Source and note. Use one coordinate pair per project; state the datum. |
| **B. CCC camps** | State \| Number of camps \| Fiscal year or date \| Camp type (state park, private land, federal land) \| Enrollees \| Work categories \| Source. State whether the count includes all camp types or only federal camps. |
| **C. Land use and drought** | Year \| Region or state \| Cropland harvested (acres) \| Abandoned farmland (acres) \| Dust Bowl migration out \| Source. Define “abandoned” and “migration out”; do not use a residual estimate as a count. |
| **D. Settlement and migration** | Year \| State or region \| Net migration \| Farm population \| Source. State whether net migration is estimated from births/deaths or from census residuals. |

**Row grain and required rows.** Panel A: the major TVA dams and reservoirs (for example, Norris, Wheeler, Pickwick, Chickamauga, Kentucky, Fontana) plus the initial land-acquisition totals. Panel B: the states with the largest CCC camp counts and a national total; use fiscal years 1933–1942. Panel C: 1930, 1935, 1940 for the southern Plains and the Dust Bowl counties; define the county set. Panel D: 1930, 1940 for the southern Plains, California, and the major destination states.

**Values to gather.** Use TVA annual reports and land-acquisition records, CCC annual reports and RG 35, the Census of Agriculture, and the 1930/1940 census migration reports. The manuscript’s Map 26 needs counts and mapped coordinates; App. B, Table 8 currently lacks them. Do not invent a camp count or a migration total from a secondary summary.

**Cautions and limitations.** CCC camp counts vary by fiscal year and by whether state, private, and federal camps are included. TVA land acquisition includes reservoir take and may include easements, not just fee simple. Dust Bowl migration estimates are often residual estimates, not counts; “Okies” is not a census category. County boundaries and census definitions change. Do not present a single “Dust Bowl” number without the county set and years.

---

### 7.2 Appendix C. Gazetteer (1)

#### 7.2.1 App. C, Table 1 — `app-c-table-01`

**Owner and location.** `chapters/53-appendix-c.md`, Gazetteer; §C.2. **Display number:** App. C, Table 1. **Status:** planned; the entry list exists, the table does not.

**Purpose.** Give readers a concise gazetteer of the places named in the book, with historical and present names, Indigenous homelands, and map references, without inventing translations or equating a colonial name with a nation’s own name. The gazetteer is a reading aid, not evidence for the maps’ geography.

**Format.** One table, one row per entry, alphabetical by the entry’s preferred name. Use a repeated header if the table breaks. The catalog of maps, figures, and images is prose or a separate list, not another table number.

**Columns.**

| Column | Required content and rules |
|---|---|
| **Entry** | The preferred name used in the book. For contested or dual names, use the form the book uses and put the alternate in “Historical and present names.” |
| **Historical and present names** | The historical name(s), the present name, and the state or country. Do not invent a translation. If the historical name is a colonial imposition, say so. |
| **Indigenous nation(s) or homeland** | The specific nation(s) and the preferred name where known. Do not write “Native Americans” or “Indigenous peoples” as a substitute for a nation. If the homeland is contested, say so. |
| **Type** | City; town; site; region; river; bay; mountain range; archaeological site; neighborhood. Use one label. |
| **First chapter** | The chapter where the place first appears, with the section if useful. |
| **Maps** | The map number(s) where the place appears. Use the registered map numbers, not draft aliases. |
| **Coordinates** | Latitude and longitude, with the datum, for a point. For a region, give a representative point and a note; do not pretend a point defines a boundary. |
| **Naming note** | A short note on naming, translation, or contested usage. No invented etymology. |
| **Source** | The community, archival, or reference source for the name and coordinates. |

**Row grain and required rows.** The 77 entries listed in the README: Acoma; Albany; American Bottom; Beringia; Black Hills; Boston; Cahokia; Chaco Canyon; Charleston; Chattanooga; Cherokee Nation; Chesapeake; Chicago; Chickamauga; Colfax; Comanchería; Detroit; Dinétah; Edisto Island; Fort Duquesne; Fort Necessity; Fort Sumter; Gettysburg; Guam/Guåhan; Harlem; Hawaii/Hawaiʻi; Hochelaga; Indian Territory; Jamestown; Kansas; Lecompton; Levittown; Little Bighorn; Los Angeles; Lowell; Manhattan; Memphis; Mexico City; Montgomery; Montreal; Natchez; Nauvoo; New Amsterdam; New Echota; New Orleans; New Sweden; New York; Niagara; Oklahoma; Onondaga; Patuxet; Philadelphia; Phoenix; Poverty Point; Promontory Summit; Quebec; Richmond; Río Grande; Roanoke; Salem; San Antonio; San Francisco; San Juan Pueblo/Ohkay Owingeh; Santa Fe; Savannah; Seneca Falls; Serpent Mound; St. Augustine; St. Louis; Tahlequah; Tenochtitlan; Tsenacomoco; Tulsa; Valley Forge; Washington, D.C.; Wounded Knee; Yorktown.

**Values to gather.** Use the nation’s own spelling and the community’s preferred name where known; the README’s slash forms (Guam/Guåhan, Hawaii/Hawaiʻi) are a starting point, not a license to invent a third spelling. Coordinates must come from a named gazetteer or map, not memory. For archaeological sites, use the site’s published coordinates and note the source. For disappeared or renamed places, give the present location and the source of the identification.

**Cautions and limitations.** Do not describe Serpent Mound’s builders or date as conclusively Adena; do not describe Beringia as a proven single route; do not treat an Indigenous homeland as blank space. Historical names are not always the inhabitants’ names; a colonial name may be a misnomer or a translation. Coordinates are points, not boundaries. Verify Indigenous names with community sources before publication; if a community has not authorized a name or image, say so and use the most defensible published form.

---

### 7.3 Appendix D. Chronology (7)

All seven tables share the same five tracks. A row is a period or turning point, not every event. Each cell carries dated events and a chapter/source key; uncertainty is marked in the cell or a note. Do not duplicate an event at a boundary year; place it in one table and cross-reference it in the next.

**Standard columns for every Appendix D table.**

| Column | Required content and rules |
|---|---|
| **Period** | The row’s date range or turning point. Use en dashes for ranges. |
| **Politics and law** | Dated political, constitutional, legal, and policy events. Put the date first, then the event, then the chapter key. |
| **War and foreign affairs** | Dated wars, diplomacy, treaties, military action, and foreign policy. |
| **Economy and technology** | Dated economic, industrial, technological, and communications events. |
| **Society and culture** | Dated social, cultural, religious, intellectual, and demographic events. |
| **Land, environment, and demography** | Dated land use, environment, agriculture, extraction, migration, and population events. |
| **Cross-references and sources** | The chapter/section key, the named note key, and any uncertainty marker. Do not put a full bibliography in the cell. |

#### 7.3.1 App. D, Table 1 — `app-d-table-01`

**Owner and location.** `chapters/54-appendix-d.md`, §D.1. **Display number:** App. D, Table 1. **Status:** planned; the chronology is a prose seed.

**Coverage.** Deep past–1606.

**Purpose.** Present the period’s turning points across the five tracks so readers can see contemporaneous developments without treating any one track as the cause of the others.

**Suggested period rows (revise against the chapters; do not force every event into a row).**

- Before c. 20,000 BCE — peopling and the last glacial maximum
- c. 20,000–13,000 BCE — pre-Clovis and Clovis-era evidence
- c. 13,000–8000 BCE — Paleoindian to Archaic transition
- c. 8000–3000 BCE — Archaic economies and early earthworks
- c. 3000–1000 BCE — Poverty Point and the lower Mississippi
- c. 1000 BCE–500 CE — Adena and Hopewell
- c. 500–1000 CE — late Woodland and the rise of Cahokia
- c. 1000–1350 CE — Cahokia, Chaco, and the Mississippian world
- c. 1350–1500 CE — dispersal, drought, and political reconfiguration
- 1492–1551 — contact, conquest, and the first epidemics
- 1551–1606 — European claims and Indigenous diplomacy

**Cautions.** A chronology is not a causal argument. Use the date the evidence supports; mark `c.` or `?` where the date is uncertain; do not import a 2025–26 event without a dated record; do not duplicate an event at a boundary. The five tracks are filing categories, not a claim that politics drives the others. For 2001–2026, every entry is a research task until checked against a dated record.

---

#### 7.3.2 App. D, Table 2 — `app-d-table-02`

**Owner and location.** `chapters/54-appendix-d.md`, §D.2. **Display number:** App. D, Table 2. **Status:** planned; the chronology is a prose seed.

**Coverage.** 1607–1699.

**Purpose.** Present the period’s turning points across the five tracks so readers can see contemporaneous developments without treating any one track as the cause of the others.

**Suggested period rows (revise against the chapters; do not force every event into a row).**

- 1607–1620 — Jamestown, Powhatan, and the first Virginia settlements
- 1620–1640 — Plymouth, Massachusetts Bay, and the great migration
- 1640–1660 — English Civil War, Caribbean slavery, and colonial law
- 1660–1675 — Restoration, proprietary colonies, and the Covenant Chain
- 1675–1680 — King Philip’s War and its aftermath
- 1680–1699 — Pueblo Revolt, the Glorious Revolution, and imperial war

**Cautions.** A chronology is not a causal argument. Use the date the evidence supports; mark `c.` or `?` where the date is uncertain; do not import a 2025–26 event without a dated record; do not duplicate an event at a boundary. The five tracks are filing categories, not a claim that politics drives the others. For 2001–2026, every entry is a research task until checked against a dated record.

---

#### 7.3.3 App. D, Table 3 — `app-d-table-03`

**Owner and location.** `chapters/54-appendix-d.md`, §D.3. **Display number:** App. D, Table 3. **Status:** planned; the chronology is a prose seed.

**Coverage.** 1700–1799.

**Purpose.** Present the period’s turning points across the five tracks so readers can see contemporaneous developments without treating any one track as the cause of the others.

**Suggested period rows (revise against the chapters; do not force every event into a row).**

- 1700–1730 — colonial growth, slavery, and the first Great Awakening
- 1730–1750 — revival, print, and imperial rivalry
- 1750–1763 — the Seven Years’ War and the 1763 settlement
- 1763–1775 — imperial reform and colonial resistance
- 1775–1783 — the War for Independence
- 1783–1789 — confederation, debt, and the Constitutional Convention
- 1789–1799 — the federal republic, party formation, and the 1790s

**Cautions.** A chronology is not a causal argument. Use the date the evidence supports; mark `c.` or `?` where the date is uncertain; do not import a 2025–26 event without a dated record; do not duplicate an event at a boundary. The five tracks are filing categories, not a claim that politics drives the others. For 2001–2026, every entry is a research task until checked against a dated record.

---

#### 7.3.4 App. D, Table 4 — `app-d-table-04`

**Owner and location.** `chapters/54-appendix-d.md`, §D.4. **Display number:** App. D, Table 4. **Status:** planned; the chronology is a prose seed.

**Coverage.** 1800–1899.

**Purpose.** Present the period’s turning points across the five tracks so readers can see contemporaneous developments without treating any one track as the cause of the others.

**Suggested period rows (revise against the chapters; do not force every event into a row).**

- 1800–1815 — Jeffersonian expansion and the War of 1812
- 1815–1830 — the Market Revolution and the Missouri crisis
- 1830–1848 — removal, reform, and continental expansion
- 1848–1860 — the sectional crisis and the road to secession
- 1861–1865 — the Civil War and emancipation
- 1865–1877 — Reconstruction and counterrevolution
- 1877–1890 — industrialization, the West, and Jim Crow
- 1890–1899 — populism, depression, and empire

**Cautions.** A chronology is not a causal argument. Use the date the evidence supports; mark `c.` or `?` where the date is uncertain; do not import a 2025–26 event without a dated record; do not duplicate an event at a boundary. The five tracks are filing categories, not a claim that politics drives the others. For 2001–2026, every entry is a research task until checked against a dated record.

---

#### 7.3.5 App. D, Table 5 — `app-d-table-05`

**Owner and location.** `chapters/54-appendix-d.md`, §D.5. **Display number:** App. D, Table 5. **Status:** planned; the chronology is a prose seed.

**Coverage.** 1900–1945.

**Purpose.** Present the period’s turning points across the five tracks so readers can see contemporaneous developments without treating any one track as the cause of the others.

**Suggested period rows (revise against the chapters; do not force every event into a row).**

- 1900–1916 — Progressivism, reform, and overseas empire
- 1917–1920 — World War I, the Red Scare, and the suffrage amendment
- 1920–1929 — prosperity, culture, and exclusion
- 1929–1933 — the Great Depression and the banking crisis
- 1933–1939 — the New Deal and its limits
- 1939–1945 — the Second World War and the Holocaust

**Cautions.** A chronology is not a causal argument. Use the date the evidence supports; mark `c.` or `?` where the date is uncertain; do not import a 2025–26 event without a dated record; do not duplicate an event at a boundary. The five tracks are filing categories, not a claim that politics drives the others. For 2001–2026, every entry is a research task until checked against a dated record.

---

#### 7.3.6 App. D, Table 6 — `app-d-table-06`

**Owner and location.** `chapters/54-appendix-d.md`, §D.6. **Display number:** App. D, Table 6. **Status:** planned; the chronology is a prose seed.

**Coverage.** 1946–2000.

**Purpose.** Present the period’s turning points across the five tracks so readers can see contemporaneous developments without treating any one track as the cause of the others.

**Suggested period rows (revise against the chapters; do not force every event into a row).**

- 1946–1953 — Cold War origins, containment, and Korea
- 1953–1960 — affluence, conformity, and the early civil rights movement
- 1960–1968 — the rights revolution, the Great Society, and Vietnam
- 1968–1974 — polarization, Watergate, and the end of the postwar boom
- 1974–1980 — stagflation, détente, and the turn to the right
- 1980–1991 — the Reagan revolution and the end of the Cold War
- 1991–2000 — globalization, the new economy, and culture wars

**Cautions.** A chronology is not a causal argument. Use the date the evidence supports; mark `c.` or `?` where the date is uncertain; do not import a 2025–26 event without a dated record; do not duplicate an event at a boundary. The five tracks are filing categories, not a claim that politics drives the others. For 2001–2026, every entry is a research task until checked against a dated record.

---

#### 7.3.7 App. D, Table 7 — `app-d-table-07`

**Owner and location.** `chapters/54-appendix-d.md`, §D.7. **Display number:** App. D, Table 7. **Status:** planned; the chronology is a prose seed.

**Coverage.** 2001–October 29, 2026.

**Purpose.** Present the period’s turning points across the five tracks so readers can see contemporaneous developments without treating any one track as the cause of the others.

**Suggested period rows (revise against the chapters; do not force every event into a row).**

- 2001–2008 — September 11, the war on terror, and the financial crisis
- 2008–2016 — the Obama era, recovery, and polarization
- 2016–2021 — the populist turn, impeachment, and January 6
- 2021–October 29, 2026 — the unsettled present

**Cautions.** A chronology is not a causal argument. Use the date the evidence supports; mark `c.` or `?` where the date is uncertain; do not import a 2025–26 event without a dated record; do not duplicate an event at a boundary. The five tracks are filing categories, not a claim that politics drives the others. For 2001–2026, every entry is a research task until checked against a dated record.

---
## 8. Non-published table-shaped material

The 80-table count excludes the following items. They are recorded here so no one mistakes a planning table, a figure draft, or an editorial inventory for a published table.

### 8.1 Figure-backing tables

Six table-shaped drafts are named in the README as backing for figures. They become charts or diagrams, not additional published tables. Their underlying data must be preserved in the figure’s production record, and their numbers must not be turned into a smooth series merely by plotting them.

| Tracking ID | Owner and location | Disposition |
|---|---|---|
| **`ch16-figure-data`** | Ch. 16, §2.3 | Backing for Figure 3 (the electorate, 1824–1840). Not a separate table number. |
| **`ch24-figure-data`** | Ch. 24, after Study Questions | Backing for Figure 4 (industry and urbanization, 1865–1900). Relocate to the production record. |
| **`ch26-figure-data`** | Ch. 26, §4.3 | Backing for Figure 5 (disfranchising constitutions, 1890–1910). Verify the legal mechanisms. |
| **`ch28-figure-data`** | Ch. 28, §1.2 | Backing for Figure 6 (a national audience, 1870–1900). Verify the rounded estimates. |
| **`ch33-figure-data`** | Ch. 33, §2.2 | Backing for Figure 7 (banking, unemployment, and prices, 1929–1933). Audit the series definitions. |
| **`ch35-figure-data`** | Ch. 35, §1.2 | Backing for Figure 8 (neutrality’s statutory architecture, 1935–1941). Use direct statute citations. |

A seventh figure-backing table is present in the current Chapter 9 file:

| Tracking ID | Owner and location | Disposition |
|---|---|---|
| **`ch09-figure-data`** | Ch. 9, §1, “Draft Figure 1 data (planning table)” | Backing for Figure 1 (imperial debt and colonial revenue, 1756–1770). Not a published table. The colonial-revenue column is unsourced and must not be guessed. |

The README’s six named figure-backing tables are not present as separate blocks in the current chapter files. Do not assume they were lost; they may have been folded into the figures’ prose or never seeded. Rebuild each from the figure’s caption and the chapter’s evidence notes, and record the data in the figure’s production record.

### 8.2 Editorial and catalog tables

Three table-shaped editorial records are not published:

| Tracking ID | Location | Disposition |
|---|---|---|
| **`app-b-editorial-crosswalk`** | Appendix B, “Tables in the Chapters” | Editorial inventory; superseded by the README register. Omit from publication. |
| **`app-c-editorial-concordance`** | Appendix C, “Concordance of Draft Map Numbers” | Editorial repair aid; retain in the production record, not in the book. |
| **`app-c-editorial-figure-list`** | Appendix C, “Figures” | Convert to brief catalog entries; not an extra published table. |

### 8.3 Page-budget and planning tables

Every chapter opens with a page-and-word budget table. It is an unnumbered production table. It must not be captioned, numbered, counted in the 80, or typeset as a reader-facing table. The structural checker reports it as an uncaptioned planning table; that `INFO` is expected and is not a defect.

### 8.4 Table-shaped figures

A figure that is laid out as a grid of numbers is still a figure. Do not give it a table number, a table caption, or a row in the 80-table register. The six figure-backing drafts and the Chapter 9 debt table are the current examples. If a future figure needs a data appendix, put the data in the figure’s production record or in the relevant Appendix B panel, not in a new unregistered table.

## 9. Register discrepancies and decisions needed

The following discrepancies were found while compiling this guide. They are recorded rather than silently repaired. Each is a decision for the owner of the README register and the affected chapter.

| Item | README register | Actual manuscript | Decision needed |
|---|---|---|---|
| **Ch. 8, Table 2 location** | §5.2 | §5.1, “The Peace of Paris and the reshuffling of empires,” under “Draft Table 2” | Correct the README to §5.1, or move the table to §5.2 and update the chapter. The table belongs with the Peace of Paris, so §5.1 is the better location. |
| **Ch. 31, Table 2 location** | §5.4 | §5.3, “Table 2: the Senate votes” | Correct the README to §5.3, or move the table to §5.4. The table belongs with the Senate fight, so §5.3 is the better location. |
| **Current table-block count** | 81 pipe-table blocks (historical inventory) | 65 blocks: 51 historiographical + 13 registered data + 1 figure-backing | Update the README’s inventory sentence to distinguish the historical count from the current file count. Do not use 81 as the published-table count. |
| **Figure-backing tables** | Six named (`ch16`, `ch24`, `ch26`, `ch28`, `ch33`, `ch35`) | Not present as separate blocks; Chapter 9 has a seventh figure-backing table | Rebuild the six from the figures’ evidence, or record that they were never seeded. Do not count them as published tables. |
| **Chapter 22 table placeholders** | Tables 1 and 2 registered | The draft has bracketed display labels (`[Table 1. ...]`, `[Table 2. ...]`) before each table, alongside a prose reference | Replace each bracket with the table itself or a clean heading. Do not leave a bracketed placeholder in the typeset book. |
| **Chapter 29 table placeholder** | Table 1 registered | Bracketed display label `[Table 1. The election of 1912]` before the table | Replace with the table or a clean heading; the prose reference is already present. |
| **Chapter 30 table placeholder** | Table 1 registered | Bracketed display label `[Table 1. Instruments of Caribbean control, 1901–1917]` before the table | Replace with the table or a clean heading; the prose reference is already present. |
| **Chapter 31 table placeholders** | Tables 1 and 2 registered | Bracketed display labels before both tables | Replace with the tables or clean headings; the prose references are already present. |
| **Chapter 32 table placeholder** | Table 1 registered | Bracketed display label `[Table 1. Immigration quota systems]` before the table | Replace with the table or a clean heading; the prose reference is already present. |
| **Ch. 30 Table 1 heading** | §1.4, Table 1 | Heading reads “Table 1 and Map 23: the instruments, 1901–1917” | Keep the heading, but ensure the table and map are referenced separately in the prose and the caption does not imply they are one object. |
| **Appendix B/C/D files** | 8 + 1 + 7 tables planned | Files are still Stage 2 seeds; no table blocks exist | Build the tables from this guide; do not treat the seed’s numbered list as data. |

Two further consistency checks are not errors but need a decision before typesetting:

1. **Table captions in the drafts sometimes say “Draft Table” or omit the display number.** The final caption must use the registered display number and the exact title. The guide supplies the required caption for each chapter data table; the historiographical tables’ captions are already in the register’s form.
2. **The source lines still say “Status: `planned`.”** That is correct for the draft stage, but a verified table’s source line must say what was verified, against which source and locator, and on what date. Do not leave `planned` in a published table.

## 10. Research checklist by source family

The following checklist is organized by the kind of data the tables need. It is not a bibliography; it tells you what to open, what to record, and what not to do.

**Suggested order of work.** Start with App. B, Table 2 (elections) and App. B, Table 1 (population), because the chapter election and resource tables depend on them. Then build App. B, Tables 3–7. Then verify the 13 chapter data tables against those foundations. Then build App. B, Table 8, the gazetteer, and the chronology. Verify the 51 historiographical tables last, because they need the works themselves, not the reference series, and they are the easiest to leave in a plausible but unverified state.

### 10.1 Population, urbanization, and elections

- **Open:** the decennial census volumes and the Census Bureau’s historical tables; the Census of Population and Housing for 2020; the historical statistics series used by the chapter (for example, McCusker and Menard for colonial estimates); the official state canvasses and the Electoral College result for elections.
- **Record:** observation year, geographic scope, race/ethnicity category definitions, urban threshold, total population, component populations, and the source table/page.
- **Do not:** add colonial estimates to census counts; treat Hispanic origin as a race; compare a 1790 “urban” share with a 2020 “urban” share without the definition; invent a national popular vote before 1824; use a media call for a presidential result.

### 10.2 Territory, treaties, and war

- **Open:** the treaty text in the Statutes at Large or a documentary edition; the Senate ratification record; the official casualty series (Defense Casualty Analysis System, National Archives, ABMC); the cost series (OMB, CBO, CRS) with its definition.
- **Record:** instrument date and effective date, parties, area and area definition, nominal cost and cost basis, service definition, death definition, cost period, and source locator.
- **Do not:** treat a lease as an annexation; treat a European cession as extinguishing Native title; add battle deaths and non-battle deaths if the source does not; compare appropriations with expenditures; mix Civil War mortality estimates.

### 10.3 Immigration, slavery, and coerced movement

- **Open:** the Yearbook of Immigration Statistics; the Census Bureau’s foreign-born tables; the 1790–1860 census schedules; SlaveVoyages; a named domestic-trade study; probate, auction, and newspaper price records.
- **Record:** admissions vs stock vs net migration; fiscal vs calendar year; region definitions; census year and scope; voyage vs resident population; trade estimate and method; price category and market.
- **Do not:** equate admissions with net migration; treat the transatlantic database as a domestic census; add the panels into one total; use a price sample as an average; ignore the undercount.

### 10.4 Economy, labor, and communications

- **Open:** Treasury historical debt tables; BEA GDP series; Census historical statistics; BLS labor series; Piketty–Saez inequality tables; Census/Ayer newspaper and telephone series; County Business Patterns for regional employment.
- **Record:** nominal vs real, price index and base year, stock vs flow, series break, unemployment definition, union-density denominator, inequality unit and tax treatment, missing years.
- **Do not:** splice series without a note; compare a 1790 nominal dollar with a 2020 dollar; treat a stock series as a flow; interpolate a missing communications year without saying so.

### 10.5 New Deal land use and public works

- **Open:** TVA annual reports and land-acquisition records; CCC annual reports and RG 35; Census of Agriculture; 1930/1940 census migration reports.
- **Record:** project type, coordinates and datum, construction dates, capacity, land acquired (fee vs easement), camp type and fiscal year, county set, migration method.
- **Do not:** count all camp types as one; treat reservoir take as fee simple; use a residual migration estimate as a count; add bison, forest, carbon-dioxide, or extreme-weather series that the appendix does not support.

### 10.6 Gazetteer and chronology

- **Open:** the nation’s own sources and community-authorized names; the published site or map coordinates; the chapter’s dated evidence; the National Archives and other repositories for 2025–26 records.
- **Record:** preferred name, historical/present name, nation/homeland, type, first chapter, map number, coordinates and datum, naming note, source.
- **Do not:** invent a translation or etymology; treat a point as a boundary; describe Serpent Mound as conclusively Adena; describe Beringia as a proven single route; import a 2025–26 event without a dated record; duplicate an event at a chronology boundary.

### 10.7 Historiographical tables

- **Open:** the named work itself, not only a review or publisher description. If the work is not accessible, use an authorized excerpt or a scholarly review and say so in the source line.
- **Record:** the exact claim, the page or chapter, the work’s scope, and the strongest published criticism. A row’s “limitation” should cite a critic or the work’s own stated limits, not the compiler’s impression.
- **Do not:** invent a token opposing view; list a work you have not identified; use a review’s paraphrase as the historian’s argument; make the limitation a caricature; add a “winner” column; confuse a publication year with the historical period.

## 11. Sign-off checklist

A table is ready to publish only when every applicable item is checked. The chapter-level checklist in `AGENTS.md` §7 still governs; this is the table-specific subset.

### 11.1 Per table

- [ ] The planning ID, display number, owner, and exact section match the README register and the manuscript.
- [ ] The table is introduced in prose by number before it appears.
- [ ] The header row, separator, and every body row have the same number of cells; no merged cells or nested tables.
- [ ] The leading cell of every body row is bold; no whole-row bold.
- [ ] Numeric columns are right-aligned; text columns are left-aligned.
- [ ] The caption states the table number, title, date range, units, geography, and any panel labels.
- [ ] The source line names the compiler, the verified sources, the transformations, and the status; full citations are in the combined notes.
- [ ] The alt text describes the table’s structure and pattern without inventing content.
- [ ] The textual reference is the exact sentence in the prose.
- [ ] Every cell has a source and locator, or an explicit “not available” explanation.
- [ ] Units, denominators, observation years, rounding, and definitions are stated.
- [ ] Stocks and flows, nominal and real, appropriations and expenditures, and peak and cumulative measures are not mixed.
- [ ] Percentages do not cross incompatible boundaries; residuals are explained.
- [ ] The table fits the text block, or breaks at a row boundary with a repeated header.
- [ ] The proof has been inspected for row splits, header repetition, caption placement, note keys, and emphasis.

### 11.2 Per group

- [ ] The 80-table count still reconciles: 51 historiographical + 13 chapter data/comparison + 16 appendix.
- [ ] No table-shaped figure, page-budget table, or editorial inventory has been counted as a published table.
- [ ] Every chapter data table has a corresponding historiographical table with the next display number, unless the chapter has no data table.
- [ ] Appendix B’s eight datasets agree with the chapter tables that cite them (population, elections, territory, war, immigration, slavery, economy, land).
- [ ] Appendix C’s gazetteer entries match the maps’ labels and the chapters’ first mentions.
- [ ] Appendix D’s chronology dates match the chapter dates and do not duplicate events at the boundaries.
- [ ] The README register’s locations and the manuscript’s headings agree, or the discrepancy is recorded in §9.
- [ ] No second numbering list exists in chapter notes, Appendix C, or a separate production file.

### 11.3 Whole-book

- [ ] `python3 tools/check_book.py --strict` passes, or every reported error and warning is resolved or declared as a blocker.
- [ ] The combined footnote list contains a definition for every note key used in a table’s source line.
- [ ] The table’s source line does not point to a separate Sources list or a planning key that the reader cannot resolve.
- [ ] Rights and credit are cleared for any third-party table, map, or image reproduced in a table.
- [ ] The measured page count has been reconciled with the 10-page Appendix B allowance; if the tables do not fit, the plan is revised rather than the evidence cut.
- [ ] The build, if available, has been inspected in proof; a Markdown render is not a typeset proof.

## 12. A note on authority

This guide is deliberately derivative. It does not assign a new table number, create a new table, or authorize a new dataset. The README register is the assignment list; the chapter and appendix files are the local drafts; the combined footnote lists are the evidence; the book’s build is the proof. When this guide and those sources disagree, the source with the evidence wins, and the disagreement is recorded rather than smoothed away.

The most important caution is not technical. A table can look authoritative while resting on a review, a summary, or a number copied from a chart. The book’s standard is higher: every row should be traceable to a source the compiler actually opened, every number should carry its definition, and every limitation should be stated in the table or its note. A table that cannot meet that standard should be narrowed, qualified, or left out — not filled with plausible values.

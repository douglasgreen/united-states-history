# Working on this book

This is a collaborative, single-authored history of the United States, *A Nation in Question*, written to be read aloud. The title, author, rights statement, and language live in `metadata.yaml`. This file governs the writing process and house style; `README.md` governs the book’s plan.

The deliverable is **exactly 50 numbered chapters, plus an unnumbered Introduction and Appendices A–E**, totaling approximately 1,000 typeset pages. Chapter 50 is the conclusion, not an additional fifty-first chapter. The chapter count is fixed; the page count is an estimate, not a reason to pad or omit evidence.

## 1. Repository and sources of truth

| File or directory | Responsibility |
|---|---|
| **`README.md`** | Canonical book outline, scope, page budget, chapter status, and complete register of tables and illustrations |
| **`metadata.yaml`** | Title, author, rights, and language |
| **`AGENTS.md`** | Process, conventions, and acceptance checks |
| **`chapters/00-introduction.md`** | Introduction |
| **`chapters/01-chapter-1.md` … `chapters/50-chapter-50.md`** | Chapters 1–50, including the conclusion |
| **`chapters/51-appendix-a.md` … `chapters/55-appendix-e.md`** | Appendices A–E |

### Stable file names

- Use the exact naming pattern above. Pad only the leading file number: `01-chapter-1.md`, not `01-chapter-01.md`.
- Keep descriptive titles and date ranges inside the files and in `README.md`, not in file names. Changing a title does not change a path.
- The file prefix equals the chapter number for Chapters 1–50. Prefixes 51–55 identify appendices, not Chapters 51–55.
- Never rename or renumber a file to repair a mistaken citation. Repair the citation and any affected planning records.
- Use relative links in `README.md` to the actual manuscript files.

### One plan, not competing plans

`README.md` is the only maintained book outline. Do not create or maintain `outline.md` as a second authority. Chapter files contain the local, more detailed development of the README outline; Appendix C is a reader-facing catalog, not a competing illustration plan. Appendix D is the published chronology and must agree with the planned coverage and manuscript.

When scope, section structure, an opening scene, a bridge, a page allocation, or a visual changes during writing, update the relevant README record and affected chapter or appendix together. Resolve contradictions by checking evidence and making an explicit decision, not by assuming either an older plan or newer prose must be right.

### Applying these rules to the existing draft

The first draft uses descriptive chapter file names and an `outline.md`; these are legacy artifacts, not the convention going forward. A revision of this instruction file alone does not authorize moving the outline, renaming the manuscript, or rewriting chapters.

When migration is requested, inventory the existing files and references first. Move and reconcile the outline into `README.md`, preserving useful material; map every old chapter path to its new path; then rename files and repair links and build inputs as one coordinated change. Reconcile the visual registers and appendix promises against the actual manuscript. Retire `outline.md` only after its content and references have been accounted for. Do not overwrite a draft with an outline or discard unresolved editorial notes. Until migration is complete, locate existing chapters by their numeric prefix and record actual paths rather than inventing links to files that do not yet exist.

## 2. The writing process: plan → seed → research → draft → check → integrate → release

These are separate writing steps with saved outputs. Do not turn a short outline into supposedly finished prose in one pass. For a new book, finish the complete book plan before seeding files, and seed every file before expanding individual chapters. For an existing book, audit and reconcile the plan before resuming the relevant stage; do not destroy existing prose to recreate an earlier stage.

Work only within the requested scope. If asked to outline, stop with an outline; if asked to draft, do not describe the result as checked. Report the stage reached, checks actually performed, and remaining blockers. A request to revise one chapter is not authorization to rewrite the rest of the book.

### Stage 1 — Plan the whole book in `README.md`

Write the complete outline in `README.md` before drafting chapters. It must contain:

1. The book’s guiding question, thesis, audience, chronological and geographic limits, and an explicit research cutoff date for recent events.
2. The five through-lines: land and environment; liberty and unfreedom; pluralism and belonging; capitalism and inequality; power and the world.
3. Parts and their purposes, the Introduction, exactly 50 numbered chapters, and all five appendices. State which chapter owns each major event or argument; mark intentional overlaps and their different jobs.
4. For every chapter: file link, title, dates, guiding question, provisional claim, coverage and exclusions, principal people and places, planned sections, opening scene, In Focus object, central historiographical disagreement, visuals, backward connection, and next-chapter hand-off.
5. For the Introduction and each appendix: contents, purpose, scope, and page allocation. List promised documents, datasets, maps, and other reference material individually, not merely as categories.
6. A complete table and illustration register as specified in §3, including comparison tables and debate tables.
7. A page budget and a status record for each manuscript file.

Budget the whole book, not just its narrative. Include epigraphs, visuals, captions, the combined notes and citations, Further Reading, front matter, and appendices. An illustrative allocation is 24 pages for the Introduction, 925 for the 50 chapters, 41 for appendices, and 10 for other front/back matter: 1,000 in total. These are planning allowances, not claims about the existing draft. Chapter allocations usually fall within 16–20 pages, averaging about 18.5 under that example. Charge each item once and reconcile the arithmetic whenever allocations change.

Page counts depend on layout. Record word counts as a working measure, calibrate them against a representative typeset chapter, and revise the budget after actual builds. Do not silently equate a Markdown page or an assumed words-per-page ratio with a finished page. Any part-ending reflection must have an assigned home and page allowance; it must not become an unplanned extra chapter.

**Exit check:** every required file has an outline entry; the count and budget reconcile; coverage has no unexplained gaps or duplication; every planned visual has a register entry.

### Stage 2 — Seed every manuscript file from the outline

Create the Introduction, all 50 chapter files, and all five appendix files using the stable names in §1. Copy each file’s own README outline into it, including its title, scope, claims, planned sections, visuals, and hand-offs. Do not replace the copied outline with a generic template that loses the plan.

Track stages in the README status record using `planned`, `seeded`, `researched`, `drafted`, `checked`, and `integrated`. Record the last review date, review scope, and outstanding blockers. Unfinished material is not `checked`; a substantive later change reopens the affected checks.

**Exit check:** all 56 manuscript files exist, each matches its README entry, and none is empty or represented only by a title.

### Stage 3 — Expand one file into a researched outline

This is a distinct deliverable, not prose drafting. In the chapter file, expand the seed into section and subsection headings with bullet-level arguments, evidence, consequences, and transitions. Preserve the outline’s scope, or update `README.md` explicitly if research requires a change.

For each substantive claim, attach a named citation footnote with the precise supporting passage, page, document identifier, table, or timestamp. Plan the opening scene, quotations and epigraphs, close reading, historiographical positions, statistics, visuals, and cross-references with the same care as the narrative. Identify counterevidence and what each source cannot establish. List open questions and planned checks as named editorial footnotes attached to the relevant outline item, in the same list as the citation notes.

Use primarily accessible web sources so another reader can check the evidence. This includes digitized primary documents, scholarly articles and books, institutional collections, and original datasets; it does not mean replacing scholarship with unsourced summaries. Search for leads, then open and read the actual source. Build the chapter’s single annotated footnote list now, using §4; citations and other notes belong together, not in a separate Sources list. A search result, catalog listing, or unread book is not evidence for a historical claim.

Do not manufacture a scene to fill the architecture. Establish what witnesses or records support the setting, actions, dialogue, weather, objects, and participants. Where a detail cannot be established, omit it, qualify the inference, or choose another scene. Never invent thoughts, composite witnesses, overheard remarks, or sensory details.

**Exit check:** the argument has a usable evidence trail, quotations have been transcribed from identified editions, visuals have sources and production plans, and gaps are explicitly marked. An unsupported central claim or scene blocks drafting it as fact; it does not become true because the outline needs it.

### Stage 4 — Write from the researched outline

Expand the researched outline into prose, following §§5–6. Keep the named citation references immediately beside the claims they support. Remove planning bullets as they become prose; retain unresolved questions as editorial footnotes rather than letting them disappear.

Drafting may expose new research needs. Return to Stage 3 for those claims, read the sources, and add or update their citation notes before asserting them. Do not write from memory and attach plausible citations afterward. New visuals or scope changes require a README update during the same change, not at the end of the book.

Keep adjacent chapters open when writing the opening and bridge. Match the actual preceding close and following opening; when either is still provisional, record that dependency. Avoid repeating an earlier chapter’s full explanation when a checked cross-reference will do.

**Exit check:** the complete chapter architecture is present, the roadmap matches the actual sections, notes and source records remain traceable, and the status is `drafted`, not `checked`.

### Stage 5 — Check the chapter in separate passes

Do not substitute a stylistic reread for verification. Use the checklist in §7 in distinct passes: evidence and quotations; argument and chronology; cross-references and visuals; prose and rendering. Reopen the cited sources and target sections. Record what was checked, what changed, and what remains unresolved.

When a source fails to support a claim, correct, qualify, replace, or remove the claim. Do not merely remove its citation and leave it unsupported. Preserve permanent evidence notes; remove editorial notes only when their questions have actually been resolved. If access or tooling prevents a check, say so and leave the relevant blocker open.

**Exit check:** all chapter-level checks pass and no unsupported central assertion, invented scene detail, unresolved factual correction, or missing required visual remains. A bounded scholarly uncertainty may remain if the prose and permanent note accurately describe it.

### Stage 6 — Integrate across the whole book

After chapter checks, read and check the manuscript as a whole. Reconcile `README.md`, the Introduction, Chapters 1–50, and appendices for scope, chronology, recurring terms, claims, statistics, numbering, and hand-offs. Search for duplicate explanations, contradictory accounts, dangling links, and promised material that was never supplied.

Check Appendix A’s excerpts against the cited editions; Appendix B’s actual tables against every data reference; Appendix C against the README illustration register and actual assets; Appendix D against chapter dates and events; and Appendix E against the historians and works the book discusses. A list of intended tables or maps is not the promised table or map.

Read the epigraphs, openings, roadmaps, summaries, closing notes, and bridges in sequence. Check the Introduction’s stated method and language conventions against the manuscript and this file, locating the actual sections rather than assuming old section numbers. Chapter 50 must conclude the argument without pretending that its own future is already known.

**Exit check:** chapter boundaries and appendices agree, the README registers and status records are current, and all affected chapter checks have been rerun after integration edits.

### Stage 7 — Build and release

Use the repository’s actual build tooling; discover it rather than inventing commands or claiming that a nonexistent pipeline passed. If no build is available, report that limitation. Inspect rendered output for the single combined note list, citation links and return links, tables, images, captions, emphasis, and page breaks. Resolve build warnings and inspect both representative pages and known difficult passages.

Reconcile the measured page count with the approximately 1,000-page budget. Confirm exactly 50 numbered chapters, one Introduction, and Appendices A–E. Remove planning debris and resolve editorial blockers before release. Do not delete permanent citations or scholarly caveats to make the book look finished. Report build results, remaining limitations, and any deliberate departures from the plan.

## 3. The complete table and illustration register

Maintain the register in `README.md` from Stage 1 onward. It covers **every table, map, figure, photograph, facsimile, and other image**, including those in the Introduction, In Focus boxes, debates, and appendices. No unregistered item may be added to the manuscript. Planned items may be revised or removed, but the plan and affected references must change with them.

For each item, record:

- A unique, stable planning ID, its type, and its display number.
- A short title, its analytical purpose, and the claim it supports.
- Its owning file and section, plus other places that reproduce or reference it.
- Its chronological/geographic coverage; for data, units, denominators, definitions, and base years.
- Source keys and exact source locators; any transformations or calculations. When a source is cited in a manuscript, map its planning key to the named citation note in the owning file; a register key alone is not a reader-facing citation.
- Asset path or table location, caption, source/credit line, and alt text for images. Detailed production information may live with the asset, linked from the register.
- Rights or license evidence, required attribution, and permission status. Do not assume that a host’s license covers all material it displays or that the book’s rights statement grants rights to third-party images.
- Production and verification status: `planned`, `sourced`, `produced`, or `verified`, with specific blockers where necessary.

Use separate book-wide sequences for maps, figures, and images: “Map 12”, “Figure 3”, “Image 2”. Tables are numbered within their owning chapter or appendix: “Ch. 16, Table 1”, “App. B, Table 2”. Planning IDs such as `ch16-table-01` and `app-b-table-02` disambiguate records; they are not prose citations. Assign planned numbers centrally, not independently in chapter drafts. Freeze released numbering; any necessary renumbering is a coordinated change to the register, manuscript, captions, and references.

Plan one substantive map or figure per chapter by default. Record justified exceptions in the README; do not add decorative filler merely to satisfy a count. Additional tables and images must earn their space and fit the budget. A shared visual has one owner and number, with its other uses recorded; Appendix C’s catalog entry is not a new visual.

Every item needs a short caption, a source line, and an explicit textual reference by number. Data drawn from an appendix must point to the actual supporting table, not a convenient number. Maps must state the relevant date and distinguish boundaries, claims, and uncertain reconstructions. A placeholder caption, a map description, or a link to an image is not a finished asset. Tables must contain the promised data or comparison, not merely their titles.

## 4. Evidence and the combined footnote list

### Source selection and verification

- Prefer accessible, stable, document-specific URLs from archives, libraries, museums, Indigenous institutions, government repositories, scholarly publishers, and reputable research organizations. Judge the particular source, its provenance, context, and limits; a prestigious domain alone does not verify a claim.
- Use primary evidence for what a document said or a record counted, and scholarship for interpretation and context. A primary source can establish that someone made a claim without establishing that the claim was true.
- Prefer digitized editions and open scholarly texts where possible. Necessary print or restricted sources are allowed only when actually consulted; identify the edition and locator, and state access limitations. A publisher’s description verifies bibliographic details, not an unread book’s argument or a quotation’s wording.
- Distinguish `discovered`, `read`, and `verified for this claim`. Only the last supports a checked assertion. Search snippets and AI summaries are leads, not final verification. If access fails, find an accessible authoritative edition or flag the check as blocked; do not claim to have read it.
- Corroborate disputed, consequential, or surprising claims where possible with independent evidence. Repeated copies of one report are not independent sources. Represent the strongest competing interpretation fairly before answering it.
- Never invent an author, title, URL, page number, quotation, access date, or verification result. A link that opens is not proof that its contents support the sentence.

### One list for citations and other notes

**All source citations, explanatory notes, scholarly qualifications, and working editorial questions use the same named-footnote system and appear in one list.** Do not split citations into a separate `## Sources`, References, or bibliography list. A citation note can also explain uncertainty; there is no need to create two notes for one evidentiary problem.

Put a named footnote reference immediately after the assertion, quotation, statistic, or caption it supports. The reference must take the reader directly to the citation and its locator, not merely to a source key that requires a second lookup. Author–date shorthand alone is not the evidence trail. A note may cover a clearly bounded cluster of related facts, but must identify which source supports which claim. Cite opening scenes, epigraphs, close readings, and visual source lines as carefully as the body.

Further Reading remains a selective, annotated reader’s guide, not a second citation ledger or a substitute for citation notes. A work may appear there as a recommendation and also be cited in a footnote. README production-source records may remain planning metadata; when used in the manuscript, their evidence must be cited through the combined footnotes.

### Named references, reuse, and file-end order

- Use descriptive named references such as `[^ch01-migration-evidence]` or `[^ch01-white-sands-study]`, not numbered keys such as `[^1]`. Prefix keys with the chapter, `intro`, or appendix identifier to avoid collisions when files are combined. Do not rename keys merely because their order changes.
- Give each key exactly one definition and at least one reference. Citation, explanatory, and editorial notes share one sequence in order of first reference; they are not grouped into separate lists by type.
- Reuse a key when the same source passage and the same qualification support more than one occurrence. If another claim needs a different page, passage, version, or qualification, create a distinct descriptive key rather than silently changing what an existing note supports.
- Give the first citation of a work/version in each chapter its full details. Later notes may use author, short title, and the new exact locator if the full citation is unambiguous within that chapter. Do not use “ibid.”, hard-coded note numbers, or footnote references nested inside note definitions. If the first full citation is removed or moved later, promote the earliest remaining citation so the details are not lost.
- After the closing block, place all definitions together at the very end of the file as plain Markdown footnote definitions. Do not add a manual heading, bullets, or numbering; separate definitions with blank lines and indent continuation paragraphs when needed. Leave note numbering and any rendered heading to the build. The Introduction and appendices follow the same rule after their main text.
- Check that rendered references, repeated references, note order, and return links work in the combined book. Source-file order alone does not establish correct rendering. There must be one note list per manuscript unit, not separate citation and commentary sequences.

### Required citation-note fields

The first full citation of each work/version includes:

- Author or responsible institution; exact title; original date and publication or hosting institution.
- Edition, translator/editor, document or collection identifier, and other bibliographic details needed to identify the version actually used.
- A direct URL or DOI link to the consulted text or data, and the date actually accessed. For an offline source, give its full print/archive locator and state that it was consulted offline; do not invent a URL.
- The exact page, passage, document, table, dataset variables, or timestamp supporting the attached claim. An entire website or a book title without a usable locator is insufficient.
- **Used for:** a concise description of the specific claim, quotation, epigraph, dataset, or visual supported, with section or visual IDs where useful. Keep this annotation inside the citation note; “background” or “general reference” alone is inadequate.
- Relevant limitations: conflicting versions, uncertain attribution, translation issues, incomplete data, or restricted access.

Each shortened citation still needs its own precise locator, a clear “Used for” description, and any qualification particular to that claim. A note citing several sources must distinguish their contributions. Explanatory notes without external claims need no invented bibliography; explanatory or editorial notes that rely on evidence include its citation in that same note.

Use the following as a structural template only; bracketed fields and the example URL are placeholders, not real citations:

```markdown
[A claim supported by a consulted source].[^ch01-study]

[An unresolved question about the claim’s context].[^ch01-context-check]

[Another claim supported by the same passage and qualification].[^ch01-study]

[A claim supported by a different page of that work].[^ch01-study-dating]

[^ch01-study]: [Author or institution], [title formatted by type], [date; edition/publication details], [exact locator]. [Consulted text](https://example.org/replace-with-source). Accessed [actual date]. Used for: §2.1, [specific claims supported]. Limitations: [if applicable].

[^ch01-context-check]: Editorial check — [specific unresolved question and the evidence needed to resolve it].

[^ch01-study-dating]: [Author], [short title], [different exact locator]. Used for: §3.2, [specific dating claim]. [Any qualification particular to this claim].
```

Build and maintain this single list during research, drafting, and checking. In a researched outline, put unread candidates in a clearly labeled editorial note attached to the research question: `discovered — not yet consulted`. Such a note is a task, not verified support. Resolve these tasks before calling the chapter checked; remove unused leads, but retain evidence citations when editorial questions are answered. Becoming confident does not make attribution unnecessary.

When revising a file that uses the former separate Sources format, move the complete source details and “Used for” annotations into citation-note definitions, add or repair references at the supported claims/captions, and remove the redundant list only after all support is accounted for. Preserve stable identifiers where possible and map planning source keys to their citation-note keys. Do not bulk-convert unrelated chapters merely because this convention changed.

### Quotations and numbers

Quote exactly from the consulted edition, checking spelling, capitalization, punctuation, and omissions character by character. Record a page or equivalent locator for every quotation, including epigraphs and appendix excerpts. Use square brackets for insertions and spaced ellipsis for omissions. If modernizing or translating a passage, say so and identify the version or translator. Never silently repair the source.

Statistics carry a source, observation year or period, units, population or denominator, and the series/table locator. State rounding, uncertainty, and calculations. Supply per-capita comparisons where absolute figures would mislead; inflation-adjusted money must name the price index and base year. Do not combine incompatible estimates or change definitions without explanation.

## 5. The shape of a finished chapter

The researched outline supplies the argument; the architecture supports it rather than replacing it. Required lengths below are drafting targets, not permission to repeat material. The chapter’s total allowance includes its combined notes and citations, tables, and reading list.

1. **Title.** One level-one heading with chapter number, descriptive title, and date range where appropriate.
2. **Epigraphs.** Two to four, normally three, chosen to disagree productively. Include a voice from the period and a historian. Each block quotation has an attribution beginning “— ” with author/speaker, title formatted by type, date, and precise locator, with a named citation footnote in the combined list.
3. **The scene.** An unnumbered, documented opening vignette of 250–400 words: a place, person, object, or day. End with the guiding question. Follow with a short framing paragraph stating years, scope, and evidentiary limits.
4. **Roadmap.** A paragraph matching the actual numbered sections: “The chapter proceeds in six movements. §1 … §6 …”. Write or revise it after the structure is settled.
5. **Numbered sections.** Usually `## 1.` through `## 6.`, or through `## 7.` for a longer chapter, with `### N.M` subsections. The first subsection states the section’s claim and structure. Follow chronology where the argument permits; close sections on consequences rather than repetitive summaries. Keep section numbers stable after references are established; any restructuring requires repairing affected references.
6. **One In Focus box.** A 150–250-word close reading of a single document, object, image, or place, placed where the argument needs it and beginning **In Focus.** Cite the consulted source in the box. Register any reproduced image separately.
7. **Planned visuals.** Produce the registered map or figure and any approved additional items; cite them by number in the text and provide captions, sources, credits, and accessible descriptions.
8. **The Debate.** The last numbered section, normally §6 or §7, with four subsections: “What is settled”; “What is open”; “The historiographical lesson”; “The map of positions”. The last contains a registered comparison table covering the positions discussed, with named historians and works, core claim, strength, and weakness. State rival arguments fairly and check them against the works actually consulted.
9. **`## Legacies`.** About 200–300 words connecting the chapter’s problems to later history and the present. State a supported connection, not a modern political score.
10. **`## Optional threads`.** Include only when useful: at most three short notes on the transnational frame, archives and silences, or distant chapter connections. Do not insert an empty heading.
11. **`## Summary`.** One bullet per major claim already argued. No new evidence or inflated verdicts.
12. **`## Study Questions`.** Eight to twelve analytical questions, from accessible to genuinely open, not recall quizzes. Include a comparison of interpretations, a contingency question, and a task using an identified source.
13. **`## Further Reading`.** A selective, tiered, annotated guide: primary sources, syntheses, specialized studies and articles, grouped by topic where useful. Give the relevant edition and two sentences explaining each selection’s value and limits. Verify bibliographic details; distinguish a recommendation from a work actually used as evidence.
14. **Closing block.** A `> *A closing note.*` paragraph and a `> *And a bridge.*` paragraph. The bridge names the next chapter’s planned first scene; its opening must take it up. Chapter 50 has a closing note but no artificial bridge to a nonexistent Chapter 51.
15. **One combined footnote list.** End with the named definitions for all citations, explanatory notes, qualifications, and editorial questions, following §4. Do not add a separate Sources list; Further Reading does not replace citation notes.

The **Introduction** has its own outlined structure, without epigraphs, an In Focus box, or a bridge. Its framing section carries the book’s numbered claims. It explains the method, sources and silences, language, periodization, and reader’s route; it does not mechanically inherit narrative-chapter apparatus that its outline does not require.

The **appendices** are reference material: A, Documents; B, Tables and Data; C, Maps and Gazetteer; D, Chronology; E, Historiographical Essay and Further Reading. They have no narrative roadmap, summary, or study questions. They use the same evidence and typography rules, include actual promised material, and each ends with one combined footnote list for citations and other notes. Every table, map, and image needs a source line with a citation reference where full evidence details are required.

## 6. House style

These conventions apply to the book’s own prose, headings, tables, and captions. Quotations and titles retain the source’s spelling and wording. Technical examples, file paths, URLs, and source identifiers retain their literal characters.

### Prose and historical reasoning

- Write to be read aloud. Read at least a representative page aloud, or use text-to-speech if available, and check every revised passage for cadence. Do not claim a listening check that was not performed.
- Give each sentence a main idea; keep most under 25 words. A longer sentence earns its length through a clear turn, not stacked clauses.
- Give each paragraph one job. Vary length with the argument; do not force every paragraph into a word quota. Cut paragraphs that merely repeat a claim or roadmap.
- Use past tense for historical narrative, not the historic present. Present tense is appropriate for the book’s argument, a document’s wording, and clearly identified present conditions, not for invented immediacy in a past scene.
- Prefer concrete nouns and active verbs. Start with a person where that clarifies a policy. Cut “it is important to note”, “arguably”, “of course”, “in many ways”, and “the fact that”. Define technical terms at first use.
- Mark inference as inference: “the record suggests”, “probably”, “the surviving evidence does not show”. Give contested estimates as estimates or ranges.
- Distinguish a precipitating event, structural conditions, and contingent choices. Adding “in part” does not rescue an unsupported causal explanation; show the mechanism and evidence.
- Do not give historical actors knowledge of later outcomes. Scenes and narrative must preserve what was uncertain then. Keep retrospective analysis explicit; roadmaps and legacies may orient the reader without attributing hindsight to participants.
- Where no voice survives, name the silence. Do not ventriloquize, infer consensus from an absent record, or treat an archive’s exclusions as proof of nonexistence.
- Use historical place names, adding the present name in parentheses where useful; prefer nation-specific Indigenous names where known and explain genuinely contested names.

### Typography and spelling

- Use curly quotation marks and apostrophes: “ ” and ’.
- Use spaced em dashes for breaks — like this — and en dashes for ranges and coordinated compounds: “1861–65”, “Chs. 5–13”, “North–South”. Never use a hyphen between numbers to mean a range.
- Use the ellipsis character “…”, not three periods; a marked omission within a quotation uses spaced ellipsis.
- Use American date order: “July 4, 1776”. Give full years before 1800 and at first mention; a standalone year is never abbreviated. Write “the 1850s”; use CE and BCE for the deep past. Explain “years before present” and its reference year when used in scientific dating.
- Spell out one through nine in prose; use figures for 10 and above. Exceptions include proper names, dates, statistics, populations, money, and item numbers. Tables, data, and appendices use figures.
- Use ordinary spaces, not non-breaking spaces, hyphenation tricks, or Markdown hard breaks within paragraphs.
- Use American English: -ize/-ization, behavior, defense, center, program, labor, analyze, judgment; license as noun and practice as noun and verb. Quotations and work titles keep their original spelling.

### Titles, italics, and bold

- Italicize books, journals, newspapers, ships, films, and court cases: *Uncle Tom’s Cabin*, *The New York Times*, USS *Arizona*, *Brown v. Board of Education*.
- Put articles, essays, speeches, sermons, chapters, and titled short documents in quotation marks, not italics: “A Model of Christian Charity”, “I Have a Dream”, “Letter from Birmingham Jail”. Acts, treaties, amendments, and official documents are capitalized and roman: the Voting Rights Act of 1965, the Treaty of Guadalupe Hidalgo, the Fourteenth Amendment, the Emancipation Proclamation.
- Other italics are for a technical or foreign term at first occurrence, a word discussed as a word, deliberate emphasis, and the fixed closing-block labels. A chapter carries no more than a dozen emphasis italics; title italics do not count toward that limit.
- Bold names a move and closes after the lead phrase: **The claim.** The paragraph continues in plain text. The vocabulary is **The scene.**, **The claim.**, **The turning point.**, **The cost.**, **A closer look.**, **The measure.**, and **In Focus.** Do not invent extra labels without changing this file.
- Bold also marks the leading cell of table rows and numbered claims in the Introduction. Do not bold whole paragraphs. Check paired emphasis markers and rendered output; a mechanical count alone cannot prove correct rendering.

### Names and house words

- Use a person’s full name and identifying role at first substantive mention in a chapter, surname thereafter. Identify a person who appears only once as well. Explain alternate names where needed.
- Capitalize **Native American** and **Indigenous**. Use the specific nation and its preferred name where known: Haudenosaunee, Wampanoag, Cherokee, Diné. Use “Indian” only in quotation or historical proper names such as the Indian Removal Act, the Bureau of Indian Affairs, and Indian Territory.
- Prefer “enslaved people” in the book’s prose; retain historical proper names and exact quotations. Capitalize **Black** and **White** when referring to people.
- Capitalize historical regions and named periods/programs: the South, the North, the West, the Southwest, the Sunbelt, the Rust Belt, the New Deal, the Great Society, Reconstruction, the Cold War, the Progressive Era, the Market Revolution, the Civil War.
- Keep “the civil rights movement” lowercase outside a formal name such as the Civil Rights Act of 1964.
- Slurs and degrading period language appear only in quotation, only when necessary to the historical argument, and with an explanation in the same paragraph of why they are reproduced.

### Cross-references and tables

- Use “Ch. 11, §2.2”, “Chs. 3–4”, “§5.3”, “Ch. 26, §§3.2 and 4.1”, “App. D (Chronology)”, and “App. B, Table 2”. There is no space between § and its number.
- Before citing a section or table, open it and confirm that it supports the attributed claim, not merely the general topic. A missing or provisional target is an unresolved dependency, not a checked reference.
- Connect each chapter to its predecessor and successor, using the Introduction before Chapter 1 and no fictitious successor after Chapter 50. Keep bridges, openings, and Appendix D aligned.
- Use pipe tables with a header and a separator such as `|---|---|`. Bold each body row’s leading cell. Keep cells short; comparisons belong in tables, sustained argument in prose. Give each table its registered caption and source line.

## 7. Acceptance checklist

Before calling a chapter checked, complete every applicable item. Whole-book items are required again at integration and release.

- [ ] **Plan and scope:** README entry, actual title/dates, file path, section count, page allowance, status, and registered items agree. There are exactly 50 numbered chapters at book level.
- [ ] **Evidence:** every factual assertion is traceable to consulted evidence through a named citation note; citations retain full identification, exact locators, and “Used for” annotations as specified in §4; access problems and uncertainty are explicit. No invented scene detail, unread-source attribution, or unsupported correction remains.
- [ ] **Quotations:** every quotation, epigraph, and excerpt matches the identified edition character by character, with a precise locator and marked omissions/insertions.
- [ ] **Reasoning:** evidence supports the causal claims; counterarguments receive their strongest fair statement; retrospective judgments are distinguished from actors’ knowledge. Summary and conclusion do not claim more than the chapter established.
- [ ] **Chronology:** title, framing, narrative, adjoining chapters, research cutoff, and Appendix D agree. Explain intended overlaps; investigate apparent gaps. Do not assert events beyond the evidence cutoff as accomplished facts.
- [ ] **Statistics:** source series, dates, units, denominators, base years, rounding, estimates, and calculations are stated and checked.
- [ ] **References:** every cited section and table exists and supports the claim; relative links resolve; every named footnote has exactly one definition and at least one reference. Reused notes support the same passage/qualification, shortened citations resolve unambiguously, and planning source keys map to actual citation notes.
- [ ] **Visuals:** the README register matches every actual table and illustration, its number, placement, caption, credit, source, rights status, and textual reference. Required assets and appendix datasets actually exist; placeholders are not counted as finished.
- [ ] **Architecture and hand-offs:** epigraphs, scene, roadmap, numbered sections, In Focus box, debate, legacies, summary, questions, reading list, close, and bridge fulfill their jobs. Agreed Introduction, conclusion, and appendix exceptions are respected.
- [ ] **Language and sound:** terminology, names, tense, spelling, quotation marks, dashes, ellipses, and emphasis follow §6. Cadence has been checked; repetitions and mechanical scaffolding have been cut.
- [ ] **Notes and citations:** citations, explanations, qualifications, and editorial questions appear in one named-footnote list, ordered by first reference; no separate Sources or citation list remains. Editorial questions are resolved or remain declared blockers, permanent citations are retained, and Further Reading is not being used as an evidence ledger.
- [ ] **Integration:** Introduction, README, chapter claims, appendices, recurring datasets, and visual counts agree; no obsolete second outline or contradictory register is being maintained.
- [ ] **Rendering and budget:** available builds pass without unresolved warnings; the combined notes, citation/return links, tables, images, and emphasis have been inspected; measured length has been reconciled with the budget. Unavailable checks are reported, not asserted as passed.

## 8. Web research with TinyFish

TinyFish Search and Fetch are the project’s default web research tools. Use them for source discovery, reading, and verification; record bibliographic evidence in the manuscript, not just in a tool transcript. Use local read/edit tools for repository files. Tool signatures can change, so the live catalog is authoritative; do not guess parameter names.

### Discover tools, then search and read

Inside code mode, discover the exact paths and signatures before first use:

```js
const catalog = search({ query: "tinyfish search fetch_content" });
return catalog.items;
```

Then call the discovered search tool with a focused question and purpose:

```js
const results = await tools.tinyfish.search({
  query: "Library of Congress primary source analysis citation",
  purpose: "Find guidance on evaluating and identifying digitized primary evidence"
});
return results;
```

Open relevant results with `fetch_content`. Always pass `format`, `links`, `image_links`, `iframe_links`, and `page_metadata` explicitly:

```js
const content = await tools.tinyfish.fetch_content({
  urls: ["https://www.ala.org/rusa/sections/history/resources/primarysources/using"],
  purpose: "Read source-evaluation and citation guidance, not just a search snippet",
  format: "markdown",
  links: false,
  image_links: false,
  iframe_links: false,
  page_metadata: false
});
return content;
```

Keep output focused on the passages and metadata needed for the check rather than dumping entire long documents. Inspect both `results` and `errors`; a successful result for one URL does not mean every URL succeeded.

- Run independent searches or fetches in parallel with `Promise.allSettled`. A search followed by reading its result is a dependency, not an independent pair.
- For academic discovery, prefer `domain_type: "research_paper"` where appropriate; use `pub_year_min` and `pub_year_max` for its publication-year filters. For web/news searches, use date windows or `recency_minutes`, not both together.
- Fetch up to 10 URLs per request when the live signature permits it. Keep the consulted edition, locator, and actual access date in the source record.
- If a page blocks access or a PDF does not extract, try another accessible authoritative edition or supported fetch format. Search snippets may guide that search but do not complete a quotation or claim check. Record unresolved access limitations.
- Search and Fetch are free; interactive browser automation is metered. Use automation only when interaction is needed. For authenticated work, use the authorized profile and vault options. After an automation error or timeout, check the existing run rather than retrying blindly; it may still be running. Use asynchronous automation only on an explicit request for background execution.
- Deep research and datasets are slow, billed, and opt-in. Do not start them merely because a chapter needs research. Scheduled monitors and usage-history tools are also only for explicit requests.
- If a tool returns an insufficient-credit or subscription message, show the exact top-up/upgrade link as a clickable Markdown link and ask the user to open it. Show any returned “Add money” link immediately. Do not hide the error, silently substitute a weaker tool, or retry the metered operation blindly.

# Kindle Publishing Reference for *A Nation in Question*

**Purpose.** This document collects the Amazon Kindle Direct Publishing (KDP) rules that bear on converting *A Nation in Question* to EPUB 3 and publishing it to Amazon Kindle. It is a production reference, not a restatement of the whole KDP manual. It separates what KDP requires from what this repository still has to do.

**Scope.** The focus is the Kindle eBook edition: reflowable EPUB, cover, metadata, navigation, text and CSS, images and charts, tables, notes, accessibility, quality checks, and the commercial rules that affect a CC0 book. Print-on-demand and the print wraparound cover use a separate KDP workflow and are outside this document.

**Source versions.** The comprehensive source is Amazon’s *Amazon Kindle Publishing Guidelines*, version 2026.3 (copyright 2025, revision history through 2026.3), cited below as **KPG 2026.3**. The KDP Help pages cited below were consulted on **November 25, 2026**. The cover policy was rechecked on that date against KPG 2026.3 §4.2 and the current eBook Manuscript Formatting Guide (S24). KDP changes its rules; recheck the sources in the [Sources](#sources) table before upload.

**Last updated.** November 25, 2026.

**Repository note.** This file lives in `docs/` and is not one of the 56 manuscript files, so `tools/check_book.py` does not check it. The manuscript rules in `AGENTS.md` still govern any prose that is moved from this reference into the book.

**Contents.** [Bottom line](#1-bottom-line-for-this-book) · [Format](#2-format-and-package) · [Cover](#3-cover) · [Metadata](#4-metadata-and-title-setup) · [Navigation](#5-navigation) · [HTML and CSS](#6-html-and-css) · [Images](#7-images-maps-and-charts) · [Tables](#8-tables) · [Notes and links](#9-notes-cross-references-and-links) · [Accessibility](#10-accessibility) · [QA and release](#11-quality-assurance-and-release-checks) · [Royalties and CC0](#12-royalties-delivery-fees-and-the-cc0-decision) · [Action list](#13-action-list) · [Open decisions](#14-open-decisions) · [Quick reference](#appendix-a-kdp-quick-reference) · [Sources](#sources)

**How to read this document.** “Required” means KDP states that a failure can block conversion, publication, or sale. “Recommended” means KDP’s best practice, which may still affect quality review. “Project action” is this repository’s response. When the comprehensive PDF and a current KDP Help page differ, the more specific or more recent KDP Help page usually describes what the upload system actually does; the difference is noted where it matters.

**Not legal advice.** Rights, public-domain, and royalty classifications need the author’s own review; confirm with KDP and, where the stakes warrant, counsel.

---

## 1. Bottom line for this book

| Decision | Current KDP rule | Project status |
|---|---|---|
| **Format** | Upload a reflowable EPUB 3; KDP converts it into Kindle delivery formats. EPUB 2.0 is also accepted. MOBI is no longer accepted for reflowable books, and fixed-layout MOBI ended in March 2025. | The build already produces EPUB 3, and `make epubcheck` passes under EPUB 3.2 rules. Upload the EPUB, not the PDF, MOBI, or KPF. |
| **Layout model** | Reflowable is preferred for text-heavy books because it supports every Kindle device, adjustable type, screen readers, and Enhanced Typesetting. Fixed layout and Print Replica are fallbacks for image-heavy or exact-layout books. | Reflowable only. Print Replica would defeat the book’s accessibility and reading goals. |
| **Cover** | A separate marketing cover is required. KDP’s manuscript guide says **not** to include the cover in the manuscript; KDP adds the marketing cover during title setup. The guidelines’ internal-cover section explicitly does not apply to KDP eBooks. Ideal marketing cover is 1,600 × 2,560 px at 300 PPI, RGB, JPEG, ≤5 MB in the guidelines (≤50 MB in the upload criteria); KDP asks for minimal compression. | Master is 1,600 × 2,560 px, 5.19 MB, 100% JPEG, 300 dpi, ratio 1.60:1; upload it as the marketing cover. The build makes a 1.13 MB, 80% JPEG derivative for proofs, the with-cover EPUB, and a strict 5 MB fallback. The default KDP EPUB contains no cover. |
| **Interior visuals** | Images must be legible at 300 PPI at their display size; maps and charts with text need at least 80% screen width. Missing promised images are a critical quality issue. | 39 maps, 9 figures, and 8 images are registered, but **none is produced**. This is the largest release blocker. |
| **Tables** | Use HTML tables, not images. Keep tables below 100 rows and 11 columns. Test at font size 3. | 95 Markdown table blocks, including three Appendix C production schedules that are not display tables; the widest have 10 columns; Appendix B prints lettered panels. Within the row/column ceiling but at the wide edge. Test and split where needed. |
| **Notes** | Use bidirectional hyperlinks; `aside` plus `epub:type="footnote"` is preferred; notes at the end of a chapter or book; pop-ups must not be blank. | 3,355 notes are present with `aside` markup and backlinks. Repeated-note links and pop-ups still need a Kindle Previewer check. |
| **Body text** | Body text must use defaults: no forced font size, font family, line height, color, background, or justification. | `styles/epub.css` now leaves body line height and alignment to Kindle; blockquote and list horizontal margins are percentages; figure images fill the column. |
| **Kindle validation** | Kindle Previewer 4 compiles the EPUB and flags errors and warnings; KDP says these can prevent a title from becoming available. | EPUBCheck passes, but Kindle Previewer has not been run. The desktop Previewer runs on Windows and macOS, not Linux. |
| **AI disclosure** | KDP requires disclosure of AI-generated text, images, and translations. AI-assisted work does not require disclosure. | The cover is recorded as OpenAI ChatGPT output. It must be disclosed as an AI-generated image. The manuscript text and any future interior images still need a classification decision. |
| **Rights and royalty** | KDP treats works in the public domain, or consisting primarily of public-domain content, as eligible only for the 35% royalty option. Public-domain content is not eligible for KDP Select. | The book is dedicated to CC0. That may make the 70% royalty option unavailable and may make KDP Select incompatible with the book’s nonexclusive status. Confirm the rights selection with KDP before pricing. |

---

## Part I — The KDP rules that matter

## 2. Format and package

### 2.1 What to upload

KDP accepts EPUB, DOCX, KPF, HTML, RTF, TXT, and PDF for eBook manuscripts, but it recommends EPUB for books produced with third-party tools. EPUB files must meet the specifications in the Kindle Publishing Guidelines (S17). Amazon accepts both EPUB 2.0 and EPUB 3.0 files that meet the guidelines (S18).

This project does not use DOCX. The Word-specific parts of KDP’s manuscript guide, including its image-compression settings, do not apply to this build. The source is Markdown, and Pandoc writes the EPUB.

MOBI is no longer the route for new books. KDP stopped accepting MOBI for reflowable eBooks on August 1, 2021, and ended MOBI support for fixed-layout eBooks in March 2025 (S17, S18). The project’s EPUB is the correct upload format.

Do **not** upload the PDF proof as the eBook manuscript. PDF is accepted for some KDP workflows, but a PDF-interior eBook may become a Print Replica or convert poorly. It would not reflow, would not support the reader’s type settings, and would not be accessible in the way this book requires.

### 2.2 Reflowable, fixed layout, or Print Replica

KDP’s format comparison is clear: reflowable is for text-heavy titles; it supports all Kindle devices and apps, adjustable orientation and font settings, dictionary lookup, highlighting, word search, X-Ray, screen readers, refreshable braille, and Enhanced Typesetting (S1 §3). Fixed layout is for image-heavy books with little text; it gives up text selection, dictionary lookup, user font settings, and screen-reader support. Print Replica preserves an exact print layout but is not compatible with Kindle e-readers and lacks text resizing and screen-reader support (S1 §3).

This book is a long narrative history with many notes, tables, and documentary quotations. Reflowable is the only defensible choice. The maps and charts should be designed to work inside a reflowable column, not used as an excuse to switch to fixed layout.

KDP converts the uploaded EPUB into Kindle delivery formats. The EPUB is the source; the author does not produce KFX. Whether the converted book supports Enhanced Typesetting is shown in Kindle Previewer under **View → Book Information**; the value should read **Supported** (S14).

### 2.3 Package limits

| Limit | KDP rule | Current book |
|---|---|---|
| **EPUB file size** | 650 MB maximum (S1 §11.4.2; S23). | 2,105,185 bytes (2.11 MB) for the current KDP EPUB without a cover. Large headroom. |
| **Manuscript page count** | 8,000 pages or fewer (S23). | About 1,031 text pages by the book’s own measure; well under. |
| **HTML files in the EPUB** | Fewer than 300 (S1 §9). | 58 XHTML files: title page, navigation, and 56 manuscript units. No cover document. |
| **Size of one HTML file** | Less than 30 MB (S1 §9). | Far below. |
| **Marketing cover image** | 50 MB maximum in the upload criteria; the guidelines recommend 5 MB or fewer, and KDP asks for minimal compression (S2; S3; S1 §4.1). | Master: 5,191,936 bytes (5.19 MB), 100% JPEG; use it for the marketing upload. Build derivative: 1,130,762 bytes (1.13 MB), 80% JPEG; use it for proofs, the with-cover EPUB, or a strict 5 MB fallback. Both meet the 50 MB maximum. |
| **Cover in the EPUB** | Not required for KDP; KDP adds the marketing cover (S24; S1 §4.2). | None by design. `cover.xhtml`, the cover image, and the `cover-image` manifest property are absent. |

The 50 MB figure is a limit on the cover image, not on the manuscript; the EPUB ceiling is 650 MB. The 650 MB ceiling is not the practical limit for an illustrated book. Delivery fees, the file-size-based minimum list price, and download time impose a much lower working budget; see §12.

### 2.4 Validation

`make epub` builds the KDP EPUB; `make epubcheck` runs EPUBCheck on it. `make epub-with-cover` builds the wide-distribution edition, and `make epubcheck-with-cover` validates that one. EPUBCheck validates the EPUB package against the EPUB specification. It does not emulate Kindle conversion, and it does not test Kindle-specific layout, Enhanced Typesetting, pop-up notes, or the cover’s on-device appearance.

KDP’s own gate is Kindle Previewer 4, which compiles the EPUB and runs checks for common errors. KDP states that errors or warnings can prevent a title from becoming available and strongly recommends fixing all of them (S1 §2.2.1). Kindle Previewer runs on Windows 10 and later and on Intel or Apple Silicon Macs with macOS 12 or later (S14). It does not run natively on Linux. The Linux build can run EPUBCheck and the repository checker, but a human must complete the Kindle Previewer or KDP Online Previewer pass on a supported machine or in a browser before publication (S21).

---

## 3. Cover

### 3.1 Two cover jobs, and why the KDP EPUB omits one

KDP distinguishes the **marketing cover** from the **internal content cover**:

- The marketing cover is uploaded separately and appears on the Amazon detail page. It is required (S2; S1 §4.1).
- The internal content cover is the image inside the book content. The guidelines’ internal-cover section begins, “This cover image guidance doesn’t apply to KDP eBooks” (S1 §4.2). The current KDP Help page repeats the generic internal-cover requirement without that KDP exclusion (S2), so the two pages appear to conflict.

KDP’s manuscript guide states the rule plainly, although its steps are written for Word: “Don’t include your cover image in your manuscript file. When you publish your eBook, we’ll automatically add the cover image you provide during title setup” (S24). For a KDP-only EPUB, omit the cover; KDP inserts the marketing cover. Do not add an HTML cover page on top of a cover image, because KDP warns that this can duplicate the cover or fail conversion (S2; S1 §4.2).

Wide distribution is different. Apple Books, Kobo, Google Play, and direct EPUB readers expect the cover inside the file. `make epub` therefore builds the KDP edition without a cover, and `make epub-with-cover` builds a separate edition with the 80% JPEG cover for those channels. Verify in KDP’s Online Previewer that the marketing cover appears once at the front of the KDP edition; if it does not, the fallback is to upload the with-cover EPUB and confirm there is no duplication.

Do not paste the cover into a chapter or another front-matter page; KDP’s quality guide treats a cover image inserted into the manuscript as a cover issue (S16).

### 3.2 Marketing cover specifications

| Specification | KDP requirement or recommendation | Source |
|---|---|---|
| **Formats** | JPEG, PNG, GIF (non-animated), or TIFF. JPEG preferred. SVG is not supported. | S2 |
| **Ideal dimensions** | 2,560 px height × 1,600 px width. | S2; S3 |
| **Minimum dimensions** | At least 1,000 px height and 625 px width; at least 500 px on the longest side for website display. | S2; S3 |
| **Maximum dimensions** | 10,000 px or fewer on each side. | S2; S3 |
| **Aspect ratio** | Ideal height/width ratio of at least 1.6:1. | S3 |
| **Resolution** | 300 PPI recommended; the criteria table also lists 72 dpi as the minimum. | S2; S3 |
| **File size** | 50 MB maximum in the upload criteria; 5 MB or fewer in the guidelines. | S2; S1 §4.1 |
| **Color** | RGB. CMYK is not supported; KDP converts CMYK to RGB. | S2; S3 |
| **Alignment** | Centered vertically and horizontally; proportional to the source within ±15%. | S1 §4.1 |
| **Content** | Title and author/contributor; no spine, bar code, back cover, or inside flap; no pricing or temporary promotions; no typos, watermarks, or placeholder text; language matches the book; text must not contradict the detail page. | S2; S1 §4.1 |

The 5 MB versus 50 MB difference is a real inconsistency between the two official sources. KDP’s cover criteria ask for minimal compression and warn that compression can affect on-device quality (S3). Upload the 100% master as the marketing cover: at 5.19 MB it is under the 50 MB hard limit and only slightly above the 5 MB guideline. The 80% build derivative is 1.13 MB; use it for local proofs and the with-cover EPUB, and keep it as the fallback if strict 5 MB compliance is required. At 80%, the title, subtitle, and author remain sharp, but the master is the better marketing upload.

KDP requires the publisher to hold the rights to the cover art and forbids cover images that infringe another publisher’s or artist’s copyright (S2; S1 §4.1). Keep the cover production record, the generator’s terms, and the prompt history with the project files.

### 3.3 Cover metadata in the EPUB

The KDP EPUB contains no `cover.xhtml`, no image item with `properties="cover-image"`, and no legacy `<meta name="cover">`. That is deliberate (S24; S1 §4.2). EPUBCheck passes without a cover.

The optional with-cover EPUB, built by `make epub-with-cover`, uses Pandoc’s `--epub-cover-image` flag. That writes `text/cover.xhtml`, declares the image in the OPF with the EPUB 3 `cover-image` property, adds the legacy `<meta name="cover">`, and puts the cover first in the spine:

```xml
<manifest>
  <item id="cimage" media-type="image/jpeg" href="media/cover.jpg"
        properties="cover-image"/>
</manifest>
```

The older `<meta name="cover" content="..."/>` method is also accepted. Pandoc emits both, which is acceptable; do not add a separate HTML cover page on top of them. The internal cover should occupy at least 50% of the allocated space, be high-resolution, and carry the same title and author as the detail page (S2; S1 §4.2).

In the current Pandoc 3.1.11.1 build, `cover-image-alt` metadata does not reach the `<image>` element inside Pandoc’s generated SVG cover. The with-cover edition therefore has no cover alt text. Add one for wide distribution, or rely on the following title page. This does not affect the KDP EPUB, which has no cover.

### 3.4 Current cover audit

| Item | Current value | Assessment |
|---|---|---|
| **Master file** | `images/cover.jpg`, 100% JPEG | Archival source and the marketing upload. |
| **Build derivative** | `build/images/cover.jpg`, 80% JPEG | Generated by `make cover`; used in proofs, the with-cover EPUB, and a strict 5 MB fallback. |
| **Dimensions** | 1,600 × 2,560 px | Matches KDP’s ideal dimensions. |
| **Aspect ratio** | 1.600:1 | Matches the 1.6:1 ideal. |
| **Resolution metadata** | 300 dpi | Matches the 300 PPI recommendation. |
| **File size** | Master 5,191,936 bytes (5.19 MB); derivative 1,130,762 bytes (1.13 MB) | Master is within the 50 MB maximum but slightly above the 5 MB guideline; derivative meets both. |
| **Color** | RGB JPEG, sRGB | Correct. |
| **Content** | Title, subtitle, author; front cover only; no pricing | Correct. |
| **EPUB presence** | None in the default KDP EPUB | Correct; KDP adds the marketing cover. The with-cover edition carries the 80% derivative. |
| **Alt text** | None in the with-cover `cover.xhtml` | Add for wide distribution, or rely on the title page. The KDP EPUB has no cover to describe. |
| **Rights** | AI-generated with OpenAI ChatGPT; OpenAI terms recorded in `images/cover.md` | The CC0 dedication covers the original text, not the generated cover. Keep the production record for KDP rights review. |
| **AI disclosure** | Cover is AI-generated | Must be disclosed in KDP as an AI-generated image. |

**Project action.** The master meets KDP’s dimensions, ratio, density, and 50 MB limit; upload it as the marketing cover. `make cover` produces the 1.13 MB, 80% derivative for proofs, the with-cover EPUB, and a strict 5 MB fallback. `make epub` omits the cover from the KDP EPUB; `make epub-with-cover` produces the wide-distribution edition. No re-export of the master is needed. If strict 5 MB compliance is required, inspect the derivative at thumbnail size and confirm that the title, subtitle, and author remain legible; if they do not, keep the master or try `make COVER_QUALITY=85 cover`.

---

## 4. Metadata and title setup

### 4.1 EPUB metadata

A reflowable EPUB does not need a `book-type` meta element. `<dc:language>` and `<dc:title>` are required (S1 §11.1). The project’s OPF has:

- `dc:identifier` — UUID;
- `dc:title` — the full title including subtitle;
- `dc:language` — `en-US`;
- `dc:creator` — Douglas S. Green;
- `dc:rights` — the CC0 dedication.

It has no `meta name="cover"` or `properties="cover-image"`, because the KDP EPUB omits the cover; KDP adds the marketing cover (S24; S1 §4.2). The optional with-cover edition adds both. The KDP EPUB also lacks `dc:description`, `dc:subject`, `dc:publisher`, and accessibility metadata. Those are optional for conversion but useful for accessibility and retail display. The title, author, and language in the file must match the values entered during KDP title setup (S7; S16).

### 4.2 KDP book details

| Field | Rule | Project action |
|---|---|---|
| **Title** | The actual title as it appears on the cover; no keywords, promotional language, URLs, or HTML. | Use “A Nation in Question.” |
| **Subtitle** | Optional; title plus subtitle must be fewer than 200 characters; no HTML. | Use “A History of the United States.” The combined EPUB title can remain as is, but split the fields in KDP. |
| **Series** | Optional; only if the book belongs to a series. | None. |
| **Description** | May use HTML. No URLs, reviews, testimonials, pricing, availability, time-sensitive promotions, or requests for reviews. | Write a description about the book’s argument and scope. Do not put “free,” CC0, or pricing in the description. |
| **Author** | Primary contributor; no HTML. | Douglas S. Green. |
| **Contributors** | Credit editors, illustrators, translators, and others who worked on the book. All contributors to a public-domain book must be entered. | Add any mapmakers, image editors, or other credited contributors. |
| **Publisher** | Optional; must not name Amazon, Kindle, KDP, another publisher, or a website. | Omit or use the author’s imprint. |
| **Keywords** | Up to seven relevant phrases; no misleading or unrelated terms. | Choose history and U.S. history phrases that match the book. |
| **Categories** | Must match the book’s central subject. | Choose U.S. history categories; do not use unrelated high-traffic categories. |
| **Language** | Must match the book and the EPUB `dc:language`. | `en-US`. |
| **ISBN** | Not required for eBooks; KDP assigns an ASIN. If an ISBN is entered, it must be unique to the eBook and match the file. | No ISBN. Use the ASIN. |
| **Accessibility features** | KDP asks during title setup; answers appear on the detail page. | Answer accurately after the accessibility pass in §10. |
| **AI content** | Disclose AI-generated text, images, and translations; AI-assisted work does not require disclosure. | Disclose the AI-generated cover. Classify the manuscript text and future interior visuals. |
| **Publishing rights** | Choose copyright or public domain. Public-domain works are eligible only for the 35% royalty option and not for KDP Select. | The CC0 dedication requires a deliberate choice. See §12. |

### 4.3 AI disclosure

KDP defines **AI-generated** content as text, images, or translations created by an AI-based tool, even if substantially edited afterward. **AI-assisted** content is content the author created and then edited, refined, checked, or improved with AI tools; it does not require disclosure (S8). AI-generated images include cover and interior images and artwork (S8).

The cover record in `images/cover.md` says the cover was generated with OpenAI ChatGPT. That is AI-generated imagery and must be disclosed. The manuscript’s text and any future maps, figures, or images need a separate determination. If a map is drawn by a human with AI assistance, it is AI-assisted; if it is generated by an image model, it is AI-generated. The distinction should be recorded per asset.

### 4.4 Public-domain and CC0 status

KDP allows public-domain content but may ask for proof and may refuse content already available through Amazon or other sites. If a free version of a public-domain title is already in the Kindle Store, KDP allows only a differentiated version with “(Translated),” “(Annotated),” or “(Illustrated)” in the title and a short bullet summary of no more than 80 characters at the start of the description (S9). Those rules apply when KDP treats a title as a public-domain edition; this book is original scholarship, not a reprint. Still, the CC0 dedication may cause KDP to treat it as a public-domain work, so keep the LICENSE, the metadata record, and the repository history as proof of authorship and dedication.

KDP’s content-quality guide also discourages content that is freely available on the web unless the publisher owns it or it is in the public domain (S16). The CC0 dedication places this book in the public-domain exception, but the author should keep proof of authorship and the license record ready if KDP asks.

The commercial consequence is significant: KDP states that works in the public domain, or consisting primarily of public-domain content, are eligible only for the 35% royalty option (S11; S13), and public-domain content is not eligible for KDP Select (S10). If the author instead selects “I own the copyright,” the book may qualify for the 70% option, but that selection must be consistent with the CC0 dedication and with the author’s actual rights. This is a legal and business decision, not a formatting one. Confirm it with KDP and, if necessary, counsel before publishing.

---

## 5. Navigation

### 5.1 What KDP requires

KDP requires a logical table of contents, and strongly recommends an HTML TOC for books that benefit from navigation. The HTML TOC should be near the beginning, not at the end; its entries must be links; it must not use page numbers; it must not be built as an HTML table; and it should be in chronological order (S1 §5.1; S6).

The logical TOC can be a `toc nav` element or an NCX file. Kindle devices and applications support **two levels of nesting** (S1 §5.2; S6). The NCX must follow the book’s order and must not omit or duplicate chapters. Guide items or landmarks for the cover (when the EPUB has one) and TOC are optional but highly recommended; the start-reading location is defined by Amazon, not the publisher (S1 §5.3). The KDP EPUB has no cover landmark; its title page and TOC landmarks remain.

If the TOC includes a list of maps or illustrations, each entry should link to the item (S1 §5.1). This matters for Appendix C when the visuals are produced.

### 5.2 Current navigation

The EPUB has:

- `title_page.xhtml` and `nav.xhtml` before the first chapter; there is no `cover.xhtml`;
- a `nav.xhtml` with 56 chapter-level entries in order;
- a `toc.ncx`;
- a hidden landmarks nav with title page and TOC;
- a `guide` with a TOC reference only.

The TOC is **flat**: one level, 56 entries. That is valid and usable. A 1,000-page book would benefit from a two-level Part/Chapter TOC, but the manuscript has no part divider pages and `--toc-depth=1` intentionally avoids dumping every `##` section into the TOC. Raising the depth to 2 would add roughly 300 section entries, which is worse. If a two-level TOC is wanted, add explicit part anchors or part divider pages and a small Lua filter or nav template, then update the README and Appendix C. Do not simply raise `--toc-depth`.

**Project action.** Keep the current TOC as the baseline. Decide whether to add 11 part-level entries. When the 56 visuals exist, add linked entries in Appendix C or a separate List of Maps and Illustrations, and make sure the links resolve in the EPUB.

---

## 6. HTML and CSS

### 6.1 KDP’s HTML and CSS rules

KDP supports most HTML5, but not forms, frames, or JavaScript; scripts are stripped (S1 §6.1, §6.3). Avoid nested `<p>` tags. File references must match the case and spelling of the source. Use UTF-8 and ordinary spaces; the only supported spaces are the normal space, non-breaking space, and zero-width non-joiner (S1 §6.5–6.7). The supported CSS values are listed in the Enhanced Typesetting reference (S22).

Layout should be single-column; do not use the CSS `position` property for alignment (S1 §11.2). Avoid negative values for positioning and margins; if a negative text-indent is used, add compensating padding. Avoid fixed values in points and pixels for font-size, width, height, margin, padding, and text-indent; use ems or percentages (S1 §6.2, §11.3.4).

For body text, KDP is strict: body text must use the default font size (1em) and line height; it must not be forced bold, italic, colored, background-colored, or set in a forced font family; it must not use non-breaking spaces in place of normal spaces; and it must not have imposed left/right margins or padding (S1 §11.3.2; S5). Paragraphs may use a text-indent of no more than 4 ems or a margin, but not double spacing. Left/right margins on special blocks should be percentages, not ems, so they do not grow too wide at large font sizes (S1 §11.3.5; S5).

Headings should specify their alignment because reflowable text is justified by default; avoid forced right or center alignment of body text (S1 §11.3.1). Page breaks after chapters and sections are supported; `page-break-inside: avoid` and `break-inside: avoid` are supported for keeping images with captions and headings with paragraphs (S1 §11.3.7).

### 6.2 Current CSS audit

| Rule | Current state | Action |
|---|---|---|
| Body line height and alignment | `body` sets neither line height nor text alignment; Kindle controls both. | Keep. |
| Blockquote margins | `margin: 0.8em 8%;` and epigraphs use `padding: 0 8%;`. | Keep; horizontal spacing is proportional. |
| List margins | `ul, ol { margin: 0.5em 0 1em 8%; }`. | Keep; left margin is proportional. |
| Table text | `table { font-size: 0.8em; line-height: 1.3; }`. | Test at font size 3; 0.8em may be too small. Consider 0.9em if the tables still fit. |
| Note text | `.footnotes { font-size: 0.85em; line-height: 1.4; }`. | Test at font size 3; consider 0.9em. |
| Figure images | `figure img { display: block; width: 100%; height: auto; margin: 0 auto; }`. | Keep; images fill the text column and preserve aspect ratio. |
| General images | `img { max-width: 100%; height: auto; }`. | Keep. |
| Link styling | `a { color: inherit; text-decoration: underline; }`. | Keep; no forced link color and links remain identifiable. |
| Long URLs | `a { overflow-wrap: break-word; word-wrap: break-word; }`. | Check in Kindle Previewer; shorten link text or add break points if URLs overflow. |
| Body font | No font family, font size, or background color. | Keep. |
| Scripting and layout | No JavaScript, forms, frames, or `position:` rules. | Keep. |
| Table rules | `currentColor` borders. | Check in Kindle Previewer’s dark mode; fall back to a neutral gray if needed. |

A compliant body rule is deliberately minimal:

```css
body {
    margin: 0;
    padding: 0;
}
```

A compliant figure rule:

```css
figure {
    margin: 1.2em 0;
    text-align: center;
    page-break-inside: avoid;
    break-inside: avoid;
}

figure img {
    display: block;
    width: 100%;
    height: auto;
    margin: 0 auto;
}

figcaption {
    margin-top: 0.5em;
    font-size: 0.85em;
    text-align: left;
    text-indent: 0;
}
```

KDP normalizes body font size, family, and color at upload, but relying on that normalization is not a substitute for clean CSS. The body line-height and forced-justification violations are now resolved. The remaining CSS checks are visual: table and note text at font size 3, long URLs in the notes, and `currentColor` rules in dark mode. The book’s bold paragraph labels and italic titles are selective emphasis, not the body-wide styling KDP prohibits, so they do not need to be removed. The project embeds no fonts; if a future design embeds one, the publisher must hold the license and follow KDP’s embedded-font rules (S1 §11.3.8).

---

## 7. Images, maps, and charts

### 7.1 KDP’s image rules

| Rule | Detail | Source |
|---|---|---|
| **Formats** | JPEG and PNG are supported. TIFF, multi-frame GIFs, and images with transparency are not. Transparent backgrounds are converted to white; flatten every image onto white and remove the alpha channel. | S1 §11.4.1; S4 |
| **Color** | Use RGB. The current KDP image page recommends sRGB and says CMYK is converted to sRGB. The 2026.3 PDF contains a contradictory sentence that Kindle “does not support sRGB”; use sRGB as the practical target and verify in Previewer. | S4; S1 §11.4.1 |
| **Resolution** | 300 PPI at the intended display size. A full-page image after margins, running heads, page numbers, and captions is treated as 4 × 6 inches, or 1,200 × 1,800 px. At 80% width the minimum is 960 × 1,440 px; at 60%, 720 × 1,080 px. | S1 §11.4.2 |
| **Display width** | Pictorial images should occupy at least 60% of the screen width; images with text, charts, or maps should occupy at least 80%. Important images should not be laid out below 40%. | S4; S1 §11.4.2 |
| **High-resolution devices** | KDP recommends images display clearly at 2× magnification; a full-width image should be captured at 3,200 px wide. | S1 §11.4.5 |
| **Minimum photographs** | Photographs below 300 × 400 px may be scaled and blurred. Images below 72 PPI can fail conversion. | S1 §11.4.5 |
| **Line art and text** | Use PNG for charts, maps, diagrams, and line art. Text in an image should have a lowercase “a” at least 6 px high. | S1 §11.4.6–11.4.7 |
| **Text as image** | Do not render paragraphs or captions as images. Prefer HTML. Captions and table text should be HTML. | S1 §11.4.8; S4 |
| **Captions** | Put captions below the image, in HTML, using a separate block or `<figcaption>`. Do not raster the caption. | S1 §11.4.9; S4 |
| **Alt text** | Every meaningful image needs an `alt` attribute; keep it to 140 characters or fewer; decorative images use `alt=""` or `role="presentation"`. | S4; S15 |
| **Aspect ratio** | Set either width or height to a percentage, not both, and set the other to `auto`. | S1 §11.4.10 |
| **SVG** | SVG has minimal support. `viewBox` is mandatory; SVG `<text>` is not supported; `preserveAspectRatio="slice"` is not supported; books with more than 25 SVG images are not supported in Enhanced Typesetting. | S1 §11.4.11 |
| **Accessibility** | Text inside images cannot be read by screen readers or braille displays. Use real text where possible; describe complex images in the surrounding prose. | S1 §11.4.7; S15 |

### 7.2 What this book needs

The README registers 39 maps, 9 figures, and 8 images. The current EPUB contains **none** of them. That is not a cosmetic gap. KDP’s content-quality guide lists “missing image section that the product description or the contents of the book indicate should be included” as a critical issue (S16). Appendix C is a catalog of maps, figures, and images; if the book is published with that catalog and no assets, KDP can treat the book as missing promised content. Either produce the visuals or change the catalog and every promise that depends on it.

A production specification that meets KDP’s rules:

| Visual type | Format | Target size | Notes |
|---|---|---|---|
| **Maps** | PNG, sRGB, flattened on white | 1,600 × 2,400 px minimum; 2,400 × 3,600 px for dense labels | At 100% width this is above the 300 PPI minimum on the 4 × 6 canonical page. Labels should remain legible on a phone. Use patterns and labels, not color alone, so the map survives grayscale. Target 100–400 KB as an indexed PNG. |
| **Charts and figures** | PNG, sRGB | 1,600 × 2,400 px; 2,400 × 3,600 px if labels are small | Line art should be PNG, not JPEG. Keep the lowercase “a” at least 6 px high in the final image. Target 100–400 KB as an indexed PNG. |
| **Photographs and facsimiles** | JPEG, sRGB | 1,600–3,200 px on the long edge | Use the highest-quality source available. Do not upscale a small image and call it high resolution. JPEG quality around 80–85; target 100–400 KB. Check rights and credit. |
| **Cover** | JPEG, RGB | 1,600 × 2,560 px | Separate marketing upload; no cover in the KDP EPUB. The master is 100% quality; the build derivative is 80%. See §3. |

KDP’s floor is 1,200 × 1,800 px for a full-width image, with 960 × 1,440 at 80% width. A 1,200–1,600 px width is the practical floor for full-width maps and charts; the project’s 1,600–2,400 px range is deliberately higher so labels survive zoom. KDP recommends 3,200 px wide for 2× magnification, so the limit is file size, not an arbitrary pixel cap. Do not drop below the 300 PPI table to save bytes. Reduce file size with indexed PNG, stripped metadata, and JPEG quality around 80–85 for photographs; a flat-color indexed PNG at 2,400 × 3,600 can be smaller than an RGB PNG at 1,600 × 2,400, so measure the actual file.

Every visual needs:

1. a figure number and caption in HTML, below the image;
2. a source line and credit;
3. alt text of 140 characters or fewer;
4. a fuller prose description in the surrounding text when the image carries historical argument that a short alt cannot convey;
5. a rights basis recorded in the README register.

For maps, the caption must state the date and the area covered and must distinguish boundaries, claims, and uncertain reconstructions. For charts, state units, denominators, and base years. Put all of that text in HTML below the image; never bake the title, caption, source line, or credit into the PNG. A map’s labels, legend, scale bar, axis labels, and data labels may be inside the image because they are part of the visual; a separate figure title, caption, source line, or credit may not. This is both KDP’s rule and the book’s evidence standard (S4; S1 §11.4.8–11.4.9).

Appendix C §§2.7, 3.3, and 4.5 are the approved caption and alt-text schedule for the 56 registered visuals. The owning chapter, the README register, and the production file must use those strings. A compliant block is:

```html
<figure>
  <img src="map-12.png"
       alt="Map of canals, roads, and railroads, 1825–1840, showing completed, under-construction, and projected routes, including the Erie Canal." />
  <figcaption><strong>Map 12. Canals, roads, and railroads, 1825–1840.</strong> Completed and projected lines show the Erie Canal crossing the Appalachian divide through the Mohawk corridor. Source: drawn for this volume from Henry Schenck Tanner’s 1840 map and description. Credit: the author and the named repository.</figcaption>
</figure>
```

The CC0 dedication covers the book’s original text; it does not clear third-party images, maps, facsimiles, or quotations. KDP requires the publisher to hold the necessary rights for all content. Each visual needs its own rights basis, credit line, and, where required, permission record. Do not treat “public domain” as a global clearance without checking the jurisdiction and the particular source.

For complex maps, the alt text should identify the map’s subject and scope, not attempt to transcribe every label. The caption and adjacent paragraph can carry the interpretation. This satisfies both KDP’s alt-text rule and the book’s evidence standard.

### 7.3 File size and delivery

KDP sets no separate count limit on maps and charts. The constraints are the 650 MB package, the delivered file size, and legibility on a phone. The 650 MB package ceiling is generous; the commercial limit is not. The KDP EPUB is 2.11 MB without a cover. A 56-image program adds about 5.6–22.4 MB at the 100–400 KB working target; at 0.5 MB per image it adds about 28 MB, and at 1 MB per image about 56 MB. That is enough to change both the delivery fee and the minimum list price. See §12.

KDP’s 70% royalty option deducts a delivery fee based on the file size KDP determines, at **US$0.15 per MB** on Amazon.com (S11). The 35% option does not deduct delivery costs (S11). KDP reports the “file size after conversion” in the pricing tab, and that converted size, not the raw EPUB, is what the delivery fee uses. KDP also recompresses images during conversion. Measure the converted book in KDP or Kindle Previewer; do not assume the EPUB byte count is the billing size.

---

## 8. Tables

### 8.1 KDP’s table rules

KDP recommends HTML `<table>` markup, not images of tables. An image table cannot paginate, cannot be read by assistive technology, and cannot be navigated cell by cell. A table significantly wider than the screen forces panning, which KDP treats as a poor experience (S1 §11.5.1). Keep tables below **100 rows and 11 columns** for devices of all sizes (S1 §11.5.1).

Use simple tables with standard rows and columns. `thead`, `tbody`, and `tfoot` are best practice. Include column and row headings and a table caption. Avoid nested tables and merged cells where possible; Enhanced Typesetting does not support nested tables (S1 §11.5.2; S15). Split a table that is too wide or too long rather than shrinking the type.

For books with Enhanced Typesetting, tables with more than three columns get an enhanced table viewer with panning, zooming, and text lookup (S1 §11.5.4). But books with large tables might not support Enhanced Typesetting at all. Check **Book Information** in Kindle Previewer. If Enhanced Typesetting is not supported, the table viewer is not available and a wide table is more likely to be cut off.

KDP’s quality guide is blunt: a table with content cut off at the bottom of the screen at **font size 3** is a critical issue (S16). Test every table at that setting, not only at the default.

### 8.2 Current table inventory

The manuscript has 95 Markdown table blocks, including three Appendix C production schedules that are not display tables. The README registers 80 display tables; it counts a multi-panel reference table once, while Appendix B prints each lettered panel as a separate Markdown block. The widest tables have 10 columns; the longest have 32 printed rows. Five Appendix B panels have 10 columns, and fifteen are set to full width. All are within KDP’s 100-row and 11-column ceiling.

That does not make them safe. A 10-column table on a phone at font size 3 is likely to be cramped even with the table viewer. Appendix B’s panels are the right instinct: split a large reference table into lettered panels with their own captions. Appendix D’s planned six-column chronology is also at the edge; plan panels or a narrower matrix.

### 8.3 Accessibility gaps in the current HTML

Pandoc produces `<thead>` and `<th>` header cells for the column headers, which is good. Two gaps remain:

1. **Captions are paragraphs after the table, not `<caption>` elements.** Appendix B uses `<p><strong>Caption.</strong> …</p>` after the table. KDP and accessibility guidance call for a table caption; a `<caption>` element is the semantic way to provide it. Move the caption before the table or generate a `<caption>` with a Lua filter.
2. **Leading cells are bold `<td>` cells, not row headers.** The house style bolds the first cell of each row. Visually that reads as a row header; semantically it is a data cell. For screen readers, promote the leading cell to `<th scope="row">` where it labels the row.

A small Pandoc Lua filter can promote the first body cell to a row header and move a following “Caption.” paragraph into a `<caption>` before the table. That is preferable to hand-editing the tables, and it keeps the Markdown source readable.

### 8.4 Project actions

- Test every table at font size 3 on a phone profile and a 6-inch e-reader profile.
- Split any table that is cut off or requires horizontal panning.
- Add `<caption>` semantics and row headers.
- Do not rasterize tables to solve layout problems; that trades a layout issue for an accessibility failure.
- Check that table text is not split across cells or cut off at the right edge.
- Check that Appendix B’s source lines and notes remain attached to the right panel after any split.

---

## 9. Notes, cross-references, and links

### 9.1 KDP’s note rules

KDP strongly recommends the HTML5 `aside` element with `epub:type="footnote"` for notes. Regardless of the element, KDP requires **bidirectional hyperlinks**: the text links to the note and the note links back to the text. On some devices, bidirectionally linked notes appear in a pop-up. KDP recommends placing note text at the end of the chapter or book (S1 §11.3.12; S5).

Non-footnote internal links should not be bidirectional. Use A → B and B → C, not A ↔ B, to avoid unintended pop-ups (S1 §7.1). Cross-references to chapters, tables, figures, and charts should link to the relevant location when the book says “see Chapter 11” or “see Table 2” (S1 §7.1).

External links should be present only when they directly enhance the reader experience. KDP recommends archiving them and including the archived link; prohibited links include pornography, other commercial eBook stores, forms that request customer information, illegal or harmful content, and malicious links (S1 §7.2). Link text should be self-describing; avoid “click here,” “see more,” and repetitive links on the same page (S1 §7.2).

### 9.2 Current notes

The book has 3,355 notes. Pandoc emits each note as:

```html
<aside epub:type="footnote" id="fn1">
  <p><a href="#fnref1" class="footnote-back" role="doc-backlink">1</a>. …</p>
</aside>
```

The reference is an `epub:type="noteref"` link. This is close to KDP’s preferred method. The notes sit at the end of each manuscript unit, which is within KDP’s “end of chapter or book” recommendation.

The custom `tools/dedupe-notes.lua` filter is the part to watch. Pandoc expands a named note at every reference. The filter keeps the first note and replaces later references with a span link to the first note. That avoids printing the same note several times, but the later reference is a plain internal link without `epub:type="noteref"`, and the note’s backlink returns to the first reference only. A reader who follows a repeated note from a later page may not have a return link to that page. KDP requires bidirectional links for notes; this is a potential compliance gap for any key referenced more than once.

There are two possible fixes:

1. **Do not dedupe.** Let Pandoc print a separate note for each reference. This preserves a one-to-one backlink at the cost of repeated note text.
2. **Extend the filter.** Give every reference its own anchor and append a matching backlink to the single note. The note would carry several return links, one per reference. This is more work but produces a cleaner reading experience.

Either way, test the pop-up behavior in Kindle Previewer. Ensure the pop-up is not blank and the return link lands on the right reference.

### 9.3 Cross-references and external links

The book uses cross-references such as “Ch. 11, §2.2” and “App. B, Table 2.” They are plain text. KDP recommends linking them to the relevant location. A Lua filter can map the chapter number to the split XHTML file and the section number to the heading ID, but it needs a stable map of chapter files and section anchors. That map already exists implicitly in the file names and headings. Start with the most important cross-references: chapter hand-offs, table references, and appendix references.

The notes contain many external URLs. Before release:

- run a link checker over the note URLs;
- replace dead links with archived copies, or mark them “(URL inactive)” as KDP recommends;
- make the link text more specific than the repeated “Consulted text” label where possible;
- remove or replace links to prohibited categories;
- keep the URLs in the notes, not in the KDP product description.

KDP can remove external links at its discretion and treats broken or incorrect links as quality issues (S16). A history book with hundreds of source links needs a link check as part of the release gate.

---

## 10. Accessibility

KDP’s accessibility guidance asks for:

- the primary language and any language changes defined in the content;
- well-structured headings, lists, tables, captions, and row/column headings;
- text alternatives for meaningful images and null alt text for decorative images;
- self-describing link titles;
- sufficient contrast and no reliance on thin or light type;
- MathML for mathematical content (S1 §8; S15).

The current book has `lang="en-US"` and `xml:lang="en-US"` on every XHTML document. It does not use phrase-level `lang` attributes for foreign-language quotations; if any are present, they should be tagged. The book has no interior images; when they are added, each needs alt text. Appendix C §§2.7, 3.3, and 4.5 supply the approved alt text for all 56 registered visuals. The KDP EPUB has no cover document, so there is no cover SVG to describe; the title page carries the title and author. The optional with-cover EPUB has a cover SVG without alt text, which should be fixed for wide distribution. The table captions and row headers are not yet semantic. Those are the main accessibility gaps.

A useful EPUB 3 accessibility metadata block would include, at minimum:

```xml
<meta property="schema:accessMode">textual</meta>
<meta property="schema:accessMode">visual</meta>
<meta property="schema:accessModeSufficient">textual</meta>
<meta property="schema:accessibilityFeature">structuralNavigation</meta>
<meta property="schema:accessibilityFeature">tableOfContents</meta>
<meta property="schema:accessibilityFeature">alternativeText</meta>
<meta property="schema:accessibilityHazard">none</meta>
<meta property="schema:accessibilitySummary">A reflowable history with a linked table of contents, structured headings, HTML tables, and alt text for maps and figures.</meta>
```

Do not copy that block blindly. If a map’s argument is not fully available in the alt text and surrounding prose, `accessModeSufficient` should not claim that text alone is sufficient. Run the DAISY Consortium’s ACE accessibility checker on the EPUB, as KDP recommends (S1 §9.1; S15), and reconcile its findings with the metadata.

KDP asks about accessibility features during title setup. The answers appear on the detail page. Choose them after the accessibility pass, not before, and make sure they match the EPUB metadata.

---

## 11. Quality assurance and release checks

### 11.1 KDP’s quality categories

KDP’s content-quality guide divides problems into **critical**, **destructive**, and **distracting** issues. A critical issue can remove a book from sale until corrected; excessive destructive or distracting issues can produce a quality warning or removal (S16). The critical issues most relevant here are:

- body text rendered throughout as bold, italicized, underlined, or hyperlinked, rather than selectively emphasized;
- body text with more than a quarter-screen of extra margin or padding;
- body text not in the default color, or forced white text or black background that becomes unreadable in another theme;
- in-line page numbering;
- a table with content cut off at font size 3;
- a missing image section that the description or contents promise;
- a repeated chapter or duplicated text;
- an unlinked footnote, a broken internal link, a broken external link, a missing NCX, or a TOC out of order;
- a missing, blurry, oversized, or wrongly inserted cover;
- metadata that does not match the file;
- unsupported characters;
- missing content or wrong content.

The current build is at risk on several of these: the unproduced visuals, the wide tables, the repeated-note backlink behavior, and the fact that Kindle Previewer has not been run. The body CSS defaults are now fixed, but table and note text still need visual testing at font size 3. The current EPUB is also a proof, not a release candidate: Appendices C–E are researched outlines rather than final prose, and the 56 visuals are unproduced. KDP quality review is not the place to discover that.

### 11.2 Release checklist

| Check | Tool or evidence | Current status |
|---|---|---|
| Structural checker | `python3 tools/check_book.py --strict` | Passes: 56 files, 533,270 words, 3,355 notes, 95 tables, 27 local links, 0 errors. |
| EPUB build | `make epub` | Passes; `build/a-nation-in-question.epub` is 2.11 MB and contains no cover. |
| With-cover EPUB | `make epub-with-cover` | Passes; `build/a-nation-in-question-with-cover.epub` is 3.24 MB; for wide distribution only. |
| EPUBCheck | `make epubcheck` | Passes for both editions: 0 fatals, 0 errors, 0 warnings. |
| Kindle conversion | Kindle Previewer 4 | **Not run.** Needs Windows or macOS, or KDP Online Previewer. |
| Enhanced Typesetting | Previewer → View → Book Information | **Not checked.** Large tables may disable it. |
| Cover master | KDP cover criteria and Previewer | 1,600 × 2,560 px, 1.6:1, 300 dpi, 100% JPEG, 5.19 MB. Within the 50 MB maximum; slightly above the 5 MB guideline. |
| Cover derivative | `make cover`; inspect | 80% JPEG, 1.13 MB, 1,600 × 2,560, 300 dpi. For proofs, the with-cover EPUB, and a strict 5 MB fallback; check title and author at thumbnail size. |
| Cover in EPUB | Inspect `content.opf` and spine | None in the KDP EPUB by design; KDP adds the marketing cover. |
| Single cover | Previewer: cover, then next page | No cover in the EPUB; verify KDP adds exactly one cover and no duplicate. |
| TOC links | Previewer, Go To menu | 56 links in order; verify each resolves. |
| NCX/landmarks | EPUBCheck and Previewer | Present; verify. |
| Notes | Previewer pop-ups and return links | 3,355 notes; repeated-note behavior not verified. |
| Images | Previewer, font size 3, device profiles | **No interior images.** Produce and test 56. |
| Tables | Previewer, font size 3, phone and e-reader | 95 blocks; 10-column panels untested. |
| Background themes | White, black, mint, sepia | Not checked. `currentColor` rules need a dark-mode check. |
| Font settings | Change size and typeface | Body defaults are clean; verify at multiple sizes. |
| External links | Link checker and archive | Not run. |
| Accessibility | ACE checker | Not run. |
| Metadata | KDP title setup | Title/subtitle split and description still to write. |
| AI disclosure | KDP title setup | Cover must be disclosed; text classification open. |
| Rights | KDP publishing rights | CC0/public-domain decision open. |
| Missing content | README/Appendix C against assets | **56 visuals promised, none produced.** |
| Typos and characters | Previewer, spell check, manual proof | Not run for the EPUB. |

### 11.3 What EPUBCheck does not prove

EPUBCheck passing is necessary, not sufficient. It does not prove that Kindle Previewer will accept the conversion, that tables fit at font size 3, that notes pop up, that images are legible, that the cover looks right on a device, that links resolve, or that the book meets KDP’s content-quality standards. The release gate requires both the structural/EPUB checks and the Kindle-specific visual and behavioral checks.

---

## Part II — This project

## 12. Royalties, delivery fees, and the CC0 decision

### 12.1 The two royalty options

KDP offers a 35% royalty option and a 70% royalty option. The 70% option is available for list prices from **US$2.99 to US$12.99** on Amazon.com effective July 7, 2026 (S12). The 70% royalty is 70% of the list price after VAT and delivery costs are subtracted: 0.70 × (list price − VAT − delivery). The 35% royalty is 35% of the list price after VAT, with no delivery-cost deduction (S11). Applying 70% to the price and then subtracting the full delivery fee understates the royalty; the delivery fee is inside the parentheses. At US$9.99 with an 8 MB file, for example, 0.70 × (9.99 − 1.20) = $6.15, not $5.79.

Delivery costs on Amazon.com are **US$0.15 per MB** of the file size KDP determines, rounded up to the nearest kilobyte, with a US$0.01 minimum (S11). The 70% option is available only in certain territories; sales outside those territories earn 35% (S11). The table below ignores VAT, territory mix, price matching, and currency, so it is a planning example, not a royalty quote. The 70% columns apply only if the book qualifies for the 70% option; a public-domain classification makes them unavailable.

| File size | Delivery fee at US$0.15/MB | 35% at US$9.99 | 35% at US$12.99 | 70% at US$9.99 | 70% at US$12.99 |
|---|---|---|---|---|---|
| **2.11 MB** (current, no cover) | $0.32 | $3.50 | $4.55 | $6.77 | $8.87 |
| **3 MB** (first price-tier boundary) | $0.45 | $3.50 | $4.55 | $6.68 | $8.78 |
| **10 MB** (second price-tier boundary) | $1.50 | $3.50 | $4.55 | $5.94 | $8.04 |
| **25 MB** | $3.75 | $3.50 | $4.55 | $4.37 | $6.47 |
| **40 MB** | $6.00 | $3.50 | $4.55 | $2.79 | $4.89 |
| **50 MB** | $7.50 | $3.50 | $4.55 | $1.74 | $3.84 |
| **75 MB** | $11.25 | $3.50 | $4.55 | $0.00 | $1.22 |
| **100 MB** | $15.00 | $3.50 | $4.55 | $0.00 | $0.00 |

At US$9.99, the 35% and 70% options break even at about 33 MB; at US$12.99, at about 43 MB. Above those sizes, the 35% option pays more because it does not deduct delivery. That is counterintuitive but follows directly from KDP’s formulas. It matters for a 56-image history book. The table shows $0.00 where the formula would go negative; use KDP’s estimator for the actual floor.

The 35% option also has a file-size-based minimum list price on Amazon.com: **under 3 MB, $0.99; 3 MB to under 10 MB, $1.99; 10 MB or more, $2.99**; the maximum is $200 (S12). The 70% option’s minimum is $2.99 regardless of size. The current 2.11 MB EPUB preserves the $0.99 floor. Adding about 0.9 MB of visuals crosses into the $1.99 tier, and a 10 MB book cannot be priced below $2.99 under either option. This matters more than the delivery fee if the book is 35%-only because of its public-domain status.

### 12.2 The public-domain problem

KDP states that books consisting primarily of public-domain content are eligible only for the 35% royalty option (S11; S13). KDP Select requires exclusive rights and states that public-domain content is not eligible (S10). The book’s CC0 dedication means others may copy and distribute it; that is incompatible with the exclusivity KDP Select requires. So the likely outcome for a CC0 book is:

- 35% royalty only, if KDP treats it as public domain;
- no KDP Select enrollment, and therefore no Kindle Unlimited inclusion through KDP Select;
- no delivery-fee deduction under the 35% option;
- a 650 MB package ceiling, but no per-MB royalty penalty.

If the author instead selects “I own the copyright” and qualifies for the 70% option, the delivery fee applies and the image budget becomes a royalty decision. The author should not select a rights option that contradicts the CC0 dedication merely to reach 70%. Confirm the correct selection with KDP and, if necessary, counsel.

### 12.3 Practical image budget

- Current KDP EPUB: 2.11 MB, no cover.
- 56 images at 0.25 MB each: about 14 MB added, roughly 16 MB total.
- 56 images at 0.5 MB each: about 28 MB added, roughly 30 MB total.
- 56 images at 1 MB each: about 56 MB added, roughly 58 MB total.
- The 100–400 KB working target puts the image program at roughly 5.6–22.4 MB, for a total of roughly 7.7–24.5 MB.
- At 35%, delivery is not deducted; the main size penalties are the minimum list price tiers and download time.
- At 70% and US$12.99, keep the delivered file under about 43 MB to beat the 35% option; under 40 MB is a safer target.

Do not optimize the book to a byte count before the images exist. Produce the visuals at KDP’s resolution standard, keep each map or chart in the 100–400 KB range where the labels allow it, measure the converted file, and then decide whether more compression is needed.

### 12.4 DRM, ISBN, and print

- **DRM** is optional. KDP says royalty rates and payment structure are unchanged by the DRM choice. A DRM-free book lets verified purchasers download EPUB and PDF files (effective January 20, 2026), which is consistent with a CC0 book’s intent (S19). DRM would restrict that. This is a decision for the author, not a formatting requirement.
- **ISBN** is not required for a Kindle eBook; KDP assigns an ASIN (S20). If an ISBN is entered, it must be unique to the eBook and match the metadata. A print edition needs its own ISBN and a separate wraparound cover.
- **Print** is outside this document. The current cover is front-only; a print edition needs spine and back cover, trim size, and a separate KDP print workflow.

---

## 13. Action list

### P0 — before any KDP upload

1. **Produce the 56 interior visuals or remove the promises.** The README and Appendix C register 39 maps, 9 figures, and 8 images; the EPUB has none. KDP treats a missing promised image section as a critical issue. Do not publish a catalog of absent maps.
2. **Verify the body CSS in Kindle Previewer.** The body line-height and forced justification are removed; blockquote and list horizontal margins are percentages; figure images fill the column. Check the result at multiple font sizes and in all four background themes.
3. **Upload the 100% cover master and keep the 80% derivative for proofs.** The master is 1,600 × 2,560, 1.6:1, 300 dpi, 100% JPEG (5.19 MB); KDP asks for minimal compression. `make cover` produces the 1.13 MB, 80% derivative for proofs, the with-cover EPUB, and a strict 5 MB fallback. The KDP EPUB omits the cover by design; confirm in the Online Previewer that KDP adds it once. Update `images/cover.md` after any change.
4. **Decide the KDP publishing-rights selection.** CC0 may mean public domain, 35% only, no KDP Select. Confirm with KDP; record the decision.
5. **Disclose the AI-generated cover.** Classify the manuscript text and any future interior images as AI-generated or AI-assisted.
6. **Run Kindle Previewer 4 or KDP Online Previewer.** Check conversion, Enhanced Typesetting, cover, TOC, notes, tables, and images. Linux cannot run the desktop Previewer.
7. **Add alt text, captions, and row headers** for every visual and table before release.

### P1 — before the release candidate

8. **Test every table at font size 3** on phone and e-reader profiles; split or reflow the 10-column panels that fail.
9. **Fix note backlinks for repeated references.** Either stop deduping or extend the filter so every reference has a return path.
10. **Add a two-level Part/Chapter TOC** if the book will use part dividers; otherwise keep the flat 56-entry TOC and document the choice.
11. **Link Appendix C entries** to the produced visuals, and add a List of Maps and Illustrations if the TOC promises one.
12. **Link the most important cross-references** and run an external-link check; archive or mark dead links.
13. **Add EPUB accessibility metadata and run ACE.** Reconcile the results with the KDP accessibility answers.
14. **Write the KDP description, keywords, and categories** within the metadata rules; do not put URLs, reviews, pricing, or “free” in the description.
15. **Split the KDP title and subtitle fields** while keeping the cover and EPUB title consistent.

### P2 — polish and business decisions

16. **Measure the converted file size** and model the delivery fee before choosing a price and royalty option.
17. **Decide DRM.** DRM-free is consistent with CC0 and allows purchaser downloads; DRM restricts them. Royalties are unchanged.
18. **Decide whether a print edition is in scope.** If so, commission a wraparound cover and follow the separate print guidelines.
19. **Recheck the KDP sources** before upload; the guidelines and help pages change.

---

## 14. Open decisions

| Decision | Why it matters | Owner |
|---|---|---|
| **Public domain or copyright selection in KDP** | Determines 35% versus 70%, KDP Select eligibility, and whether KDP asks for public-domain proof. | Author, with KDP or counsel. |
| **Price and royalty option** | The 70% band ends at US$12.99; delivery fees can erase the advantage on an illustrated file. | Author. |
| **DRM on or off** | DRM-free allows EPUB/PDF downloads and fits CC0; DRM restricts them. Royalties are unchanged. | Author. |
| **KDP Select** | Public-domain content is ineligible; CC0 is nonexclusive. Enrollment is unlikely to be available. | Author. |
| **AI classification of the manuscript** | AI-generated text must be disclosed; AI-assisted text does not. The cover is already AI-generated. | Author. |
| **Part dividers and two-level TOC** | A 1,000-page book benefits from part navigation, but the manuscript has no part pages. | Editor and production. |
| **Image program** | 56 visuals are promised; they drive file size, cost, rights, alt text, and the missing-content risk. | Author, visual editor, rights. |
| **Print edition** | Separate trim, ISBN, wraparound cover, and KDP print workflow. | Author and production. |

---

## Appendix A. KDP quick reference

| Topic | Rule | Source |
|---|---|---|
| **Upload format** | EPUB 2 or 3; EPUB recommended for third-party tools. | S17, S18 |
| **Layout** | Reflowable for text-heavy books; fixed layout and Print Replica are fallbacks. | S1 §3 |
| **Package size** | 650 MB; 8,000 pages; fewer than 300 HTML files; each under 30 MB. | S1 §9, §11.4.2; S23 |
| **Cover** | 1,600 × 2,560 ideal; 1.6:1; 300 PPI; RGB; JPEG; ≤5 MB preferred; separate marketing upload; omit from the KDP manuscript and let KDP add it. | S1 §4; S2; S3; S24 |
| **Metadata** | `dc:title` and `dc:language` required; title/author/language must match KDP setup. | S1 §11.1; S7 |
| **Navigation** | HTML TOC near the front; NCX or `toc nav`; two levels maximum; no page numbers. | S1 §5; S6 |
| **Body text** | Defaults only; no forced font, size, line height, color, background, or justification. | S1 §11.3.2; S5 |
| **Images** | JPEG/PNG; RGB/sRGB; 300 PPI; 1,200 × 1,800 full page; 80% width for text-bearing images; alt text. | S1 §11.4; S4 |
| **Tables** | HTML, not images; under 100 rows and 11 columns; captions and headers; test at font size 3. | S1 §11.5; S16 |
| **Notes** | `aside` plus `epub:type="footnote"`; bidirectional links; end of chapter or book. | S1 §11.3.12; S5 |
| **Accessibility** | Language, headings, lists, table headers, alt text, contrast, ACE check. | S1 §8; S15 |
| **Validation** | Kindle Previewer 4; EPUBCheck is necessary but not sufficient. | S1 §2.2.1; S14 |
| **AI** | Disclose AI-generated text, images, translations; AI-assisted does not require disclosure. | S8 |
| **Public domain** | May require proof; 35% only; not KDP Select eligible; differentiation rules if a free store version exists. | S9, S10, S11 |
| **Royalty** | 35% or 70%; 70% band US$2.99–$12.99; US$0.15/MB delivery fee on the 70% option. | S11, S12 |
| **ISBN** | Not required for eBooks; ASIN assigned. | S20 |

---

## Appendix B. Cover specification comparison

| Specification | KDP ideal or rule | Current cover | Action |
|---|---|---|---|
| **Dimensions** | 1,600 × 2,560 px | 1,600 × 2,560 px | Matches. |
| **Aspect ratio** | At least 1.6:1 | 1.600:1 | Matches. |
| **Resolution** | 300 PPI recommended | 300 dpi | Matches. |
| **File size** | ≤5 MB preferred; 50 MB maximum; minimal compression recommended | Master 5.19 MB (100%); derivative 1.13 MB (80%) | Upload the master; both are under the 50 MB maximum. The derivative is the proof and strict 5 MB fallback. |
| **Format** | JPEG preferred; JPEG/PNG/GIF/TIFF accepted | JPEG | Keep JPEG. |
| **Color** | RGB; CMYK converted | RGB/sRGB | Keep RGB/sRGB. |
| **Content** | Title, author; no spine/back; no pricing; no watermarks | Title, subtitle, author; front only | Keep. |
| **Language** | Match the book | English | Keep. |
| **EPUB treatment** | Do not include the cover in the KDP manuscript; KDP adds the marketing cover | No cover in the KDP EPUB; derivative in the with-cover edition | Correct. Verify one cover in Previewer. |
| **AI** | Disclose AI-generated images | AI-generated with ChatGPT | Disclose in KDP. |

---

## Appendix C. File-size and royalty examples

The table in §12.1 is the working example. Two rules of thumb:

- At **35%**, delivery costs are not deducted. The 650 MB ceiling, download performance, and the file-size-based minimum list price are the constraints: under 3 MB, $0.99; 3 MB to under 10 MB, $1.99; 10 MB or more, $2.99. The current 2.11 MB EPUB keeps the $0.99 floor.
- At **70%**, every 10 MB of delivered file size costs about **US$1.50** in delivery on Amazon.com. On a US$12.99 book, the 70% option stops beating the 35% option at about **43 MB**; on a US$9.99 book, at about **33 MB**.

These are planning figures. KDP determines the delivered file size, applies VAT and territory rules, may price-match, and may recompress images. Use KDP’s royalty estimator after upload for the actual numbers.

---

## Sources

All web sources were consulted on **November 25, 2026**. The Kindle Publishing Guidelines PDF is version 2026.3.

| Key | Source | Used for |
|---|---|---|
| **S1** | Amazon, *Amazon Kindle Publishing Guidelines*, version 2026.3. [PDF](https://kindlegen.s3.amazonaws.com/AmazonKindlePublishingGuidelines.pdf). | Comprehensive rules for formats, covers, navigation, HTML/CSS, images, tables, notes, accessibility, QA, and package limits. Section numbers are cited in the text. |
| **S2** | Amazon KDP, “Cover Image Guidelines for Kindle eBooks.” [Page](https://kdp.amazon.com/en_US/help/topic/G6GTK3T3NUHKLEFX). | Marketing and internal cover requirements; 50 MB maximum; 1,600 × 2,560 recommendation; OPF methods; no duplicate HTML cover. The internal-cover section is generic Kindle guidance; S1 §4.2 says it does not apply to KDP eBooks. |
| **S3** | Amazon KDP, “What criteria does my eBook’s cover image need to meet?” [Page](https://kdp.amazon.com/help/topic/G200645690). | Cover dimensions, 1.6:1 ratio, 72 dpi table, 300 PPI recommendation, RGB, 50 MB limit, and the caution against compressing the marketing cover. |
| **S4** | Amazon KDP, “Image Guidelines — Reflowable.” [Page](https://kdp.amazon.com/help/topic/G75V4YX5X8GRGXWV). | Image formats, sRGB, 60%/80% width guidance, alt text, captions, figure markup, no text as images. |
| **S5** | Amazon KDP, “Text Guidelines — Reflowable.” [Page](https://kdp.amazon.com/en_US/help/topic/GH4DRT75GWWAGBTU). | Body defaults, paragraph formatting, margins, page breaks, fonts, page numbers, footnotes. |
| **S6** | Amazon KDP, “Navigation Guidelines.” [Page](https://kdp.amazon.com/en_US/help/topic/GY3AD8C6C6GAG42N). | HTML TOC, NCX/`toc nav`, two-level nesting, guide items. |
| **S7** | Amazon KDP, “Metadata Guidelines for Books.” [Page](https://kdp.amazon.com/help/topic/G201097560). | Title, subtitle, description, author, contributors, publisher, keywords, categories. |
| **S8** | Amazon KDP, “Content Guidelines.” [Page](https://kdp.amazon.com/en_US/help/topic/G200672390). | AI-generated versus AI-assisted disclosure; public-domain and poor-experience policies. |
| **S9** | Amazon KDP, “Publishing Public Domain Content.” [Page](https://kdp.amazon.com/help?topicId=G200743940). | Public-domain proof, differentiation rules, publishing-rights selection. |
| **S10** | Amazon KDP, “KDP Select Enrollment.” [Page](https://kdp.amazon.com/en_US/help/topic/GD9PMU58BV24QFZ7). | Exclusivity requirement; public-domain ineligibility. |
| **S11** | Amazon KDP, “Digital Book Pricing Page.” [Page](https://kdp.amazon.com/en_US/help/topic/G200634500). | 35%/70% royalty formulas; delivery costs at US$0.15/MB; public-domain 35% limitation. |
| **S12** | Amazon KDP, “eBook List Price Requirements.” [Page](https://kdp.amazon.com/help/topic/G200634560). | 70% price band US$2.99–$12.99 effective July 7, 2026; 35% minimum list price by file size: $0.99 under 3 MB, $1.99 from 3 to under 10 MB, $2.99 at 10 MB or more. |
| **S13** | Amazon KDP, “eBook Royalties.” [Page](https://kdp.amazon.com/help/topic/G200644210). | Royalty mechanics; public-domain 35% limitation. |
| **S14** | Amazon KDP, “Kindle Previewer.” [Page](https://kdp.amazon.com/help/topic/G202131170). | Previewer 4, supported platforms, EPUB support, Enhanced Typesetting check. |
| **S15** | Amazon KDP, “Accessibility for eBooks.” [Page](https://kdp.amazon.com/help/topic/GBPE3QVZ2J3HLQ4B). | Accessibility best practices for images, language, headings, tables, color; ACE recommendation. |
| **S16** | Amazon KDP, “Guide to Kindle Content Quality.” [Page](https://kdp.amazon.com/en_US/help/topic/G200952510). | Critical, destructive, and distracting issues; tables, images, links, notes, formatting, metadata. |
| **S17** | Amazon KDP, “What file formats are supported for eBook manuscripts?” [Page](https://kdp.amazon.com/en_US/help/topic/G200634390). | EPUB, DOCX, KPF, and MOBI status. |
| **S18** | Amazon KDP, “MOBI Support for eBooks Frequently Asked Questions.” [Page](https://kdp.amazon.com/help/topic/GULSQMHU5MNH4EZM). | EPUB 2/3 acceptance; end of MOBI support. |
| **S19** | Amazon KDP, “Digital Rights Management.” [Page](https://kdp.amazon.com/en_US/help/topic/GDDXGH9VR22ACM8U). | Optional DRM; DRM-free EPUB/PDF downloads; royalties unchanged. |
| **S20** | Amazon KDP, “Get an ISBN.” [Page](https://kdp.amazon.com/help/topic/GTJ8LBXL6Z4WV5QX). | No ISBN required for eBooks; ASIN. |
| **S21** | Amazon KDP, “Upload and Preview Book Content.” [Page](https://kdp.amazon.com/help/topic/G200641240). | KDP Online Previewer and upload workflow. |
| **S22** | Amazon KDP, “Attributes and Tags Supported by Enhanced Typesetting.” [Page](https://kdp.amazon.com/en_US/help/topic/GB5GDY7WAJDN9GFK). | Supported CSS/HTML values for Enhanced Typesetting. |
| **S23** | Amazon KDP, “Advanced Macintosh Techniques” (help page on reducing manuscript file size). [Page](https://kdp.amazon.com/help/topic/A1NXD7HGI9Q8K3). | 650 MB and 8,000-page outer limits. |
| **S24** | Amazon KDP, “eBook Manuscript Formatting Guide.” [Page](https://kdp.amazon.com/help/topic/G200645680). | Cover image: do not include it in the manuscript; KDP adds the marketing cover provided during title setup. |

**Note on conflicts.** The official sources disagree in places. The guidelines recommend a 5 MB marketing cover, while the cover upload criteria allow 50 MB. The guidelines contain a sentence saying Kindle does not support sRGB, while the current image page recommends sRGB and describes automatic CMYK conversion. The guidelines say the internal-cover guidance does not apply to KDP eBooks, while the KDP cover help page repeats the generic internal-cover requirement; the manuscript guide separately says not to put the cover in the manuscript. This document resolves the cover conflict in favor of the manuscript guide and the explicit KDP exclusion: omit the cover from the KDP manuscript, and include it in a separate wide-distribution EPUB. The cover criteria also list 72 dpi in one table and 300 PPI in another; treat 300 PPI as the quality target and 72 dpi as the floor. The cover criteria caution against compressing the marketing cover; the 80% build derivative is a project choice for proofs, the wide-distribution edition, and a strict 5 MB fallback, not a KDP requirement. In each case this document follows the stricter or more current operational rule and recommends verifying in Kindle Previewer. When KDP’s upload system and this summary disagree, the upload system controls.

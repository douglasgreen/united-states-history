# Cover production record

- **Master asset:** [`cover.jpg`](cover.jpg)
- **Dimensions:** 1600 × 2560 pixels, RGB JPEG
- **Aspect ratio:** 1.6:1
- **Embedded density:** 300 dpi
- **Quality:** 100 (the archival master)
- **SHA-256:** `ec8e29bf220a66eeb3264f2cc0e3678b6f6c9dde74d91629ef65d445a7b8ef67`
- **Generated:** November 24, 2026
- **Generator:** OpenAI ChatGPT image generation
- **Master file:** 1600 × 2560 JPEG at 300 dpi, 5,191,936 bytes (5.19 MB), prepared November 25, 2026, for the Amazon KDP cover specification

## Build derivative

`make cover` generates `build/images/cover.jpg` from the master. `make html`,
`make pdf`, and `make epub-with-cover` use it and will build it if missing:

- **Quality:** 80 (override with `make COVER_QUALITY=85 cover`)
- **Dimensions and density:** 1600 × 2560 pixels at 300 dpi, sRGB
- **Size:** about 1.13 MB (1,130,762 bytes in the current build)
- **Metadata:** stripped; no ICC, XMP, or editing history
- **Uses:** HTML and PDF proofs, the optional with-cover EPUB, and a strict
  5 MB fallback; the 100% master is the KDP marketing-cover upload
- **Not committed:** `build/` is disposable; regenerate it from the master

In a side-by-side crop at reading size, the 80% derivative retains sharp title
and subtitle text and is visually indistinguishable from the master. It is
well below KDP’s 5 MB guideline. The 100% master is retained because KDP’s
cover criteria ask authors to avoid compressing the marketing cover; it is
5.19 MB, still below the 50 MB hard limit.

## EPUB policy

The KDP EPUB (`make epub`) deliberately contains no cover image and no
`cover.xhtml`. KDP’s manuscript guide says not to include the cover in the
manuscript because KDP adds the marketing cover uploaded during title setup.
The optional `make epub-with-cover` target embeds the 80% derivative for
wide-distribution EPUB editions, where the retailer does not supply a cover.

## Prompt

> Front cover art, portrait 2:3, full bleed, editorial illustration with visible fabric texture. Overhead view of an enormous patchwork quilt filling the frame, abstractly evoking the American landscape without drawing a literal map. Patches in deep indigo, madder red, ochre, sage, dusty rose, and cream; some solid, some striped, some starry, some faintly printed with map contours, ledger rules, or newspaper columns. Along the lower edge, many hands of different skin tones, ages, and sleeves — work shirt, lace cuff, denim, leather glove — stitch, tug, and repair the quilt. One long seam is open, its raw edges and loose red thread visible. A cream fabric label is stitched near the top center. Warm raking light, tactile and serious, not cute. On the label: “A NATION IN QUESTION” in a bold high-contrast serif, two lines, dark ink. Below it on the label: “A History of the United States” in smaller italic serif. At the bottom, on a calm strip of quilt: “Douglas S. Green” in letterspaced small caps. No other text.

## Rights

The author records that OpenAI’s terms grant publication rights to the generated output. The book’s CC0 1.0 dedication covers its original text; the generated cover is used on the basis of the generator’s terms rather than the CC0 dedication.

## Production status

`produced`. The 1600 × 2560 master at 300 dpi meets the Amazon KDP marketing-cover dimensions and the 50 MB hard limit; it is the marketing-cover upload, since KDP asks for minimal compression. The 80% build derivative meets the 5 MB guideline and is the version used in proofs, the with-cover EPUB, and a strict 5 MB fallback. At a 6 × 9 inch trim the front image is about 267 pixels per inch; at 5.5 × 8.5 inches it is about 291 pixels per inch. A print edition also needs a full wraparound cover with spine and back at the selected trim. The cover is not an interior figure and does not enter the 500-word text-page measure.

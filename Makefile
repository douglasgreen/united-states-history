# A Nation in Question — Pandoc and WeasyPrint build entry points.
#
# The Markdown manuscript is the source of truth. Outputs are written to
# build/ and are not committed.
#
#   make check      structural checker (strict)
#   make epub       reflowable EPUB 3 for KDP, without a cover (KDP adds it)
#   make epub-with-cover  reflowable EPUB 3 with a cover for wide distribution
#   make epubcheck  EPUBCheck validation of the KDP EPUB
#   make epubcheck-with-cover  EPUBCheck validation of the wide-distribution EPUB
#   make cover      80% JPEG cover derivative for proofs and wide distribution
#   make pdf        US Letter proof PDF with the cover
#   make html       standalone browser proof with the cover
#   make clean      remove build/
#
# Requirements: pandoc, magick (ImageMagick 7), weasyprint, python3. The KDP
# EPUB deliberately omits the cover: KDP adds the marketing cover uploaded
# during title setup. The cover master stays at 100% quality in images/ for
# the KDP marketing upload; the build derivative is recompressed to
# COVER_QUALITY for local proofs, the with-cover edition, and a strict 5 MB
# fallback.

PANDOC ?= pandoc
MAGICK ?= magick
WEASYPRINT ?= weasyprint
PYTHON ?= python3
EPUBCHECK ?= epubcheck

BOOK := a-nation-in-question
BUILD := build
SOURCES := $(sort $(wildcard chapters/*.md))
METADATA := metadata.yaml
COVER := images/cover.jpg
COVER_QUALITY ?= 80
EPUB_CSS := styles/epub.css
HTML_CSS := styles/html.css
PDF_CSS := styles/pdf.css

PANDOC_FLAGS := --metadata-file=$(METADATA) --toc --toc-depth=1

.PHONY: all check epub epub-with-cover epubcheck epubcheck-with-cover cover pdf html clean

all: epub epubcheck pdf html

check:
	$(PYTHON) tools/check_book.py --strict

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/cover.html: tools/cover.html | $(BUILD)
	cp tools/cover.html $@

$(BUILD)/images/cover.jpg: $(COVER) | $(BUILD)
	mkdir -p $(BUILD)/images
	$(MAGICK) $(COVER) -colorspace sRGB -strip \
		-density 300 -units PixelsPerInch \
		-quality $(COVER_QUALITY) $@
	chmod 0644 $@

$(BUILD)/$(BOOK).epub: $(SOURCES) $(METADATA) $(EPUB_CSS) tools/epub-links.lua | $(BUILD)
	$(PANDOC) $(PANDOC_FLAGS) $(SOURCES) \
		--split-level=1 \
		--lua-filter=tools/epub-links.lua \
		--lua-filter=tools/dedupe-notes.lua \
		--css=$(EPUB_CSS) \
		--output=$@

$(BUILD)/$(BOOK)-with-cover.epub: $(SOURCES) $(METADATA) $(EPUB_CSS) $(BUILD)/images/cover.jpg tools/epub-links.lua | $(BUILD)
	$(PANDOC) $(PANDOC_FLAGS) $(SOURCES) \
		--split-level=1 \
		--lua-filter=tools/epub-links.lua \
		--lua-filter=tools/dedupe-notes.lua \
		--css=$(EPUB_CSS) \
		--epub-cover-image=$(BUILD)/images/cover.jpg \
		--output=$@

$(BUILD)/$(BOOK).html: $(SOURCES) $(METADATA) $(HTML_CSS) $(BUILD)/cover.html $(BUILD)/images/cover.jpg | $(BUILD)
	$(PANDOC) $(PANDOC_FLAGS) $(SOURCES) \
		--standalone \
		--lua-filter=tools/dedupe-notes.lua \
		--css=../$(HTML_CSS) \
		--include-before-body=$(BUILD)/cover.html \
		--output=$@

$(BUILD)/$(BOOK)-print.html: $(SOURCES) $(METADATA) $(PDF_CSS) $(BUILD)/cover.html $(BUILD)/images/cover.jpg tools/epub-links.lua | $(BUILD)
	$(PANDOC) $(PANDOC_FLAGS) $(SOURCES) \
		--standalone \
		--lua-filter=tools/epub-links.lua \
		--lua-filter=tools/dedupe-notes.lua \
		--css=../$(PDF_CSS) \
		--include-before-body=$(BUILD)/cover.html \
		--output=$@

$(BUILD)/$(BOOK).pdf: $(BUILD)/$(BOOK)-print.html $(PDF_CSS)
	$(WEASYPRINT) $(BUILD)/$(BOOK)-print.html $@

epub: $(BUILD)/$(BOOK).epub

epub-with-cover: $(BUILD)/$(BOOK)-with-cover.epub

epubcheck: $(BUILD)/$(BOOK).epub
	$(EPUBCHECK) $<

epubcheck-with-cover: $(BUILD)/$(BOOK)-with-cover.epub
	$(EPUBCHECK) $<

cover:
	$(MAKE) -B $(BUILD)/images/cover.jpg

pdf: $(BUILD)/$(BOOK).pdf
html: $(BUILD)/$(BOOK).html

clean:
	rm -rf $(BUILD)

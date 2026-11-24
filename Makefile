# A Nation in Question — Pandoc and WeasyPrint build entry points.
#
# The Markdown manuscript is the source of truth. Outputs are written to
# build/ and are not committed.
#
#   make check      structural checker (strict)
#   make epub       reflowable EPUB 3 with the cover
#   make epubcheck  EPUBCheck validation of the built EPUB
#   make pdf        US Letter proof PDF with the cover
#   make html       standalone browser proof with the cover
#   make clean      remove build/
#
# Requirements: pandoc, weasyprint, python3. The EPUB target uses Pandoc's
# --epub-cover-image flag; metadata.yaml also records the cover for other
# Pandoc writers and for production records.

PANDOC ?= pandoc
WEASYPRINT ?= weasyprint
PYTHON ?= python3
EPUBCHECK ?= epubcheck

BOOK := a-nation-in-question
BUILD := build
SOURCES := $(sort $(wildcard chapters/*.md))
METADATA := metadata.yaml
COVER := images/cover.jpg
EPUB_CSS := styles/epub.css
HTML_CSS := styles/html.css
PDF_CSS := styles/pdf.css

PANDOC_FLAGS := --metadata-file=$(METADATA) --toc --toc-depth=1

.PHONY: all check epub epubcheck pdf html clean

all: epub epubcheck pdf html

check:
	$(PYTHON) tools/check_book.py --strict

$(BUILD):
	mkdir -p $(BUILD)

$(BUILD)/cover.html: tools/cover.html | $(BUILD)
	cp tools/cover.html $@

$(BUILD)/images/cover.jpg: $(COVER) | $(BUILD)
	mkdir -p $(BUILD)/images
	cp $(COVER) $@

$(BUILD)/$(BOOK).epub: $(SOURCES) $(METADATA) $(EPUB_CSS) $(COVER) tools/epub-links.lua | $(BUILD)
	$(PANDOC) $(PANDOC_FLAGS) $(SOURCES) \
		--split-level=1 \
		--lua-filter=tools/epub-links.lua \
		--css=$(EPUB_CSS) \
		--epub-cover-image=$(COVER) \
		--output=$@

$(BUILD)/$(BOOK).html: $(SOURCES) $(METADATA) $(HTML_CSS) $(BUILD)/cover.html $(BUILD)/images/cover.jpg | $(BUILD)
	$(PANDOC) $(PANDOC_FLAGS) $(SOURCES) \
		--standalone \
		--css=../$(HTML_CSS) \
		--include-before-body=$(BUILD)/cover.html \
		--output=$@

$(BUILD)/$(BOOK)-print.html: $(SOURCES) $(METADATA) $(PDF_CSS) $(BUILD)/cover.html $(BUILD)/images/cover.jpg tools/epub-links.lua | $(BUILD)
	$(PANDOC) $(PANDOC_FLAGS) $(SOURCES) \
		--standalone \
		--lua-filter=tools/epub-links.lua \
		--css=../$(PDF_CSS) \
		--include-before-body=$(BUILD)/cover.html \
		--output=$@

$(BUILD)/$(BOOK).pdf: $(BUILD)/$(BOOK)-print.html $(PDF_CSS)
	$(WEASYPRINT) $(BUILD)/$(BOOK)-print.html $@

epub: $(BUILD)/$(BOOK).epub

epubcheck: $(BUILD)/$(BOOK).epub
	$(EPUBCHECK) $<

pdf: $(BUILD)/$(BOOK).pdf
html: $(BUILD)/$(BOOK).html

clean:
	rm -rf $(BUILD)

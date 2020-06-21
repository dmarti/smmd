LISTINGS = $(shell find domains -type f)

PAGES = $(KEYWORDS:%/index.md=%/index.html)

all : index.html

index.html : tools/make-table.py ${PAGES}
	tools/make-table.py > $@

domain/%/index.html : domain/%/index.md
	pandoc $< > $@

clean :
	rm -f index.html

.PHONY : all clean pristine

.PRECIOUS : data/github/% data/libraries/%

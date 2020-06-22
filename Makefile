LISTINGS = $(shell find domain -type f -name *.md)

# PAGES = $(LISTINGS:%/index.md=%/index.html)

# PAGES = $(shell find domain -type d | xargs -n 1 echo "$1/index.html")

PAGES = $(shell tools/list-pages.sh)

all : index.html

index.html : tools/make-table.py ${PAGES}
	tools/make-table.py > $@

domain/%/index.html : domain/%/index.md
	pandoc $< > $@

clean :
	rm -f index.html
	rm -f ${PAGES}

.PHONY : all clean pristine

.PRECIOUS : data/github/% data/libraries/%

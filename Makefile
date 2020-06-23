LISTINGS = $(shell find domain -type f -name *.md)

PAGES = $(shell tools/list-pages.sh)

all : index.html

index.html : Makefile tools/list-pages.sh tools/make-table.py ${PAGES}
	tools/make-table.py > $@

clean :
	rm -f index.html
	rm -f ${PAGES}

hooks : .git/hooks/pre-add

.git/hooks/% : Makefile
	echo "#!/bin/sh" > $@
	echo "make `basename $@`" >> $@
	chmod 755 $@

pre-push : all

.PHONY : all clean hooks deploy pre-push

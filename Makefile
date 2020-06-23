LISTINGS = $(shell find domain -type f -name *.md)

PAGES = $(shell tools/list-pages.sh)

all : index.html

index.html : tools/make-table.py ${PAGES}
	tools/make-table.py > $@

domain/%/index.html : domain/%/index.md
	pandoc $< > $@

clean :
	rm -f index.html
	rm -f ${PAGES}

deploy : all
	(git branch -D gh-pages || true) &> /dev/null
	rm -rf build && mkdir -p build
	cp -a Makefile .git index.html domain/*/*.html build
	make -C build gh-pages

gh-pages :
	basename `pwd` | grep -q build || exit 1
	rm -f .git/hooks/pre-push
	git checkout -b gh-pages
	git add -f Makefile domain/*/index.html
	git commit -m "this is a temporary branch, do not commit here."
	git push -f --set-upstream origin gh-pages

hooks : .git/hooks/pre-push

.git/hooks/% : Makefile
	echo "#!/bin/sh" > $@
	echo "make `basename $@`" >> $@
	chmod 755 $@

pre-push : deploy

.PHONY : all clean hooks deploy pre-push

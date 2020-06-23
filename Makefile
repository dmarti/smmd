LISTINGS = $(shell find domain -type f -name *.md)

all : index.html

index.html : Makefile tools/make-table.py ${LISTINGS}
	tools/make-table.py > $@

clean :
	rm -f index.html

hooks : .git/hooks/pre-add

.git/hooks/% : Makefile
	echo "#!/bin/sh" > $@
	echo "make `basename $@`" >> $@
	chmod 755 $@

pre-push : all

.PHONY : all clean hooks deploy pre-push

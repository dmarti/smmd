#! /usr/bin/bash

set -e

trap popd EXIT
pushd $PWD
cd $(dirname "$0")

DOMAIN=$1

if ! [ -e domain/$DOMAIN ]; then
	mkdir domain/$DOMAIN
	cp skel/* domain/$DOMAIN
fi

exec $EDITOR domain/$DOMAIN/index.md

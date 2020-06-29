#!/bin/bash

cleanup(){
        docker rm -f smmd-preview
        popd
}
trap 'cleanup' EXIT
pushd $PWD
cd $(dirname "$0")

docker build -t smmd-preview . 
docker rm -f smmd-preview
docker run --name smmd-preview \
	--volume "$(pwd)":/jekyll-site \
	-p 4000:4000 \
	smmd-preview

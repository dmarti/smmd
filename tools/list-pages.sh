#!/usr/bin/bash

find domain -type d -mindepth 1 | perl -ne 'chomp; print "$_/index.html\n"'


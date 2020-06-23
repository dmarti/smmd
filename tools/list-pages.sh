#!/usr/bin/bash

find domain -mindepth 1 -type d | perl -ne 'chomp; print "$_/index.html\n"'


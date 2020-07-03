#!/usr/bin/env python3

import json
import sys

import tldextract

from smEntry import ListEntry

with open(sys.argv[1]) as infile:
    data = json.load(infile)

for v in data['vendors']:
    policy = v['policyUrl']
    tld = tldextract.extract(policy)
    domain = '.'.join([tld.domain, tld.suffix])
    ent = ListEntry()
    ent['domain'] = domain
    ent['company-name'] = v['name']
    ent['list-name'] = "IAB Europe TCF"
    ent['list'] = 'iab-tcf'
    ent['list-data-url'] = 'https://vendorlist.consensu.org/vendorlist.json'
    ent['list-home'] = 'https://iabeurope.eu/transparency-consent-framework/'
    # print(v)
    ent.write_to_file('_list/%s/%s/index.md' % (ent['list'], ent['domain']))


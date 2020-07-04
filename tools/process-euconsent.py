#!/usr/bin/env python3

import json
import sys

import tldextract

from smEntry import Entry

with open(sys.argv[1]) as infile:
    data = json.load(infile)

for v in data['vendors']:
    policy = v['policyUrl']
    tld = tldextract.extract(policy)
    domain = '.'.join([tld.domain, tld.suffix])
    ent = Entry.from_file("domain/%s" % domain, True)
    ent['domain'] = domain
    if ent.get('company-name'):
        ent['iab-listing-name'] = v['name']
    else:
        ent['company-name'] = v['name']
    old_policy = ent.get('privacy-policy', policy).strip()
    if old_policy == policy:
        ent['privacy-policy'] = policy
    else:
        ent['iab-privacy-policy'] = policy
    if ent.get('company-name'):
        ent['iab-listing-name'] = v['name']
    else:
        ent['company-name'] = v['name']
    if not ent.get('home'):
        ent['home'] = "https://%s" % ent.domain
    print(v)
    ent.write_to_file('domain/%s/index.md' % ent.domain)


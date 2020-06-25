#!/usr/bin/env python3

from datetime import datetime
import os

def clean_key(k):
    k = k.strip()
    k = k.lower()
    k = k.replace('_', '-')
    k = k.replace(' ', '-')
    return k

class Entry(object):
    def __init__(self):
        self.data = {}

    @property
    def domain(self):
        return self.data.get('domain', "FIXME missing domain name")

    @property
    def name(self):
        return self.data.get('name', "FIXME missing company name")

    @property
    def home(self):
        homepage = self.data.get('home')
        if homepage:
            return homepage
        domain = self.data.get('homain')
        if domain:
            return "https://%s/" % domain
        return None

    def as_html(self):
        pagelink = '<a href="domain/%s">%s</a>' % (self.domain, self.name)
        homelink = '<a target="_blank" href="%s">%s</a>' % (self.home, self.domain)

        return "<tr><td>%s</td><td>%s</td></tr>" % (pagelink, homelink)

    def as_markdown(self):
        result = "---\n"
        for k in self.data.keys():
            if not "\n" in self.data[k]:
                result += "%s: %s\n" % (k, self.data[k])
        result += "---\n"
        for k in self.data.keys():
            if "\n" in self.data[k]:
                result += "## %s\n" % k
                result += self.data[k]
        return result

    @classmethod
    def from_file(cls, pathname):
        try:
            with open(pathname) as mdfile:
                ent = cls()
                in_section = None
                for line in mdfile.readlines():
                    if line.startswith('## '):
                        in_section = line[3:]
                        ent.data[in_section] = ''
                        continue
                    if in_section:
                        ent.data[in_section] += line
                        continue
                    try:
                        (key, value) = line.split(':')
                        key = clean_key(key)
                        ent.data[key] = value.strip()
                        in_section = None
                    except ValueError:
                        pass
            return(ent)
        except IsADirectoryError:
            return cls.from_file(os.path.join(pathname, 'index.md'))
        except:
            raise


#!/usr/bin/env python3

import os
import sys
import tempfile

def spew_file(pathname, content):
    os.makedirs(os.path.split(pathname)[0], exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=os.path.dirname(pathname), mode='w+',
                                     delete=False, encoding='utf-8') as scratch:
        scratch.write(content)
    os.replace(scratch.name, pathname)

class ListEntry(dict):
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __getitem__(self, key):
        val = dict.__getitem__(self, key)
        return val

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    def get(self, key, default=None):
        try:
            return self[key]
        except:
            return default

    def as_markdown(self):
        result = "---\n"
        result += "category: list-entry\n"
        result += "layout: list-entry\n"
        for k in sorted(self.keys()):
            val = self[k]
            if ' ' in val:
                val = '"%s"' % self[k]
            result += "%s: %s\n" % (k, val)
        result += "---\n"
        result += "\nThis is an automatically generated list entry.\n"
        return result

    def write_to_file(self, pathname):
        spew_file(pathname, self.as_markdown())


class Entry(dict):
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)
        self.body = ''
        self.pathname = None

    def __getitem__(self, key):
        val = dict.__getitem__(self, key)
        if 'home' == key and not 'http' in val:
            val = val.strip()
            val = " https://%s\n" % val
        return val

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)

    def update(self, *args, **kwargs):
        for k, v in dict(*args, **kwargs).items():
            self[k] = v

    @property
    def domain(self):
        return self['domain'].strip()

    def get(self, key, default=None):
        try:
            return self[key]
        except:
            return default

    def as_markdown(self):
        for k in ('domain',  'company-name', 'home', 'email', 'ccpa-email', 
                  'privacy-policy', 'opt-out-url', 'owned-by',
                  'california-date', 'vermont-id'):
            self[k] = self.get(k, '')
        result = "---\n"
        for k in sorted(self.keys()):
            if ' ' in self[k].strip() and not '"' in self[k]:
                self[k] = self[k].strip()
                self[k] = '"%s"' % self[k]
            spacer = ''
            if not self[k].startswith(' '):
                spacer = ' '
            result += '%s:%s%s' % (k, spacer, self[k])
            if not self[k].endswith("\n"):
                result += "\n"
        result += "---\n"
        result += self.body
        return result

    def write_to_file(self, pathname=None):
        if not pathname:
            pathname = self.pathname
        spew_file(pathname, self.as_markdown())

    @classmethod
    def from_file(cls, pathname, make_new=False):
        try:
            with open(pathname) as mdfile:
                ent = cls()
                ent.pathname = pathname
                in_head = False
                current_key = None
                for line in mdfile.readlines():
                    if line.startswith('---'):
                        in_head = not in_head
                        continue
                    if not in_head:
                        ent.body += line
                        continue
                    if current_key and line.startswith(' '):
                        ent[current_key] += line
                        continue
                    try:
                        (key, value) = line.split(':', 1)
                        ent[key] = value
                        current_key = key
                    except ValueError:
                        raise
            return(ent)
        except IsADirectoryError:
            return cls.from_file(os.path.join(pathname, 'index.md'))
        except:
            if make_new:
                tmp = cls()
                tmp.pathname = pathname
                return tmp
            raise

    @classmethod
    def exists(cls, domain):
        datadir = os.path.normpath(os.path.join(__file__, '../../domain'))
        pathname = os.path.join(datadir, domain, 'index.md')
        return os.path.isfile(pathname)

    @classmethod
    def lookup(cls, domain):
        datadir = os.path.normpath(os.path.join(__file__, '../../domain'))
        pathname = os.path.join(datadir, domain, 'index.md')
        return cls.from_file(pathname, True)



if __name__ =='__main__':
    for f in sys.argv[1:]:
        print(Entry().from_file(f).as_markdown())
        


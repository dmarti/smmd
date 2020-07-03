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


class Entry(dict):
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)
        self.body = ''

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

    def write_to_file(self, pathname):
        spew_file(pathname, self.as_markdown())

    @classmethod
    def from_file(cls, pathname, make_new=False):
        try:
            with open(pathname) as mdfile:
                ent = cls()
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
                return cls()
            raise

if __name__ =='__main__':
    for f in sys.argv[1:]:
        print(Entry().from_file(f).as_markdown())
        

#!/usr/bin/env python3

from datetime import datetime
import os

tablestyle = '''
* {
  font-family: sans-serif;
}
table {
  border: 1px solid #1C6EA4;
  background-color: #EEEEEE;
  text-align: left;
  border-collapse: collapse;
}
table td, table.s th {
  border: 1px solid #AAAAAA;
  padding: 3px 2px;
  vertical-align: bottom;
}
th {
  vertical-align: bottom;
}
table tr:nth-child(even) {
  background: #D0E4F5;
}
table thead {
  background: #1C6EA4;
  background: -moz-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: -webkit-linear-gradient(top, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  background: linear-gradient(to bottom, #5592bb 0%, #327cad 66%, #1C6EA4 100%);
  border-bottom: 2px solid #444444;
}
table thead th {
  font-weight: bold;
  color: #FFFFFF;
  border-left: 2px solid #D0E4F5;
}
table thead th:first-child {
  border-left: none;
}

table tfoot {
  font-weight: bold;
  color: #FFFFFF;
  background: #D0E4F5;
  background: -moz-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: -webkit-linear-gradient(top, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  background: linear-gradient(to bottom, #dcebf7 0%, #d4e6f6 66%, #D0E4F5 100%);
  border-top: 2px solid #444444;
}
table tfoot .links {
  text-align: right;
}
table tfoot .links a{
  display: inline-block;
  background: #1C6EA4;
  color: #FFFFFF;
  padding: 2px 8px;
  border-radius: 5px;
}

th  {
    padding-left: 1em;
    padding-right: 1em;
}

table.sortable th:not(.sorttable_sorted):not(.sorttable_sorted_reverse):not(.sorttable_nosort):after {
    content: "▴▾"
}
'''

class Entry(object):
    def __init__(self):
        self.data = {}

    @property
    def domain(self):
        return self.data.get('Domain', "FIXME missing domain name")

    @property
    def name(self):
        return self.data.get('Name', "FIXME missing company name")

    @property
    def home(self):
        homepage = self.data.get('Home')
        if homepage:
            return homepage
        domain = self.data.get('Domain')
        if domain:
            return "https://%s/" % domain
        return None

    def as_html(self):
        pagelink = '<a href="domain/%s">%s</a>' % (self.domain, self.name)
        homelink = '<a target="_blank" href="%s">%s</a>' % (self.home, self.domain)

        return "<tr><td>%s</td><td>%s</td></tr>" % (pagelink, homelink)

    def as_markdown(self):
        result = ''
        for k in self.data.keys():
            result += "%s: %s" % (k, self.data[k])
        result += str(self.data)
        return result

if __name__ == '__main__':
    entries = []
    for root, dirs, files, rootfd in os.fwalk('domain'):
        domaindir = root
        if 'domain' == domaindir:
            continue
        try:
            with open("%s/index.md" % domaindir) as mdfile:
                ent = Entry()
                in_section = None
                for line in mdfile.readlines():
                    if line.startswith('## '):
                        in_section = line[3:]
                        ent.data[in_section] = ''
                    if in_section:
                        ent.data[in_section] += line
                        continue
                    try:
                        (key, value) = line.split(':')
                        ent.data[key] = value.strip()
                        in_section = None
                    except ValueError:
                        pass
                entries.append(ent)
        except:
            raise

    print('<html><head><title>Results</title><style type="text/css">')
    print(tablestyle)
    print('</style>')
    print('<script src="sorttable.js"></script>')
    print('</head><body><table class="sortable">')
    print('<tr><th>Company</th><th>Company home page</th>')

    for e in entries:
        print(e.as_html())
    print('</table></html>')


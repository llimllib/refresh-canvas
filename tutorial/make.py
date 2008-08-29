#!/usr/bin/env python
from glob import glob
from mako.template import Template
from mako.lookup import TemplateLookup

for f in glob("*.mak"):
    base = f[:f.find(".mak")]
    file(base + '.html', 'w').write(
        Template(filename=f,
                 lookup=TemplateLookup(directories=['.'])).render())

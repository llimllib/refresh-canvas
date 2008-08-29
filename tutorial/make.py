#!/usr/bin/env python
from mako.template import Template
from mako.lookup import TemplateLookup

file('tutorial.html', 'w').write(
    Template(filename="template.mak",
             lookup=TemplateLookup(directories=['.'])).render())

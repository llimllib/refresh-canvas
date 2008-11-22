#!/usr/bin/env python
from glob import glob
from mako.template import Template
from mako.lookup import TemplateLookup

pages = eval(file("data.py").read())

def required(page, required_vars):
    for var in required_vars: page[var] = page.get(var, "")

toc = [(page["title"], page["name"]+".html") for page in pages]

for i, page in enumerate(pages):
    page["prev"] = pages[i-1]["name"] if i > 0 else ""
    page["next"] = pages[i+1]["name"] if i+1 < len(pages) else ""
    page["toc"]  = toc

    required(page, ["code", "explain_before", "explain_after", "title"])
    file(page['name'] + '.html', 'w').write(
        Template(filename="templates/template.mak",
                 lookup=TemplateLookup(directories=['.'])).render(**page))

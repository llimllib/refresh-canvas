#!/usr/bin/env python
from glob import glob
from mako.template import Template
from mako.lookup import TemplateLookup
from sys import argv
from os import unlink
from os.path import join, isdir
from shutil import copytree, rmtree
from subprocess import Popen, PIPE

def clean():
    for f in glob("*.html"): unlink(f)

def build():
    pages = eval(file("data.py").read())

    def required(page, required_vars):
        for var in required_vars: page[var] = page.get(var, "")

    toc = [(page["title"], page["name"]+".html") for page in pages]

    for i, page in enumerate(pages):
        page["prev"] = pages[i-1]["name"] if i > 0 else ""
        page["next"] = pages[i+1]["name"] if i+1 < len(pages) else ""
        page["toc"]  = toc

        required(page, ["code", "explain_before", "explain_after", "title", "hidden_code",
                        "library"])
        file(join("build", page['name'] + '.html'), 'w').write(
            Template(filename="templates/template.mak",
                     lookup=TemplateLookup(directories=['.'])).render(**page))

    if isdir("build/js"):
        rmtree("build/js")
    copytree("js", "build/js")

def deploy():
    print "deploying"
    for f in ['build/*.html', 'js']:
        cmd = "rsync -avuz -e ssh %s llimllib@billmill.org:~/static/canvastutorial" % f
        p = Popen(cmd, shell=True, stderr=PIPE)

if __name__ == "__main__":
    clean()
    build()
    if argv[-1].lower() == "deploy":
        deploy()

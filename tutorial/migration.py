from os import mkdir, path
OUTDIR = 'chapters'

if __name__ == "__main__":
    if not path.isdir(OUTDIR):
        mkdir(OUTDIR)

    pages = eval(file("data.py").read())
    for i, page in enumerate(pages):
        # indent the multiline params
        out = ["order: %d" % i]
        for k, v  in page.items():
            lines = v.split("\n")
            # handle multilines better
            if len(lines) == 1:
                out.append ("%s: '%s'" % (k,v))
            else:
                out.append("%s: |\n  %s" % (k, "\n  ".join(lines)))
        file(path.join(OUTDIR, page['name']+'.yaml'), "w").write("\n\n".join(out))

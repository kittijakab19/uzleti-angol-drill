# -*- coding: utf-8 -*-
"""A page-source.html-bol keszit teljes HTML dokumentumot:
   index.html          -> kulso data.js-sel (a helyi szerverhez)
   uzleti-angol-drill.html -> mindent egybe agyazva (duplakattintasra is megy)"""
import io, os
page = io.open('page-source.html', encoding='utf-8').read()
head_extra, rest = page.split('<style>', 1)
rest = '<style>' + rest

def doc(body):
    return ('<!DOCTYPE html>\n<html lang="hu">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            '<meta name="robots" content="noindex, nofollow, noarchive, nosnippet">\n'
            '<meta name="googlebot" content="noindex, nofollow">\n'
            '<style>html{color-scheme:light dark}img{max-width:100%}[hidden]{display:none!important}</style>\n'
            + head_extra + '</head>\n<body>\n' + body + '\n</body>\n</html>\n')

io.open('index.html', 'w', encoding='utf-8').write(doc(rest))
data = io.open('data.js', encoding='utf-8').read().replace('</script', '<\\/script')
io.open('uzleti-angol-drill.html', 'w', encoding='utf-8').write(
    doc(rest.replace('<script src="data.js" charset="utf-8"></script>', '<script>\n' + data + '\n</script>')))
for f in ('index.html', 'uzleti-angol-drill.html'):
    print(f, os.path.getsize(f), 'bytes')

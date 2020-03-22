# -*- coding: utf-8 -*-
import json
import sys


with open(sys.argv[1], 'r', encoding="utf-8") as f:
    file_name = sys.argv[1].split(".")[0]
    content = f.read()

data = json.loads(content)

content = """<style>
 .randomize > * {display: none;}
 .randomize > *:nth-child(2) {display: block;}
</style>
"""

content += '\n<div class="randomize">'

for poetry in data:
    poetry_content = '\n<div class="poetry">\n'
    is_first = True

    poetry_content += '<div class="poetry-title">' + poetry["title"].split("/")[0] + "</div>" + "\n"
    poetry_content += '<div class="poetry-author">' + poetry["author"] + "</div>" + "\n"
    poetry_content += '<div class="poetry-cotent">\n'

    for p in poetry["paragraphs"]:
        if len(p) <= 0:
            pass
        elif "序" in p:
            pass
        else:
            poetry_content += "<p>" + p + "</p>" + "\n"

    content += poetry_content + "</div>\n" + "</div>"

content += "\n</div>"

with open(f'{file_name}.html', 'w', encoding="utf-8") as f:
    f.write(content)

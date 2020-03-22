import re
from bs4 import BeautifulSoup

soup = BeautifulSoup(open("random_old_saying.html", 'rb'), "html.parser")

li_list = soup.findAll("li")
content = ""

for li in li_list:
    li_content = "\n<li>\n"
    is_first = True
    for line in li.text.splitlines():
        if re.match(r'^\s*$', line):
            pass
        elif "相关博文" in line:
            pass
        else:
            if is_first:
                li_content += line.lstrip() + "\n"
                is_first = False
            else:
                li_content += "<br/> " + line.lstrip() + "\n"

    li_content += "</li>"
    content += li_content

with open("temp.html", "w") as h:
    h.write(content)

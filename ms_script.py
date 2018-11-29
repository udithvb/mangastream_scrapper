from bs4 import BeautifulSoup
import requests
import urllib
import os
url = "https://readms.net/r/the_seven_deadly_sins/291/5503/1"


source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")
title = "_".join(soup.html.title.text[:-15].split(" "))
os.mkdir(title)
os.chdir(os.path.join(os.getcwd(),title))


def get_image_url(soup_obj, index):
    img_link = soup_obj.find("img")
    img_txt = img_link.__str__()
    txt = img_txt.split(" ")[2]
    txt = txt[5:-3]
    format_code = "{:03d}".format(i)
    urllib.request.urlretrieve(f"http:{txt}",format_code)

def find_next_link(soup_obj):
    nxt_link = soup_obj.findAll("a")
    for link in nxt_link:
        link = str(link)
        if "→" in link:
            yes = link
            break
        else:
            pass

    yes = yes.split("\"")
    return f"http://readms.net{yes[1]}"


def find_pages(soup_obj):

    dropdown = soup.findAll("li")

    for link in dropdown:
        if "Last" in str(link):
            gotit = link
            break
        else:
            pass
    return gotit.text[-3:-1]


pages = int(find_pages(soup))
for i in range(pages):
    source = requests.get(url).text
    soup = BeautifulSoup(source,"lxml")
    get_image_url(soup,i)
    url = find_next_link(soup)

print(f"Done, saved in {os.getcwd()}")
#os.rmdir(title)
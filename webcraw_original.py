import urllib.request
import pandas as pd
title = []
date = []
url = []
author = []
article = []
p = 0

def get_title(n):
    splittitle = titleurlFind[n].index("</a>")
    title.append(titleurlFind[n][:splittitle])
def get_date(n):
    splitdate = dateFind[n].index("</span>")
    date.append(dateFind[n][28:splitdate])
def get_author(n):
    splitauth = authorFind[n].index("</a>")
    author.append(authorFind[n][:splitauth])
def get_link(n):
    spliturl = titleurlFind[n-1].index("class=\"entry-title\"><a href=\"")
    url.append(titleurlFind[n-1][spliturl+29:titleurlFind[n-1].find(title[-1])-9])
def get_article():
    arti = []
    artistr = str()
    page = urllib.request.urlopen(url[-1])
    text = page.read().decode("utf8")
    rem = text.find("<span id=\"more")
    rem2= text.find("</div><br /><br />")
    text = text.replace(text[rem:rem2+18],"")
    articleFind = text.split("<p>")
    i = 0
    for line in articleFind[1:-3]:
        i = i + 1
        articleall = articleFind[i].index("</p>")
        arti.append(articleFind[i][:articleall])
        artistr = artistr + arti[-1] + "\n\n"
    article.append(artistr)

while p != 3:
    p = p + 1
    cate = 'cutting-edge/ai'
    page = urllib.request.urlopen("https://technews.tw/category/%s/page/%d"%(cate, p))
    text = page.read().decode("utf8")
    titleurlFind = text.split("bookmark\">")
    authorFind = text.split("author\">")
    dateFind = text.split("發布日期</span>")
    n = 0
    for line in dateFind[1:]:
        n = n + 1
        get_title(n)
        get_date(n)
        get_author(n)
        get_link(n)
        get_article()
AI_dict = {
        "Title":title,
        "Author":author,
        "Date":date,
        "Link":url,
        "Article":article
        }
AI_df = pd.DataFrame(AI_dict)
#AI_df.to_csv("web_crawler.csv",index = False)
AI_df.to_excel("web_crawler.xlsx",index = False)
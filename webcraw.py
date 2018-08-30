import urllib.request
import pandas as pd
'''Main feature:\n
    Easy to grab your web info, and have some module to hadle what you want yo do.\n
    
    '''

class Technews:
    '''In this case, default website is \"https://technews.tw/category/celebrity/\".'''
    def option(self, title, date, link, author, article):
        '''This place are  Temporary storage of all options'''
        self.title = title
        self.date = date
        self.link = link
        self.author = author
        self.article = article
        
    def reset(self, n = 1):
        '''Set all option empty. If you want to grab Info that you have to 
        run this def'''
        self.option([],[],[],[],[])

    def page_set(self, url = 'https://technews.tw/category/celebrity/', cate = '', page = 1):
        '''You have set your web, includind url, category, page.
        In this case, default website is \"https://technews.tw/category/celebrity/\".'''
        self.cate = cate
        if cate != '':
            url = url.replace(url[url.find('category/')+9:], cate)
        if page != 1:
            url = url + '/page/'
            url = url.replace(url[url.find('/page/'):], '')
            url = url + '/page/%d'%(page)
        page = urllib.request.urlopen(url)
        self.url = url
        self.text = page.read().decode("utf8")
        

    def main(self, n):
        self.titleFind(n)
        self.dateFind(n)
        self.authorFind(n)
        self.linkFind(n)
        self.articleFind()
        
    def whole_page(self):
        '''To grab your whole current page. '''
        n = 1
        split = self.text.split("發布日期</span>")
        for lin in split[1:]:
            self.main(n)
            n = n + 1
            
    def start_until(self, start = 1, end = 1):
        ''''If you want to grab several page, you can set start and end pages.'''
        self.whole_page()
        while start != end:
            start = start + 1
            self.page_set(self.url, self.cate, page = start)
            self.whole_page()
    def web_df(self):
        AI_dict = {
                "Title":self.title,
                "Author":self.author,
                "Date":self.date,
                "Link":self.link,
                "Article":self.article
        }
        
        df = pd.DataFrame(AI_dict)
        self.df = df
            
    def titleFind(self, n):
        split = self.text.split("bookmark\">")
        find = split[n].index("</a>")
        title = self.title.append(split[n][:find])
        return(title)
    
    def authorFind(self, n):
        split = self.text.split("author\">")
        find = split[n].index("</a>")
        author = self.author.append(split[n][:find])
        return(author)
    
    def dateFind(self, n):
        split = self.text.split("發布日期</span>")
        find = split[n].index("</span>")
        date = self.date.append(split[n][28:find])
        return(date)
        
    def linkFind(self, n):
        split = self.text.split("bookmark\">")
        find = split[n-1].index("class=\"entry-title\"><a href=\"")
        link = self.link.append(split[n-1][find+29:split[n-1].find(self.title[-1])-9])
        return(link)
    
    def articleFind(self):
        arti = []
        artistr = str()
        page = urllib.request.urlopen(self.link[-1])
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
        article = self.article.append(artistr)
        return(article)


class Digitimes:
        
    def option(self, title, date, link, author, article):
        '''This place are  Temporary storage of all options'''
        self.title = title
        self.date = date
        self.link = link
        self.author = author
        self.article = article
        
    def reset(self, n = 1):
        '''Set all option empty. If you want to grab Info that you have to 
        run this def'''
        self.option([],[],[],[],[])

    def page_set(self, url = 'https://www.digitimes.com.tw/iot/channel_10.asp?cat2=10', cate = '', page = 1):
        '''You have set your web, includind url, category, page.
        In this case, default website is \"https://technews.tw/category/celebrity/\".'''
        
        if cate == '工業4.0':
            cate = 'iot/channel_10.asp?cat2=10'
        
        if cate == '車聯網':
            cate ='iot/channel_30.asp?cat2=30'
        
        if cate == '智慧醫療':
            cate = 'iot/channel_70.asp?cat2=70'
            
        if cate == '智慧城市':
            cate = 'iot/channel_80.asp?cat2=80'
            
        if cate == 'AI/軟體':
            cate = 'iot/channel_100.asp?cat2=100'
            
        if cate == '嵌入式平台':
            cate = 'iot/channel_85.asp?cat2=85'
            

        self.cate = cate
        if cate != '':
            url = url.replace(url[url.find('iot/'):], cate)
        if page != 1:
            url = url + '/page/'
            url = url.replace(url[url.find('/page/'):], '')
            url = url + '/page/%d'%(page)
        page = urllib.request.urlopen(url)
        self.url = url
        self.text = page.read().decode("utf8")

    def main(self, n):
        self.titleFind(n)
        self.dateFind(n)
        self.authorFind(n)
        self.linkFind(n)
        self.articleFind()
        
    def whole_page(self):
        '''To grab your whole current page. '''
        n = 1
        split = self.text.split("發布日期</span>")
        for lin in split[1:]:
            self.main(n)
            n = n + 1
            
    def start_until(self, start = 1, end = 1):
        ''''If you want to grab several page, you can set start and end pages.'''
        self.whole_page()
        while start != end:
            start = start + 1
            self.page_set(self.url, self.cate, page = start)
            self.whole_page()
    def web_df(self):
        AI_dict = {
                "Title":self.title,
                "Author":self.author,
                "Date":self.date,
                "Link":self.link,
                "Article":self.article
        }
        
        df = pd.DataFrame(AI_dict)
        self.df = df
            
    def titleFind(self, n):
        split = self.text.split("bookmark\">")
        find = split[n].index("</a>")
        title = self.title.append(split[n][:find])
        return(title)
    
    def authorFind(self, n):
        split = self.text.split("author\">")
        find = split[n].index("</a>")
        author = self.author.append(split[n][:find])
        return(author)
    
    def dateFind(self, n):
        split = self.text.split("發布日期</span>")
        find = split[n].index("</span>")
        date = self.date.append(split[n][28:find])
        return(date)
        
    def linkFind(self, n):
        split = self.text.split("bookmark\">")
        find = split[n-1].index("class=\"entry-title\"><a href=\"")
        link = self.link.append(split[n-1][find+29:split[n-1].find(self.title[-1])-9])
        return(link)
    
    def articleFind(self):
        arti = []
        artistr = str()
        page = urllib.request.urlopen(self.link[-1])
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
        article = self.article.append(artistr)
        return(article)

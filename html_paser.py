# coding:utf-8
import re
from bs4 import BeautifulSoup
import urllib.parse
class HtmlParser(object):
     def parse(self,page_url,html_content,html_encode="utf-8"):
      if page_url is None or html_content is None:
        return
      soup=BeautifulSoup(html_content,"html.parser",from_encoding=html_encode)
      new_urls=self._get_newurls(page_url,soup)

      new_data=self._get_newdata(page_url,soup)

      return new_urls,new_data

     def _get_newurls(self,page_url,soup):
        new_urls = set()
        links=soup.find_all("a",href=re.compile(r"/item/\w"))
        for link in links:
            new_path=link['href']
            new_url=urllib.parse.urljoin(page_url,new_path)
            new_urls.add(new_url)
        return new_urls

     def _get_newdata(self,page_url,soup):
      data={"url":page_url}
      title_node=soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
      data["title"]=title_node.get_text()
      summary_node = soup.find("div", class_="lemma-summary")
      data["summary"] = summary_node.get_text()
      return data

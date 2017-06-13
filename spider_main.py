# coding:utf-8
from Baikespider import  html_downloader,html_output,html_paser,url_manager
class SpiderMain(object):
 def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownLoader()
        self.parser = html_paser.HtmlParser()
        self.out_put = html_output.HtmlOutput()


 def craw(self,root_url):
     self.urls.add_new_url(root_url)
     count = 1;
     while self.urls.has_new_new_url():
         try:
          new_url=self.urls.get_new_url()
          print("craw %d : %s" % (count, new_url))
          html_content=self.downloader.download(new_url)
          new_urls,new_data=self.parser.parse(new_url,html_content)
          self.urls.add_new_urls(new_urls)
          self.out_put.collect_data(new_data)
          if count>=5:
               break
          count=count+1
         except Exception as e:
          print("craw failed!\n" + str(e))
     self.out_put.out_html()



if __name__=="__main__":
      rootUrl = "http://baike.baidu.com/item/Android"
      object=SpiderMain();
      object.craw(rootUrl);


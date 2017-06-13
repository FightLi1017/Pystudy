# coding:utf-8

import time

class HtmlOutput(object):
     def __init__(self):
          self.datas = []

     def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

     def out_html(self):
          for data in  self.datas:
           print("地址连接 %s   , 标题%s   , \n内容%s" % (data['url'],data['title'],data['summary']))

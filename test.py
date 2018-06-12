# -*- coding:utf-8 -*-

import urllib
from urllib import request
import re




if __name__ == "__main__":
    url = "http://www.qiushibaike.com/hot/page/1"
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    request = request.Request(url,headers = headers)

    try:
        response = urllib.request.urlopen(request)
        content = response.read().decode('UTF-8')
        #print(content)
    except urllib.request.URLError as e:
        if hasattr(e,'code'):
            print(e.code())
        if hasattr(e,'reason'):
            print(e.reason())

    pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>',re.S)
    items = re.findall(pattern,content)
    for item in items:
        author = "作者：" + item[0].replace("\n","")
        likenum_int = "点赞数：" + item[2]
        joke_content = item[1].replace("\n","").replace('<br/>',"\n")+"\n\n"
        print(author + "\n" + likenum_int + "\n"  + joke_content)
        #print(item[0].replace("\n","") + ":\n" + item[1].replace("\n","").replace('<br/>',"\n")+"\n")

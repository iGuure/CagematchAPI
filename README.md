Scrapy pratice
==============
Here are some web crawler projects using Scrapy. In addition, notes while learning web crawling and Scrapy are also included.

Requirements
------------
+ Python 2.7
    - [Scrapy](http://scrapy.org "Scrapy official website") 1.0.3
+ Works on Linux, Windows, Mac OSX, BSD

Douban Movie Top250
-------------------
For generating an `items.json` file containing all scrapy items, serialized in JSON, you can use the following command:

    scrapy crawl doubanmovietop250 -o items.json

Then, run `output.py` for decoding purpose in order to gain the exact result.

Notes while learing
-------------------
#### 1.UnicodeEncodeError-"GBK" related for Windows
It's because the content you've crawled and the terminal you're using(cmd) are using different character encoding forms. Usually cmd uses cp936(similar to GBK) as default.

My solution: Use Linux instead :)

##### For further reading: 
+ [【整理】Python中遇到"UnicodeDecodeError: ‘gbk’ codec can’t decode bytes in position 2-3: illegal multibyte sequence"之类的编码或解码的错误时如何处理](http://www.tuicool.com/articles/nEjiEv)
+ [网络爬虫的乱码处理](http://blog.csdn.net/preterhuman_peak/article/details/42420515)

#### 2.UnicodeEncodeError-"ASCII" related
The default encoding of Python is ASCII, which you can use the following command to check out:
    
    import sys
    print sys.getdefaultencoding()
    # 'ascii'

On the other hand, our data are usually encoded in Unicode or UTF-8. As a result, when the character stream no longer belongs to ASCII, it will throw out an exception.

My solution: Use the following command:

    import sys
    reload(sys)
    sys.setdefaultencoding('utf-8')

##### For further reading: 
+ [解决Python2.7的UnicodeEncodeError: ‘ascii’ codec can’t encode异常错误](http://wangye.org/blog/archives/629/)
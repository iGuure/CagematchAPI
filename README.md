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
For generating an `items.json` file containing all Scrapy items, serialized in JSON, you can use the following command:

    scrapy crawl doubanmovietop250 -o items.json

Then, run `output.py` for decoding purpose in order to gain the exact result.

Pro Wrestling
-------------
For personal mania.
##### The following objects are currently included:
+ WWE Photos

    For crawling all kinds of WWE photos(PPV, RAW, superstar, etc) and transform them into a format that can be post on a Discuz! forum. Remember to add url to your command:

        `scrapy crawl wwephotos -a [url] -o items.json`
        
    and don't forget to run `output.py>yourFile.txt` for transformation and output.

+ TNA Photos

    For crawling photos of TNA wrestlers(roster and alumni). You will get a list of urls of those photos and their corresponding wrestlers' name.

+ Cagematch

    For crawling many interesting stats from the biggest CAGE in the world -- cagematch.net. Currently, you can get the list of Top 250 wrestlers via CagematchAPI. More stats crawling will be added soon.

pixiv
-----
TBC

Notes while learning
--------------------
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

#### 3."restrict_xpaths" doesn't work
Maybe you have override the `parse` function when using a `CrawlSpider` as it is stated in the docs.

My solution: Use another name instead of `parse` for the callback function.

##### For further reading: 
+ [Scrapy rule doesn't work with 'restrict_xpaths'](http://stackoverflow.com/questions/32709245/scrapy-rule-doesnt-work-with-restrict-xpaths)
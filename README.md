# Selenium

## 參考文章
### [selenium github](https://github.com/SeleniumHQ/selenium)
### [官方舊文檔](https://docs.seleniumhq.org/docs/)
### [Selenium with Python 非官方使用手冊](https://selenium-python.readthedocs.io/index.html)
### [官方 API documentation](https://seleniumhq.github.io/selenium/docs/api/py/)
    * 有selenium的安裝，和各瀏覽器driver的載點，和基礎範例
    * 安裝流程：
    * 1.pip安裝selenium 
    * 2.把driver放在 /usr/bin 或 /usr/local/bin (不用root權限)

## todo
* 用Selenium做爬蟲、自動化測試
* 可用Python或JS實作
* [Puppeteer VS Selenium](https://linuxhint.com/puppeteer_vs_selenium/)
* [使用Python的Selenium控制瀏覽器](http://tn00343140a.pixnet.net/blog/post/3465687-%E4%BD%BF%E7%94%A8python%E7%9A%84selenium%E6%8E%A7%E5%88%B6%E7%80%8F%E8%A6%BD%E5%99%A8)
* [Python 學習筆記 : Selenium 模組瀏覽器自動化測試 (二)](http://yhhuang1966.blogspot.com/2018/05/python-selenium_27.html)
* [Python 走入現實：selenium](https://ithelp.ithome.com.tw/articles/10203693?sc=iThelpR)
* [莫烦 高级爬虫: 让 Selenium 控制你的浏览器帮你爬](https://morvanzhou.github.io/tutorials/data-manipulation/scraping/5-01-selenium/)
* [[爬蟲實戰] 如何使用 Selenium 以及 Python 輕鬆抓取 Agoda 的旅館資訊?](https://www.youtube.com/watch?v=MQH4Rau_F_A)
* [[Selenium] 如何使用 Selenium 撰寫網路爬蟲?](https://www.youtube.com/watch?v=DdZ9ScpYbE8)

## 以下為舊文章待整理
## Selenium remote server文章
* [Remote Webdriver](http://www.easonhan.info/webdriver/2013/05/28/remote-server/)
* [Selenium grid for RC and WebDriver](https://github.com/SeleniumHQ/selenium/wiki/Grid2)
* [Selenium Ubuntu Node Configuration on VirtualBox](http://brome-hq.logdown.com/posts/305608-selenium-ubuntu-node-configuration-on-virtualbox)
* [Running selenium tests on Virtual box guest](http://stackoverflow.com/questions/30531849/running-selenium-tests-on-virtual-box-guest)


## Selenium Grid 相關文章
* [官方介紹](http://www.seleniumhq.org/docs/07_selenium_grid.jsp)
* [如何架設 Selenium Grid (包含 hub 與 node)](http://blog.darkwing.co/2016/03/%E5%A6%82%E4%BD%95%E6%9E%B6%E8%A8%AD-selenium-grid-%E5%8C%85%E5%90%AB-hub-%E8%88%87-node/)
* [使用 Selenium Grid 並行測試](http://openhome.cc/Gossip/JUnit/SeleniumGrid.html)
* [Slenium DOC 官方網站](http://docs.seleniumhq.org/docs/index.jsp)
* [Running Standalone Selenium Server for use with RemoteDrivers](http://docs.seleniumhq.org/docs/03_webdriver.jsp#running-standalone-selenium-server-for-use-with-remotedrivers)



* [WebDriver and the Selenium-Server](http://docs.seleniumhq.org/docs/03_webdriver.jsp#webdriver-and-the-selenium-server)

```
You may, or may not, need the Selenium Server, depending on how you intend to use Selenium-WebDriver. If your browser and tests will all run on the same machine, and your tests only use the WebDriver API, then you do not need to run the Selenium-Server; WebDriver will run the browser directly.
```




### 官方網站Doc
#### Test Design Considerations

```
This chapter presents programming techniques for use with Selenium-WebDriver and Selenium RC. We also demonstrate techniques commonly asked about in the user forum such as how to design setup and teardown functions, how to implement data-driven tests (tests where one can vary the data between test passes) and other methods of programming common test automation tasks.
```




我們可以把找到的內容使用 get_attribute ()方法做比對，比如下面的最大長度

```Python
def test_search_text_field_max_length(self):
    # get the search textbox
    search_field = self.driver.find_element_by_id("search")
    # check maxlength attribute is set to 128
    self.assertEqual("128", search_field.get_attribute("maxlength"))
```

selenium的is_displayed()方法可以確定DOM上的某個項目有沒有出現

[xpath上指定父節點的方法](http://stackoverflow.com/questions/28237694/xpath-get-parent-node-from-child)
* 例如  test3_name = driver.find_element_by_xpath('//td[. = "horse_test"]/parent::tr')




[Selenium的延迟等待](https://my.oschina.net/u/928852/blog/98885)


[Selenium如何解決ElementNotFound的錯誤? (Wait 的使用情境)](http://www.qa-knowhow.com/?p=1561)


[Selenium Officce Doc](http://www.seleniumhq.org/docs/)


[Selenium gitbook](http://selenium-python.readthedocs.io/installation.html)

[selenium + PhontomJS Python爬虫利器五之Selenium的用法](http://cuiqingcai.com/2599.html)


[Selenium自动化测试Python一：Selenium入门](http://www.jianshu.com/p/4ce5ecef5f6c)


[凌俣Linty selenium 介紹詳細](http://www.jianshu.com/users/af76d4b3d108/latest_articles)

### 開啟chrome時遇到
```
selenium.common.exceptions.WebDriverException: Message: session not created exception from unknown error: Runtime.executionContextCreated has invalid
```

[解決方法:更新chrome外掛](http://stackoverflow.com/questions/40373801/python-selenium-webdriver-session-not-created-exception-when-opening-chrome
https://bugs.chromium.org/p/chromedriver/issues/detail?id=1548)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 在yahoo中搜索關鍵字的範例

browser = webdriver.Firefox()

browser.get('http://www.yahoo.com')
assert 'Yahoo' in browser.title

elem = browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)

# 關閉瀏覽器
# browser.quit()
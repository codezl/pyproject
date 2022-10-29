# a utils py file
# -*- coding: UTF-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service


chormDriver = 'C:\Python39\chromedriver.exe' # chrom(谷歌浏览器driver存放目录)


def getDriver(url):
    url = 'https://v.qq.com/x/cover/m441e3rjq9kwpsc/m00253deqqo.html'
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 无窗口模式

    driver = webdriver.Chrome(chrome_options=option)

    driver.get(url)
    resultList = driver.find_elements_by_class_name('tab__item')
    for item in resultList:
        item.click()
    seleniumPage = driver.page_source
    driver.quit()
    soup = BeautifulSoup(seleniumPage, 'html.parser')
    episodeListRectItem = soup.find_all('div', attr={'class': 'episode-list-rect__item'})
    print(episodeListRectItem)


# 打开浏览器 （模拟点击等）
def testBrowser():
    url = 'https://v.qq.com/x/cover/m441e3rjq9kwpsc/m00253deqqo.html'
    option = webdriver.ChromeOptions()
    option.add_argument('headless')  # 无窗口模式,后台运行
    # executable_path、 chrome_options 废弃
    # browser = webdriver.Chrome(executable_path=chormDriver, chrome_options=option)
    browser = webdriver.Chrome(service=Service(chormDriver), options=option)

    browser.get(url)
    print(browser.page_source)


if __name__ == '__main__':
    # getDriver('')
    testBrowser()

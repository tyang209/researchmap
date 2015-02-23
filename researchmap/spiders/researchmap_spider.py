from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.spider import Spider
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy import Selector
from researchmap.items import ResearchmapItem
import re
from scrapy import log
from scrapy.log import ScrapyFileLogObserver
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class researchmap_spider(CrawlSpider):
	name = "researchmap_spider"
	def __init__(self,name=None,**kwargs):
		super(researchmap_spider, self).__init__(name, **kwargs)
		# ScrapyFileLogObserver(open("spider.log",'w'), level = log.INFO).start()
		# ScrapyFileLogObserver(open("spider_error.log",'w'), level = log.ERROR).start()

		self.driver = webdriver.Chrome("chromedriver.exe")
		allowed_domains = ["researchmap.jp"]
		self.start_urls=["http://researchmap.jp/read0155942/?lang=english"	]


	def parse(self, response):
		self.driver.get(response.url)
		self.driver.set_window_size(1920, 1000)
		time.sleep(5)
		items = []
		textLinks = self.driver.find_elements_by_xpath("//a[contains(@class,'hover_highlight syslink')]")
		print type(textLinks)
		for textLink in textLinks:
			print textLink
			webdriver.ActionChains(self.driver).move_to_element(textLink).click(textLink).perform()
			time.sleep(2)
			ShowForm = Select(self.driver.find_element_by_xpath("//select[contains(@name,'visible_row')]"))
			ShowForm.select_by_value("100")
			time.sleep(3)
			textDiv = self.driver.find_element_by_xpath("//textarea")
			print textDiv.get_attribute('innerHTML')	
			exitButton = self.driver.find_element_by_xpath("//input[contains(@name,'cancel_btn')]")
			exitButton.click()
			# webdriver.ActionChains(self.driver).move_to_element(exitButton).click(exitButton).perform()
			time.sleep(5)

			# $x("//a[contains(@class,'hover_highlight syslink')]")
		# hxs = Selector(text=response.body,type="html")
		# self.log('URL: %s' %response.url,level=log.INFO)
		# self.log('Headers: %s' %response.request.headers.to_string(),level=log.INFO)		
		#$x("//a[contains(@class,'hover_highlight syslink')]")
		return items





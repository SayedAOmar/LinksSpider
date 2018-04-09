# coding: utf-8

import requests
from   bs4 import BeautifulSoup
import re
class LinksSpider:
	"""docstring for EmailHunter"""
	def __init__(self):
		self.Auther  		= "Sayed A. Omar"
		self.version 		= "V0.1"
		self.links_file     = open('links.csv','a+')
		self.links          = []

	def spider(self,url):
		self.links.append(url)
		for link in self.links:
			data 				= requests.get(link).text
			soup 				= BeautifulSoup(data,'html5lib')
			for a in soup.findAll('a'):
				new_link        = a.get('href')
				if new_link and new_link.startswith('http'):
					if new_link not in self.links:
						self.links.append(new_link)
						new_link = new_link.encode('utf-8').strip()
						self.links_file.write(new_link+'\n')
			if len(self.links) % 10 == 0:
				print len(self.links)
		return links

if __name__ == '__main__':
	spider = LinksSpider()
	spider.spider('URL_GOES_HERE')



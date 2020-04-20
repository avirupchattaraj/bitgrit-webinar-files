import os
import requests
from scrapy import Selector

website_data=requests.get('https://msclubsrm.in/team.html').content
# print(website_data)
sel=Selector(text=website_data)
names=sel.xpath('//h4[@class="card-title cardtitle"]/text()').extract()
designations=sel.xpath('//h6[@class="card-subtitle"]/text()').extract()
length=len(names)
for i in range(length):
    print(names[i],designations[i])
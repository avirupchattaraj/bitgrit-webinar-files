import os
import scrapy
from scrapy import Selector

html="""<html>
    <head>
        <title>Webpage for scraping</title>
        <meta charset="utf-8">
    </head>
    <body>
        <h1>Hello I am Webpage</h1>
        <h3 id="bitgrit">I am ready for scraping</h3>
        <h3>Welcome to webinar</h3>
    </body>
</html>"""
sel=Selector(text=html)
data=sel.xpath('//h3[@id="bitgrit"]/text()').extract()
print(data)
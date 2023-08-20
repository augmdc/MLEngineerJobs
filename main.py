import scrapy
from scrapy.crawler import CrawlerProcess
import StackOverFlowScraper

scraped_data = []
def collect_items(item, response, spider):
    scraped_data.append(dict(item))

process = CrawlerProcess()
process.crawl(StackOverFlowScraper.StackOverFlowSpyder,callback=collect_items)
process.start()

for item in scraped_data:
    print(item)

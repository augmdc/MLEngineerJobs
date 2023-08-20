import scrapy
class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    excerpt = scrapy.Field()
    link = scrapy.Field()
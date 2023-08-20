import scrapy
from ArticleItem import ArticleItem

class StackOverFlowSpyder(scrapy.Spider):
    """
    Spyder to crawl StackOverFlow blog
    """
    name = "StackOverflow"
    start_urls = [
        "https://stackoverflow.blog/code-for-a-living/",
    ]
    custom_settings = {
        'CONCURRENT_REQUESTS': 2,    # Number of concurrent requests
        'DOWNLOAD_DELAY': 3,         # Delay between requests (in seconds)
    }

    def parse(self, response):
        """
        Gets a list of articles from StackOverflow's blog that relate to AI
        """
        keywords = ["AI", "Artificial Intelligence", "LLM", "Large Language Model", "large language model"]
        #pattern = r"https://stackoverflow\.blog/\d{4}/\d{2}/\d{2}"
        articles = response.css('article')
        excerpts = articles.css('div.lh-excerpt::text').getall()
        #for article in articles:
            #matching_links = article.css('a')
            #links = matching_links.css('::attr(href)').get()
            #titles = matching_links.css('::attr(title)').get()

        for excerpt in excerpts:
            item = ArticleItem()
            item['title'] = "Your Title Here"  # You can set a title if needed
            item['excerpt'] = excerpt
            yield item
            


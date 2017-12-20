from toapi import Item, XPath
from config import SITE_URL


class Page(Item):
    next_page = XPath('//a[@class="next"][1]/@href')

    def clean_next_page(self, next_page):
        return "/{}{}".format(SITE_URL, next_page)

    class Meta:
        source = XPath('//div[@class="pager"]')
        route = '[/category/\d+/\?page=\d+|/search/\?cat=1001&keyword=.+]'

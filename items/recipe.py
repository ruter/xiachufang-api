from toapi import Css, Item, XPath
from config import SITE_URL


class Recipe(Item):
    url = Css('a.recipe', attr='href')
    cover = Css('a.recipe > div.cover > img', attr='data-src')
    name = Css('a.recipe > div.info > p.name')

    def clean_url(self, url):
        return "/{}{}".format(SITE_URL, url)

    def clean_name(self, name):
        return name.strip()

    class Meta:
        source = XPath('//div[@class="normal-recipe-list"]/ul[@class="list"]/li')
        route = '[/category/\d+/\?page=\d+|/search/\?cat=1001&keyword=.+]'

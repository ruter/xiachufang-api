from toapi import Css, Item, XPath
from config import SITE_URL


class Recipe(Item):
    url = Css('a.recipe', attr='href')
    name = Css('a.recipe > div.info > p.name')
    cover = Css('a.recipe > div.cover > img', attr='data-src')

    def clean_name(self, name):
        return name.strip()

    class Meta:
        source = XPath('//div[@class="normal-recipe-list"]/ul[@class="list"]/li')
        route = {
            '/category/:cat/': '/category/:cat/',
            '/category/:cat/?page=:page': '/category/:cat/?page=:page',
            '/search/:keyword': '/search/?keyword=:keyword&cat=1001'
        }

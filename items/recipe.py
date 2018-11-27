from toapi import Css, Item, XPath
from config.site import URL


class Recipe(Item):
    url = Css('div.recipe > a', attr='href')
    name = Css('div.recipe > div.info > p.name > a')
    cover = Css('div.recipe > a > div.cover > img', attr='data-src')

    def clean_name(self, name):
        return name.strip()

    class Meta:
        source = XPath('//div[contains(@class, "main-panel")]//div[@class="normal-recipe-list"]/ul[@class="list"]/li')
        route = {
            '/category/:cat/': '/category/:cat/',
            '/category/:cat/?page=:page': '/category/:cat/?page=:page',
            '/search/:keyword': '/search/?keyword=:keyword&cat=1001'
        }

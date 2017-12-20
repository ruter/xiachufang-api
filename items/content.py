from lxml import etree

from toapi import Css, Item, XPath


class Content(Item):
    name = Css('h1.page-title[itemprop="name"]')
    cover = Css('div.recipe-show > div.cover > img', attr='src')
    grade = Css('div.recipe-show > div.container > div.stats > div.score > span.number')
    materials = Css('div.recipe-show > div.ings > table tr')

    def clean_name(self, name):
        return name.strip()

    def clean_materials(self, nodes):
        materials = [{
            'name': node.findtext('td[@class="name"]').strip() or node.findtext('td[@class="name"]/a').strip(),
            'unit': node.findtext('td[@class="unit"]').strip()
        } for node in nodes]
        return materials

    class Meta:
        source = XPath('//div[contains(@class,"main-panel")]/div[1]')
        route = '/recipe/\d+/'

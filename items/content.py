import re
from lxml import etree

from toapi import Css, Item, XPath


class Content(Item):
    name = Css('h1.page-title[itemprop="name"]')
    cover = Css('div.recipe-show > div.cover > img', attr='src')
    grade = Css('div.recipe-show > div.container > div.stats > div.score > span.number')
    materials = Css('div.recipe-show > div.ings > table tr')
    steps = Css('div.steps > ol li', attr='html')
    tip = Css('div.tip')

    def clean_name(self, name):
        return name.strip()

    def clean_materials(self, nodes):
        materials = [{
            'name': node.findtext('td[@class="name"]').strip() or node.findtext('td[@class="name"]/a').strip(),
            'unit': node.findtext('td[@class="unit"]').strip()
        } for node in nodes]
        return materials

    def clean_steps(self, nodes):
        # HTML tag <p/>
        re_p = re.compile('</?p[^>]*>')
        # HTML tag <br/>
        re_br = re.compile('<br\s*?/?>')
        steps = [{
            'step': idx + 1,
            'desc': re_br.sub('\n', re_p.sub('', etree.tounicode(node.find('p')).strip())).strip(),
            'img': node.find('img').get('src') if node.find('img') is not None else ''
        } for idx, node in enumerate(nodes)]
        return steps

    def clean_tip(self, tip):
        return tip.strip()

    class Meta:
        source = XPath('//div[contains(@class,"main-panel")]/div[1]')
        route = { '/recipe/:no/': '/recipe/:no/' }

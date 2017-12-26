from lxml import etree
from toapi import Css, Item


class Category(Item):
    categories = Css('div.cates-list')

    def clean_categories(self, nodes):
        categories = []
        for node in nodes:
            topic = {
                'name': node.findtext('div/h3').strip(),
                'list': []
            }
            cates_list = node.find('div[3]')
            h4_nodes = cates_list.findall('h4')
            ul_nodes = cates_list.findall('ul')
            for idx, el in enumerate(h4_nodes):
                tmp_dict = {
                    'name': el.text.strip(),
                    'types': []
                }
                for a in ul_nodes[idx].findall('li/a'):
                    tmp_dict['types'].append({
                        'name': a.text.strip(),
                        'link': a.get('href', '#')
                    })
                topic['list'].append(tmp_dict)
            categories.append(topic)
        return categories

    class Meta:
        source = Css('div.category-container > div')
        route = { '/category/': '/category/' }

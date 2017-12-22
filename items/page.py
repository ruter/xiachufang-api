from toapi import Css, Item, XPath


class Page(Item):
    next = Css('a.next', attr='href')

    class Meta:
        source = XPath('//div[@class="pager"]')
        route = {
            '/category/:cat/': '/category/:cat/',
            '/category/:cat/?page=:page': '/category/:cat/?page=:page',
            '/search/:keyword': '/search/?keyword=:keyword&cat=1001'
        }

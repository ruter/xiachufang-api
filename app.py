from toapi import Api
from config.site import URL
from items.page import Page
from items.recipe import Recipe
from items.content import Content
from items.category import Category
from settings import MemCacheSettings

api = Api(URL, settings=MemCacheSettings)
api.register(Page)
api.register(Recipe)
api.register(Content)
api.register(Category)

if __name__ == '__main__':
    api.serve()

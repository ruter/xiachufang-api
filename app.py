from toapi import Api
from config.site import URL
from items.page import Page
from items.recipe import Recipe
from items.content import Content
from settings import RedisCacheSettings

api = Api(URL, settings=RedisCacheSettings)
api.register(Page)
api.register(Recipe)
api.register(Content)

if __name__ == '__main__':
    api.serve()

from toapi import Api
from config import SITE_URL
from items.page import Page
from items.recipe import Recipe
from items.content import Content
from settings import MySettings

api = Api(SITE_URL, settings=MySettings)
api.register(Page)
api.register(Recipe)
api.register(Content)

if __name__ == '__main__':
  api.serve()

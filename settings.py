import os

from fake_useragent import UserAgent
from toapi.cache import MemoryCache, RedisCache, JsonSerializer
from toapi.settings import Settings


class MemCacheSettings(Settings):

    cache = {
        'cache_class': MemoryCache,
        'cache_config': {},
        'serializer': None,
        'ttl': None
    }
    storage = {
        "PATH": os.getcwd(),
        "DB_URL": None
    }
    web = {
        "with_ajax": False,
        "request_config": {"headers": {'User-Agent': UserAgent().random}},
        "headers": None
    }


class RedisCacheSettings(Settings):

    cache = {
        'cache_class': RedisCache,
        'cache_config': {
            'host': '127.0.0.1',
            'port': 6379,
            'db': 0
        },
        'serializer': JsonSerializer,
        'ttl': None
    }
    storage = {
        "PATH": os.getcwd(),
        "DB_URL": None
    }
    web = {
        "with_ajax": False,
        "request_config": {"headers": {'User-Agent': UserAgent().random}},
        "headers": None
    }
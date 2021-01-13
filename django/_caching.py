# https://docs.djangoproject.com/en/3.1/topics/cache/#the-low-level-cache-api
# https://testdriven.io/blog/django-caching/
# https://realpython.com/caching-in-django-with-redis/
# https://medium.com/fintechexplained/advanced-python-how-to-implement-caching-in-python-application-9d0a4136b845
# https://realpython.com/lru-cache-python/
from django.core.cache import caches
from django.core.cache import cache as default_cache 
cache = caches['default']
# cache1 = caches['myalias']
# cache2 = caches['myalias']
cache.set('my_key', 'hello, world!', 30, None)
cache.get('my_key')
cache.add('add_key', 'New value')
cache.get('my_new_key')
cache.get_or_set('some-timestamp-key', datetime.now)
cache.get_or_set('my_new_key', 'my new value', 100)
cache.set('a', 1)
cache.set('b', 2)
cache.set('c', 3)
cache.get_many(['a', 'b', 'c'])
cache.delete('a')
cache.delete_many(['a', 'b', 'c'])
cache.clear()
cache.touch('a', 10)

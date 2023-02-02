from django.urls import re_path
from wagtailcache.cache import cache_page

from . import views


app_name = 'blog'

urlpatterns = [
    re_path(r'^tag/(?P<tag>[-\w]+)/', cache_page(views.tag_view), name="tag"),
    re_path(r'^category/(?P<category>[-\w]+)/feed/$', cache_page(views.LatestCategoryFeed()), name="category_feed"),
    re_path(r'^category/(?P<category>[-\w]+)/', cache_page(views.category_view), name="category"),
    re_path(r'^author/(?P<author>[-\w]+)/', cache_page(views.author_view), name="author"),
    re_path(r'(?P<blog_slug>[\w-]+)/rss.*/',
        cache_page(views.LatestEntriesFeed()),
        name="latest_entries_feed"),
    re_path(r'(?P<blog_slug>[\w-]+)/atom.*/',
        cache_page(views.LatestEntriesFeedAtom()),
        name="latest_entries_feed_atom"),
]

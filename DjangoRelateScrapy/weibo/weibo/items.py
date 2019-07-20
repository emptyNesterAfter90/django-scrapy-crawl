# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem

from microblog.models import HotSpot, FreshNews, FunnyStory, Society, Fashion, TopEvent, TopList


class WeiboItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # publishTime = scrapy.Field()
    # repost = scrapy.Field()
    # comment = scrapy.Field()
    # approve = scrapy.Field()
    # address = scrapy.Field()
    django_model = HotSpot


class FreshNewsItem(DjangoItem):
    # content = scrapy.Field()
    # author = scrapy.Field()
    # publishTime = scrapy.Field()
    # address = scrapy.Field()
    # image = scrapy.Field()
    django_model = FreshNews


class FunnyStoryItem(DjangoItem):
    # image = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # publishTime = scrapy.Field()
    # repost = scrapy.Field()
    # comment = scrapy.Field()
    # approve = scrapy.Field()
    # address = scrapy.Field()
    django_model = FunnyStory


class SocietyItem(DjangoItem):
    # image = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # publishTime = scrapy.Field()
    # repost = scrapy.Field()
    # comment = scrapy.Field()
    # approve = scrapy.Field()
    # address = scrapy.Field()
    django_model = Society


class FashionItem(DjangoItem):
    # image = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # publishTime = scrapy.Field()
    # repost = scrapy.Field()
    # comment = scrapy.Field()
    # approve = scrapy.Field()
    # address = scrapy.Field()
    django_model = Fashion


class TopEventItem(DjangoItem):
    # image = scrapy.Field()
    # content = scrapy.Field()
    # author = scrapy.Field()
    # publishTime = scrapy.Field()
    # repost = scrapy.Field()
    # comment = scrapy.Field()
    # approve = scrapy.Field()
    # address = scrapy.Field()
    django_model = TopEvent


class TopListItem(DjangoItem):
    django_model = TopList

# -*- coding: utf-8 -*-
import json
import re

import scrapy
from scrapy import Request
from scrapy.spiders import CrawlSpider

from weibo.items import WeiboItem, FreshNewsItem, FunnyStoryItem, SocietyItem, FashionItem, TopEventItem, TopListItem


class WblogSpider(CrawlSpider):
    name = 'WBlog'
    aallowed_domains = ['weibo.com']
    offset = [0, 0, 0, 0, 0, 0, 0]
    head_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=1760&page={0}&lefnav=0&cursor=&__rnd=1556722532018"
    fresh_news_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=novelty&page={0}&lefnav=0&cursor=1:5&__rnd=1557138124"
    funny_story_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=10011&page={0}&lefnav=0&cursor=&__rnd=1558513242509"
    society_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=7&page={0}&lefnav=0&cursor=&__rnd=1558518277085"
    fashion_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=12&page={0}&lefnav=0&cursor=&__rnd=1558519017783"
    topevent_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=0&page={0}&lefnav=0&cursor=&__rnd=1558519668238"
    toplist_url = "https://weibo.com/a/aj/transform/loadingmoreunlogin?ajwvr=6&category=99991&page={0}&lefnav=0&cursor=&__rnd=1558522368554"

    # start_urls = [base_url.format(offset)]

    def start_requests(self):
        yield Request(self.fresh_news_url.format(self.offset[0]), callback=self.parse_fresh_news)
        yield Request(self.head_url.format(self.offset[1]), callback=self.parse_head)
        yield Request(self.funny_story_url.format(self.offset[2]), callback= self.parse_funny_story)
        yield Request(self.society_url.format(self.offset[3]), callback= self.parse_society)
        yield Request(self.fashion_url.format(self.offset[4]), callback= self.parse_fashion)
        yield Request(self.topevent_url.format(self.offset[5]), callback=self.parse_topevent)
        yield Request(self.toplist_url.format(self.offset[6]), callback=self.parse_toplist)

    def parse_head(self, response):
        data = json.loads(response.text)
        if data and 'data' in data:
            pattern = re.compile('<div class="UG_list_b".*?<img src="(.*?)" alt="">.*?<a href="(.*?)".*?_blank">(.*?)</a>.*?subinfo S_txt2">(.*?)</span></a>.*?'
                + 'S_txt2">(.*?)</span>.*?praised S_ficon W_f16">ñ</em><em>(.*?)</em>.*?ficon_'
                + 'repeat S_ficon W_f16">.*?</em><em>(.*?)</em>.*?forward S_ficon W_f16.*?</em><em>'
                + '(.*?)</em>.*?</div>', re.S)
            result = re.findall(pattern, data.get('data'))
            for info in result:
                item = WeiboItem()
                item['content'] = info[2]
                item['author'] = info[3]
                item['publishTime'] = info[4]
                item['repost'] = info[5]
                item['comment'] = info[6]
                item['approve'] = info[7]
                item['address'] = info[1]
                item['image'] = info[0]
                yield item

            if self.offset[0] < 5:
                self.offset[0] += 1
                url = self.head_url.format(self.offset[0])
                yield Request(url, callback=self.parse_head)

    def parse_fresh_news(self, response):
        results = json.loads(response.text)
        if results and 'data' in results.keys():
            data = results.get('data')
            pattern = re.compile('<div class="UG_list_b.*?<img src="(.*?)">.*?list_title_b"><a href="(.*?)"'
                                 + '.*?"_blank">(.*?)</a></h3>.*?subinfo S_txt2">(.*?)</span></a>.*?subi'
                                 + 'nfo S_txt2">(.*?)</span>.*?</div>', re.S)
            results = re.findall(pattern, data)
            for info in results:
                item = FreshNewsItem()
                item['content'] = info[2]
                item['author'] = info[3]
                item['publishTime'] = info[4]
                item['address'] = 'https://weibo.com/' + info[1]
                item['image'] = info[0]
                yield item

            if self.offset[1] < 5:
                self.offset[1] += 1
                url = self.fresh_news_url.format(self.offset[1])
                yield Request(url, callback=self.parse_fresh_news)

    def parse_funny_story(self, response):
        data = json.loads(response.text)
        if data and 'data' in data:
            pattern = re.compile('<div.*?UG.*?href="(.*?)".*?W_piccut.*?src="(.*?)".*?list_title'
                                 + '(.*?)</h3>.*?subinfo S_txt2">(.*?)</span></a>.*?subinfo S_txt2">'
                                 + '(.*?)</span>.*?ficon_praised.*?<em>(.*?)</em>.*?ficon_repeat'
                                 + '.*?<em>(.*?)</em>.*?ficon_forward.*?<em>(.*?)</em>.*?</div>', re.S)
            result = re.findall(pattern, data.get('data'))
            for info in result:
                item = FunnyStoryItem()
                item['content'] = re.sub(r'[0-9a-z_]+|\u200b', '', ''.join(re.findall('>(.*?)<', info[2])))
                item['author'] = info[3]
                item['publishTime'] = info[4]
                item['repost'] = info[5]
                item['comment'] = info[6]
                item['approve'] = info[7]
                item['address'] = info[0]
                item['image'] = info[1]
                yield item

            if self.offset[2] < 5:
                self.offset[2] += 1
                url = self.funny_story_url.format(self.offset[2])
                yield Request(url, callback=self.parse_funny_story)

    def parse_society(self, response):
        data = json.loads(response.text)
        if data and 'data' in data:
            pattern = re.compile('<div.*?UG.*?href="(.*?)".*?W_piccut.*?src="(.*?)".*?list_title'
                                 + '(.*?)</h3>.*?subinfo S_txt2">(.*?)</span></a>.*?subinfo S_txt2">'
                                 + '(.*?)</span>.*?ficon_praised.*?<em>(.*?)</em>.*?ficon_repeat'
                                 + '.*?<em>(.*?)</em>.*?ficon_forward.*?<em>(.*?)</em>.*?</div>', re.S)
            result = re.findall(pattern, data.get('data'))
            for info in result:
                item = SocietyItem()
                item['content'] = re.sub(r'[0-9a-z_]+|\u200b', '', ''.join(re.findall('>(.*?)<', info[2])))
                item['author'] = info[3]
                item['publishTime'] = info[4]
                item['repost'] = info[5]
                item['comment'] = info[6]
                item['approve'] = info[7]
                item['address'] = info[0]
                item['image'] = info[1]
                yield item

            if self.offset[3] < 5:
                self.offset[3] += 1
                url = self.society_url.format(self.offset[3])
                yield Request(url, callback=self.parse_society)

    def parse_fashion(self, response):
        data = json.loads(response.text)
        if data and 'data' in data:
            pattern = re.compile(
                '<div class="UG_list_b".*?<img src="(.*?)" alt="">.*?<a href="(.*?)".*?_blank">(.*?)</a>.*?subinfo S_txt2">(.*?)</span></a>.*?'
                + 'S_txt2">(.*?)</span>.*?praised S_ficon W_f16">ñ</em><em>(.*?)</em>.*?ficon_'
                + 'repeat S_ficon W_f16">.*?</em><em>(.*?)</em>.*?forward S_ficon W_f16.*?</em><em>'
                + '(.*?)</em>.*?</div>', re.S)
            result = re.findall(pattern, data.get('data'))
            for info in result:
                item = FashionItem()
                item['content'] = info[2]
                item['author'] = info[3]
                item['publishTime'] = info[4]
                item['repost'] = info[5]
                item['comment'] = info[6]
                item['approve'] = info[7]
                item['address'] = info[1]
                item['image'] = info[0]
                yield item

            if self.offset[4] < 5:
                self.offset[4] += 1
                url = self.fashion_url.format(self.offset[4])
                yield Request(url, callback=self.parse_fashion)

    def parse_topevent(self, response):
        data = json.loads(response.text)
        if data and 'data' in data:
            pattern = re.compile('<div.*?UG.*?href="(.*?)".*?W_piccut.*?src="(.*?)".*?list_title'
                                 + '(.*?)</h3>.*?subinfo S_txt2">(.*?)</span></a>.*?subinfo S_txt2">'
                                 + '(.*?)</span>.*?ficon_praised.*?<em>(.*?)</em>.*?ficon_repeat'
                                 + '.*?<em>(.*?)</em>.*?ficon_forward.*?<em>(.*?)</em>.*?</div>', re.S)
            result = re.findall(pattern, data.get('data'))
            for info in result:
                item = TopEventItem()
                item['content'] = re.sub(r'[0-9a-z_]+|\u200b', '', ''.join(re.findall('>(.*?)<', info[2])))
                item['author'] = info[3]
                item['publishTime'] = info[4]
                item['repost'] = info[5]
                item['comment'] = info[6]
                item['approve'] = info[7]
                item['address'] = info[0]
                item['image'] = info[1]
                yield item

            if self.offset[5] < 5:
                self.offset[5] += 1
                url = self.topevent_url.format(self.offset[5])
                yield Request(url, callback=self.parse_topevent)

    def parse_toplist(self, response):
        data = json.loads(response.text)
        if data and 'data' in data:
            pattern = re.compile('<div.*?UG.*?href="(.*?)".*?W_piccut.*?src="(.*?)".*?list_title'
                                 + '(.*?)</h3>.*?subinfo S_txt2">(.*?)</span></a>.*?subinfo S_txt2">'
                                 + '(.*?)</span>.*?ficon_praised.*?<em>(.*?)</em>.*?ficon_repeat'
                                 + '.*?<em>(.*?)</em>.*?ficon_forward.*?<em>(.*?)</em>.*?</div>', re.S)
            result = re.findall(pattern, data.get('data'))
            for info in result:
                item = TopListItem()
                item['content'] = re.sub(r'[0-9a-z_]+|\u200b', '', ''.join(re.findall('>(.*?)<', info[2])))
                item['author'] = info[3]
                item['publishTime'] = info[4]
                item['repost'] = info[5]
                item['comment'] = info[6]
                item['approve'] = info[7]
                item['address'] = info[0]
                item['image'] = info[1]
                yield item

            if self.offset[6] < 5:
                self.offset[6] += 1
                url = self.toplist_url.format(self.offset[6])
                yield Request(url, callback=self.parse_toplist)

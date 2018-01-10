# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 2018

@author: giotto
"""

from scrapy.spiders import CrawlSpider
from scrapy import Request
from lyriker.items import Lyriker_Item
# from scrapy.conf import settings

from scrapy.utils.log import configure_logging
import logging
import os
import time
import sys

logger = logging.getLogger('Songs_Spider')


class Songs_Spider(CrawlSpider):
    name = "songs_hunter"
    # set here for all spiders, not optimal

    cwd = str(os.getcwd())
    if sys.argv[0] == 'shell':
        log_file_name = str(time.strftime("%Y%m%d_")) + 'lyricker.log'
    else:
        log_file_name = str(time.strftime("%Y%m%d_")
                            ) + sys.argv[1] + 'lyricker.log'

    if '/root' in cwd or '/home/complus' in cwd:
        full_log_file_name = '/home/complus/python_log_files/' + log_file_name
    elif '/giotto' in cwd:
        full_log_file_name = (
            '/home/giotto/Documents/statistics/python_log_files/' +
            log_file_name)
    else:
        full_log_file_name = log_file_name

    configure_logging(install_root_handler=False)
    logging.basicConfig(
        filename=full_log_file_name,
        filemode='a',
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG
    )
    start_urls = ['https://www.lyrics.com/artist/Foo%20Fighters/144725', ]

    def __init__(self, artist=None,):
        print artist

        self.allowed_domains = ["lyrics.com"]
        artist = artist.replace('_', '+')
        self.first_url = "https://www.lyrics.com/artist/" + artist + '/'

    def start_requests(self):
        yield Request(self.first_url, meta={
            'dont_redirect': True,
            'handle_httpstatus_list': [301, 302]
        }, callback=self.parse,
            )

    def parse(self, response):

        songs_urls = response.xpath('//strong/a/@href').extract()
        for url_target in songs_urls:
            url_target = 'https://www.' + self.allowed_domains[0] + url_target
            logger.debug(url_target)

            yield Request(url_target, meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [301, 302, 404]
            }, callback=self.song_parser,)

    def song_parser(self, response):
        raw_text = response.xpath(
            '//pre[@id="lyric-body-text"]/text()').extract()
        text = (' ').join(raw_text)
        lyrics = text.replace('\r', ' ').replace(
            '\n', ' ').replace('  ', ' ').replace('  ', ' ')
        print lyrics

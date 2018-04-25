# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import Join, MapCompose

class ItjuziscrapyItem(Item):
    co_name = Field()
    link = Field()
    industry = Field()
    city = Field()
    money = Field()
    found_time = Field()
    found_capital = Field()
    trademark = Field()
    founder_name = Field()
    founder_intro = Field()
    tags = Field(
            input_processor=MapCompose(unicode.strip),
            out_processor=Join(),
            )
    investors = Field(
            input_processor=MapCompose(unicode.strip),
            out_processor=Join(),
            )
    event_time = Field()
    event_round = Field()
    co_intro = Field()
    co_size = Field()
# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality += 1
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality += 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality += 1
                if item.sell_in < 0:
                    item.quality = 0
            elif item.name == "Sulfuras, Hand of Ragnaros":
                pass
            else:
                if item.quality > 0:
                    if item.name == "Conjured Mana Cake":
                        item.quality -= 2
                    else:
                        item.quality -= 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
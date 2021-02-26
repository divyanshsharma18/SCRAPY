# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutoriaItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    # page_number = 2

    start_urls = ['https://www.amazon.in/s?k=horror+books&page=1 &qid=1593146517&ref=sr_pg_3']

    def parse(self, response):
        items = AmazontutoriaItem()
        title = response.css('span.a-size-medium a-color-base a-text-normal').css('::text').extract()
        # author = response.css('.a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        # price = response.css('.a-spacing-top-small .a-price-whole').css('::text').extract()

        for x in range(0, len(title)):

            items['title'] = title[x]
            # items['author'] = author[x]
            # items['price'] = price[x]




            yield items
        # next_page = 'https://www.amazon.in/s?k=horror+books&page=' + str(
        #     AmazonSpiderSpider.page_number) + '&qid=1592763563&ref=sr_pg_2'
        #
        # if AmazonSpiderSpider.page_number <= 10:
        #     AmazonSpiderSpider.page_number += 1
        #     yield response.follow(next_page, callback=self.parse)
            #yield response.urljoin(next_page)



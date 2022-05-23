# -*- coding: utf-8 -*-
import scrapy


class BoardsCSSSpider(scrapy.Spider):
    name = "boards-css"
    start_urls = [
        'https://www.boards.ie/discussion/2058237577/new-cap-for-2023/p1',
        'https://www.boards.ie/discussion/2058214934/new-cap/p1',
        'https://www.boards.ie/discussion/2057938257/post-2020-cap/p1',
        'https://www.boards.ie/discussion/2057780562/cap-payments-reference-years-2000-2002/p1',
        'https://www.boards.ie/discussion/2057336158/the-new-cap/p1',
        'https://www.boards.ie/discussion/2057111876/cap-reform/p1',
        'https://www.boards.ie/discussion/2056998752/cap-2013/p1'
    ]

    def parse(self, response):
        for datalist in response.css("ul.DataList"):
            for li in datalist.css("li.Item"):
                yield {
                    'title': response.css("#Item_0 > h1::text").extract_first(),
                    'time_1': li.css("div.postbit-header::text").extract_first(),
                    'time': li.css("a.Permalink::text").extract_first(),
                    'text': li.css("div.Item-Body > div.Message > *::text").getall(),
                    'text_1': li.css("div.Item-Body > div.Message::text").getall()
                }
            

        next_page_url = response.css("#PagerBefore > a.Next::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))


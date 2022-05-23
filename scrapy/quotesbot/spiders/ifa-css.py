# -*- coding: utf-8 -*-
import scrapy


class IFAcssSpider(scrapy.Spider):
    name = "ifa-css"
    start_urls = [
        'https://www.ifa.ie/markets-and-prices/grain-price-update-20th-may/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-18th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-18th-may-2/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-18th-may/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-13th-may/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-13th-may/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-11th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-11th-may/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-11th-may/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-6th-may/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-4th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-4th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-11th-may/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-11th-may/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-6th-may/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-4th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-4th-may/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-4th-may/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-29th-april/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-29th-april-2/',
        'https://www.ifa.ie/markets-and-prices/timber-market-report-january-march-2022/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-price-27th-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-27th-april/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-22nd-april/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-21st-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-20th-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-20th-april/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-14th-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-13th-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-13th-april/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-13th-april/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-6th-april/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-6th-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-6th-april/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-1st-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-30th-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-30th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-30th-march-2/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-25th-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-23rd-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-23rd-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-23rd-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-15th-march/',
        'https://www.ifa.ie/markets-and-prices/market-report-15th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-15th-march/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-11th-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-9th-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-9th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-9th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-2nd-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-2nd-march/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-25th-february/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-23rd-february/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-23rd-february/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-23rd-february/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-18th-february/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-16th-february/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-16th-february/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-11th-february/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-9th-february/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-9th-february/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-9th-february/',
        'https://www.ifa.ie/markets-and-prices/beef-prices-rise-5c-kg-to-10c-kg-but-costs-outstripping-price-increase/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-7th-february/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-2nd-february/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-2nd-feb/',
        'https://www.ifa.ie/markets-and-prices/timber-price-survey-nov-dec-2021/',
        'https://www.ifa.ie/markets-and-prices/ifa-grain-update-26th-january/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-26th-january/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-26th-january/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-26th-january/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-21st-january/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-19th-january/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-19th-january/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-19th-january/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-14th-january/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-12th-january/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-12th-january/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update12th-january/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-5th-january/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-5th-january/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-5th-january/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-24th-december/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-22nd-december/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-17th-december/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-15th-december/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-15th-december/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-15th-december/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-10th-december/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-8th-december/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-8th-december/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-8th-december-2/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-3rd-december/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-1st-december/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-1st-december/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-1st-december/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-24th-november/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-24th-november/',
        'https://www.ifa.ie/markets-and-prices/pig-market-report-24th-november/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-19th-november/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-17th-november/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-17th-november/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-17th-november/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-12th-november/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-10th-november/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-10th-november-2/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-10th-november/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-6th-november/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-3rd-november/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-3rd-november/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-3-november/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-28th-october/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-27th-october/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-27th-october/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-27th-october/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-22nd-october/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-20th-october/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-20th-october/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-19th-october/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-15th-october/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-13th-october/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-13th-october/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-12th-october/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-9th-october-2/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-6th-october/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-6th-october/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-6th-october-2/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-4th-october/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-1st-october/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-29th-september/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-29th-september/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-28th-september/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-24th-september/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-22nd-september/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-22nd-september/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-21st-september/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-15th-september/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-15th-september/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-15th-september/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-13th-sept/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-8th-september/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-1st-september/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-8th-september/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-25th-august/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-25th-august/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-23rd-august/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-20th-august/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-18th-august/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-18th-august/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-17th-august/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-13th-august/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-11th-august/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-11th-august/',
        'https://www.ifa.ie/markets-and-prices/grain-market-report-11th-august/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-11th-august/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-6th-august/',
        'https://www.ifa.ie/markets-and-prices/milk-processors-must-pay-more-than-36cpl-for-july-milk/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-4th-august/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-4th-august/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-4th-august/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-30th-july/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-28th-july/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-28th-july/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-28th-july-2/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-23rd-july/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-21st-july/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-21st-july/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-21st-july/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-14th-july/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-14th-july/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-13th-july/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-9th-july/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-7th-july/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-7th-july/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-6th-july/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-2nd-july/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-30th-june/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-30th-june/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-30th-june/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-25th-june/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-23rd-june/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-23rd-june/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-22nd-june/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-18th-june/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-16th-june/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-16th-june/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-16th-june/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-11th-june/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-9th-june/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-9th-june/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-9th-june/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-4th-june/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-2nd-june/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-2nd-june/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-1st-june/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-price-19th-may/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-19th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-18th-may/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-14th-may/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-12th-may/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-12th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-12th-may/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-7th-may/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-5th-may/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-5th-may/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-5th-may/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-30th-april/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-28th-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-28th-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-28th-april/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-28th-april-2/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-23rd-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-21st-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-21st-april/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-16th-april/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-14th-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-14th-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-14th-april/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-9th-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-7th-april/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-7th-april/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-7th-april/',
        'https://www.ifa.ie/markets-and-prices/grain-market-report-1st-april/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-factory-prices-31st-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-31st-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-30th-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-25th-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-24th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-24th-march-2/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-22nd-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-16th-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-16th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-16th-march/',
        'https://www.ifa.ie/markets-and-prices/horticulture-spring-market-report/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-12th-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-10th-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-10th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-10th-march/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-6th-march/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-3rd-march/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-3rd-march/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-3rd-march/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-26th-feb/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-26th-feb/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-24th-feb/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-24th-feb/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-23rd-feb/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-19th-feb/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-17th-feb/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-17th-feb/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-17th-feb/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-12th-feb/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-10th-feb/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-10th-feb/',
        'https://www.ifa.ie/markets-and-prices/pig-market-update-10th-feb/',
        'https://www.ifa.ie/markets-and-prices/fertiliser-market-update-10th-feb/',
        'https://www.ifa.ie/markets-and-prices/beef-sheep-update-5th-feb/',
        'https://www.ifa.ie/markets-and-prices/grain-market-update-3rd-feb/',
        'https://www.ifa.ie/markets-and-prices/weekly-cattle-prices-3rd-feb/',
        'https://www.ifa.ie/markets-and-prices/potato-market-update-3rd-feb/'
    ]

    def parse(self, response):
        for quote in response.css("main.site-main"):
            for content in response.css("div.single-content"):
                yield {
                    'title': quote.css(".entry-title::text").extract_first(),
                    'time': quote.css(".entry-date::text").extract_first(),
                    'text': content.css("p::text").getall()
                }

        # next_page_url = response.css("li.next > a::attr(href)").extract_first()
        # if next_page_url is not None:
        #     yield scrapy.Request(response.urljoin(next_page_url))

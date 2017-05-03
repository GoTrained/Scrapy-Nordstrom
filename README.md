# Scrapy-Nordstrom
Web Scraping products from Nordstrom search results using Scrapy

## Problem

When you search Nordstrom for a word, it gives you a URL like this:
http://shop.nordstrom.com/sr?origin=keywordsearch&keyword=suitcase

When you try to scrape it, you get only the first 12 items.

Some may resort to Selenium to solve such issues. However, here we are offering a solution using Scrapy.

## Solution

If you click the next page, you will discover that this is how the URL is formed; notice the ending "top=72".
http://shop.nordstrom.com/sr?origin=keywordsearch&keyword=suitcase&page=1&top=72

The trick is to scrape only 12 per page. So for example, instead of having 11 pages, you will have 63 pages. However, the parameter "top" is not set to 72 but to 12 only.

So you should use this URL instead:
http://shop.nordstrom.com/sr?origin=keywordsearch&keyword=suitcase&page=1&top=12


There are two Scrapy spiders, one of which uses LinkExtractor.

## Usage

- Change `url` to reflect the keyword you are searching for
- Change `range` to reflect the number of pages + 1
- In your Terminal, navigate to the nordstrom folder
- To run the "nord", use:
```scrapy crawl nord -o nord.csv```
- To run the "nordrules" spider, use:
```scrapy crawl nordrules -o nord-rules.csv```
 
 
# Scrapy Online Course

Check this [Scrapy tutorial](https://www.udemy.com/scrapy-tutorial-web-scraping-with-python/?couponCode=GITHUB-NORDSTROM) to learn much more:
- [Scrapy: Powerful Web Scraping & Crawling with Python](https://www.udemy.com/scrapy-tutorial-web-scraping-with-python/?couponCode=GITHUB-NORDSTROM)



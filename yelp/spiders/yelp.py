import scrapy


class YelpSpider(scrapy.Spider):
    name = "yelpscraper"

    def start_requests(self):
        url = 'https://www.yelp.com/search?'
        search = getattr(self, 'search', 'restaurants')
        location = getattr(self, 'location', 'San Francisco, CA')
        url = url + 'find_desc=' + search + '&find_loc=' + location
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for place in response.css("li.regular-search-result"):
            yield {
                'Name': place.xpath("div/div[1]/div[1]/div/div[2]/h3/span/a/span/text()").extract_first(),
                'Ratings': place.xpath("div/div[1]/div[1]/div/div[2]/div[1]/div/@title").extract_first()
                    .replace(" star rating", ""),
                'Reviews': place.xpath("div/div[1]/div[1]/div/div[2]/div[1]/span/text()").extract_first()
                    .strip().replace(" reviews", ""),
                'Price': place.xpath("div/div[1]/div[1]/div/div[2]/div[2]/span[1]/span/text()").extract(),
                'Category': place.xpath("div/div[1]/div[1]/div/div[2]/div[2]/span[2]/a/text()").extract(),
                'Neighbourhood': place.xpath("div/div[1]/div[2]/span[1]/text()").extract_first().strip(),
                'Address': ", ".join(place.xpath("div/div[1]/div[2]/address/text()").extract()).strip(),
                'Phone': place.xpath("div/div[1]/div[2]/span[3]/text()").extract_first().strip(),
            }

        for next in response.css("a.pagination-links_anchor"):
            yield response.follow(next, callback=self.parse)

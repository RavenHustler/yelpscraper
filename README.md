# Yelp Data Scraper
Yelp data scraper built with Python and Scrapy. Scrape Yelp for restaurants, bars, or anything else. Highly customizable!

Installation:
-------------


    $ git clone https://github.com/RavenHustler/yelp-data-scraper
    $ cd yelpscraper
    $ pip install -r requirements.txt


Usage:
-------------
Example usage for scraping Yelp.


Find Bars data in New Orleans, LA.

    scrapy crawl yelpscraper -a search="Bars" -a location="New Orleans, LA"


Find Barbers in New York using zipcode.

    scrapy crawl yelpscraper -a search="Barbershop" -a location="100001"


Save the results in a json file.

    scrapy crawl yelpscraper -a search=Cafe -a location="New Orleans, LA" -o cafes.json

----------
I used Python 2.7 and Scrapy to build this.
Feel free to send in pull requests.
Next step will be to call the scrapy spider from another python script to make the usage easier.

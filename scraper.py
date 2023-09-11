import requests
from bs4 import BeautifulSoup
import pandas as pd

class DataCollection:
    
    def british_airways_data_scraper(pages = 10, page_size = 100):
        base_url = "https://www.airlinequality.com/airline-reviews/british-airways"
        
        reviews = []

        # for i in range(1, pages + 1):
        print('Scrapping in progress ...'.center(53, '='))
        for i in range(1, pages + 1):

            print(f"Scraping page {i}")

            # Create URL to collect links from paginated data
            url = f"{base_url}/page/{i}/?sortby=post_date%3ADesc&pagesize={page_size}"

            # Collect HTML data from this page
            response = requests.get(url)

            # Parse content
            content = response.content
            parsed_content = BeautifulSoup(content, 'html.parser')
            for para in parsed_content.find_all("div", {"class": "text_content"}):
                reviews.append(para.get_text())

        print('Scrapping completed successfully ...'.center(53, '#'))
            
        return reviews
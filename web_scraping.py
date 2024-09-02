import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging


# logging

class webScraper:
    def __init__(self, url):
        self.url = url
        self.data = []

    def scrape(self):
        page = 1
        while True:
            response = requests.get(f"{self.url}&page={page}")
            if response.status_code != 200:
                break
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            items = soup.find_all('div', class_='product-item')
            if not items:
                break
            
            for item in items:
                name = item.find('a', class_ = 'product-title').get_text(strip=True)
                price = item.find('span', class_='product-price').get_text(strip=True)
                self.data.append({'name': name, 'price': price})
                
            page += 1
            
    def save_to_csv(self, filename='scrapped_data.csv'):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        
    def load_from_csv(self, filename='scarped_data.csv'):
        self.data = pd.read_csv(filename).to_dict(orient = 'records')
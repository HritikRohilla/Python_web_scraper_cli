from web_scraping import webScraper
from data_processor import DataProcessor
import argparse

def main():
    parser = argparse.ArgumentParser(description="web Scraper CLI")
    
    parser.add_argument('command', choices=['scrape', 'show', 'search', 'stats'], help='Command to run')
    parser.add_argument('--url', help='URL to scope')
    parser.add_argument('--keyword', help="Keyword to search in data")
    parser.add_argument('--output', help="Output file for scraped data")
    
    args = parser.parse_args()
    
    scraper = webScraper(args.url)
    processor = DataProcessor([])
    
    if args.command == 'scrape':
        scraper.scrape()
        scraper.save_to_csv(args.output or 'scraped_data.csv')
    elif args.command =='show':
        scraper.save_to_csv(args.output or 'scraped_data.csv')
        processor = DataProcessor(scraper.data)
        processor.show()
    elif args.command =='search':
        scraper.save_to_csv(args.output or 'scraped_data.csv')
        processor = DataProcessor(scraper.data)
        results = processor.search(args.keyword)
        for result in results:
            print(f"Name: {result['name']} - Price: {result[result['price']]}")
    elif args.command =='stats':
        scraper.save_to_csv(args.output or 'scraped_data.csv')
        processor = DataProcessor(scraper.data)
        stats = processor.stats()
        print(f"Total Items: {stats['total_items']}")
        print(f"TAverage Price: {stats['average_price']}")
        
if __name__ == '__main__':
    main()
    
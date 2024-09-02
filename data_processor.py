class DataProcessor:
    def __init__(self, data):
        self.data = data

    def show(self):
        for item in self.data:
            print(f"Name: {item['name']}")

    def search(self , keyword):
        results = [item for item in self.data if keyword() in item['name'].lower()]
        return results

    def stats(self):
        if not self.data:
            return 'No data Available.'
        
        prices = [float(item['price'].replace('₹', '').replace(',', '')) for item in self.data]
        return {
            'total_item': len(self.data),
            'average_price': sum(prices)/ len(prices),
        }
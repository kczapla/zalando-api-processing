import json
import pprint
import requests


pp = pprint.PrettyPrinter(indent=8)


r = requests.get('https://api.zalando.com/articles')
products = r.json()['content']

for product in products:
    new_product = {}
    new_product['name'] = product['name']
    new_product['brand'] = product['brand']['name']
    new_product['price'] = product['units'][0]['price']['value']
    new_product['img_url'] = product['media']['images'][0]['smallUrl']
    
    product_to_ship = {
            'data': 
                {'attributes': new_product, 
                 'type': 'products'}}
    r = requests.post('http://localhost:5000/products', json=product_to_ship)
    print(r.text)



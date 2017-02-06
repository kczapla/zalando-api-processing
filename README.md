# REST API Zalando manipulation

## Env setup

Ensure that following apps are installed:

* Python3.5+
* psql 8.1+
* and access to PostgreSQL server


When you meet following requirements, Execute:

```sh
cd /path/to/project/dir/
virtualenv env
source env/bin/activate
pip install -r ./requirements.txt
```

## Init DB

Change fields:

```python
# config.py
db_user = 'testuser'
db_password = 'test'
db_addr = 'localhost'
db_name = 'zalando'
```

Init db:

```sh
python ./migrate.py db init  # only first time
python ./migrate.py db migrate
python ./migrate.py db upgrade
```

## Populate your DB

Run following code:

```sh
python ./fetch-from-zalndo.py
```

You can chanage the fetching item limit:

```python
# fetch-from-zalando.py
limit = 500  # will set number of itmes to 500
```

## API Parameters

### Sorting and limiting

| Parameter | Function | Endpoint |
| maxitems | Limits the maximum number of items | /search?maxitems=5 |
| sort | The way of sorting of the products | /search?sort=brand&maxitems=10 |
| name | Searching for the given product | /search?name=Glasses |
| brand | Searching for the prodcuts of given brand | /search?brand=BOSS |

### Obtaining products

| Parameter | Function | Endpoint |
| articles | Get all products from the database | /products |
| articles/<id> | Get product by id from the database | /products/<id> |


### Add new product to the database

```sh
curl -H "Content-Type: application/json" -X POST -d '{ "data": { "attributes": { "brand": "Studio 75", "img_url": "https://i6.ztat.net/catalog/TU/02/1C/00/IK/11/TU021C00I-K11@16.jpg", "name": "YASDALLAS - Occasion wear - navy blazer", "price": 67 }, "type": "products" }}' http://localhost:5000/products
```

## To improve

* Support for full text query
* Sorting direction
* Improve DB model - to add relations for brands and prices
* Add unit tests

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.mod_products.controllers import ProductsList

app = Flask(__name__)
app.config.from_object('config')

# Rest API
api = Api(app)

## Add resources
api.add_resource(ProductsList, '.json')
api.add_resource(BrandsList, '.json')


# DB init
db = SQLAlchemy()
db.init_app(app)

# Import module component
from app.mod_products.controllers import mod_products as products_module

# Register blueprint(s)
app.register_blueprint(products_module, url_prefix='/api/v1/products')

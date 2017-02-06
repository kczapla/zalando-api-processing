from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

# DB init
db = SQLAlchemy(app)
#  db.init_app(app)

# Rest API
api = Api(app)

# Import module component
from app.mod_products.controllers import mod_products as products_module

# Register blueprint(s)
app.register_blueprint(products_module, url_prefix='/api/v1/products')

# Add resources
from app.mod_products.controllers import ProductsList, ProductUpdate
api.add_resource(ProductsList, '/products')
api.add_resource(ProductUpdate, '/products/<id>')

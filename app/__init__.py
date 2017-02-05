from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy()
db.init_app(app)

# Import module component
from app.mod_products.controllers import mod_products as products_module

# Register blueprint(s)
app.register_blueprint(products_module)

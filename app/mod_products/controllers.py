from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource
from .models import Products, ProductsSchema
from app import db


mod_products = Blueprint('products', __name__)

schema = ProductsSchema()


class ProductsList(Resource):
    def get(self):
        products_query = Products.query.all()
        results = schema.dump(products_query, many=True).data
        return results

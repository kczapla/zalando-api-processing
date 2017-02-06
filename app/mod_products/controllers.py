from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource
from .models import Products, ProductsSchema
from app import db

from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

mod_products = Blueprint('products', __name__)

schema = ProductsSchema()


class ProductsList(Resource):
    def get(self):
        products_query = Products.query.all()
        results = schema.dump(products_query, many=True).data
        return results

    def post(self):
        raw_dict = request.get_json(force=True)
        try:
            schema.validate(raw_dict)
            product_dict = raw_dict['data']['attributes']
            product = Products(
                    name=product_dict['name'], 
                    price=product_dict['price'], 
                    brand=product_dict['brand'])
            product.add(product)
            query = Products.query.get(product.id)
            results = schema.dump(query).data
            return results, 201
        except ValidationError as err:
            resp = jsonify({'error': err.messages})
            resp.status_code = 403
            return resp
        except SQLAlchemyError as e:
            db.session.rollback()
            resp = jsonify({'error': str(e)})
            resp.status_code = 403
            return resp

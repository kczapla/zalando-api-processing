from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource, reqparse
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
                    img_url=product_dict['img_url'],
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


class ProductUpdate(Resource):
    def get(self, id):
        product_query = Products.query.get_or_404(id)
        result = schema.dump(product_query).data
        return result


class ProductSearch(Resource):
    def __init__(self):
        choices=['name', 'price', 'brand'], 
        parser = reqparse.RequestParser()
        parser.add_argument(
                'name', 
                help='Item name')
        parser.add_argument(
                'brand', 
                help='Brand name')
        parser.add_argument(
                'q', 
                choices=choices, 
                help='Match prodcut by any column')
        parser.add_argument(
                'maxitems', 
                type=int, 
                help='Limits max items per page')
        parser.add_argument(
                'sort', 
                choices=['name', 'price', 'brand'], 
                help='Choose column to sort')
        parser.add_argument('direction', help='Direction of the sorting')
        self.parser = parser

    def get(self):
        args = self.parser.parse_args()
        products_query = None

        brand_arg = args.get('brand')
        if brand_arg:
            print(brand_arg)
            products_query = Products.query.filter_by(brand=brand_arg)

        name_arg = args.get('name')
        if name_arg:
            products_query = Products.query.filter_by(name=name_arg)

        sort_arg = args.get('sort')
        if sort_arg:
            products_query = products_query.order_by(sort_arg)

        maxitems_arg = args.get('maxitems')
        if maxitems_arg:
            products_query = products_query.limit(maxitems_arg)

        results = schema.dump(products_query, many=True).data
        return results

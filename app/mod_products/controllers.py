from flask import Blueprint, request, jsonify, make_response
from flask_restful import Api, Resource
from .models import Brands, Products, BrandsSchema, ProductsSchema
from app import db


mod_products = Blueprint('products', __name__, url_prefix='/products')

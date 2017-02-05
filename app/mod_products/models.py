from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from sqlalchemy.exc import SQLAlchemyError
from app import db


# Fields validators
not_blank_field = validate.Length(min=1, error='Field cannot be blank')


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
    brand = db.relationship('Brands', backref='product')


class ProductsSchema(Schema):
    id = fields.Str(dump_only=True)  # User can only read this field
    name = fields.Str(validate=not_blank_field)
    price = fields.Integer(validate=not_blank_field)
    brand = fields.Relationship(
            related_url='/brands/{brand_id}',
            related_url_kwargs={'brand_id': '<brand_id>'})

    class Meta:
        type_ = 'products'
        self_url = '/products/{id}'
        self_url_many = '/products/'
        self_url_kwargs = {'id': '<id>'}
        strict = True

from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from sqlalchemy.exc import SQLAlchemyError
from app import db


# Fields validators
not_blank_field = validate.Length(min=1, error='Field cannot be blank')


class CRUD():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class Products(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(250))


class ProductsSchema(Schema):
    id = fields.Str(dump_only=True)  # User can only read this field
    name = fields.Str(validate=not_blank_field)
    price = fields.Integer(validate=not_blank_field)
    brand = fields.Str(validate=not_blank_field)

    class Meta:
        type_ = 'products'
        self_url = '/products/{id}'
        self_url_many = '/products/'
        self_url_kwargs = {'id': '<id>'}
        strict = True

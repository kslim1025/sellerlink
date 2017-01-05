
from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import Thing

class ProductComments(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    comment_id = db.Column('comment_id', db.String(1024), ForeignKey('comment.guid'))
    item_id = db.Column('item_id', db.String(1024), ForeignKey('product.guid'))

class ProductActions(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    action_id = db.Column('action_id', db.String(1024), ForeignKey('action.guid'))
    item_id = db.Column('item_id', db.String(1024), ForeignKey('product.guid'))

class ProductOffers(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))
    item_id = db.Column('item_id', db.String(1024), ForeignKey('product.guid'))

class ProductRequests(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    request_id = db.Column('request_id', db.String(1024), ForeignKey('request.guid'))
    item_id = db.Column('item_id', db.String(1024), ForeignKey('product.guid'))

class ProductImages(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    product_id = db.Column('product_id', db.String(1024), ForeignKey('product.guid'))
    image_id = db.Column('image_id', db.String(1024), ForeignKey('imageobject.guid'))

# productattributes

class Product(db.Model, Thing):
    category = db.Column('category', db.String(1024))
    purchaseDate = db.Column('purchaseDate', db.DateTime)
    releaseDate = db.Column('releaseDate', db.DateTime)
    productionDate = db.Column('productionDate', db.DateTime)
    sku = db.Column('sku', db.String(1024))
    weight = db.Column('weight', db.Integer)
    depth = db.Column('depth', db.Integer)
    width = db.Column('width', db.Integer)
    height = db.Column('height', db.Integer)
    productID = db.Column('productID', db.String(1024))
    gtin8 = db.Column('gtin8', db.String(1024))
    gtin14 = db.Column('gtin14', db.String(1024))
    gtin13 = db.Column('gtin13', db.String(1024))
    gtin12 = db.Column('gtin12', db.String(1024))
    model = db.Column('model', db.String(1024))
    mpn = db.Column('mpn', db.String(1024))
    award = db.Column('award', db.String(1024))
    alternateName = db.Column('alternateName', db.String(1024))
    color = db.Column('color', db.String(1024))

    brand_id = db.Column('brand_id', db.String(1024), ForeignKey('organization.guid'))
    brand = db.relationship('organization', foreign_keys='brand_id')

    logo_id = db.Column('logo_id', db.String(1024), ForeignKey('imageobject.guid'))
    logo = db.relationship('ImageObject', foreign_keys='logo_id')
    
    manufacturer_id = db.Column('manufacturer', db.String(1024), ForeignKey('organization.guid'))
    manufacturer = db.relationship('organization', foreign_keys='manufacturer_id')

    images = db.relationship('image_object', secondary='ProductImages')
    offers = db.relationship('offers', secondary='ProductOffers')
    requests = db.relationship('requests', secondary='ProductRequests')
    
    comments = db.relationship('comment', secondary='ProductComments')
    actions = db.relationship('action', secondary='ProductActions')

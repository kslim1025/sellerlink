
from database import db

from models.thing import Thing
from models.geo_coords import GeoCoords

"""
class PlaceActions(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    place_id = db.Column('place_id', db.String(1024), db.ForeignKey('place.guid'))
    action_id = db.Column('action_id', db.String(1024), db.ForeignKey('action.guid'))

class PlaceComments(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    place_id = db.Column('place_id', db.String(1024), db.ForeignKey('place.guid'))
    comment_id = db.Column('comment_id', db.String(1024), db.ForeignKey('comment.guid'))

class PlaceEvents(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    event_id = db.Column('product_id', db.String(1024), db.ForeignKey('event.guid'))
    place_id = db.Column('place_id', db.String(1024), db.ForeignKey('place.guid'))

class PlaceServices(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    service_id = db.Column('service_id', db.String(1024), db.ForeignKey('service.guid'))
    place_id = db.Column('place_id', db.String(1024), db.ForeignKey('place.guid'))

class PlaceProducts(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    product_id = db.Column('product_id', db.String(1024), db.ForeignKey('product.guid'))
    place_id = db.Column('place_id', db.String(1024), db.ForeignKey('place.guid'))

class PlaceImages(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    place_id = db.Column('place_id', db.String(1024), db.ForeignKey('place.guid'))
    image_id = db.Column('image_id', db.String(1024), db.ForeignKey('imageobject.guid'))
"""

class Place(Thing, db.Model):
    
    telephone = db.Column('telephone', db.String(1024))
    faxNumber = db.Column('faxNumber', db.String(1024))
    branchCode = db.Column('branchCode', db.String(1024))
    
    geo_id = db.Column('geo_id', db.String(1024), db.ForeignKey('geocoords.guid'))
    geo = db.relationship('GeoCoords')
        
    # geo_box
    
    #images = db.relationship('image_object', secondary='PlaceImages')
        
    #products = db.relationship('products', secondary='PlaceProducts')
    #services = db.relationship('services', secondary='PlaceServices')
        
    #events = db.relationship('events', secondary='PlaceEvents')
        
    #comments = db.relationship('comments', secondary='PlaceComments')
    #actions = db.relationship('actions', secondary='PlaceActions')

    discriminator = db.Column('type', db.String(100))
    __mapper_args__ = {'polymorphic_on': discriminator}
    

from sqlalchemy.ext.declarative import declared_attr

from database import db

from models.thing import Thing, GUID
from models.geo_coords import GeoCoords
from models.organization import Organization

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
    
    address_id = db.Column('address_id', db.String(1024), db.ForeignKey('postaladdress.guid'))
    address = db.relationship('PostalAddress')
    
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

class LocalBusiness(Place):
    __mapper_args__ = {'polymorphic_identity': 'localbusiness'}
    id = db.Column(GUID(), db.ForeignKey('place.guid'), primary_key=True)
    
    currenciesAccepted = db.Column('currenciesAccepted', db.String(1024)) #	The currency accepted (in ISO 4217 currency format).
    # openingHours = db.Column('openingHours',  The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.
    """
    Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su.
    Times are specified using 24:00 time. For example, 3pm is specified as 15:00.
    Here is an example: <time itemprop="openingHours" datetime="Tu,Th 16:00-20:00">Tuesdays and Thursdays 4-8pm</time>.
    If a business is open 7 days a week, then it can be specified as <time itemprop="openingHours" datetime="Mo-Su">Monday through Sunday, all day</time>.
    """
    
    paymentAccepted = db.String('paymentAccepted', db.String(1024))	 # Cash, credit card, etc.
    priceRange  = db.String('priceRange', db.String(1024))
    
    # organization = db.relationship()

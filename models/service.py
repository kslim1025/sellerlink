
from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import Thing

"""
class ServiceOpeningHours(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    service_id = db.Column('service_id', db.String(1024), ForeignKey('service.guid'))
    openhours_id = db.Column('openhours_id', db.String(1024), ForeignKey('openinghours.guid'))

class ServiceActions(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    service_id = db.Column('service_id', db.String(1024), ForeignKey('service.guid'))
    action_id = db.Column('action_id', db.String(1024), ForeignKey('action.guid'))

class ServiceComments(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    service_id = db.Column('service_id', db.String(1024), ForeignKey('service.guid'))
    comment_id = db.Column('comment_id', db.String(1024), ForeignKey('comment.guid'))

class ServiceOffers(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))
    item_id = db.Column('item_id', db.String(1024), ForeignKey('service.guid'))

class ServiceRequests(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    request_id = db.Column('request_id', db.String(1024), ForeignKey('request.guid'))
    item_id = db.Column('item_id', db.String(1024), ForeignKey('service.guid'))

class ServiceAreas(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    place_id = db.Column('place_id', db.String(1024), ForeignKey('place.guid'))
    service_id = db.Column('service_id', db.String(1024), ForeignKey('service.guid'))
"""

class Service(db.Model, Thing):
    category = db.Column('category', db.String(1024))
    serviceType = db.Column('serviceType', db.String(1024))

    areaServed = db.Column('areaServed', db.String(1024))
    
    #logo_id = db.Column('logo_id', db.String(1024), ForeignKey('imageobject.guid'))    
    #provider_id = db.Column('provider_id', db.String(1024), ForeignKey('person.guid'))

    #logo = db.relationship('image_object')
    #provider = db.relationship('Person')
    
    #actions = db.relationship('Action', secondary=ServiceActions)
    #comments = db.relationship('Comment', secondary=ServiceComments)
    
    #offers = db.relationship('Offer', secondary=ServiceOffers)
    #requests = db.relationship('Request', secondary=ServiceRequests)
    
    #openHours = db.relationship('Openinghours', secondary=ServiceOpeningHours)
    #areaServed = db.relationship('Place', secondary=ServiceAreas)


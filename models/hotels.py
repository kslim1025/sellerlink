
from database import db
from sqlalchemy.schema import ForeignKey

from models import common

# Room/Product and RoomOffers for availability calendar
class RoomOffers(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))
    room_id = db.Column('room_id', db.String(1024), ForeignKey('room.guid'))

class RoomRequests(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    request_id = db.Column('request_id', db.String(1024), ForeignKey('request.guid'))
    room_id = db.Column('room_id', db.String(1024), ForeignKey('room.guid'))

class Room(db.Model, Thing):
    telephone = db.Column('telephone', db.String(1024)) 
    smokingAllowed = db.Column('smokingAllowed', db.Boolean)
    petsAllowed = db.Column('petsAllowed', db.String(1024))
    alternateName = db.Column('alternateName', db.String(1024))
    permittedUsage = db.Column('permittedUsage', db.String(1024))
    branchCode = db.Column('branchCode', db.String(1024))
    faxNumber = db.Column('faxNumber', db.String(1024))
    floorSize = db.Column('floorSize', db.Integer)
    globalLocationNumber = db.Column('globalLocationNumber', db.String(1024))

    isicV4 = db.Column('isicV4', db.String(1024))
    logo_id = db.Column('logo_id', db.String(1024), ForeignKey('image_object.guid'))
    image_id = db.Column('image_id', db.String(1024), ForeignKey('image_object.guid'))
    containsPlace_id = db.Column('containsPlace_id', db.String(1024), ForeignKey('place.guid'))
    
#amenityFeature = db.relationship('LocationFeatureSpecification')
#geo = db.relationship('GeoCoordinates')
#geo_id = db.Column('geo_id', db.String(1024), ForeignKey('GeoCoordinates.guid'))
#amenityFeature_id = db.Column('amenityFeature_id', db.String(1024), ForeignKey('LocationFeatureSpecification.guid'))

class HotelOpeningHours(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    hotel_id = db.Column('hotel_id', db.String(1024), ForeignKey('hotel.guid'))
    openhours_id = db.Column('openhours_id', db.String(1024), ForeignKey('openinghours.guid'))

class HotelActions(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    hotel_id = db.Column('hotel_id', db.String(1024), ForeignKey('hotel.guid'))
    action_id = db.Column('action_id', db.String(1024), ForeignKey('action.guid'))

class HotelComments(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    hotel_id = db.Column('hotel_id', db.String(1024), ForeignKey('hotel.guid'))
    comment_id = db.Column('comment_id', db.String(1024), ForeignKey('comment.guid'))

class HotelOffers(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))
    hotel_id = db.Column('item_id', db.String(1024), ForeignKey('hotel.guid'))

class HotelRequests(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    offer_id = db.Column('request_id', db.String(1024), ForeignKey('request.guid'))
    hotel_id = db.Column('item_id', db.String(1024), ForeignKey('hotel.guid'))

class HotelImages(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    image_id = db.Column('image_id', db.String(1024), ForeignKey('image_object.guid'))
    hotel_id = db.Column('hotel_id', db.String(1024), ForeignKey('hotel.guid'))

class Hotel(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    name = db.Column('name', db.String(1024))
    url = db.Column('url', db.String(1024))
    sameAs = db.Column('sameAs', db.String(1024)) 
    address = db.Column('address', db.String(1024))
    branchCode = db.Column('branchCode', db.String(1024))
    naics = db.Column('naics', db.String(1024))

    areaServed_id = db.Column('areaServed_id', db.String(1024), ForeignKey('place.guid'))
    areaServed = db.relationship('place', foreign_keys='areaServed_id')
    location_id = db.Column('location_id', db.String(1024), ForeignKey('place.guid'))
    location = db.relationship('place', foreign_keys='location_id')
    containedInPlace_id = db.Column('containedInPlace_id', db.String(1024), ForeignKey('place.guid'))
    containedInPlace = db.relationship('Place', foreign_keys='containedInPlace_id')

    faxNumber = db.Column('faxNumber', db.String(1024))
    taxID = db.Column('taxID', db.String(1024))
    award = db.Column('award', db.String(1024))
    dissolutionDate = db.Column('dissolutionDate', db.DateTime)
    legalName = db.Column('legalName', db.String(1024))
    telephone = db.Column('telephone', db.String(1024))
    currenciesAccepted = db.Column('currenciesAccepted', db.String(1024))
    isicV4 = db.Column('isicV4', db.String(1024))
    description = db.Column('description', db.String(1024))
    alternateName = db.Column('alternateName', db.String(1024))
    priceRange = db.Column('priceRange', db.String(1024))
    paymentAccepted = db.Column('paymentAccepted', db.String(1024))
    brand_id = db.Column('brand_id', db.String(1024), ForeignKey('organization.guid'))
    brand = db.relationship('organization')
    openingHours = db.relationship('HotelOpeningHours', secondary='hotel_opening_hours')
    owner_id = db.Column('owner_id', db.String(1024), ForeignKey('person.guid'))
    owner = db.relationship('person', foreign_keys='owner_id')
    photo_id = db.Column('photo_id', db.String(1024), ForeignKey('image_object.guid'))
    photo = db.relationship('imageobject', foreign_keys='photo_id')
    logo_id = db.Column('logo_id', db.String(1024), ForeignKey('image_object.guid'))
    logo = db.relationship('imageobject', foreign_keys='logo_id')
    # event, review
    offers = db.relationship('offers', secondary=HotelOffers)



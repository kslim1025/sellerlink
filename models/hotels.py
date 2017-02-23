
from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import GUID
from models.place import LocalBusiness

"""
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
"""
 
#amenityFeature = db.relationship('LocationFeatureSpecification')
#geo = db.relationship('GeoCoordinates')
#geo_id = db.Column('geo_id', db.String(1024), ForeignKey('GeoCoordinates.guid'))
#amenityFeature_id = db.Column('amenityFeature_id', db.String(1024), ForeignKey('LocationFeatureSpecification.guid'))

"""
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
"""

class LodgingBusiness(LocalBusiness):

    # amenityFeature, audience, availableLanguage, checkinTime, checkoutTime, petsAllowed, starRating
    license_number = db.Column('license_number', db.String(1000))
    license_expiry = db.Column('license_expiry', db.DateTime())

    last_inspection = db.Column('last_inspection', db.DateTime())
    status_code = db.Column('status_code', db.String(1000))

    checkinTime = db.Column('checkinTime', db.DateTime())
    checkoutTime = db.Column('checkoutTime', db.DateTime())
    rooms = db.Column('rooms', db.Integer())

    __mapper_args__ = {'polymorphic_identity': 'lodgingbusiness'}
    id = db.Column(GUID(), db.ForeignKey('local_business.id'), primary_key=True)

class Hotel(LodgingBusiness):

    """
    areaServed_id = db.Column('areaServed_id', db.String(1024), ForeignKey('place.guid'))
    areaServed = db.relationship('place', foreign_keys='areaServed_id')
    location_id = db.Column('location_id', db.String(1024), ForeignKey('place.guid'))
    location = db.relationship('place', foreign_keys='location_id')
    containedInPlace_id = db.Column('containedInPlace_id', db.String(1024), ForeignKey('place.guid'))
    containedInPlace = db.relationship('Place', foreign_keys='containedInPlace_id')
    """

    __mapper_args__ = {'polymorphic_identity': 'hotel'}
    id = db.Column(GUID(), db.ForeignKey('lodging_business.id'), primary_key=True)

class Motel(LodgingBusiness):
    __mapper_args__ = {'polymorphic_identity': 'motel'}
    id = db.Column(GUID(), db.ForeignKey('lodging_business.id'), primary_key=True)

class BedAndBreakfast(LodgingBusiness):
    __mapper_args__ = {'polymorphic_identity': 'bedandbreakfast'}
    id = db.Column(GUID(), db.ForeignKey('lodging_business.id'), primary_key=True)

class Resort(LodgingBusiness):
    __mapper_args__ = {'polymorphic_identity': 'resort'}
    id = db.Column(GUID(), db.ForeignKey('lodging_business.id'), primary_key=True)



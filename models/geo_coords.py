
from database import db

from models.thing import Thing, GUID

class PostalAddress(Thing, db.Model):

    streetAddress = db.Column('streetAddress', db.String(1024))
    streetAddress2 =db.Column('streetAddress2', db.String(1024))
    streetAddress3 = db.Column('streetAddress3', db.String(1024))
    postOfficeBoxNumber = db.Column('postOfficeBoxNumber', db.String(1024))
    addressLocality = db.Column('addressLocality', db.String(1024))
    postalCode = db.Column('postalCode', db.String(24))
    addressCountry = db.Column('addressCountry', db.String(1024))
    addressRegion = db.Column('addressRegion', db.String(1024))

    geo_id = db.Column('geo_id', GUID(), db.ForeignKey('geocoords.guid'))
    geo = db.relationship('GeoCoords', cascade="all,delete")
 
    # ContactPoint
    
class GeoCoords(Thing, db.Model):
    __table_args__ = (db.Index('uix_1', 'latitude', 'longitude', unique=True),)
    
    latitude = db.Column('latitude', db.Numeric(precision='23,20')) #String(32)) #Float(precision='23,20') ) # 41.8645403460001
    longitude = db.Column('longitude', db.Numeric(precision='23,20')) #String(32)) #Float(precision='23,20') )
    elevation = db.Column('elevation', db.Float)
    addressCountry = db.Column('addressCountry', db.String(1024))
    postalCode = db.Column('postalCode', db.String(24))

    accuracy = db.Column('accuracy', db.Integer) # Accuracy radius in meters
    

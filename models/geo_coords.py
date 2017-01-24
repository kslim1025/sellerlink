
from database import db

from models.thing import Thing

class PostalAddress(Thing, db.Model):
    addressCountry = db.Column('addressCountry', db.String(1024))
    addressLocality = db.Column('addressLocality', db.String(1024))
    addressRegion = db.Column('addressRegion', db.String(1024))
    postOfficeBoxNumber = db.Column('postOfficeBoxNumber', db.String(1024))
    postalCode = db.Column('postalCode', db.String(1024))
    streetAddress = db.Column('streetAddress', db.String(1024))
    
    # ContactPoint
    
class GeoCoords(Thing, db.Model):
    latitude = db.Column('latitude', db.String(1024))
    longitude = db.Column('longitude', db.String(1024))
    elevation = db.Column('elevation', db.String(1024))
    addressCountry = db.Column('addressCountry', db.String(1024))
    postalCode = db.Column('postalCode', db.String(1024))
        

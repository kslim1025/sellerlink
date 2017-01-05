
from database import db

from models.thing import Thing

class GeoCoords(Thing, db.Model):
    latitude = db.Column('latitude', db.String(1024))
    longitude = db.Column('longitude', db.String(1024))
    elevation = db.Column('elevation', db.String(1024))
    addressCountry = db.Column('addressCountry', db.String(1024))
    postalCode = db.Column('postalCode', db.String(1024))
        

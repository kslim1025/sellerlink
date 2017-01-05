
from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import Thing

# itemavailability
class RequestAreas(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    place_id = db.Column('place_id', db.String(1024), ForeignKey('place.guid'))
    request_id = db.Column('request_id', db.String(1024), ForeignKey('request.guid'))


class Request(db.Model, Thing):
    availabilityStarts = db.Column('availabilityStarts', db.DateTime)
    availabilityEnds = db.Column('availabilityEnds', db.DateTime)
    priceValidUntil = db.Column('priceValidUntil', db.DateTime)
    deliveryLeadTime = db.Column('deliveryLeadTime', db.Integer)
    sku = db.Column('sku', db.String(1024))
    category = db.Column('category', db.String(1024))
    mpn = db.Column('mpn', db.String(1024))
    price = db.Column('price', db.String(1024))
    priceCurrency = db.Column('priceCurrency', db.String(1024))
    alternateName = db.Column('alternateName', db.String(1024))
    gtin8 = db.Column('gtin8', db.String(1024))
    gtin14 = db.Column('gtin14', db.String(1024))
    gtin13 = db.Column('gtin13', db.String(1024))
    gtin12 = db.Column('gtin12', db.String(1024))

    buyer_id = db.Column('buyer_id', db.String(1024), ForeignKey('person.guid'))
    buyer = db.relationship('person')
    
    areaServed = db.relationship('place', secondary='RequestAreas')
    


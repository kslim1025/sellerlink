
from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import Thing

"""
class OfferComments(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    comment_id = db.Column('comment_id', db.String(1024), ForeignKey('comment.guid'))
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))

class OfferActions(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    action_id = db.Column('action_id', db.String(1024), ForeignKey('action.guid'))
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))

class OfferAreas(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    place_id = db.Column('place_id', db.String(1024), ForeignKey('place.guid'))
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))
"""

# itemavailability

class Offer(Thing, db.Model):
    
    advanceBookingRequirement = db.Column(db.String(1024))
    aggregateRating = db.Column(db.String(1024))
    
    eligibleDuration = db.Column(db.String(1024))
    eligibleQuantity = db.Column(db.String(1024))
    
    inventoryLevel = db.Column(db.String(1024))

    serialNumber = db.Column(db.String(1024))
    validFrom = db.Column(db.DateTime)
    validThrough = db.Column(db.DateTime)
    
    availabilityStarts = db.Column('availabilityStarts', db.DateTime)
    availabilityEnds = db.Column('availabilityEnds', db.DateTime)
    deliveryLeadTime = db.Column('deliveryLeadTime', db.Integer)
    
    category = db.Column('category', db.String(1024))
    
    price = db.Column('price', db.String(1024))
    priceCurrency = db.Column('priceCurrency', db.String(1024))
    priceValidUntil = db.Column('priceValidUntil', db.DateTime)

    sku = db.Column('sku', db.String(1024))
    mpn = db.Column('mpn', db.String(1024))
    gtin8 = db.Column('gtin8', db.String(1024))
    gtin12 = db.Column('gtin12', db.String(1024))
    gtin13 = db.Column('gtin13', db.String(1024))
    gtin14 = db.Column('gtin14', db.String(1024))

    #acceptedPaymentMethod #PaymentMethod, LoanOrCredit
    #addOn #Offers
    #availability #ItemAvailability
    #availabilityAtOrFrom #Place
    #availableDeliveryMethod #DeliveryMethod
    #businessFunction #sell, lease, repair, dispose...

    #eligibleCustomerType #BusinessEntityType
    #eligibleTransactionVolume #PriceSpecification
    #eligibleRegion #Place
    #includesObject #TypeAndQuantityNode
    #ineligibleRegion #GeoShape, Place
    #itemCondition = db.Colume(db.String(1024)) #OfferItemCondition
    #itemOffered #Person
    #warranty #WarrantyPromise

    #offeredBy
    #seller_id = db.Column('seller_id', db.String(1024), ForeignKey('person.guid'))
    #seller = db.relationship('Person')              
    
    #areaServed = db.relationship('Place', secondary='OfferAreas')
    
    #comments = db.relationship('Comment', secondary='OfferComments')
    #actions = db.relationship('Action', secondary='OfferActions')
    
    #review

    discriminator = db.Column('type', db.String(100))
    __mapper_args__ = {'polymorphic_on': discriminator}

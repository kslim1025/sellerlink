
from database import db
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declared_attr

from models.thing import Thing, GUID
from models.geo_coords import PostalAddress

class OrgAreas(db.Model):
    guid = db.Column('guid', GUID(), primary_key=True)
    org_id = db.Column('org_id', db.String(32), ForeignKey('organization.guid'))
    place_id = db.Column('place_id', db.String(32), ForeignKey('place.guid'))
   

class Organization(db.Model, Thing):
    
    legalName = db.Column('legalName', db.String(1024)) 
    """ an orgs legal name"""
    foundingDate = db.Column('foundingDate', db.DateTime)
    telephone = db.Column('telephone', db.String(1024))
    duns = db.Column('duns', db.String(1024))

    address_id = db.Column('address_id', GUID(), db.ForeignKey('postaladdress.guid'))
    address = db.relationship('PostalAddress')

    #founder_id = db.Column('founder_id', db.String(1024), ForeignKey('person.guid'))
    #founder = db.relationship('person')
    #areaServed = db.relationship('Place', secondary='OrgAreas')

    # aggregateRating, alumni, award, brand, contactPoint, department, dissolutionDate, duns, email
    # employee, event, faxNumber, founder, foundingDate, foundingLocation, funder, globalLocationNumber
    # hasOfferCatalog, hasPOS, isicV4, leiCode, location, logo, makesOffer, member, memberOf, naics
    # numberOfEmployees, owns, parentOrganization, review, seeks, sponsor, subOrganization, taxID, vatID


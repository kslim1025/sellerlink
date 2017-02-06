
from database import db
from sqlalchemy.schema import ForeignKey
from sqlalchemy.ext.declarative import declared_attr

from models.thing import Thing

class OrgAreas(db.Model):
    guid = db.Column('guid', db.String(1000), primary_key=True)
    org_id = db.Column('org_id', db.String(1000), ForeignKey('organization.guid'))
    place_id = db.Column('place_id', db.String(1000), ForeignKey('place.guid'))
   

class Organization(Thing):
    
    legalName = db.Column('legalName', db.String(1024)) 
    """ an orgs legal name"""
    foundingDate = db.Column('foundingDate', db.DateTime)
    telephone = db.Column('telephone', db.String(1024))
    duns = db.Column('duns', db.String(1024))

    #founder_id = db.Column('founder_id', db.String(1024), ForeignKey('person.guid'))
    #founder = db.relationship('person')
    #areaServed = db.relationship('Place', secondary='OrgAreas')

class OrgTable(Organization, db.Model):

    @declared_attr
    def __tablename__(cls):
        return "organization"
    


from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import Thing

class OrgAreas(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    org_id = db.Column('org_id', db.String(1024), ForeignKey('organization.guid'))
    place_id = db.Column('place_id', db.String(1024), ForeignKey('place.guid'))
   

class Organization(db.Model, Thing):
    legalName = db.Column('legalName', db.String(1024))
    foundingDate = db.Column('foundingDate', db.DateTime)
    telephone = db.Column('telephone', db.String(1024))
    duns = db.Column('duns', db.String(1024))

    founder_id = db.Column('founder_id', db.String(1024), ForeignKey('person.guid'))

    founder = db.relationship('person')
    areaServed = db.relationship('Place', secondary='OrgAreas')


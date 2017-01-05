
from database import db

from models.thing import Thing

"""
#follows, notification settings
class PersonFollows(db.Model):
    pass

# tracking history
class PersonHistory(db.Model):
    pass

# authentication
class PersonAuth(db.Model):
    pass

# active sessions and history
class PersonSession(db.Model):
    pass
"""

class PersonRelated(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    parent_id = db.Column('parent_id', db.String(1024), db.ForeignKey('person.guid'))
    person_id = db.Column('person_id', db.String(1024), db.ForeignKey('person.guid'))
    relation_type = db.Column('relation_type', db.String(1024))    

class PersonWorksFor(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    person_id = db.Column('person_id', db.String(1024), db.ForeignKey('person.guid'))
    organization_id = db.Column('organization_id', db.String(1024), db.ForeignKey('organization.guid'))

class PersonAffiliatedWith(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    person_id = db.Column('person_id', db.String(1024), db.ForeignKey('person.guid'))
    organization_id = db.Column('organization_id', db.String(1024), db.ForeignKey('organization.guid'))


class Person(Thing, db.Model):
    __tablename__ = "person"
    
    jobTitle = db.Column('jobTitle', db.String(1024))
    weight = db.Column('weight', db.Integer)
    gender = db.Column('gender', db.String(1024))
    additionalName = db.Column('additionalName', db.String(1024))
    honorificSuffix = db.Column('honorificSuffix', db.String(1024))
    email = db.Column('email', db.String(1024), unique=True)
    address = db.Column('address', db.String(1024))
    givenName = db.Column('givenName', db.String(1024))
    birthDate = db.Column('birthDate', db.DateTime)
    familyName = db.Column('familyName', db.String(1024))

    """
    parent = db.relationship('Person', secondary='PersonRelated', primaryjoin=db.and_(
            PersonRelated.person_id == Person.guid,
            PersonRelated.relation_type == "Parent") )
    spouse = db.relationship('Person', secondary='PersonRelated', primaryjoin=db.and_(
            PersonRelated.person_id == Person.guid,
            PersonRelated.relation_type == "Spouse") )
    """
    
    worksFor = db.relationship('organization', secondary=PersonWorksFor, foreign_keys='person_id')
    affiliation = db.relationship('organization', secondary=PersonAffiliatedWith, foreign_keys='person_id')


# XXX add_parent, add_spouse


from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import Thing

class EventOrganizers(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    person_id = db.Column('person_id', db.String(1024), ForeignKey('person.guid'))
    event_id = db.Column('event_id', db.String(1024), ForeignKey('event.guid'))
    status = db.Column('status', db.String(1024))

class EventAttendees(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    person_id = db.Column('person_id', db.String(1024), ForeignKey('person.guid'))
    event_id = db.Column('event_id', db.String(1024), ForeignKey('event.guid'))
    status = db.Column('status', db.String(1024))
    
class EventOffers(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    offer_id = db.Column('offer_id', db.String(1024), ForeignKey('offer.guid'))
    event_id = db.Column('event_id', db.String(1024), ForeignKey('event.guid'))

class EventStatusType(db.Model, Thing):
    pass
    
class Event(db.Model, Thing):
    inLanguage = db.Column('inLanguage', db.String(1024))
    startDate = db.Column('startDate', db.DateTime)
    endDate = db.Column('endDate', db.DateTime)
    doorTime = db.Column('doorTime', db.DateTime)
        
    attendee_id = db.Column('attendee_id', db.String(1024), ForeignKey('person.guid'))
    organizer_id = db.Column('organizer_id', db.String(1024), ForeignKey('person.guid'))
    offers_id = db.Column('offers_id', db.String(1024), ForeignKey('offer.guid'))        
    eventStatus_id = db.Column('eventStatus_id', db.String(1024), ForeignKey('eventstatustype.guid'))
       
    attendee = db.relationship('Person', secondary='EventAttendees')
    organizer = db.relationship('Person', secondary='EventOrganizers')
    offers = db.relationship('Offer', secondary='EventOffers')        
    eventStatus = db.relationship('EventStatusType')



from database import db

from models.thing import Thing

class ActionStatusType(db.Model, Thing):
    __tablename__ = "actionstatustype"
    
    

class ActionParticipants(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    action_id = db.Column('action_id', db.String(1024), db.ForeignKey('action.guid'))
    person_id = db.Column('person_id', db.String(1024), db.ForeignKey('person.guid'))

    
class Action(db.Model, Thing):
    __tablename__ = "action"

    startTime = db.Column('startTime', db.DateTime)
    endTime = db.Column('endTime', db.DateTime)
        
    agent_id = db.Column('agent_id', db.String(1024), db.ForeignKey('person.guid'))
    participant_id = db.Column('participant_id', db.String(1024), db.ForeignKey('person.guid'))
    actionStatus_id = db.Column('actionStatus_id', db.String(1024), db.ForeignKey('actionstatustype.guid'))
    
    agent = db.relationship('Person', foreign_keys='agent_id')
    participant = db.relationship('Person', secondary='ActionParticipants')
    actionStatus = db.relationship('ActionStatusType')
    
    target_type = db.Column('target_type', db.String(1024)) 
    target_id = db.Column('target_id', db.String(1024)) # FK? EntryPoint..
    object_id = db.Column('object_id', db.String(1024)) # FK? Thing..
    result_id = db.Column('result_id', db.String(1024)) # FK? Thing..
    
    #instrument = db.relationship('Thing')    
    #target = db.relationship('EntryPoint')
    #object = db.relationship('Thing')
    

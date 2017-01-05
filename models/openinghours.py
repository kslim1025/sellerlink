
from database import db

from models.thing import Thing

class OpeningHours(db.Model, Thing):
    __tablename__ = "openinghours"

    thing_type = db.Column('thing_type', db.String(1024))
    thing_id = db.Column('thing_id', db.String(1024), index=True)
    
    closes = db.Column('closes', db.DateTime)
    opens = db.Column('opens', db.DateTime)
    dayOfWeek = db.Column('DayOfWeek', db.String(1024))
    validThrough = db.Column('validThrough', db.DateTime)
    validFrom = db.Column('validFrom', db.DateTime)


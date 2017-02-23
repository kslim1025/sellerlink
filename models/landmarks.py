
from database import db

from models.thing import GUID
from models.place import Place

class Landmark(Place):
    __mapper_args__ = {'polymorphic_identity': 'landmark'}

    id = db.Column(GUID(), db.ForeignKey('place.guid'), primary_key=True)
    landmark_category = db.Column('landmark_category', db.String(1024))

    def __repr__(self):
        return "<Landmark(id=%s, place_guid=%s, geo_id=%s)>" % (self.id, self.guid, self.geo_id)


from database import db

from models.thing import GUID
from models.place import Place

class HistoricPlace(Place):
    __mapper_args__ = {'polymorphic_identity': 'historicplace'}

    id = db.Column(GUID(), db.ForeignKey('place.guid'), primary_key=True)

    def __repr__(self):
        return "<HistoricPlace(id=%s, place_guid=%s, geo_id=%s)>" % (self.id, self.guid, self.geo_id)
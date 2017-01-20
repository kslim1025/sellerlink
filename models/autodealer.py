
from database import db

from models.thing import GUID
from models.place import LocalBusiness

class AutomotiveBusiness(LocalBusiness):
    __mapper_args__ = {'polymorphic_identity': 'automotivebusiness'}

    id = db.Column(GUID(), db.ForeignKey('local_business.id'), primary_key=True)

class AutoDealer(AutomotiveBusiness):
    __mapper_args__ = {'polymorphic_identity': 'autodealer'}

    id = db.Column(GUID(), db.ForeignKey('automotive_business.id'), primary_key=True)


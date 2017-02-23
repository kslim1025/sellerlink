
from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def drop_all():
    db.drop_all()


def create_all():
    db.create_all()


def remove_session():
    db.session.remove()

def init(app):
    db.app = app
    db.init_app(app)
    
def get_or_create(session, model, **kwargs):
    
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance, True
    else:
        params = dict( (k,v) for k,v in kwargs.iteritems() )
        instance = model(**params)
	session.add( instance )
        return instance, False

def get_config_db():

	from config import prod as config

	from app import create_app

	from models import thing
	from models import place, organization
	from models import geo_coords
	from models import autodealer
	from models import historicplace
	from models import landmarks
	import models.hotels
	#import models.restaurant

	application = create_app(config)

	init(application)
       
	return db.metadata


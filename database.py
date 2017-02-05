
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
        return instance
    else:
        params = dict( (k,v) for k,v in kwargs.iteritems() )
        instance = model(**params)
        return instance
        

from sqlalchemy.sql.expression import func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import UUID
import uuid

class GUID(TypeDecorator):
    """Platform-independent GUID type.

    Uses Postgresql's UUID type, otherwise uses
    CHAR(32), storing as stringified hex values.

    """
    impl = CHAR

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            return dialect.type_descriptor(UUID())
        else:
            return dialect.type_descriptor(CHAR(32))

    def process_bind_param(self, value, dialect):
        if value is None:
            return value
        elif dialect.name == 'postgresql':
            return str(value)
        else:
            if not isinstance(value, uuid.UUID):
                return "%.32x" % uuid.UUID(value).int
            else:
                # hexstring
                return "%.32x" % value.int

    def process_result_value(self, value, dialect):
        if value is None:
            return value
        else:
            return uuid.UUID(value)
            
from database import db

# XXX Versioning

class Thing(object):
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
        
    guid = db.Column('guid', GUID(), primary_key=True, default=uuid.uuid4)
    description = db.Column('description', db.Text, nullable=True)
    name = db.Column('name', db.String(1024))
    alternateName = db.Column('alternateName', db.String(1024), nullable=True)
    sameAs = db.Column('sameAs', db.String(1024), nullable=True) 
    url = db.Column('url', db.String(1024), nullable=True)
    
    date_created = db.Column('date_created', db.DateTime, default=func.now())
    date_modified = db.Column('date_modified', db.DateTime, onupdate=func.utc_timestamp(), nullable=True)

    #location_id = db.Column('location_id', db.String(1024), db.ForeignKey('place.guid'))
    #location = db.relationship('Place')
    
    """
    @declared_attr
    def image_id(cls):
        return db.Column('image_id', db.String(1024), db.ForeignKey('imageobject.guid'))
    
    @declared_attr
    def image(cls):
        return db.relationship('ImageObject')
        
    @declared_attr
    def potentialAction_id(cls):
        return db.Column('potentialAction_id', db.String(1024), db.ForeignKey('action.guid'))
        
    @declared_attr
    def potentialAction(cls):
        return db.relationship('Action')
    """    


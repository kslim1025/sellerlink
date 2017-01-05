
from database import db

from models.thing import Thing


class ImageObject(db.Model, Thing):
    
    datePublished = db.Column('datePublished', db.DateTime)
    keywords = db.Column('keywords', db.String(1024))
    contentRating = db.Column('contentRating', db.String(1024))
    width = db.Column('width', db.Integer)
    height = db.Column('height', db.Integer)
    fileFormat = db.Column('fileFormat', db.String(1024))
    contentSize = db.Column('contentSize', db.String(1024))
    sourceUrl = db.Column('sourceURL', db.String(1024))
    exifData = db.Column('exifData', db.String(1024))
    
    uploaded_by = db.Column('uploaded_by', db.String(1024), db.ForeignKey('person.guid'))


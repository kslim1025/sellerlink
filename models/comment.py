
from database import db
from sqlalchemy.schema import ForeignKey

from models.thing import Thing

class CommentAuthor(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    person_id = db.Column('person_id', db.String(1024), ForeignKey('person.guid'))
    comment_id = db.Column('comment_id', db.String(1024), ForeignKey('comment.guid'))
    
class CommentResponsible(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    person_id = db.Column('person_id', db.String(1024), ForeignKey('person.guid'))
    comment_id = db.Column('comment_id', db.String(1024), ForeignKey('comment.guid'))
        
class Comment(db.Model, Thing):
    status = db.Column('status', db.String(1024))
    datePublished = db.Column('datePublished', db.DateTime)
    alternativeHeadline = db.Column('alternativeHeadline', db.String(1024))
    text = db.Column('text', db.Text)

    contentLocation_id = db.Column('contentLocation_id', db.String(1024), ForeignKey('place.guid'))
    creator_id = db.Column('creator_id', db.String(1024), ForeignKey('person.guid'))
    accountablePerson_id = db.Column('accountablePerson_id', db.String(1024), ForeignKey('person.guid'))    

    contentLocation = db.relationship('Place')        
    creator = db.relationship('Person', secondary='CommentAuthor')    
    accountablePerson = db.relationship('Person', secondary='CommentResponsible')

    keywords = db.Column('keywords', db.String(1024))
    headline = db.Column('headline', db.String(1024))
    contentRating = db.Column('contentRating', db.String(1024))


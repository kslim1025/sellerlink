
from flask import Blueprint, render_template, abort, request
from flask import flash, url_for, redirect
from jinja2 import TemplateNotFound
import json


blueprint = Blueprint('api', __name__,
                        template_folder='../templates')

from database import db

from models.restaurant import Restaurant
from models.geo_coords import GeoCoords

# XXX oauth, and rate limiting

class APIQuery(object):
    def __init__(self, cls):
        self.cls = cls
        self.ignoreKeys = ["discriminator"]
        
    def query_json(self):
        obj = self.cls().query.all()
        
        ret = []
        for row in obj:
            o = {}
            for col in row.__dict__.keys():
                if col[0] == "_": continue 
                if col in self.ignoreKeys: continue
            
                o[col] = str(getattr(row, col))
            ret.append( o )

        return json.dumps(ret)
        
        
@blueprint.route('/restaurant.json')
def restaurant_query():
    return APIQuery(Restaurant).query_json()


@blueprint.route('/geocoords.json')
def geocoords_query():
    return APIQuery(GeoCoords).query_json()


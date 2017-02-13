
import json, sys
from geojson import FeatureCollection, Feature, Point
import geojson

from database import get_or_create
from models import geo_coords, landmarks

def insert_data(db):

	d = geojson.load(open("historic.geojson", "r+"))

	for x in list(d['features']):

		d = {}
		d['lat'] = x['geometry']['coordinates'][1]
		d['lng'] = x['geometry']['coordinates'][0]

		gc = geo_coords.GeoCoords()
		geo, isFound = get_or_create(db.session, geo_coords.GeoCoords, latitude=float(d['lat']), longitude=float(d['lng']))

		d = {}
		d['name'] = x['properties']['name'] if 'name' in x['properties'] else ""
		d['landmark_category'] = x['properties']['historic'] if 'historic' in x['properties'] else ""

		lp = landmarks.Landmark()
		lp.geo = geo
		lp.name = d['name'].encode('ascii', 'xmlcharrefreplace')
		lp.landmark_category = d['landmark_category']

		db.session.add(lp)

		db.session.commit()	
 

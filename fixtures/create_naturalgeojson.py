
import json, sys
from geojson import FeatureCollection, Feature, Point
import geojson

from models import geo_coords, landmarks
from database import get_or_create

def insert_data(db):

	"""
	ret = db.session.query(landmarks.Landmark).all()
	for x in ret:
		db.session.delete(x)
	db.session.commit()
	return
	"""

	d = geojson.load(open("natural.geojson", "r+"))

	for x in list(d['features']):

		lat = float( x['geometry']['coordinates'][1] )
		lng = float( x['geometry']['coordinates'][0] )

		gc = geo_coords.GeoCoords()
		geo, isFound = get_or_create(db.session, geo_coords.GeoCoords, latitude=lat, longitude=lng)

		lp = landmarks.Landmark()
		lp.name = x['properties']['name'].encode('ascii', 'xmlcharrefreplace') if 'name' in x['properties'] else ""
		lp.geo = geo
		lp.landmark_category = x['properties']['natural'] if 'natural' in x['properties'] else ""

		db.session.add(lp)

		db.session.commit()


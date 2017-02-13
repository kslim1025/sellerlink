
import json, sys
from geojson import FeatureCollection, Feature, Point
import geojson

from database import get_or_create
from models import geo_coords, landmarks

def test_data(db):
	d = geojson.load(open("historic.geojson", "r+"))

	mismatch = { 'name': [], 'geo': [], 'category': [] }

	data = {}
	ret = db.session.query(landmarks.Landmark).all()
	for row in ret:
		data[ row.name ] = row
	
	for x in list(d['features']):

		d = {}
		d['lat'] = x['geometry']['coordinates'][1]
		d['lng'] = x['geometry']['coordinates'][0]
		d['name'] = x['properties']['name'] if 'name' in x['properties'] else ""
		d['landmark_category'] = x['properties']['historic'] if 'historic' in x['properties'] else ""

		if d['name'] in data:
			k = d['name']
			match = 1

			if data[k].geo.latitude == d['lat'] and data[k].geo.longitude == d['lng']: match += 1
			else: mismatch['geo'].append( (d, "%s != %s or %s != %s" % (d['lat'], data[k].geo.latitude, d['lng'], data[k].geo.longitude)) )

			if data[k].landmark_category == d['landmark_category']: match += 1
			else: mismatch['category'].append( (d, "%s != %s" % (d['landmark_category'], data[k].landmark_category)) )

			if match == 3:
				del data[ k ]
		else: mismatch['name'].append( d )

	print len(data)
	for x in mismatch:
		print "%s: %d" % (x, len(mismatch[x]))

	print mismatch['name']

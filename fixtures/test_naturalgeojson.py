
import json, sys
from geojson import FeatureCollection, Feature, Point
import geojson

from models import geo_coords, landmarks

def test_data(db):

	mismatch = { 'name': [], 'geo': [], 'category': [] }

	cnt = 0
	total = 0

	d = geojson.load(open("natural.geojson", "r+"))
	for x in list(d['features']):

		lat = float( x['geometry']['coordinates'][1] )
		lng = float( x['geometry']['coordinates'][0] )

		name = x['properties']['name'].encode('ascii', 'xmlcharrefreplace') if 'name' in x['properties'] else ""
		landmark_category = x['properties']['natural'] if 'natural' in x['properties'] else ""

		total += 1
		row = db.session.query(landmarks.Landmark).filter(geo_coords.GeoCoords.latitude==lat, geo_coords.GeoCoords.longitude==lng)
		if row.count() == 1:
			row = row.first()

			match = 1

			if row.landmark_category == landmark_category: match += 1
			else: mismatch['category'].append( (d, "%s != %s" % (landmark_category, row.landmark_category)) )

			if row.name == name: match += 1
			else: mismatch['name'].append( (d, "%s != %s" % (name, row.name)) )

			if match == 3: cnt += 1
		else: mismatch['geo'].append( {'name': name} )

	print "%d vs %d total" % (cnt, total)
	for x in mismatch:
		print "%s: %d" % (x, len(mismatch[x]))

	print mismatch['name']



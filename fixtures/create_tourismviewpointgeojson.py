
import json, sys
from geojson import FeatureCollection, Feature, Point
import geojson

from models import geo_coords, landmarks
from database import get_or_create

def insert_data(db):

	d = geojson.load(open("tourism_viewpoint.geojson", "r+"))

	for x in list(d['features']):
        	if x['geometry']['type'] <> "Point":
			last = False
			avg = [0,0] 
			for coords in x['geometry']['coordinates'][0]:
				if last <> False: 
					avg[0] = (last[0] + coords[0])/2
					avg[1] = (last[1] + coords[1])/2
				last = coords
			x['geometry']['coordinates'] = avg

		lat = float( x['geometry']['coordinates'][1] )
		lng = float( x['geometry']['coordinates'][0] )

                gc = geo_coords.GeoCoords()
                geo, isFound = get_or_create(db.session, geo_coords.GeoCoords, latitude=lat, longitude=lng)

		lp = landmarks.Landmark()
		lp.name = x['properties']['name'].encode('ascii', 'xmlcharrefreplace') if 'name' in x['properties'] else ""
		lp.geo = geo
		lp.landmark_category = x['properties']['amenity'] if 'amenity' in x['properties'] else "viewpoint"

		db.session.add(lp)

		db.session.commit()


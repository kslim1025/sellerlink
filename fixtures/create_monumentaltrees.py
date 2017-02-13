
import json, sys
from lxml import etree

from models import geo_coords, landmarks

from database import get_or_create

def insert_data(db):

	d = etree.parse(open("monumentaltrees.xml", "r+")).getroot()

	for x in list(d):
		if x.tag == "m": 

			lat = float(x.attrib['lat'])
			lng = float(x.attrib['lng'])

	                gc = geo_coords.GeoCoords()
        	        geo, isFound = get_or_create(db.session, geo_coords.GeoCoords, latitude=lat, longitude=lng)

			lp = landmarks.Landmark()
			lp.name = x.attrib['t'].encode('ascii', 'xmlcharrefreplace')
			lp.url = "http://www.monumentaltrees.com/" + x.attrib['u']
			lp.geo = geo
			lp.landmark_category = "tree"

			db.session.add(lp)

			db.session.commit()

       

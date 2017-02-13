
import json, sys

from database import get_or_create
from models import geo_coords, landmarks

from lxml import etree

def test_data(db):

	mismatch = { 'name': [], 'geo': [], 'category': [] }

	data = {}
	ret = db.session.query(landmarks.Landmark).filter(landmarks.Landmark.url.like("http://www.monumentaltrees%")).all()
	for row in ret:
		data[ row.name ] = row

	print len(ret)
        d = etree.parse(open("monumentaltrees.xml", "r+")).getroot()

        for x in list(d):
                if x.tag == "m":

                        lat = float(x.attrib['lat'])
                        lng = float(x.attrib['lng'])
                        name = x.attrib['t'].encode('ascii', 'xmlcharrefreplace')
                        url = "http://www.monumentaltrees.com/" + x.attrib['u']
                        landmark_category = "tree"

			if name in data:
				k = name
				match = 1

				if data[k].landmark_category == landmark_category: match += 1
				else: mismatch['category'].append( (d, "%s != %s" % (landmark_category, data[k].landmark_category)) )

				if match == 2:
					del data[ k ]
			else: mismatch['name'].append( {'name': name, 'url': url} )

	print len(data)
	for x in mismatch:
		print "%s: %d" % (x, len(mismatch[x]))

	print mismatch['name']


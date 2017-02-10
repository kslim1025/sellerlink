
from imposm.parser import OSMParser
from geojson import Feature, Point, FeatureCollection
import geojson
import sys

if True:
	d = geojson.load(open("historic.geojson", "r+"))
	print len(d.features)
 	sys.exit(0)

files = ['florida-latest.osm']

outfile = "historic.geojson"
tags = {"historic"}

class Historic(object):
	data = []
	tag_filter = {}

	def __init__(self, tag_filter={}):
		self.tag_filter = tag_filter

	def nodes(self, nodes):
		for osmid, tags, refs in nodes:
			if len(set(tags).intersection(set(self.tag_filter))) > 0:
				# refs[0] = lng, refs[1] = lat
				pt = Point(refs)
				ft = Feature(geometry=pt, properties=tags)
				self.data.append( ft )				

historic = Historic(tag_filter=tags)
p = OSMParser(concurrency=4, nodes_callback=historic.nodes)
p.parse(files[0])

geojson.dump( FeatureCollection(historic.data), open(outfile, "w+") )


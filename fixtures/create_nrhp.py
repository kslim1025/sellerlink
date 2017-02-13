
from models import historicplace, geo_coords
import json, sys

from database import get_or_create

def insert_data(db):

	hp = historicplace.HistoricPlace()
	gc = geo_coords.GeoCoords()

	""" query test
	# "lat":27.68618,"lng":-82.74634},{"lat":27.68618,"lng":-82.15296},{"lat":28.21044,"lng":-82.15296},
	ret = [x[0] for x in db.session.query(geo_coords.GeoCoords.guid).filter(geo_coords.GeoCoords.latitude>=27.68618, geo_coords.GeoCoords.latitude<=28.21044, geo_coords.GeoCoords.longitude>=-82.74634, geo_coords.GeoCoords.longitude<=-82.15296).all()]

	ret = hp.query.filter(historicplace.HistoricPlace.geo_id.in_(ret)).all()
	d = set()
	for x in ret:
		d.add( x )

	print len(d)
	"""

	def add_row(row):
		geo, isFound = get_or_create(db.session, geo_coords.GeoCoords, latitude=row['latitude'], longitude=row['longitude'])

		hp = historicplace.HistoricPlace()
		hp.geo = geo
		hp.name = row['name']
		hp.description = row['description']

		db.session.add(hp)

	d = json.load(open("NRHP1.json", "r+"))
	for row in d:
		add_row(row)
		db.session.commit()

	d = json.load(open("NRHP2.json", "r+"))
	for row in d:
		add_row(row)
		db.session.commit()

	db.session.commit()
	

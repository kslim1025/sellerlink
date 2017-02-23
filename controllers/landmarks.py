
from flask import Blueprint, render_template, abort, request
from flask import flash, url_for, redirect, jsonify
from jinja2 import TemplateNotFound

import urllib


blueprint = Blueprint('landmarks_user', __name__,
                        template_folder='../templates')

from database import db
from models import landmarks, historicplace, geo_coords

# index
# map

# XXX move this to main api and not landmark-specific
@blueprint.route("/tour.json", methods=['POST'])
def tour_json():
	d = {}

	rq = request.get_json()

	places = set()
	facets = {}
	places_by_polygon = {} # so we can limit routing to nearby places first

        gc = geo_coords.GeoCoords()
	hp = historicplace.HistoricPlace()
	lp = landmarks.Landmark()

	from sqlalchemy import func, distinct

	for rect in rq['polygons']:
		if rect[0:4] <> "rect": continue

		latlngs = rq['polygons'][rect]['latlngs']
		latmin = latlngs[0]['lat']
		latmax = latlngs[2]['lat']
		lngmin = latlngs[0]['lng']
		lngmax = latlngs[2]['lng']

        	ret = [x[0] for x in db.session.query(geo_coords.GeoCoords.guid).filter(geo_coords.GeoCoords.latitude>=latmin, 
				geo_coords.GeoCoords.latitude<=latmax, 
				geo_coords.GeoCoords.longitude>=lngmin, 
				geo_coords.GeoCoords.longitude<=lngmax).all()]

		geo_q = landmarks.Landmark.geo_id.in_(ret)

		# gather facet aggregate information
		"""
        	q = db.session.query(landmarks.Landmark.landmark_category, func.count(landmarks.Landmark.guid)).filter(geo_q).group_by(landmarks.Landmark.landmark_category)
		for f in q.all():
			if f[0] not in facets: facets[f[0]] = 0
			facets[ f[0] ] = f[1]

		q = db.session.query(landmarks.Landmark).filter(geo_q)
		for row in q.all():
			places.add( row )
		"""

		q = db.session.query(historicplace.HistoricPlace).filter(geo_q)
		if 'historic_place' not in facets: facets['historic_place'] = 0
		facets[ 'historic_place' ] += q.count()
		for row in q.all():
			places.add( row )

        i = 0
        for x in places:
		cat = getattr(x, 'landmark_category', None)
		if cat is None: cat = x.discriminator
                tmp = { 'category': cat, 'name': x.name, 'pos': {'lat': float(x.geo.latitude), 'lng': float(x.geo.longitude)} }
                d[i] = tmp
                i += 1

	return jsonify({'facets': facets, 'places': d})


@blueprint.route("/nearby.json", methods=['POST'])
def nearby_json():
	d = {}

	"""
	ret = q.all()
        for x in ret:
		places.add( x )
	"""

	i = 0
	for x in places:
		tmp = { 'name': x.name, 'pos': {'lat': float(x.geo.latitude), 'lng': float(x.geo.longitude)} }
		d[i] = tmp
		i += 1

	return jsonify(d)

"""
@blueprint.route("/<string:name>")
def view(name):
    model = None #Service()

    return render_template("service_view.html", name=urllib.unquote_plus(name), model=model)
"""


from flask import Blueprint, render_template, abort, request
from flask import flash, url_for, redirect, jsonify
from jinja2 import TemplateNotFound

import urllib


blueprint = Blueprint('historicplace_user', __name__,
                        template_folder='../templates')

from database import db
from models import historicplace, geo_coords

# index
@blueprint.route("/map")
def index():
    #return render_template("test_map.html")
    
    return render_template("historicplace_map.html")

@blueprint.route("/nearby.json", methods=['POST'])
def nearby_json():
	d = {}

	rq = request.get_json()
	places = set()

        gc = geo_coords.GeoCoords()
	hp = historicplace.HistoricPlace()
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

        	ret = hp.query.filter(historicplace.HistoricPlace.geo_id.in_(ret)).all()
        	for x in ret:
			places.add( x )

	i = 0
	for x in places:
		tmp = { 'name': x.name, 'pos': {'lat': x.geo.latitude, 'lng': x.geo.longitude} }
		d[i] = tmp
		i += 1

	return jsonify(d)

"""
@blueprint.route("/<string:name>")
def view(name):
    model = None #Service()

    return render_template("service_view.html", name=urllib.unquote_plus(name), model=model)
"""

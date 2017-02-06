
import sys

from config import prod as config

from database import db, get_or_create

import database, app

from models import thing
from models import place, organization
from models import geo_coords
from models import autodealer
from models import historicplace

#import models.thing, models.offer#, models.request, models.comment
#import models.action, models.imageobject, models.openinghours
#import models.service, models.products
#import models.restaurant
#import models.person
#import models.events
# also model for system users and listing ownership


if __name__ == '__main__':
    application = app.create_app(config)

    database.init(application)
    database.create_all()

    if len(sys.argv) > 1 and sys.argv[1] == "--historicplace":
        from models import historicplace, geo_coords
       
	import json, sys
	hp = historicplace.HistoricPlace()
	gc = geo_coords.GeoCoords()
	# "lat":27.68618,"lng":-82.74634},{"lat":27.68618,"lng":-82.15296},{"lat":28.21044,"lng":-82.15296},
	ret = [x[0] for x in db.session.query(geo_coords.GeoCoords.guid).filter(geo_coords.GeoCoords.latitude>=27.68618, geo_coords.GeoCoords.latitude<=28.21044, geo_coords.GeoCoords.longitude>=-82.74634, geo_coords.GeoCoords.longitude<=-82.15296).all()]

	ret = hp.query.filter(historicplace.HistoricPlace.geo_id.in_(ret)).all()
	d = set()
	for x in ret:
		d.add( x )

	print len(d)

	"""
	d = json.load(open("outfile2.json", "r+"))
	for row in d:
		geo = get_or_create(db.session, geo_coords.GeoCoords, latitude=float(row['latitude']), longitude=float(row['longitude']))

		hp = historicplace.HistoricPlace()
		hp.geo = geo
		hp.name = row['name']
		hp.description = row['description']
	
		db.session.add(hp)

	db.session.commit()	
	"""
	sys.exit(0)
 
        #geo = get_or_create(db.session, geo_coords.GeoCoords, latitude=1, longitude=1)
        
        #print geo.guid
        #db.session.add(geo)
        #db.session.commit()
        #sys.exit(0)
        #print historicplace.HistoricPlace.query.all()[0]
        #db.session.delete(historicplace.HistoricPlace.query.all()[0])
        #db.session.commit()
        #print geo_coords.GeoCoords.query.all()
        #sys.exit(0)
        
        db.session.add( hp )
        db.session.commit()
        
    else:
        application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

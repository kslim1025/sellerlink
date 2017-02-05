
import sys

from config import development as config
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
        
        geo = get_or_create(db.session, geo_coords.GeoCoords, latitude=1, longitude=1)
        
        print geo.guid
        db.session.add(geo)
        db.session.commit()
        sys.exit(0)
        #print historicplace.HistoricPlace.query.all()[0]
        #db.session.delete(historicplace.HistoricPlace.query.all()[0])
        #db.session.commit()
        #print geo_coords.GeoCoords.query.all()
        #sys.exit(0)
        
        hp = historicplace.HistoricPlace()
        geo = geo_coords.GeoCoords(1, 1)

        hp.name = "test"
        hp.description = "test"
        hp.geo = geo
        
        print hp
        
        db.session.add( hp )
        db.session.commit()
        
    else:
        application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

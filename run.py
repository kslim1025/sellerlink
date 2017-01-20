
from config import development as config
from database import db

import database, app

from models import thing
from models import place, organization
from models import autodealer

#import models.thing, models.offer#, models.request, models.comment
#import models.action, models.imageobject, models.openinghours
#import models.place, models.geo_coords#, models.service, models.products
#import models.restaurant
#import models.person, models.organization
#import models.events

if __name__ == '__main__':
    application = app.create_app(config)

    database.init(application)
    database.create_all()
    
    application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

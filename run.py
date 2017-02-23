
import sys

from config import development as config
#from config import prod as config

from database import db, get_or_create

import database, app

# pull in configured models
database.get_config_db()
"""
from models import thing
from models import place, organization
from models import geo_coords
from models import autodealer
from models import historicplace
"""

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

    if len(sys.argv) > 1 and sys.argv[1] == "--fixtures":      
	# XXX support ,-delimited list of fixtures
	arg = sys.argv[2]
	
	import importlib
	try:
		m = importlib.import_module('fixtures.create_%s' % arg)
		m.insert_data(db)
	except Exception as e:
		import traceback
		traceback.print_exc()

    elif len(sys.argv) > 1 and sys.argv[1] == "--testfixture":
	arg = sys.argv[2]

	import importlib
	try:
		m = importlib.import_module('fixtures.test_%s' % arg)
		m.test_data(db)
	except Exception as e:
		import traceback
		traceback.print_exc()
		
    elif len(sys.argv) > 1 and sys.argv[1] == "--dropall":
	database.drop_all()

    else:
        application.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)

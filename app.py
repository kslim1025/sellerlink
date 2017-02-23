import logging

from flask import Flask, request as req
from flask import request, render_template
from flask_sqlalchemy import SQLAlchemy

#from controllers import food, restaurant, service
from controllers import autodealer, historicplace, landmarks
#from controllers import api

# https://sqlalchemy-continuum.readthedocs.io/en/latest/

from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView

from database import db
#from models.restaurant import Restaurant
#from models.service import Service


def index_view():
	return render_template("index.html")
    
def tour_view():
	return render_template("tour.html")

    
def create_app(config_filename):

    app = Flask(__name__)
    app.config.from_object(config_filename)

    # static pages
    app.add_url_rule("/", 'index', index_view)
   
    app.add_url_rule("/tour", "tour", tour_view)
 
    #app.register_blueprint(pages.blueprint)
    #app.register_blueprint(admin.blueprint, url_prefix='/admin')
    
    #app.register_blueprint(api.blueprint, url_prefix='/api')
    
    # signpost 
    
    #app.register_blueprint(food.blueprint, url_prefix='/food')
    #app.register_blueprint(restaurant.blueprint, url_prefix='/restaurant')
    #app.register_blueprint(service.blueprint, url_prefix="/service")
    
    app.register_blueprint(autodealer.blueprint, url_prefix='/localbusiness/autodealer')
    
    app.register_blueprint(historicplace.blueprint, url_prefix='/historicplace')
  
    app.register_blueprint(landmarks.blueprint, url_prefix='/landmarks') 
 
    # sites/payment angular page :)
    
    # patreon/donation page
    
    # clubs, events :)
    # hotels, places ...
    # products, cars...
    # services, web design

    #admin = Admin(app)
    #admin.add_view(ModelView(Restaurant, db.session))
    
    app.logger.setLevel(logging.NOTSET)

    #from models import action, hotels, place, products, imageobject, openinghours
    #from models import offer, request

    @app.after_request
    def log_response(resp):
        app.logger.info("{} {} {}\n{}".format(
            req.method, req.url, req.data, resp)
        )
        return resp

    return app

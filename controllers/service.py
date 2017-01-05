
from flask import Blueprint, render_template, abort, request
from flask import flash, url_for, redirect
from jinja2 import TemplateNotFound

import urllib


blueprint = Blueprint('service_user', __name__,
                        template_folder='../templates')

from database import db
#from models.service import Service
#from forms.restaurant import RestaurantForm

# index

@blueprint.route("/<string:name>")
def view(name):
    model = None #Service()

    return render_template("service_view.html", name=urllib.unquote_plus(name), model=model)
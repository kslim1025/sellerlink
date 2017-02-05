
from flask import Blueprint, render_template, abort, request
from flask import flash, url_for, redirect
from jinja2 import TemplateNotFound

import urllib


blueprint = Blueprint('historicplace_user', __name__,
                        template_folder='../templates')

from database import db

# index
@blueprint.route("/map")
def index():
    #return render_template("test_map.html")
    
    return render_template("historicplace_map.html")

"""
@blueprint.route("/<string:name>")
def view(name):
    model = None #Service()

    return render_template("service_view.html", name=urllib.unquote_plus(name), model=model)
"""

from flask import Blueprint, render_template, abort, request
from flask import flash, url_for, redirect
from jinja2 import TemplateNotFound

import urllib


blueprint = Blueprint('autodealer_user', __name__,
                        template_folder='../templates')

from database import db
from models.autodealer import AutoDealer
from forms.autodealer import AutoDealerForm


# overpass/osm shop=car
# index
@blueprint.route("/")
def index():
    return render_template("model_list.html", model=AutoDealer)

@blueprint.route("/add")
def add():
    model = AutoDealer()
    form = AutoDealerForm()
    if hasattr(request, 'POST'): 
        form = AutoDealerForm(request.POST)
    
        if form.validate():
            form.populate_obj(model)
            db.session.add(model)
            db.session.commit()
            flash("AutoDealer added")
            return redirect(url_for("index"))
    
    return render_template("radar_add.html", form=form)
    
"""
@blueprint.route("/<string:name>")
def view(name):
    model = None #Service()

    return render_template("service_view.html", name=urllib.unquote_plus(name), model=model)
"""
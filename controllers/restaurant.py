
from flask import Blueprint, render_template, abort, request
from flask import flash, url_for, redirect
from jinja2 import TemplateNotFound

blueprint = Blueprint('restaurant_user', __name__,
                        template_folder='../templates')

from database import db
from models.restaurant import Restaurant
from forms.restaurant import RestaurantForm

@blueprint.route('/index')
def index():
    obj = Restaurant().query.all()
    return render_template("restaurant_list.html", obj=obj)

@blueprint.route("/add")
def add():
    form = RestaurantForm()
    model = Restaurant()
    if hasattr(request, 'POST'): 
        form = RestaurantForm(request.POST)
    
        if form.validate():
            form.populate_obj(model)
            db.session.add(model)
            db.session.commit()
            flash("Restaurant added")
            return redirect(url_for("index"))
        
    return render_template("restaurant_add.html", form=form)
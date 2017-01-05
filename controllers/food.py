from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

blueprint = Blueprint('food', __name__,
                        template_folder='../templates')

@blueprint.route('/add')
def add():
    
    return render_template("radar_add.html")


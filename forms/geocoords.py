
from flask_wtf import Form

from wtforms_alchemy import ModelForm, ModelFieldList, ModelFormField
from wtforms.fields import SelectField

from models.restaurant import Restaurant
from models.geo_coords import GeoCoords

class GeoCoordsForm(ModelForm):
    class Meta:
        model = GeoCoords
        
class RestaurantForm(ModelForm, Form):
    class Meta:
        model = Restaurant
        exclude = ['date_modified']
        # add geo_id field
        
        
    geo_id = SelectField(GeoCoordsForm, choices=[])


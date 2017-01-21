
from flask_wtf import Form

from wtforms_alchemy import ModelForm, ModelFieldList, ModelFormField
from wtforms.fields import SelectField, TextField
from wtforms.validators import DataRequired, Length

from models.autodealer import AutoDealer
from models.geo_coords import GeoCoords, PostalAddress


class GeoCoordsForm(ModelForm):
    class Meta:
        model = GeoCoords

class PostalAddressForm(ModelForm):
    class Meta:
        model = PostalAddress
                
class AutoDealerForm(Form):
    class Meta:
        csrf = True
        
    name = TextField(validators=[DataRequired(), Length(max=100)])
    url = TextField(validators=[Length(max=100)])
    address = SelectField(PostalAddressForm, choices=[], validators=[DataRequired()])
    phone = TextField(validators=[DataRequired(), Length(max=100)])
        
    geo_id = SelectField(GeoCoordsForm, choices=[], validators=[DataRequired()] )


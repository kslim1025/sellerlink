
from database import db

from models.place import Place
from models.offer import Offer
from models.thing import GUID

# XXX normalization
# restrictedDiet, recipeIngredient, currency


class MenuNutrition(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    name = db.Column('name', db.String(1024))
    description = db.Column('description', db.String(1024))
    unit = db.Column('unit', db.String(1024))
    value = db.Column('value', db.String(1024))
    #calories = db.Column('calories', db.String(1024))
    
class MenuItemNutrition(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    nutrition_id = db.Column(db.String(1024), db.ForeignKey('menu_nutrition.guid'))
    item_id = db.Column(db.String(1024), db.ForeignKey('menu_item.guid'))

class MenuAddonNutrition(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    nutrition_id = db.Column(db.String(1024), db.ForeignKey('menu_nutrition.guid'))
    addon_id = db.Column(db.String(1024), db.ForeignKey('menu_addon.guid'))
    
# XXX should inherit from Offer
class MenuItem(Offer):
    __mapper_args__ = {'polymorphic_identity': 'menu_item'}
    guid = db.Column(db.String, db.ForeignKey('offer.guid'), primary_key=True)
    
    recipeIngredients = db.Column('recipeIngredients', db.String(1024))
    restrictedDiets = db.Column('restrictedDiets', db.String(1024))
    
    currency = db.Column('currency', db.String(1024))

    hasNutrition = db.relationship('MenuNutrition', secondary='menu_item_nutrition')
    
    menu_id = db.Column('menu_id', db.ForeignKey('menu.guid'))
    menu = db.relationship('Menu', backref="hasItems")
    
class MenuAddon(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    name = db.Column(db.String(1024))
    currency = db.Column(db.String(1024))
    price = db.Column(db.String(1024))

    hasNutrition = db.relationship('MenuNutrition', secondary='menu_addon_nutrition')
    
    menu_item_id = db.Column('menu_item_id', db.ForeignKey('menu_item.guid'))
    menu_item = db.relationship('MenuItem', backref='hasAddons')
    
# https://github.com/schemaorg/schemaorg/issues/1288

class Menu(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    name = db.Column(db.String(1024))
    menuType = db.Column(db.String(1024)) # special, apps, entree, dinner, lunch, breakfast
    validFrom = db.Column(db.DateTime)
    validTo = db.Column(db.DateTime)
    #validFrequency 
    

class RestaurantMenus(db.Model):
    guid = db.Column('guid', db.String(1024), primary_key=True)
    restaurant_id = db.Column('restaurant_id', db.String(1024), db.ForeignKey('restaurant.id'))
    menu_id = db.Column('menu_id', db.String(1024), db.ForeignKey('menu.guid'))

class Restaurant(Place):
    __mapper_args__ = {'polymorphic_identity': 'restaurant'}
    id = db.Column(GUID(), db.ForeignKey('place.guid'), primary_key=True)
     
    acceptsReservation = db.Column(db.String(1024))
    menus = db.relationship('Menu', secondary='restaurant_menus') 
    servesCuisine = db.Column(db.String(1024))
    starRating = db.Column(db.String(1024))
    
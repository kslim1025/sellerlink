
from database import db
from sqlalchemy.schema import ForeignKey

from models.products import Product

class Car(Product):
    
	vehicleTransmission = db.Column('vehicleTransmission', db.String(1024))
	releaseDate = db.Column('releaseDate', db.DateTime)
	brand_id = db.Column('brand_id', db.String(1024), ForeignKey('Organization.guid'))
	vehicleEngine = db.relationship('EngineSpecification')
	vehicleConfiguration = db.Column('vehicleConfiguration', db.String(1024))

	color = db.Column('color', db.String(1024))
	offers = db.relationship('Offer')
	manufacturer_id = db.Column('manufacturer_id', db.String(1024), ForeignKey('Organization.guid'))
	audience_id = db.Column('audience_id', db.String(1024), ForeignKey('Audience.guid'))

	steeringPosition_id = db.Column('steeringPosition_id', db.String(1024), ForeignKey('SteeringPositionValue.guid'))
	numberOfForwardGears = db.Column('numberOfForwardGears', db.Integer)
	fuelConsumption = db.Column('fuelConsumption', db.Integer)
	numberOfDoors = db.Column('numberOfDoors', db.Integer)
	weight = db.Column('weight', db.Integer)
	isAccessoryOrSparePartFor_id = db.Column('isAccessoryOrSparePartFor_id', db.String(1024), ForeignKey('Product.guid'))
	vehicleEngine_id = db.Column('vehicleEngine_id', db.String(1024), ForeignKey('EngineSpecification.guid'))
	driveWheelConfiguration = db.Column('driveWheelConfiguration', db.String(1024))
	cargoVolume = db.Column('cargoVolume', db.Integer)
	numberOfPreviousOwners = db.Column('numberOfPreviousOwners', db.Integer)
	numberOfAxles = db.Column('numberOfAxles', db.Integer)
	knownVehicleDamages = db.Column('knownVehicleDamages', db.String(1024))
	mileageFromOdometer = db.Column('mileageFromOdometer', db.Integer)
	dateVehicleFirstRegistered = db.Column('dateVehicleFirstRegistered', db.DateTime)
	productionDate = db.Column('productionDate', db.DateTime)
	steeringPosition = db.relationship('SteeringPositionValue')
	vehicleInteriorType = db.Column('vehicleInteriorType', db.String(1024))
	vehicleModelDate = db.Column('vehicleModelDate', db.DateTime)
	isAccessoryOrSparePartFor = db.relationship('Product')
	purchaseDate = db.Column('purchaseDate', db.DateTime)
	vehicleSeatingCapacity = db.Column('vehicleSeatingCapacity', db.Integer)
	fuelType = db.Column('fuelType', db.String(1024))
	vehicleSpecialUsage = db.Column('vehicleSpecialUsage', db.String(1024))
	vehicleIdentificationNumber = db.Column('vehicleIdentificationNumber', db.String(1024))
	vehicleInteriorColor = db.Column('vehicleInteriorColor', db.String(1024))
	fuelEfficiency = db.Column('fuelEfficiency', db.Integer)
	model = db.Column('model', db.String(1024))
	numberOfAirbags = db.Column('numberOfAirbags', db.String(1024))


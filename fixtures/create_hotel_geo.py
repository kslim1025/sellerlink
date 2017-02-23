
from models import hotels, geo_coords, organization
import csv, sys
import datetime

from database import get_or_create

def insert_data(db):

	# "Board Code (200 identifies HR within the department)","License Type Code (see tables below)","Licensee Name","Rank Code","Modifier Code (see tables below)","Mailing Name (if different from Licensee Name)","Mailing Street Address Line 1","Mailing Address Line 2","Mailing Address Line 3","Mailing City","Mailing State","Mailing Zip Code","Mailing County Code (see table below)","Primary Telephone Number",
	# "Business Name (Location)",Filler,"Location Street Address Line 1","Location Address Line 2","Location Address Line 3","Location City","Location State","Location Zip Code","Location County Code (see table below)","Secondary Telephone Number",District,Region,"License Number","Primary Status Code (see table below)","Secondary Status Code (see table below)","Expiry Date","Last Inspection Date",
	# "Base Risk","Secondary Risk",
	# Latitude,Longitude,"Accuracy Score","Accuracy Type",Number,Street,City,State,County,Zip,Country
	
	# 20 Primary Status Code == Current

	lb = hotels.LodgingBusiness
	gc = geo_coords.GeoCoords

	rd = csv.DictReader(open("hrlodge-filter_geocodio_64e274307ed0309c89fd068fcc9340e364409f7f.csv", "r+"))
	for row in rd:

		# Latitude,Longitude,"Accuracy Score","Accuracy Type",Number,Street,City,State,County,Zip,Country
		m = db.session.query(lb).filter(lb.license_number==row['License Number'])
		
		if m.count() >= 1:

			geo, isFound = get_or_create(db.session, gc, latitude=row['Latitude'], longitude=row['Longitude'])

			for row in m:
				if row.geo_id is not None: continue
				
				row.geo = geo
				db.session.add(row)
				db.session.commit()

	

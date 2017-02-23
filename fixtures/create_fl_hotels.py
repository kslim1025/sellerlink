
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

	ad = geo_coords.PostalAddress
	gc = geo_coords.GeoCoords
	org = organization.Organization

	for i in xrange(1, 8):
		print "hrlodge%d.csv" % i

		rd = csv.DictReader(open("hrlodge%d.csv" % i, "r+"))
		for row in rd:
			code = row['Rank Code']
			if code == "HOTL":
				m = hotels.Hotel()
			elif code == "MOTL": 
				m = hotels.Motel()
			elif code == 'BNB':
				m = hotels.BedAndBreakfast()
                        elif code == "CNDO":
                                m = hotels.Resort()
                        elif code == "DWEL":
                                m = hotels.Resort()
			elif code == "TAPT":
				m = hotels.Resort()
                        else: continue

                        m.name = row['Business Name (Location)'].decode('utf-8').encode('ascii', 'xmlcharrefreplace')
			m.license_number = row['License Number']
			dt = row['Expiry Date'].split("/")		
			m.license_expiry = datetime.date(int(dt[2]), int(dt[0]), int(dt[1]))
			dt = row['Last Inspection Date'].split("/")
			if len(dt) == 3:
				m.last_inspection = datetime.date(int(dt[2]), int(dt[0]), int(dt[1]))

			m.status_code = row['Primary Status Code (see table below)']
			m.rooms = row['Number of Seats (food service) or Rental Units (lodging)']

			m.telephone = row['Primary Telephone Number']

			m.address, isFound = get_or_create(db.session, ad, streetAddress=row['Location Street Address Line 1'],
				streetAddress2=row['Location Address Line 2'],
				streetAddress3=row['Location Address Line 3'], 
				addressLocality=row['Location City'],
				addressRegion=row['Location State'],
				postalCode=row['Location Zip Code'])

			# Latitude,Longitude,"Accuracy Score","Accuracy Type",Number,Street,City,State,County,Zip,Country

			# XXX limit search to name and state
			morg, isFound = get_or_create(db.session, org, name=row['Licensee Name'].decode('utf-8').encode('ascii', 'xmlcharrefreplace'))
			if not isFound:
				morg.address, isFound = get_or_create(db.session, ad, streetAddress=row['Mailing Street Address Line 1'],
        	                        streetAddress2=row['Mailing Address Line 2'],
                	                streetAddress3=row['Mailing Address Line 3'],
                        	        addressLocality=row['Mailing City'],
                                	addressRegion=row['Mailing State'],
        	                        postalCode=row['Mailing Zip Code'])
				#org.telephone =

			m.organization = morg

			db.session.add(m)
			db.session.add(morg)
			db.session.commit()

	db.session.commit()
	

import json
import csv

def load_json(filename):
        tmp = json.load(open(filename, "r+"))

        keys = set()
        data = []
        for row in tmp['loaded'].values():
                row['geometry'] = "%s,%s" % (row['geometry']['location']['lat'], row['geometry']['location']['lng'])

                for x in row.keys():
                        keys.add( x )
                        if type(row[x]) == unicode: row[x] = row[x].encode('ascii', errors='replace')

                data.append( row )

        for row in tmp['blocked'].values():
                row['geometry'] = "%s,%s" % (row['geometry']['location']['lat'], row['geometry']['location']['lng'])

                for x in row.keys():
                        keys.add( x )
                        if type(row[x]) == unicode: row[x] = row[x].encode('ascii', errors='replace')

                data.append( row )

        #print keys
        return data

def write_csv(filename, data, keys):

        wd = csv.DictWriter( open(filename, "w+"), fieldnames=keys )
        wd.writeheader()
        for row in data:
                wd.writerow( row )


if __name__ == "__main__":
        import sys

        newfile = '.'.join( sys.argv[1].split('.')[:-1] ) + ".csv"

        d = load_json(sys.argv[1])
        write_csv( newfile, d, ['name', 'website', 'formatted_address', 'formatted_phone_number', 'geometry'] )


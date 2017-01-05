
# make function to map ORM to JSON-LD or RDF 


"""
class Triple:
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(1024))
    predicate = db.Column(db.String(1024))
    obj = db.Column(db.String(1024))


class Hotels(Triple, db.Model):
    __tablename__ = "hotels"

class Customers(Triple, db.Model):
    __tablename__ = "customers"

# add index 
for x in db.metadata.tables:
    tbl = db.metadata.tables[x]
    db.Index( "%s_subject_pred" % x, tbl.c.subject, tbl.c.predicate )
"""
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey

db = SQLAlchemy()

class schema(object):

    def __init__(self):
        """ Load schema.org triple rdf graph """
        
        import rdflib
        from rdflib import RDF, RDFS

        self.RDFS = RDFS
        self.g = rdflib.Graph()
        self.g.load("data.nt", format="nt")

        self.schemaNS = rdflib.Namespace("http://schema.org/")
       
 
    def add_fields(self, fields, node):
        """ Find all subjects which are within domain or supersededby node """

        # find direct field members
        for s,p,o in self.g.triples((None,self.schemaNS.domainIncludes,node)):

            # find superseded fields
            is_superseded = len(list(self.g.objects(predicate=self.schemaNS.supersededBy,subject=s))) > 0
            if is_superseded: continue

            fields.add(s)

        return fields


    def get_subclasses(self, node):
        """ find subclasses of node """

        d = []
        v = []

        oq = [node]
        while len(oq) > 0:
            n = oq.pop()
            for s,p,o in self.g.triples((n,self.RDFS.subClassOf,None)):
                d.append(o)
                if o not in v: oq.append(o)

        return d


    def get_fields(self, node):
        """ find all domain fields across full range of node """

        fields = set()

        fields = self.add_fields(fields, node)

        # find subclasses
        subclasses = self.get_subclasses(node)
        for x in subclasses:
            fields = self.add_fields(fields, x)

        # find range members
        for s,p,o in self.g.triples((node, self.schemaNS.rangeIncludes, None)):
            fields = self.add_fields(fields, o)

            subclasses = self.get_subclasses(o)
            for x in subclasses:
                fields = self.add_fields(fields, x)

        return fields


    def get_types(self, fields):
        """ add rdf type for each field """
	
        d = []
        for x in fields:
            t = list(self.g.objects(subject=x, predicate=self.schemaNS.rangeIncludes))
            if len(t) <= 0:
                t = list(self.g.objects(subject=x, predicate=RDF.type))

            
            d.append( (x.n3(), t) )

        return d


    def get_name(self, s):
        """ return RDFLib.URIRef("schemabase/name") """

        return s.split("/")[-1]


    def get_sql(self, name):
        """ return sqlalchemy schema representing schema object """

        from collections import OrderedDict
        classes = {name: OrderedDict({})} # for dependent classes
        relations = {}

        classes[name]['guid'] = "db.Column('guid', db.String(1024), primary_key=True)"

        # or int XXX
        static_types = {'Date':"db.DateTime", 'Text':"db.String(1024)", "QuantitativeValue":"db.Integer"}

        # first iterate the populated RDF schema for a rdf.type matching requested type
        if hasattr(self.schemaNS, name):
            fields = self.get_fields( getattr(self.schemaNS, name) )
 
            # get_types ... add columns and foreignkeys
            for y in fields:

                # XXX only one relation?
                if self.get_name(y) in classes[name]: continue

                found_type = False
                rel = False
                for t in self.get_types([y])[0][1]:
                    if hasattr(self.schemaNS, t):
                        rel = self.get_name(t)

                    if self.get_name(t) in static_types:
                        found_type = static_types[ self.get_name(t) ]
                        break

                if found_type <> False and self.get_name(y) not in classes[name]:
                    classes[name][self.get_name(y)] = "db.Column('%s', %s)" % (self.get_name(y), found_type)
                elif rel <> False:
                        classes[name][self.get_name(y) + "_id"] = "db.Column('%s_id', db.String(1024), ForeignKey('%s.guid'))"  % (self.get_name(y), rel)
                        classes[name][self.get_name(y)] = "db.relationship('%s')" % rel

                        if rel not in classes:
                            pass#classes[self.get_name(t)] = self.get_sql(self.get_name(t))
                elif self.get_name(y) not in classes[name]:
                    classes[name][self.get_name(y)] = "db.Column('%s', db.String(1024))" % self.get_name(y)
     
        else: print "%s not found in namespace" % name

        # check for other tables to setup foreignkey/relationships
        return classes

def get_schema(name):
    """ Returns dynamic schema as positional db.Columns for use in db.Table() """

    s = schema()
    ret = s.get_sql(name)

    args = {}
    for y in ret[name]:
        args[y] = ret[name][y]

    return args

import sys
n = sys.argv[1]
print "class %s(db.Model):" % n
ret = get_schema(n)
for x in ret:
    print "\t%s = %s" % (x, ret[x])


# PostalAddress, areaServed
# Person, Action
# Offer, Product




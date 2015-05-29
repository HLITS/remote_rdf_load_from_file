import rdflib

filename = "C:\\Users\\short\\Desktop\\Projects\\Linked Data projects\\Anthropology theses\\rdf_uri_test.txt"

with open(filename) as f:
    uriList = f.read().splitlines()
    f.close

g = rdflib.Graph()

for uri in uriList:
    g.parse(uri)

	
# simple query to check all is well
# should get results from all triples
# for a large input, should probably limit this
q = g.query('SELECT ?o WHERE {?s schema:name ?o}')

for row in q:
    print row


# Alternatively, can prepare a query in advance and then run
# q = rdflib.plugins.sparql.prepareQuery('SELECT ?o WHERE {?s schema:name ?o}', initNs = { "schema": "http://schema.org/" })
# q2 = g.query(q)
# note that namespaces used in query must be defined when preparing query, even if they are in the graph to be queried
# also, the namespace for prepareQuery is really long, so might want to import separately
# need to import rdflib.plugins.sparql as sparql 

	
# get a list of the namespaces in the graph
ns = rdflib.namespace.NamespaceManager(g)

all_ns = [n for n in g.namespace_manager.namespaces()]

for item in all_ns:
    print item
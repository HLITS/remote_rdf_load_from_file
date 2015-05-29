import rdflib.plugins.sparql as sparql
import rdflib

filename = "C:\\Users\\short\\Desktop\\Projects\\Linked Data projects\\Anthropology theses\\rdf_uri_test.txt"

def readuris():
    with open(filename) as f:
        uriList = f.read().splitlines()
        f.close

    return uriList

def makeGraph():
    g = rdflib.Graph()
    uris = readuris()
    for uri in uris:
        g.parse(uri)

    return g

def testQuery():
    g = makeGraph()

    q = sparql.prepareQuery('SELECT ?o WHERE {?s schema:name ?o}', initNs = { "schema": "http://schema.org/" })

    myquery = g.query(q)

    for row in myquery:
        print row

testQuery()
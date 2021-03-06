import requests
import rdflib.plugins.sparql as sparql
import rdflib


errLog = []
g = rdflib.Graph()
loadCount = 0
errCount = 0
filename = "C:\\Users\\short\\Desktop\\Projects\\Linked Data projects\\Anthropology theses\\rdf_uri_test.txt"


def readuris():
    with open(filename) as f:
        uriList = f.read().splitlines()
        f.close

    return uriList
	
uris = readuris()

def makeGraph():
	for uri in uris:

		r = requests.get(uri)
		
		status = r.status_code
		
		if status == 200:
			loadCount += 1
			g.parse(data=r.text, format="application/rdf+xml")
		else:
			errCount += 1
			message = "Error " + status + " " + uri
			errLog.append(message)
		
	print str(loadCount) + " were loaded correctly"
	print str(errCount) + " had errors"
	for item in errLog:
		print item
	
	return g
	
g = makeGraph()
	
g.serialize(destination="C:\\Users\\short\\Desktop\\test.rdf")
# serializes into an RDF file (or another format if desired), can load into another triplestore
# might have problems with the LC errors - actually doesn't seem to

# remote_rdf_load_from_file
Load RDF into a graph from a list of URIs

Reads a text file of URIs into a list, then uses Requests to make sure that each URI returns a 200 status code before writing it to a graph with RDFLib. Returns a report of how many were loaded successfully, and a list of errors with the associated URIs. FInally, serializes the graph to a text file as RDF/XML.

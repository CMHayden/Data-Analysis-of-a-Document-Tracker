import json
def json_readr(file):
	data = []
	for line in open(file, mode="r"):
		data.append(json.loads(line))
	return data

def getCountries(docID):
	countries = []
	i = 0
	for d in data:
		try:
			if (d["env_type"] == "reader"):
				countries.append(d["visitor_country"])
		except:
			#try:
				#if (d["subject_doc_id"] == docID):
					#countries.append(d["visitor_country"])
			#except:
			i=i+1
			print(i)
	return countries

def getBrowsers():
	browsers = []
	for d in data:
		browsers.append(d["visitor_useragent"])
	return browsers

def documentVisitors(docID):
	visitors = []
	for d in data:
		if (d["subject_doc_id"] == docID):
			if d["visitor_uuid"] not in visitors:
				visitors.append(d["visitor_uuid"])
	return visitors

def visitorDocuments(visID):
	documents = []
	for d in data:
		if (d["visitor_uuid"] == visID):
			if (d["subject_doc_id"] not in documents):
				documents.append(d["subject_doc_id"])
	return documents

def getList(variable, docID=None):
	list = []
	for d in data:
		if docID:
			if (d["subject_doc_id"] == docID):
				list.append(d[variable])
		else:
			list.append(d[variable])
	return list

def alsoLike(docID, visID = None):
	visitors = documentVisitors(docID)
	documents = []
	for d in visitors:
		documents.append(visitorDocuments(d))
	return documents
	

data = json_readr("sample_100k_lines.json")
#print(getList("visitor_country", "140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))
print(getCountries("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))
#print()
#print(getList("visitor_useragent"))
#print(getBrowsers())
#print()
#print(getList("visitor_uuid","140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))
#print(documentVisitors("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))
#print()
#print(visitorDocuments("745409913574d4c6"))
print()
#print(alsoLike("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))


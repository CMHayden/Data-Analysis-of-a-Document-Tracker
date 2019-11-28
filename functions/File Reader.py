import json

def reader(url):
	data = ["test"]
	with open("issuu_sample.json", "r") as read_file:
		data = json.load(read_file)
	return data

def getCountries(docID):
	countries = []
	for d in data:
		if (d["subject_doc_id"] == docID):
			countries.append(d["visitor_country"])
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
			visitors.append(d["visitor_uuid"])
	dic = {}
	dic[docID] = visitors
	return dic

data = reader("issuu_sample.json")
print(getCountries("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))
print(getBrowsers())
print(documentVisitors("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0"))

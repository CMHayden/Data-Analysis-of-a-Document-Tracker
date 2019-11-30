import matplotlib.pyplot as plt
import json
import re
from datetime import datetime

countriesDict = {
    'DZ':'Africa','AO':'Africa','BJ':'Africa','BW':'Africa','BF':'Africa','BI':'Africa','CM':'Africa','CV':'Africa','CF':'Africa','KM':'Africa','CD':'Africa','DJ':'Africa','EG':'Africa','GQ':'Africa','ER':'Africa','ET':'Africa','GA':'Africa','GM':'Africa','GH':'Africa','GN':'Africa','GW':'Africa','CI':'Africa','KE':'Africa','LS':'Africa','LR':'Africa','LY':'Africa','MG':'Africa','MW':'Africa','ML':'Africa','MR':'Africa','MU':'Africa','MA':'Africa','MZ':'Africa','NA':'Africa','NE':'Africa','NG':'Africa','CG':'Africa','RE':'Africa','RW':'Africa','SH':'Africa','ST':'Africa','SN':'Africa','SC':'Africa','SL':'Africa','SO':'Africa','ZA':'Africa','SS':'Africa','SD':'Africa','SZ':'Africa','TZ':'Africa','TG':'Africa','TN':'Africa','UG':'Africa','EH':'Africa','ZM':'Africa','ZW':'Africa',
    'AF':'Asia','AM':'Asia','AZ':'Asia','BH':'Asia','BD':'Asia','BT':'Asia','BN':'Asia','KH':'Asia','CN':'Asia','GE':'Asia','HK':'Asia','IN':'Asia','ID':'Asia','IR':'Asia','IQ':'Asia','IL':'Asia','JP':'Asia','JO':'Asia','KZ':'Asia','KW':'Asia','KG':'Asia','LA':'Asia','LB':'Asia','MO':'Asia','MY':'Asia','MV':'Asia','MN':'Asia','MM':'Asia','NP':'Asia','KP':'Asia','OM':'Asia','PK':'Asia','PH':'Asia','QA':'Asia','SA':'Asia','SG':'Asia','KR':'Asia','LK':'Asia','SY':'Asia','TW':'Asia','TJ':'Asia','TH':'Asia','TR':'Asia','TM':'Asia','AE':'Asia','UZ':'Asia','VN':'Asia','YE':'Asia',
    'AL':'Europe','AD':'Europe','AT':'Europe','BY':'Europe','BE':'Europe','BA':'Europe','BG':'Europe','HR':'Europe','CY':'Europe','CZ':'Europe','DK':'Europe','EE':'Europe','FO':'Europe','FI':'Europe','FR':'Europe','DE':'Europe','GI':'Europe','GR':'Europe','HU':'Europe','IS':'Europe','IE':'Europe','IM':'Europe','IT':'Europe','XK':'Europe','LV':'Europe','LI':'Europe','LT':'Europe','LU':'Europe','MK':'Europe','MT':'Europe','MD':'Europe','MC':'Europe','ME':'Europe','NL':'Europe','NO':'Europe','PL':'Europe','PT':'Europe','RO':'Europe','RU':'Europe','SM':'Europe','RS':'Europe','SK':'Europe','SI':'Europe','ES':'Europe','SE':'Europe','CH':'Europe','UA':'Europe','UK':'Europe', 'GB':'Europe','VA':'Europe',
    'AS':'Oceania','AU':'Oceania','CK':'Oceania','TL':'Oceania','FJ':'Oceania','PF':'Oceania','GU':'Oceania','KI':'Oceania','MH':'Oceania','FM':'Oceania','NR':'Oceania','NC':'Oceania','NZ':'Oceania','NU':'Oceania','NF':'Oceania','MP':'Oceania','PW':'Oceania','PG':'Oceania','PN':'Oceania','WS':'Oceania','SB':'Oceania','TK':'Oceania','TV':'Oceania','TU':'Oceania',
    'AI':'Americas','AR':'Americas','AW':'Americas','BS':'Americas','BB':'Americas','BZ':'Americas','BM':'Americas','BO':'Americas','BR':'Americas','VG':'Americas','CA':'Americas','KY':'Americas','CL':'Americas','CO':'Americas','CR':'Americas','CU':'Americas','CW':'Americas','DM':'Americas','DO':'Americas','EC':'Americas','SV':'Americas','FK':'Americas','GL':'Americas','GP':'Americas','GT':'Americas','GY':'Americas','HT':'Americas','HN':'Americas','JM':'Americas','MX':'Americas','MS':'Americas','NI':'Americas','PA':'Americas','PY':'Americas','PE':'Americas','PR':'Americas','BL':'Americas','KN':'Americas','LC':'Americas','MF':'Americas','PM':'Americas','VC':'Americas','SR':'Americas','TT':'Americas','US':'Americas','UY':'Americas','VE':'Americas'
    }

def read_JSON(file):
	data = []
	for line in open(file, mode="r"):
		data.append(json.loads(line))
	return data


def get_viewsByCountry(document_id):
	countries = []
	i = 0
	for d in data:
		try:
			if (d["subject_doc_id"] == document_id):
				countries.append(d["visitor_country"])
		except:
			break
	return countries

def get_browserInformation():
    browsers = []
    for d in data:
        try:
            browsers.append(d["visitor_useragent"])
        except:
            break
    return browsers

def clean_viewsByBrowser(dict):
    cleanDict = {}
    for browser in dict:
        toCleanse = str(browser)
        result = re.match("(?:^|(?:\.\s))(\w+)", toCleanse)
        result.group(0)

        if result.group(0) in cleanDict:
            cleanDict[result.group(0)] += dict[browser]
        else:
            cleanDict[result.group(0)] = dict[browser]
    return cleanDict

def documentVisitors(docID):
	visitors = []
	for d in data:
		try:
			if (d["subject_doc_id"] == docID):
				if d["visitor_uuid"] not in visitors:
					visitors.append(d["visitor_uuid"])
		except:
			break
	return visitors

def visitorDocuments(visID):
	documents = []
	for d in data:
		try:
		    if (d["visitor_uuid"] == visID):
			    if (d["subject_doc_id"] not in documents):
				    documents.append(d["subject_doc_id"])
		except:
			break
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

def get_viewsByContinent(dict):
    continentsDict = {'Africa': 0, 'Americas': 0, 'Asia': 0, 'Europe':0, 'Oceania': 0}
    for country in dict:
		try:
			continentsDict[countriesDict[country]] = continentsDict[countriesDict[country]] + dict[country]
		except KeyError:
			print("Countries continent not found: " + country)
    return continentsDict

def create_histogram(dict, xlabel, title):
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel("Frequency", fontsize=15)
    plt.title(title, fontsize=20)

    xRange = list(range(len(list(dict.keys()))))

    plt.xticks(xRange, list(dict.keys()))

    plt.bar(xRange, list(dict.values()), align='center', color='g')
    plt.show()

def counter(data):
    dict = {}
    for val in data:
        if val in dict:
            dict[val] += 1
        else:
            dict[val] = 1
    return dict

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time: ", current_time)

data = read_JSON("functions/sample_3m_lines.json")

#browserDict = counter(get_browserInformation())
#print(browserDict)
#cleanBrowserDict = clean_viewsByBrowser(browserDict)
#print(cleanBrowserDict)

#countries = get_viewsByCountry("130107151047-1cac70c2cbe941359e29d69402c82487")
#print(countries)
#print(get_viewsByContinent(counter(countries)))

#countries = getCountries("130107151047-1cac70c2cbe941359e29d69402c82487")
#histogram(counter((countries)), "Countries", "Counting Countries")

#browsers = getBrowsers()
#histogram(counter((browsers)), "Browsers", "Counting Browsers")

#print(documentVisitors("110411015935-6b1fc1a5af3540338aaf984038b74c23"))
#print(visitorDocuments("450e62176225c0d1"))
#print(alsoLike("110411015935-6b1fc1a5af3540338aaf984038b74c23"))

now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print("End Time: ", end_time)

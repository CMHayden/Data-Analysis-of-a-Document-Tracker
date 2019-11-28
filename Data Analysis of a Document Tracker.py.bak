import matplotlib.pyplot as plt
import json

def reader(url):
    data = ["test"]
    with open("datasets/issuu_sample.json", "r") as read_file:
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

def histogram(dict, xlabel, title):
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel("Frequency", fontsize=15)
    plt.title(title, fontsize=20)

    xRange = range(len(dict.keys()))

    plt.xticks(xRange, dict.keys())

    plt.bar(xRange, dict.values(), align='center', color='g')
    plt.show()


def countriesCounter(data):
    countriesDict = {}
    for country in data:
        if country in countriesDict:
            countriesDict[country] += 1
        else:
            countriesDict[country] = 1
    return countriesDict

def browserCounter(data):
    browsersDict = {}
    for browser in data:
		if browser in browsersDict:
			browsersDict[browser] += 1
		else:
			browsersDict[browser] = 1
    return browsersDict


data = reader("issuu_sample.json")

countries = getCountries("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0")
histogram(countriesCounter((countries)), "Countries", "Counting Countries")

browsers = getBrowsers()
histogram(browserCounter((browsers)), "Browsers", "Counting Browsers")

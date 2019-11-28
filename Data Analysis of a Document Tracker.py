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


data = reader("issuu_sample.json")

countries = getCountries("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0")
histogram(counter((countries)), "Countries", "Counting Countries")

browsers = getBrowsers()
histogram(counter((browsers)), "Browsers", "Counting Browsers")

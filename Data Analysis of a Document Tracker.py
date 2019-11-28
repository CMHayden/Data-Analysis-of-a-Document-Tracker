import matplotlib.pyplot as plt
import json
from datetime import datetime


def reader(file):
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
			print("env_type doesn't exist")
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

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time: ", current_time)

data = reader("functions/sample_3m_lines.json")

countries = getCountries("140228202800-6ef39a241f35301a9a42cd0ed21e5fb0")
histogram(counter((countries)), "Countries", "Counting Countries")

#browsers = getBrowsers()
#histogram(counter((browsers)), "Browsers", "Counting Browsers")
now = datetime.now()
end_time = now.strftime("%H:%M:%S")
print("End Time: ", end_time)

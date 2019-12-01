from datetime import datetime
import matplotlib.pyplot as plt
import collections
import re
import json

def read_JSON(file):
	data = []
	for line in open(file, mode="r"):
		data.append(json.loads(line))
	return data

def getTimes():
    browsers = []
    for d in data2:
        try:
            browsers.append(d["ts"])
        except:
            print("oops")
    return browsers

data2 = read_JSON("functions/sample_3m_lines.json")
data = getTimes()

x = []
y = []

dateDict = {}
for timestamp in data:
    if datetime.fromtimestamp(timestamp).date() in dateDict:
        dateDict[datetime.fromtimestamp(timestamp).date()] += 1
    else:
        dateDict[datetime.fromtimestamp(timestamp).date()] = 1

orderedDict = collections.OrderedDict(sorted(dateDict.items()))

print(list(orderedDict.keys())[0])
print(list(orderedDict.keys())[len(orderedDict) - 1])

for record in orderedDict:
    x.append(record)
    y.append(dateDict[record])

plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()


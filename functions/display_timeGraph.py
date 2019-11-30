from datetime import datetime
import matplotlib.pyplot as plt
import collections

data = [1342631989, 1353631990, 1333631998, 1353631990, 1333631998]
x = []
y = []

dateDict = {}
for timestamp in data:
    print(datetime.fromtimestamp(timestamp).date())
    if datetime.fromtimestamp(timestamp).date() in dateDict:
        dateDict[datetime.fromtimestamp(timestamp).date()] += 1
    else:
        dateDict[datetime.fromtimestamp(timestamp).date()] = 1

orderedDict = collections.OrderedDict(sorted(dateDict.items()))

for record in orderedDict:
    x.append(record)
    y.append(dateDict[record])

plt.plot(x,y)
plt.gcf().autofmt_xdate()
plt.show()


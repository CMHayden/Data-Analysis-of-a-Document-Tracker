import matplotlib.pyplot as plt

# Function which takes data as a parameter and stores the occurrences of country codes in a dictionary
data = ["uk", "mx", "uk", "uk", "az", "jp"]

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

histogram(countriesCounter((data)), "Countries", "Counting Countries")
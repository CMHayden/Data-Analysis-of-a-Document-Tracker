# Function which takes data as a parameter and stores the occurrences of country codes in a dictionary
data = ["uk", "mx", "uk", "uk", "az", "jp"]

countriesDict = {}

for country in data:
    if country in countriesDict:
        countriesDict[country] += 1
    else:
        countriesDict[country] = 1

print(countriesDict)
# Output: {'uk': 3, 'mx': 1, 'az': 1, 'jp': 1}

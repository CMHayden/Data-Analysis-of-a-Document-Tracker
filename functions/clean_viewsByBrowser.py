import re

data = {
   'Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_6 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/11B651 [FBAN/FBIOS;FBAV/7.0.0.17.1;FBBV/1325030;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/7.0.6;FBSS/2; FBCR/Telcel;FBID/phone;FBLC/es_ES;FBOP/5]': 2, 
   'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.63 Safari/537.36': 2, 
   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0': 1,
   'Opera/9.80 (Windows NT 6.1) Presto/2.12.388 Version/12.16':1
}

browsersDict = {}

for browser in data:
    toCleanse = str(browser)
    result = re.match("(?:^|(?:\.\s))(\w+)", toCleanse)
    result.group(0)
    
    if result.group(0) in browsersDict:
        browsersDict[result.group(0)] += data[browser]
    else:
        browsersDict[result.group(0)] = data[browser]

print(browsersDict)


from tkinter import *
from tkinter import ttk
import getopt, sys
import matplotlib.pyplot as plt
import json
import re
from datetime import datetime
from collections import Counter
import collections
import os

fullCmdArguments = sys.argv

argumentList = fullCmdArguments[1:]
unixOptions = "u:d:t:f:h"
gnuOptions = ["help"]
dictArgs = {}
jsonData = []
countriesDict = {
    'DZ': 'Africa', 'AO': 'Africa', 'BJ': 'Africa', 'BW': 'Africa', 'BF': 'Africa', 'BI': 'Africa', 'CM': 'Africa',
    'CV': 'Africa', 'CF': 'Africa', 'KM': 'Africa', 'CD': 'Africa', 'DJ': 'Africa', 'EG': 'Africa', 'GQ': 'Africa',
    'ER': 'Africa', 'ET': 'Africa', 'GA': 'Africa', 'GM': 'Africa', 'GH': 'Africa', 'GN': 'Africa', 'GW': 'Africa',
    'CI': 'Africa', 'KE': 'Africa', 'LS': 'Africa', 'LR': 'Africa', 'LY': 'Africa', 'MG': 'Africa', 'MW': 'Africa',
    'ML': 'Africa', 'MR': 'Africa', 'MU': 'Africa', 'MA': 'Africa', 'MZ': 'Africa', 'NA': 'Africa', 'NE': 'Africa',
    'NG': 'Africa', 'CG': 'Africa', 'RE': 'Africa', 'RW': 'Africa', 'SH': 'Africa', 'ST': 'Africa', 'SN': 'Africa',
    'SC': 'Africa', 'SL': 'Africa', 'SO': 'Africa', 'ZA': 'Africa', 'SS': 'Africa', 'SD': 'Africa', 'SZ': 'Africa',
    'TZ': 'Africa', 'TG': 'Africa', 'TN': 'Africa', 'UG': 'Africa', 'EH': 'Africa', 'ZM': 'Africa', 'ZW': 'Africa',
    'AF': 'Asia', 'AM': 'Asia', 'AZ': 'Asia', 'BH': 'Asia', 'BD': 'Asia', 'BT': 'Asia', 'BN': 'Asia', 'KH': 'Asia',
    'CN': 'Asia', 'GE': 'Asia', 'HK': 'Asia', 'IN': 'Asia', 'ID': 'Asia', 'IR': 'Asia', 'IQ': 'Asia', 'IL': 'Asia',
    'JP': 'Asia', 'JO': 'Asia', 'KZ': 'Asia', 'KW': 'Asia', 'KG': 'Asia', 'LA': 'Asia', 'LB': 'Asia', 'MO': 'Asia',
    'MY': 'Asia', 'MV': 'Asia', 'MN': 'Asia', 'MM': 'Asia', 'NP': 'Asia', 'KP': 'Asia', 'OM': 'Asia', 'PK': 'Asia',
    'PH': 'Asia', 'QA': 'Asia', 'SA': 'Asia', 'SG': 'Asia', 'KR': 'Asia', 'LK': 'Asia', 'SY': 'Asia', 'TW': 'Asia',
    'TJ': 'Asia', 'TH': 'Asia', 'TR': 'Asia', 'TM': 'Asia', 'AE': 'Asia', 'UZ': 'Asia', 'VN': 'Asia', 'YE': 'Asia',
    'AL': 'Europe', 'AD': 'Europe', 'AT': 'Europe', 'BY': 'Europe', 'BE': 'Europe', 'BA': 'Europe', 'BG': 'Europe',
    'HR': 'Europe', 'CY': 'Europe', 'CZ': 'Europe', 'DK': 'Europe', 'EE': 'Europe', 'FO': 'Europe', 'FI': 'Europe',
    'FR': 'Europe', 'DE': 'Europe', 'GI': 'Europe', 'GR': 'Europe', 'HU': 'Europe', 'IS': 'Europe', 'IE': 'Europe',
    'IM': 'Europe', 'IT': 'Europe', 'XK': 'Europe', 'LV': 'Europe', 'LI': 'Europe', 'LT': 'Europe', 'LU': 'Europe',
    'MK': 'Europe', 'MT': 'Europe', 'MD': 'Europe', 'MC': 'Europe', 'ME': 'Europe', 'NL': 'Europe', 'NO': 'Europe',
    'PL': 'Europe', 'PT': 'Europe', 'RO': 'Europe', 'RU': 'Europe', 'SM': 'Europe', 'RS': 'Europe', 'SK': 'Europe',
    'SI': 'Europe', 'ES': 'Europe', 'SE': 'Europe', 'CH': 'Europe', 'UA': 'Europe', 'UK': 'Europe', 'GB': 'Europe',
    'VA': 'Europe',
    'AS': 'Oceania', 'AU': 'Oceania', 'CK': 'Oceania', 'TL': 'Oceania', 'FJ': 'Oceania', 'PF': 'Oceania',
    'GU': 'Oceania', 'KI': 'Oceania', 'MH': 'Oceania', 'FM': 'Oceania', 'NR': 'Oceania', 'NC': 'Oceania',
    'NZ': 'Oceania', 'NU': 'Oceania', 'NF': 'Oceania', 'MP': 'Oceania', 'PW': 'Oceania', 'PG': 'Oceania',
    'PN': 'Oceania', 'WS': 'Oceania', 'SB': 'Oceania', 'TK': 'Oceania', 'TV': 'Oceania', 'TU': 'Oceania',
    'AI': 'Americas', 'AR': 'Americas', 'AW': 'Americas', 'BS': 'Americas', 'BB': 'Americas', 'BZ': 'Americas',
    'BM': 'Americas', 'BO': 'Americas', 'BR': 'Americas', 'VG': 'Americas', 'CA': 'Americas', 'KY': 'Americas',
    'CL': 'Americas', 'CO': 'Americas', 'CR': 'Americas', 'CU': 'Americas', 'CW': 'Americas', 'DM': 'Americas',
    'DO': 'Americas', 'EC': 'Americas', 'SV': 'Americas', 'FK': 'Americas', 'GL': 'Americas', 'GP': 'Americas',
    'GT': 'Americas', 'GY': 'Americas', 'HT': 'Americas', 'HN': 'Americas', 'JM': 'Americas', 'MX': 'Americas',
    'MS': 'Americas', 'NI': 'Americas', 'PA': 'Americas', 'PY': 'Americas', 'PE': 'Americas', 'PR': 'Americas',
    'BL': 'Americas', 'KN': 'Americas', 'LC': 'Americas', 'MF': 'Americas', 'PM': 'Americas', 'VC': 'Americas',
    'SR': 'Americas', 'TT': 'Americas', 'US': 'Americas', 'UY': 'Americas', 'VE': 'Americas'
}

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print(str(err))
    sys.exit(2)

def display_Help():
    print("""
Course Work 2 Help Guide:

This application accepts a number of parameters through the command line. 
Here is an explanation of each of these parameters:

    -t: This sets the task the program shall do. It takes options which
    dictate which task it will perform. These options are the task id
    and are as followed:

        2a: takes a file's address and a document id, and displays a histogram 
        of the countries where users have visited that document from.

        2b: takes a file's address and a document id,  and displays a histogram 
        of the continents where users have visited that document from.

        3a: takes a file's address and displays a histogram of all information 
        regarding browsers stored in a given dataset.

        3b: takes a file's address and displays a histogram of the browser name's 
        stored in a given dataset.

        4d: takes a file's address, a document id, and a user id and displays other
        documents the user may like to read.

        5: takes a file's address, a document id, and a user id and displays a graph
        showing the users relationship to documents the user may like to read.

        6: takes a file's address, a document id, and a user id and displays a graph
        of documents the user may like to read.

        7: takes a file's address and a document id and displays a line chart showing 
        spikes in activity for the document on different days.

        8: takes a file's address and a document id and calculates the average time 
        spent reading the document.

    -u: This allows for passing a user ID into the task. While not all tasks will use this,
    it is mandatory for others such as for task 4d.

    -d: This allows for passing a document ID into the task. While not all tasks will use this,
    it is mandatory for others such as for task 2a

    -f: This allows for passing a location to a dataset which you would like to analyze with 
    the provided tasks.

    -h or --help: Displays this page to help you use the system.

We hope this helps, if not for more help check the user guide which can be found in the 
adjoining report or in the github repository.

    """)


for currentArgument, currentValue in arguments:
    if currentArgument in ("-h", "--help"):
        display_Help()
        sys.exit(2)
    dictArgs[currentArgument] = currentValue


# ↓ ↓ ALL FUNCTION DEFS BELOW HERE ↓ ↓
def read_JSON(file):
    for line in open(file, mode="r"):
        jsonData.append(json.loads(line))
    return jsonData

def getTimes(data):
    browsers = []
    for d in data:
        try:
            browsers.append(d["ts"])
        except:
            None
    return browsers

def get_averageReadTime(data):
    total = 0

    for time in data:
        total = total + (time // 60)

    output = "The average time spent reading this document is" + str((total // len(data))) +  " minutes."
    print(output)
    return output

def display_timeGraph(data):
    x = []
    y = []

    dateDict = {}
    for timestamp in data:
        if datetime.fromtimestamp(timestamp).date() in dateDict:
            dateDict[datetime.fromtimestamp(timestamp).date()] += 1
        else:
            dateDict[datetime.fromtimestamp(timestamp).date()] = 1

    orderedDict = collections.OrderedDict(sorted(dateDict.items()))

    for record in orderedDict:
        x.append(record)
        y.append(dateDict[record])

    plt.plot(x,y)
    plt.xlabel("Dates", fontsize=15)
    plt.ylabel("Ts", fontsize=15)
    plt.title("Average time spent on all the browsers", fontsize=20)
    plt.gcf().autofmt_xdate()
    plt.show()

def create_histogram(dict, xlabel, title):
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel("Frequency", fontsize=15)
    plt.title(title, fontsize=20)

    xRange = list(range(len(list(dict.keys()))))

    plt.xticks(xRange, list(dict.keys()))

    plt.bar(xRange, list(dict.values()), align='center', color='g')
    plt.show()


def get_viewsByCountry(document_id, jsonData = jsonData):
    countries = []
    for d in jsonData:
        try:
            if (d["env_doc_id"] == document_id):
                countries.append(d["visitor_country"])
        except:
            None
    return countries


def get_viewsByContinent(dict):
    continentsDict = {'Africa': 0, 'Americas': 0, 'Asia': 0, 'Europe': 0, 'Oceania': 0}
    for country in dict:
        try:
            continentsDict[countriesDict[country]] = continentsDict[countriesDict[country]] + dict[country]
        except KeyError:
            print("Countries continent not found: " + country)
    return continentsDict


def get_viewsByBrowser(data):
    browsers = []
    for d in data:
        try:
            browsers.append(d["visitor_useragent"])
        except:
            None
    return browsers

def get_timeSpent(data):
    time = []
    for d in data:
        try:
            time.append(d["event_readtime"])
        except:
            None
    return time

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
    for d in jsonData:
        try:
            if (d["env_doc_id"] == docID):
                if d["visitor_uuid"] not in visitors:
                    visitors.append(d["visitor_uuid"])
        except:
            None
    return visitors


def visitorDocuments(visID):
    documents = []
    for d in jsonData:
        try:
            if (d["visitor_uuid"] == visID):
                if (d["env_doc_id"] not in documents):
                    documents.append(d["env_doc_id"])
        except Exception as e:
            print(str(e))
    return documents


def find_alsoLikes(docID, visID, data):
    visitors = documentVisitors(docID);

    dictArray = [visitors];

    documentDict = {};
    documentCounter = Counter();

    for visitor in visitors:
        documentList = visitorDocuments(visitor);
        documentDict[visitor] = documentList;
        documentCounter += Counter(documentList);

    dictArray.append(documentCounter);
    dictArray.append(documentDict);
    return dictArray


def top10(dictArray):
    print("The top 10 documents are:")
    mostCommon = dictArray[1].most_common();
    output = ""
    for x in range(10):
        try:
            output += str(x + 1) + ". " + mostCommon[x][0] + " which totalled " + str(mostCommon[x][1]) + "\n"
        except Exception as e:
            break;
    print(output)
    return output


def dotFileGenerator(arr, docID, visID=None):
    documents = arr[1];
    readers = arr[0];
    links = arr[2];
    dotFile = ["digraph also_likes {",
               " ranksep=.75; ratio=compress; size = \"15,22\"; orientation=landscape; rotate=180;",
               " {",
               "   node [shape=plaintext, fontsize=16];",
               "",
               "   Readers -> Documents ",
               "[label=\"Size: 1m\"];"]

    for reader in readers:
        if (reader == visID):
            extra = "shape=\"box\",style=filled,color=\".3 .9 .7\"];";
        else:
            extra = "shape=\"box\"];";
        str = ' "' + reader[-4:] + '"' + ' [label="' + reader[-4:] + '",' + extra;
        dotFile.append(str);

    for document in documents:
        if (document == docID):
            extra = "shape=\"circle\",style=filled,color=\".3 .9 .7\"];";
        else:
            extra = "shape=\"circle\"];";
        str = ' "' + document[-4:] + '"' + ' [label="' + document[-4:] + '",' + extra;
        dotFile.append(str);

    dotFile.append("");
    dotFile.append("{ rank = same; \"Readers\";");

    for reader in readers:
        str = '  "' + reader[-4:] + '";'
        dotFile.append(str)

    dotFile.append("};{ rank = same; \"Documents\";");

    for document in documents:
        str = '  "' + document[-4:] + '";'
        dotFile.append(str)

    dotFile.append("};");

    for key in links:
        for value in links[key]:
            str = ' "' + key[-4:] + '" -> "' + value[-4:] + '";'
            dotFile.append(str)

    dotFile.append(" };");
    dotFile.append("}");

    dotFile = '\n'.join(line for line in dotFile);

    f = open("source.dot", "w")
    f.write(dotFile);
    f.close();

    print("generating dot files and graphs...")
    try:
        os.system("dot -Tps -o 1m_3.ps source.dot")
        os.system("evince 1m_3.ps")
    except os.error as e:
        print(e)


# ↑ ↑ ALL FUNCTION DEFS ABOVE HERE ↑ ↑
try:
    dictFunctions = {
        # "3a": create_histogram(Counter(get_viewsByBrowser(read_JSON(dictArgs["-f"]))), "Browsers", "Browser Histogram"),
        # "3b": create_histogram(Counter(clean_viewsByBrowser(Counter(get_viewsByBrowser(read_JSON(dictArgs["-f"]))))), "Browsers", "Browser Histogram"),
        # "2a": create_histogram(Counter(get_viewsByCountry(dictArgs["-d"], read_JSON(dictArgs["-f"]))), "Countries", "Countries Histogram"),
        # "2b": create_histogram(Counter(get_viewsByContinent(Counter(get_viewsByCountry(dictArgs["-d"], read_JSON(dictArgs["-f"]))))), "Continents", "Continents Histogram"),
        # "4d": top10(find_alsoLikes(dictArgs["-d"], dictArgs["-u"], read_JSON(dictArgs["-f"]))),
        # "5": dotFileGenerator(find_alsoLikes(dictArgs["-d"], dictArgs["-u"], read_JSON(dictArgs["-f"])), dictArgs["-d"], dictArgs["-u"]),
        # "6": dotFileGenerator(find_alsoLikes(dictArgs["-d"], dictArgs["-u"], read_JSON(dictArgs["-f"])), dictArgs["-d"], dictArgs["-u"]),
        # "8": display_timeGraph(getTimes(read_JSON(dictArgs["-f"]))),
        # "9": get_averageReadTime(get_timeSpent(read_JSON(dictArgs["-f"])))
    }
except Exception as e:
    print(str(e))

    # sample_100k_lines (2).json
    # doc_uuid: 100806162735-00000000115598650cb8b514246272b5
    # user_uuid: 00000000deadbeef

root = Tk()
topTen = StringVar()

def twoa():
    try:
        read_JSON(file.get())
        create_histogram(Counter(get_viewsByCountry(documentID.get())), "Countries", "Countries Histogram")
    except Exception as e:
        print(str(e))

def twob():
    try:
        read_JSON(file.get())
        create_histogram(Counter(get_viewsByContinent(Counter(get_viewsByCountry(documentID.get())))), "Continents",
                         "Continents Histogram")
    except Exception as e:
        print(str(e))


def threea():
    try:
        create_histogram(Counter(get_viewsByBrowser(read_JSON(file.get()))), "Browsers", "Browser Histogram"),
    except Exception as e:
        print(str(e))


def threeb():
    try:
        create_histogram(Counter(clean_viewsByBrowser(Counter(get_viewsByBrowser(read_JSON(file.get()))))), "Browsers",
                         "Browser Histogram"),
    except Exception as e:
        print(str(e))

# sample_100k_lines (2).json
    # doc_uuid: 100806162735-00000000115598650cb8b514246272b5
    # user_uuid: 00000000deadbeef
def fourd():
    try:
        output = top10(find_alsoLikes(documentID.get(), visitorID.get(), read_JSON(file.get())))
        topTen.set("These are top top 10 values:\n" + output)
    except Exception as e:
        print(str(e))


def five():
    try:
        dotFileGenerator(find_alsoLikes(documentID.get(), visitorID.get(), read_JSON(file.get())), documentID.get(), visitorID.get())
    except Exception as e:
        print(str(e))

def eight():
    try:
        display_timeGraph(getTimes(read_JSON(file.get())))
    except Exception as e:
        print(str(e))

def nine():
    try:
        output = get_averageReadTime(get_timeSpent(read_JSON(file.get())))
        topTen.set(output)
    except Exception as e:
        print(str(e))


root.title("Data Analysis")

mainframe = ttk.Frame(root, padding="30 30 30 30")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

file = StringVar()
documentID = StringVar()
visitorID = StringVar()

file_entry = ttk.Entry(mainframe, width=7, textvariable=file)
file_entry.grid(column=4, row=1, sticky=(W, E))
documentID_entry = ttk.Entry(mainframe, width=7, textvariable=documentID)
documentID_entry.grid(column=4, row=2, sticky=(W, E))
visitorID_entry = ttk.Entry(mainframe, width=7, textvariable=visitorID)
visitorID_entry.grid(column=4, row=3, sticky=(W, E))

ttk.Label(mainframe, text="file").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="documentID").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="visitorID").grid(column=3, row=3, sticky=W)
ttk.Label(mainframe, textvariable=topTen).grid(column=3, row=8, sticky=W)

ttk.Button(mainframe, text="2a", command=twoa).grid(column=1, row=5, sticky=W)
ttk.Button(mainframe, text="2b", command=twob).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="3a", command=threea).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text="3b", command=threeb).grid(column=4, row=5, sticky=W)
ttk.Button(mainframe, text="4d", command=fourd).grid(column=5, row=5, sticky=W)
ttk.Button(mainframe, text="5", command=five).grid(column=6, row=5, sticky=W)
ttk.Button(mainframe, text="8", command=eight).grid(column=7, row=5, sticky=W)
ttk.Button(mainframe, text="9", command=nine).grid(column=8, row=5, sticky=W)
root.bind('<Return>')
root.mainloop()

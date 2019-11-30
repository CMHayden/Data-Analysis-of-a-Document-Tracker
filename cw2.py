import getopt, sys

fullCmdArguments = sys.argv

argumentList = fullCmdArguments[1:]

unixOptions = "u:d:t:f:h"
gnuOptions = ["help"]

try:
    arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

dictArgs = {}

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

def get_viewsByCountry(one, two):
    print("it works")


# ↑ ↑ ALL FUNCTION DEFS ABOVE HERE ↑ ↑

dictFunctions = {
    "2a": get_viewsByCountry(dictArgs["-d"], dictArgs["-f"]),
    # "2b": get_viewsByContinent(dictArgs["-d"], dictArgs["-f"]),
    # "3a": get_viewsByBrowser(dictArgs["-f"]),
    # "3b": clean_viewsByBrowser(dictArgs["-f"]),
    # "4d": find_alsoLikes(dictArgs["-d"], dictArgs["-u"], dictArgs["-f"]),
    # "5": create_relationshipGraph(dictArgs["-d"], dictArgs["-u"], dictArgs["-f"]),
    # "6": create_alsoLikesGraph(dictArgs["-d"], dictArgs["-u"], dictArgs["-f"])
}


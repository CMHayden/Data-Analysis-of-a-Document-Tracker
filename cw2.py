import getopt, sys

fullCmdArguments = sys.argv

argumentList = fullCmdArguments[1:]

unixOptions = "u:d:t:f:"

try:
    arguments, values = getopt.getopt(argumentList, unixOptions)
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))
    sys.exit(2)

dictArgs = {}

for currentArgument, currentValue in arguments:
    dictArgs[currentArgument] = currentValue

# ↓ ↓ ALL FUNCTION DEFS BELOW HERE ↓ ↓ 

def get_viewsByCountry(one, two):
    print("it works")


# ↑ ↑ ALL FUNCTION DEFS ABOVE HERE ↑ ↑

dictFunctions = {
    "2a": get_viewsByCountry(dictArgs["-d"], dictArgs["-f"]),
    "2b": get_viewsByContinent(dictArgs["-d"], dictArgs["-f"]),
    "3a": get_viewsByBrowser(dictArgs["-f"]),
    "3b": clean_viewsByBrowser(dictArgs["-f"]),
    "4d": find_alsoLikes(dictArgs["-d"], dictArgs["-u"], dictArgs["-f"]),
    "5": create_relationshipGraph(dictArgs["-d"], dictArgs["-u"], dictArgs["-f"]),
    "6": create_alsoLikesGraph(dictArgs["-d"], dictArgs["-u"], dictArgs["-f"])
}


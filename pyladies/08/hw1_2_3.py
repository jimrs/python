def stringShorterThanFive(listOfStrings):
    resultList = []
    
    for item in listOfStrings:
        if len(item) < 5:
            resultList.append(item)

    return resultList

def stringBeginningWithK(listOfStrings):
    resultList = []

    for item in listOfStrings:
        if item[0] == "k":
            resultList.append(item)

    return resultList

def isStringInList(string, listOfStrings):
    if string in listOfStrings:
        return True
    else:
        return False
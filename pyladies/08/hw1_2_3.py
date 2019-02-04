pets = ["pes", "kocka", "kralik", "had"]

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
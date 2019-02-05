def sortListBySecondChar(liszt):
    tupleList = []
    sortedList = []

    for item in liszt:
        tupleList.append( (item[1], item) )

    tupleList.sort()

    for item in tupleList:
        sortedList.append(item[1])

    return sortedList
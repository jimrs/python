def setAlgebra(list1, list2):
    unionList = []
    intersectionList = []
    differenceList = []

    unionList.extend(list1)
    for item in list2:
        if item not in unionList:
            unionList.append(item)

    for item in list1:
        if item in list2:
            intersectionList.append(item)

    differenceList.extend(list2)
    for item in list1:
        if item in list2:
            differenceList.remove(item)

    return unionList, intersectionList, differenceList
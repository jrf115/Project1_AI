###                                        ###
# John Fahringer 2019 jrf115@zips.uakron.edu #
# Project 1 - AI & Heurisitcs Analysis       #
# Built using Python 3.7
###                                        ###


def myreverse(aList):
    if (len(aList) != 0):
        newList = []
        listIter = len(aList) - 1
        while listIter >= 0:
            newList.append(aList[listIter])
            listIter -= 1
        return newList
    else:
        return aList


def mirror(aList):
    if (len(aList) != 0):
        newList = []
        listIter = len(aList) - 1
        while listIter >= 0:
            if (type(aList[listIter]) is list):   # Need to do a reverse on the inner contents before the oute
                aList[listIter] = mirror(aList[listIter])
            listIter -= 1
        newList = myreverse(aList)
        return newList
    else:
        return myreverse(aList)


def flatten(aList):
    def doFlat(flattenList):
        nonlocal newList
        iter = 0
        length = len(flattenList)
        while iter < length:
            if type(flattenList[iter]) is list:
                doFlat(flattenList[iter])
            else:
                newList.append(flattenList[iter])
            iter += 1
        return newList

    newList = []
    return doFlat(aList)


# def int_list:

# def invert_dict:


print("p1_0000 successfully loaded")
# Testing myreversefunction
print("Testing myreversefunction")
listTest = [1, 4, 6, 34, 2]
print(myreverse(listTest))
print(myreverse([[1, 2], [3, [4, 5]]]))
print(myreverse([]))

# Testing mirror function
print("Testing mirror function")
print(mirror([[1, 2], [3, [4, 5]]]))
print(mirror([1, 2, 4, 5]))
print(mirror([]))

# Testing flatten flatten function
print("Testing flatten function")
print(flatten([[1, 2], [3, [4, 5]]]))
print(flatten([]))
print(flatten([1, 'a']))

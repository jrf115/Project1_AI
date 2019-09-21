###                                        ###
# John Fahringer 2019 jrf115@zips.uakron.edu #
# Project 1 - AI & Heurisitcs Analysis       #
###                                        ###


def myreverse(aList):
    if (len(aList) != 0):
        newList = []
        listLength = len(aList) - 1
        while listLength >= 0:
            newList.append(aList[listLength])
            listLength -= 1
        return newList
    else:
        return "[]"

# def mirror:


# def flatten:


# def int_list:


# def invert_dict:


# Testing myreversefunction
print("p1_0000 successfully loaded")
listTest = [1, 4, 6, 34, 2]
print(myreverse(listTest))
print(myreverse([[1, 2], [3, [4, 5]]]))
print(myreverse([]))

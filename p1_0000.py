###                                        ###
# John Fahringer 2019 jrf115@zips.uakron.edu #
# Project 1 - AI & Heurisitcs Analysis       #
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



# def flatten:

# def int_list:

# def invert_dict:


print("p1_0000 successfully loaded")
# Testing myreversefunction
print("Testing myreversefunction")
listTest = [1, 4, 6, 34, 2]
print(myreverse(listTest))
print(myreverse([[1, 2], [3, [4, 5]]]))
print(myreverse([]))

def flatten(aList):
    flatList = []
    for elem in aList:
        if type(elem) == list:
            flatList.extend(flatten(elem))
        else:
            flatList.append(elem)
    print(flatList)
    return flatList

sample = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten(sample)

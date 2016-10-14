def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    interDict = {}
    diffDict = {}
    keyList = []

    for key in d1:
        if key in d2:
            keyList.append(key)
            interValue = f(d1[key], d2[key])
            interDict[key] = interValue 

    for key in d1:
        if key not in keyList:
            diffDict[key] = d1[key]
    for key in d2:
        if key not in keyList:
            diffDict[key] = d2[key]
    print(interDict, diffDict)
    return (interDict, diffDict)

def f(a, b):
    return a + b
d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

dict_interdiff(d1, d2)

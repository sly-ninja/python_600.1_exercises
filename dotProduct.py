def dotProduct(listA, listB):
    summy = 0
    for i in range(len(listA)):
        product = listA[i] * listB[i]
        summy += product
    return summy


one = [1, 2, 3]
two = [4, 5, 6]
dotProduct(one, two)
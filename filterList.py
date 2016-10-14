def applyF_filterG(L, f, g):

    # L_copy = L[:]
    # for i in L_copy:
    #     if g(f(i)) == False:
    #         L.remove(i)

    L[:] = [el for el in L if g(f(el)) == True]
    if L == []:
        return -1
    else:
        return max(L)



def summy(i):
    return i + 2
def test(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, summy, test), L)
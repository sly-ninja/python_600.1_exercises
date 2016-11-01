def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def inside_function (x):
        total = 0
        k = len(L) - 1
        for element in L:
            total += element*(x**k)
            k -= 1
        print(total)
        return total
    return inside_function

general_poly([1, 2, 3, 4])(10)
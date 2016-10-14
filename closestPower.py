def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    x = 0
    if abs(base**x - num) == 0:
        return x
    while abs(base**x - num) < abs(base**(x-1) - num):
        x += 1
    print(x-1)
    return x - 1
    

closest_power(7, 52)
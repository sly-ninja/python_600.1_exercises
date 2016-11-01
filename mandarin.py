trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''

    by_ten = int(us_num) // 10
    remainder = int(us_num) % 10

    if by_ten == 0:
        return trans[str(remainder)]
    elif by_ten == 1:
        if remainder == 0:
            return 'shi'
        else:
            return 'shi ' + trans[str(remainder)]
    elif by_ten > 1:
        if remainder == 0:
            return trans[str(by_ten)] + ' shi'
        else:
            return trans[str(by_ten)] + ' shi ' + trans[str(remainder)]

# convert_to_mandarin(1)
convert_to_mandarin(12)
convert_to_mandarin(26)
convert_to_mandarin(0)
convert_to_mandarin(99)
convert_to_mandarin(30)
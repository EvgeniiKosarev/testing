import numpy

def smm(n):
    '''
    (int)-> int

    Function returns the smallest natural number, that can be divided by numbers
    1 to n, inclusive, with no remainder.

    '''

    
    multiples = [1]
    for i in range(2, n+1):
        remainder = 0
        for k in multiples:
            if i%k ==0:
                i = i//k
            remainder = i
        else:
            if remainder != 0:
                multiples.append(remainder)

    return numpy.prod(multiples)


# new branch: optimizing


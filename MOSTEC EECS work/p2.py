## Define a procedure p2(x) that takes an integer parameter x.
##If x is greater than 1, the procedure returns the largest power
## of two that is less than x; otherwise, it returns 0.

def p2(x):
    condition = False
    power = 0
    if x > 1:
        while condition == False:
            exponent = 2 ** power
            if exponent >= x:
                condition = True
                return exponent - (2 ** (power-1))
            power += 1
    else:
        return 0

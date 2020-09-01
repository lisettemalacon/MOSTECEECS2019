def prime(x):
    if x >= 2:
        for number in range(2,x):
            if (x % number == 0):
                return False
    if x == 1 or x == 0:
            return False
    else:
        return True
    

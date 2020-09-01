def posNegMult(m,n):
    if m > 0 and n > 0:
        return sum(m for i in range(n))
    elif m < 0 and n > 0:
        return sum(m for i in range(abs(n)))
    elif m > 0  and n < 0:
        return -sum(m for i in range(abs(n)))
    elif m < 0 and n < 0:
        return -sum(m for i in range(abs(n)))
    else:
        return 0
    


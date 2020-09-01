def bisection(f, x0, x1, threshold):
    fBest = f(x0)
    xBest = x0
    
    while x0 < x1:
        test = round(f(x0 + 10** -6) - f(x0 - 10** -6)) / 2*10**-6
        if test < 0:
            x0 += threshold
        elif test > 0:
            x0 += threshold
        elif test == 0:
            xBest = x0
            fBest = f(x0)
        test = round(f(x0 + 10** -6) - f(x0 - 10** -6)) / 2*10**-6
        
    return (xBest,fBest)
        

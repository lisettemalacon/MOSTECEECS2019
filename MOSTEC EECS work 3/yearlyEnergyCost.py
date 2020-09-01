def optOverLine(f, x0, x1, threshold):
    fBest = f(x0)
    while x0 < x1:
        add = x0 + threshold
        x0 += threshold
        if f(add) < fBest:
            xBest = add
            fBest = f(add)
    return (xBest,fBest)

        

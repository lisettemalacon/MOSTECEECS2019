## when acceleration is 0, that's when velocity is at its maximum
## before then, it's the ideal acceleration, which is v(t) = at

def velocity_with_term(t, a, V):
    if (a*t) > V:
        return V
    elif (a*t) < V:
        return a*t

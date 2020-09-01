##Define a procedure perfectSquare(x), True if the integer argument x is a perfect square,
## and False otherwise. Consider 0 and 1 to be perfect squares.

def perfectSquare(x):
    for number in range(0,x+1):
        if number ** 2 == x:
            return True
    return False
    

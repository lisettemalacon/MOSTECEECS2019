##Define a procedure div(m, n), which returns the integer part of m/n,
##where both arguments are positive integers. Dont use / .
## So for example div(29,3) should return 9.

def div(m,n):
    quotient = 0
    while m >= n:
        m -= n
        quotient += 1
    return quotient

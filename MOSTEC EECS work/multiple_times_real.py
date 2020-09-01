##Define a procedure mult(m,n) that returns the product of nonnegative integers m and n.
## Your function should return an int and not make use of the * operator.


def mult(m,n):
    mylist = list(range(n))
    i = 0 
    product = 0
    while i < len(mylist): 
        i +=1
        product = product + m       
    return product

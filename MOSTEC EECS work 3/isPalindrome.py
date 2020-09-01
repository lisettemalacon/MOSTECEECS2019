def isPalindrome(x):
    check = 0
    element = 0
    reverse = -1
    length  = 0 
    while length < len(x):
            if x[element] == x[reverse]:
                length += 1
                check += 1
                element += 1
                reverse -= 1
            else:
                return False
    if check == len(x):
            return True
            
            

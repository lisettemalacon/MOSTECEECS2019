movieObjects = ["peppa's first movie ", " david is still not OP", "big circumference "]

def averageTitleLength(movieObjects):
    averageTitle = 0
    for char in movieObjects:
       for letter in char:
           averageTitle += 1
    return str(averageTitle/len(movieObjects))

print("the average title length is " + averageTitleLength(movieObjects))

def collision(coord1,w1,h1,coord2,w2,h2):
    x1 = coord1[0]
    y1 = coord1[1]
    x2 = coord2[0]
    y2 = coord2[1]
    
    width1 = x1 + w1
    height1 = y1 + h1
    width2 = x2 + w2
    height2 = x2 + h2
    
    x_intersection =  [x for x in list(range(x1,width1 + 1)) if x in list(range(x2,width2 + 1))]
    y_intersection = [y for y in list(range(y1,height1 + 1)) if y in list(range(y2,height2 +1))]
    
    if (len(x_intersection) >= 1) and (len(y_intersection) >= 1):
        return True
    else:
        return False
    
         

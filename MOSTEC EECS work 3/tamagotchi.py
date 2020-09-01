hunger = 0
happiness = 5
energy = 5

def tamagotchi(input=None):
    global hunger
    global happiness
    global energy
    
                    
    if input == 'feed':
        happiness -= 1
        energy -= 1
        hunger = 0
        
    if input == 'play':
        hunger += 1
        energy -= 1
        happiness = 5
               
    if input == 'nap':
        hunger += 1
        happiness -= 1
        energy = 5
        
    if input == None:
        hunger += 1
        happiness -= 1
        energy -=1
    
    if hunger == 5:
        hunger = 0
        happiness = 5
        energy = 5
        return ":( Starvation"
                  
    if happiness == 0:
        hunger = 0
        happiness = 5
        energy = 5
        return ":( Ran Away"
              
    if energy == 0:
        hunger = 0
        happiness = 5
        energy = 5
        return ":( Collapsed"
    return [hunger, happiness, energy]
    

    

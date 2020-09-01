import requests
from bs4 import BeautifulSoup
import json
while True:
    print("\nHi there!")
    number = input("What integer would you like to know about, friend? ")
    try:
        number = int(number)
        
        
    except: #catch a non-number situation
        print("Were you not listening to me?  I asked for an integer. Sometimes I think I'm just talking at a wall. It is like we're not even on the same page anymore. All you do is work on EECS and listen to really good music. This is getting frustrating.\n\n")
        continue #don't do code in rest of loop...start over
    print("Great, here's some information on the number {} \n".format(number))
    to_send = "http://numbersapi.com/{}".format(number)
    b = requests.get(to_send)
    print(b.text)
    
    #take input, query numbersapi.com
    #filter response, and say it back:

    

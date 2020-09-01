import requests
import json
from bs4 import BeautifulSoup
import time

def wiki_getter(phrase):
    to_send = "https://en.wikipedia.org/w/api.php?titles=" +phrase.lower() + "&action=query&prop=extracts&redirects=1&format=json&exintro="
    b = requests.get(to_send)
    data = b.json()
    keys = data.keys()

    if len(keys) < 3:
        print("The term {} cannot be found".format(phrase))
        time.sleep(0.5)
        return False
    else:
        pretext = data['query']['pages']
        number = list(pretext.keys())[0]
        extract = pretext[number]
        info = extract['extract']
        soup = BeautifulSoup(info,"html.parser")
        text = soup.get_text()
        count = 0
        for i in range(len(text)):
            if text[i:i+2] == ". " and count != 2:
                count += 1
            elif count == 2:
                print(text[0:i])
                count = 0


    

while True:
    phrase = input("What would you like to look up? ")
    time.sleep(0.5)
    wiki_getter(phrase)





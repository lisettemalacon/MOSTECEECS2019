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
        print("\n The term {} cannot be found".format(phrase))
        time.sleep(0.5)
        return False
    else:
        pretext = data['query']['pages']
        number = list(pretext.keys())[0]
        extract = pretext[number]
        info = extract['extract']
        soup = BeautifulSoup(info,"html.parser")
        text = soup.get_text()
        new_text = text.split(". ")

        if len(new_text) > 1:
            first_sentence = new_text[0]
            print(first_sentence + '.')
            second_sentence = new_text[1]
            print(second_sentence + '.')
        else:
            first_sentence = new_text[0]
            print(first_sentence)
       
    

while True:
    phrase = input("\n What would you like to look up? ")
    time.sleep(0.5)
    wiki_getter(phrase)

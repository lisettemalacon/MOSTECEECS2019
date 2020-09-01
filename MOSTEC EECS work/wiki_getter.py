import time
import requests
import json
from bs4 import BeautifulSoup



to_send = "https://en.wikipedia.org/w/api.php?titles=cat&action=query&prop=extracts&redirects=1&format=json&exintro="
b = requests.get(to_send)
data = b.json
print(data)
      #  keys = data.keys()
       # print(keys)
        


    


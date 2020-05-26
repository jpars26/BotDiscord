from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import tibiapy.client




def get_character(name):
    url = tibiapy.Character.get_url(name)

    r = requests.get('https://www.tibia.com/community/?subtopic=characters&name=Hercules+of+Revenge')
    content = r.text
    character = tibiapy.Character.from_content(content)
    return character

print(get_character('Amaral'))

def fetch_world(online_count):
    url = tibiapy.World.get_url(online_count)

    r = requests.get('https://www.tibia.com/community/?subtopic=worlds&world=Assombra')
    content = r.text
    world = tibiapy.World.from_content(content)
    return world

print(fetch_world('Antica'))

import requests
import xmltodict

rss = input("enter your rss url: ")
response = requests.get(rss)

tree = xmltodict.parse(response.content)


for episode in tree["rss"]["channel"]["item"]:
    print(episode["title"], end=": ")
    print(episode["enclosure"]["@url"])

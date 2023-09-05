""" Use the News API and the requests module to fetch the daily news related to different   topics.
Go to: "https://newsapi.org/" and explore the various options to build you application
 """

import requests
import json

query = input("What type of new you want: ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-08-05&sortBy=publishedAt&apiKey=9bba9489d313423bb3a99519b134193e"
r = requests.get(url)
#print(r.text)#This will give the value as string so we have to strintify it using JSON module
news = json.loads(r.text)
#print(news, type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("__________________________________________________")

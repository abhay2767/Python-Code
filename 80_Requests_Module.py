import requests
#GET Request:-
""" response = requests.get("https://www.google.com/")
print(response.text) """

#POST Request:-
url = "https://jsonplaceholder.typicode.com/todos/1"
data = {
    "title": 'Abhay',
    "body": 'Dubey',
    "userId": 1,
}
headers = {
    'content-type': 'application/json; charset=UTF-8',
}
response = requests.post(url, headers=headers,json=data)
print(response.text)

#bs4 Module:- (beautifulSoup) Get all website html data
#download package "pip install bs4"
from bs4 import BeautifulSoup

url1  =  "https://kafka.apache.org/documentation/"
r = requests.get(url1)
#print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())
for heading in soup.find_all("h2"):
    print(heading.text)


import requests

url = "http://localhost:7776/"

requests.post(url, json={"name": "Amintiri din Copilarie", "pages": 200, "author": "Ion Creanga"})
requests.post(url, json={"name": "2052", "author": "Jørgen Randers", "pages": 473})
requests.post(url, json={"name": "Game of Thrones", "author": "George Martin", "pages": 600})

# requests.delete(url, json={"name": "Amintiri din Copilarie"})


requests.put(url, json={"name": "2052", "pages": 90})
zoo_url = "https://zoo-animal-api.herokuapp.com/animals/rand"


import requests

response = requests.get(zoo_url)

json = response.json()
print(json)

print(json["name"])




crypto_url = "https://api.coingecko.com/api/v3/indexes"

response2 = requests.get(crypto_url)

json2 = response2.json()

print(json2)

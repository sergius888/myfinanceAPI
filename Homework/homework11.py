#ex1
 # create a function which receives a desired number of animals & returns a list of their names
 # you can use the URL https://zoo-animal-api.herokuapp.com/animals/rand/{number_of_animals}


# def animal_name(number_of_animals):
#       number_of_animals = input("How many animals? ")
#       zoo_url = f"https://zoo-animal-api.herokuapp.com/animals/rand/{number_of_animals}"
#       response = requests.get(zoo_url)
#       json = response.json()
#       animal_list = []
#       for index in range(len(json)):
#           for key in json[index]:
#               if key == 'name':
#                   x = json[index][key]
#                   animal_list.append(x)
#       return animal_list
#
# print(animal_name(2))



#or
import requests

def animals(number: int) -> list[str]:
    url = "https://zoo-animal-api.herokuapp.com/animals/rand/" + str(number)
    animals = requests.get(url).json()
    names = [x["name"] for x in animals]
    return names

print(animals(4))

#ex2
 # we can get the list of cryptocurrency coins from here https://api.coingecko.com/api/v3/coins/list
 # create a method which lists all the names
 # create a method which returns the symbol, name for a given id



def get_coins():
    url = "https://api.coingecko.com/api/v3/coins/list"
    coins = requests.get(url).json()
    return coins

def get_all_names():
    coins = get_coins()
    names = [x["name"] for x in coins]
    return names


def get_symb_and_anmes(id: str):
    coins = get_coins()
    for a_coin in coins:
        if a_coin["id"] == id:
            return a_coin["name"], a_coin["symbol"]

print(get_symb_and_anmes("neurotoken"))

 #ex3
 # let's query the NASA picture of the day
 # url https://api.nasa.gov/planetary/apod?
 # you will need an api key, you can use the demo key as a query param
 # requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "DEMO_KEY"})
 # in the dict of params you can also add other params, you can check them in nasa_query_params.png
 # create a function which returns the explanation & the link of the image for a given date


date = input("Type a date YYYY-MM-DD to get the explanation and an image/video link: ")

nasa = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key": "DEMO_KEY"}).json()
#
print(nasa["url"])
print(nasa["explanation"])


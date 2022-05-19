= Application programming interface

APIs define a set of methods which can be called from outside and interact with an application. These are language agnostic, so I can call from javascript an API written in Python. This is extremly useful to have multiple applications interact with each other.

Most used API in Web is REST API.

There are 4 HTTP methods:

GET - To retrieve information. This method must NOT change state.

POST - To create a new resource.

PUT / PATCH - To modify an existing resource. Should throw an error if the resource is not created.

DELETE - To remove an existing resource.

**How call an API**

```
# in python we use the lib requests to make the calls
import requests

url = "http://our.api.url:8000"


# call and retrieve all books, GET <url>/books
response = requests.get(f"{url}/books")
# the response is a requests.Response object and we have methods to get info from it
# print the content of the response
print(response.json())
# print the status code, 2** is good
print(response.status_code)


# call and retrieve info about one book
# some GET operations have query params to identify a specific resource
book_id = 2
response = requests.get(f"{url}/books", params={"book_id": book_id})


# call and create a new book, we will send the info in the data param which represents the body of the request
book_info = {"name": "Sapiens", "author": "Hararri"}
response = requests.post(f"{url}/books", data=book_info)
id = response.json()["id"]

# call and modify a book
requests.post(f"{url}/books", data={"id": id, author: "Yuval Hararri"})
# or another option
requests.post(f"{url}/books/{id}", data={author: "Yuval Hararri"})


# call and delete a book
requests.delete(f"{url}/books/{id}")
# or another way is to use query params
requests.delete(f"{url}/books", params={"id": id})

```

All requests generate a response. How do we know if it was successful or not? We have a status code.

200 or 2** means it is GOOD

3** means we need to go to another URL

4** means it is the client's fault (maybe a param was not right)

5** means it is the server fault

For all the status codes: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

For more info about APIs:
https://www.dataquest.io/blog/python-api-tutorial/
https://rapidapi.com/blog/how-to-use-an-api-with-python/

**FastAPI Docs**

https://fastapi.tiangolo.com/

tutorial -> https://fastapi.tiangolo.com/tutorial/

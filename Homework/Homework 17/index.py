# this is our root file, when we execute this we will start our app
# webpage for fastapi framework https://fastapi.tiangolo.com/tutorial/,
# also https://realpython.com/fastapi-python-web-apis/

# uvicorn index:app --reload --port 7777
# uvicorn is the server which will start
# index:app, index -> the file name, app -> the FastAPI object name
# --reload -> the server will restart when we modify the code
# --port <port_number> -> select on which port to start

import json
from fastapi import FastAPI

app = FastAPI(
    title="Name of our app",  # TODO for homework, name your application
    # <major_version>.<minor_version>.<patch_version>
    version="0.2.0",  # increase version after finishing homework
    description="",  # TODO add a description
)


@app.get(
    "/health",
    summary="This will be visible at start",
    description="We can describe this API call",
    response_description="We can describe the response",
)
def health() -> dict:
    return {
        "status": "online",
        "engine": "on",
    }


list_of_items = []


# TODO replace this call with your domain item, put at least 4 values
# example, if you want to do a tasks app you can add a task (name, deadline, priority, category)
# save the item in the file
@app.post("/items")
def add_new_item(request: dict):
    list_of_items.append(request)
    list_json = json.dumps(list_of_items)
    file = open("database.txt", "w")
    file.write(list_json)
    file.close()


# TODO return your domain items
# example if you want to do a tasks app return the list of tasks, and rename the url /items -> /tasks
@app.get("/items")
def get_items():
    return list_of_items


# TODO add a put method to edit your domain item
# TODO add a delete method to remove a domain item from the list
# these methods should also save the data into a file for persistence across server reboots


@app.on_event("startup")
def load_list_of_items():
    file = open("database.txt")
    json_items = file.read()
    file.close()
    list_of_items.append(json.loads(json_items))
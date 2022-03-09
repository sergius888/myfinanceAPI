# create a web server which can keep a list of games, films, tv shows & books
# GET /games returns the list of games, GET /films returns the list of films and so on
# POST /games creates a game, ...
# PUT /games/<name> can update the progress of the specified game, ...
# DELETE /games/<name> removes the game from the list which has the <name>, ...
# GET /games/progress returns the name & the progress in percent

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class EntertainmentItem:
    def __init__(self, name: str, studio: str, length: int, consumed: int):
        self.name = name
        self.studio = studio
        self.length = length
        self.consumed = consumed

    def to_json(self):
        return {
            "name": self.name,
        }

    def to_json_with_progress(self):
        return {
            "name": self.name,
            "progress": str(self.consumed / self.length * 100) + "%",
        }

    def add_progress(self, progress: int):
        self.consumed += progress


class Film(EntertainmentItem):
    def __init__(self, name: str, studio: str, length: int, watched: int):
        super().__init__(name, studio, length, watched)


class Game(EntertainmentItem):
    def __init__(self, name: str, studio: str, total_hours: int, hours_played: int):
        super().__init__(name, studio, total_hours, hours_played)


class OurHandler(BaseHTTPRequestHandler):
    games = {}
    tvshows = {}

    def do_GET(self):
        self.send_response_and_headers()
        if self.path == "/games":
            self.write_to_body(self.games)
        if self.path == "/tvshows":
            self.write_to_body(self.tvshows)
        if self.path == "/games/progress":
            self.write_to_body(self.games, "to_json_with_progress")

    def send_response_and_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_POST(self):
        input = self.read_user_input()
        if self.path == "/games":
            new_game = Game(input["name"], input["studio"], input["total_hours"], input["hours_played"])
            self.games[new_game.name] = new_game
        self.send_response_and_headers()

    def do_PUT(self):
        input = self.read_user_input()
        if "/games" in self.path:
            hours = input["hours_played"]
            name = self.path[7:]
            self.games[name].add_progress(hours)
        self.send_response_and_headers()

    def do_DELETE(self):
        if "/games" in self.path:
            # self.path = /games/spiderman
            # self.path = /games/godofwar
            name = self.path[7:]
            self.games.pop(name)
        self.send_response_and_headers()

    def read_user_input(self):
        length = self.headers['Content-Length']
        input = self.rfile.read(int(length)).decode(encoding="utf8")
        d = json.loads(input)
        return d

    def write_to_body(self, items: dict, method_to_json: str = "to_json"):
        # to call an object's function using a string, use getattr
        items_dict = [getattr(x, method_to_json)() for x in items.values()]
        json_items = json.dumps(items_dict)
        self.wfile.write(bytes(json_items, encoding="utf8"))


if __name__ == "__main__":
    server_and_port = ("localhost", 7777)
    server = HTTPServer(server_and_port, OurHandler)
    server.serve_forever()

# Create classes for these 4 types of data
# games have a name, studio, hours to finish, hours played
# films have a name, studio, length in minutes, minutes watched
# tv shows have a name, studio, number of episodes, number of episodes watched
# books have a name, author, number of pages, number of pages read
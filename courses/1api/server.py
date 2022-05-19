from http.server import HTTPServer, BaseHTTPRequestHandler
import json  # dumps & loads


# dumps -> from python object (ex dict) to json
# loads -> from json to python object

# define how to handle the request
class Handler(BaseHTTPRequestHandler):
    films = []
    # the requests.get
    def do_GET(self):
        # write the code of the response
        self.send_response(200)
        # write the headers
        self.send_header("Content-type", "application/json")
        self.send_header("our_own_key", "la misto")
        self.end_headers()
        # write the body
        d_json = json.dumps(self.films)
        self.wfile.write(bytes(d_json, encoding="utf8"))

    def do_POST(self):
        length = self.headers['Content-Length']
        input = self.rfile.read(int(length)).decode(encoding="utf8")
        d = json.loads(input)
        self.films.append(d["name"])
        self.send_response(200, message="We added the film to your watchlist!")
        self.send_header("Content-type", "application/json")
        self.end_headers()



# tell python what to execute
if __name__ == "__main__":
    # ip is like the building adress, the port is the apartment
    hostname_and_port = ("127.0.0.1", 8080)
    web_server = HTTPServer(hostname_and_port, Handler)
    web_server.serve_forever()

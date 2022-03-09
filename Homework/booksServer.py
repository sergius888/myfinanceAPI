# create a web server to keep a list of books
# when we call POST we can add a book to the list, we specify the name & how many pages it has
# when we call DELETE we just specify the name & remove the book from the list
# we can record our reading progress, how many pages we read, we use PUT and specify the name of the book and
# how many pages we read since our last input (we need to keep a value of pages_read and add to it the new number)
# GET returns a list of the book names & the percentage of how much we read

from http.server import HTTPServer, BaseHTTPRequestHandler
import json  # dumps & loads


# define how to handle the request
from courses.oop_course.oop_book import Book


class Handler(BaseHTTPRequestHandler):
    books = {}  # initialize the list of books, empty list

    def do_POST(self):
        # first, read the input
        new_book = self.read_input()
        # validate the input
        new_book_name = new_book["name"]
        if new_book_name in self.books.keys():
            self.send_response(409, message="The book already exists!")
        else:
            # add the info if valid
            self.books[new_book_name] = Book(new_book["name"], new_book["author"], new_book["pages"])
            self.send_response(200, message="We added the book to your library!")
        self.add_headers()

    def do_DELETE(self):
        a_book = self.read_input()
        if a_book["name"] in self.books.keys():
            self.books.pop(a_book["name"])
        self.send_response(200, message="We removed the book!")
        self.add_headers()

    def do_PUT(self):
        a_book = self.read_input()
        # example: a_book = {"name": "2052", "pages": 90}
        name = a_book["name"]
        pages = a_book["pages"]
        if name in self.books.keys():
            self.books[name].add_pages_read(pages)
            self.send_response(200, message="We added the read pages!")
        else:
            self.send_response(404, message="The book was not added to inventory!")
        self.add_headers()

    def do_GET(self):
        # write the code of the response
        self.send_response(200)
        # write the headers
        self.add_headers()
        if self.path == "/progress":
            info = self.get_books_progress()
        else:
            info = [b.__dict__ for b in self.books.values()]
        # write the body
        d_json = json.dumps(info)
        self.wfile.write(bytes(d_json, encoding="ISO-8859-1"))

    def read_input(self):
        length = self.headers['Content-Length']
        input = self.rfile.read(int(length)).decode(encoding="utf8")
        return json.loads(input)

    def add_headers(self):
        print(self.books)
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def get_books_progress(self):
        return [{
            "name": b.name,
            "percent_read": b.get_percent_read(),
        } for b in self.books.values()]


# tell python what to execute
if __name__ == "__main__":
    # ip is like the building adress, the port is the apartment
    hostname_and_port = ("127.0.0.1", 7776)
    web_server = HTTPServer(hostname_and_port, Handler)
    web_server.serve_forever()
# create a web server to keep a list of books
# when we call POST we can add a book to the list, we specify the name & how many pages it has
# when we call DELETE we just specify the name & remove the book from a list
# we can record our reading progress, how many pages we read, we use PUT and specify the name of the book and
# how many pages we read since our last input (we need to keep a value of pages_read and add to it the new number)
# GET returns a list of the book names & the percentage of how much we read


from http.server import HTTPServer, BaseHTTPRequestHandler
import json  # dumps & loads

tasklist = ['Task 1', 'Task 2', 'Task 3']


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Hello S'.encode())



def main():
    PORT = 7777
    server = HTTPServer(('localhost', PORT), requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ = '__main__':
    main()
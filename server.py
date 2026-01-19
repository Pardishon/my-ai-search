from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index2.html'
        return SimpleHTTPRequestHandler.do_GET(self)

os.chdir('/workspaces/my-ai-search')
server = HTTPServer(('localhost', 8080), MyHandler)
print("Сервърът е стартиран на http://localhost:8080")
print("Всички заявки ще бъдат редиректирани към index2.html")
server.serve_forever()

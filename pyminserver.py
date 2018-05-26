from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from inspect import getargspec, getsource
import importlib
import __main__

class handle(BaseHTTPRequestHandler):
    def initialise_text_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def initialise_image_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'image/png')
        self.end_headers()

    def do_GET(self):
        fName = __main__.__file__[0:-3]
        header = handle.parseHeaders(str(self.headers))
        output = importlib.import_module(fName).main(self.path, **header)
        if type(output) == file:
            self.initialise_image_header()
            output = output.read()
        else:
            self.initialise_text_header()
        self.wfile.write(output)

    def do_POST(self):
        self.initialise_text_header()
        try:
            assert(hasattr(importlib.import_module(__main__.__file__[0:-3]), "post"))
        except AssertionError:
            print "Error: No function post() found. Passing."
            return
        try:
            assert(len(tuple(getargspec(importlib.import_module(__main__.__file__[0:-3]).post))[0]) == 1 and type(tuple(getargspec(importlib.import_module(__main__.__file__[0:-3]).post))[2]) == str)
        except AssertionError:
            print "Error: Invalid parameters for post(request, **headers). Passing."
            return
        fName = __main__.__file__[0:-3]
        header = handle.parseHeaders(str(self.headers))
        output = importlib.import_module(fName).post(self.path, **header)
        self.wfile.write(output)

    @staticmethod
    def parseHeaders(head):
        return dict(map(lambda x: x.split(": "), [x.replace('\r', "") for x in head.split("\n") if x != ""]))

def start(server_class=HTTPServer, handler_class=handle, port=80):
    try:
        assert(hasattr(importlib.import_module(__main__.__file__[0:-3]), "main"))
    except AssertionError:
        print "Error: No function main() found. Exiting."
        exit()
    try:
        assert(len(tuple(getargspec(importlib.import_module(__main__.__file__[0:-3]).main))[0]) == 1 and type(tuple(getargspec(importlib.import_module(__main__.__file__[0:-3]).main))[2]) == str)
    except AssertionError:
        print "Error: Invalid parameters for main(request, **headers). Exiting."
        exit()
    server_address = ('', port)
    httpServe = server_class(server_address, handler_class)
    print "Running on http://127.0.0.1:{}/ (Press CTRL+C to quit)".format(port)
    httpServe.serve_forever()

if __name__ == "__main__":
    exit()
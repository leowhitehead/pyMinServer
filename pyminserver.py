from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
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

    def do_HEAD(self):
        self.initialise_text_header()

    @staticmethod
    def parseHeaders(head):
        head = head.split("\n")
        head = [x.replace('\r', "") for x in head if x != ""]
        head = dict(map(lambda x: x.split(": "), head))
        return head

def start(server_class=HTTPServer, handler_class=handle, port=80):
    server_address = ('', port)
    httpServe = server_class(server_address, handler_class)
    print "Running on http://127.0.0.1:{}/ (Press CTRL+C to quit)".format(port)
    httpServe.serve_forever()

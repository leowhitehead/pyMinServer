from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

configs = {
    "port": 80,
    "imgExtensions": ("jpeg", "jpg", "exif", "tff", "gif", "bmp", "png", "eps")
}


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
        import main
        header = handle.parseHeaders(str(self.headers))
        output = main.main(self.path, **header)
        print type(output)
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

def start(server_class=HTTPServer, handler_class=handle, port=configs["port"]):
    server_address = ('', port)
    httpServe = server_class(server_address, handler_class)
    print "Running on http://127.0.0.1:{}/ (Press CTRL+C to quit)".format(configs["port"])
    httpServe.serve_forever()

import pyMinServer

def main(request, **header):
    """A simple example site demo. main() handles all get requests.
    'request' is the request path, '**header' is the"""
    print "Request: GET {}".format(request)
    request = request[1:]
    if request in ["", "index", "index.html", "index.htm"]:
        return "<html><h1>Index of site</h1></html>"
    elif request in ["about", "about.html", "about.htm"]:
        return "<html><h1>About Page</h1></html>"
    elif request == "favicon.ico":
        return open("image.jpg", "rb").read()
    else:
        return "<html><h1>Error 404</h1><br><p>File Not Found</p></html>"

if __name__ == "__main__":
    pyMinServer.start()
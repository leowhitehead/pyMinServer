import pyMinServer

def main(request, **headers):
    print "request: GET {}".format(request)
    if request.startswith("/index"):
        return "<html><body><h1>Index Page!</h1><img src=\"img.jpg\"></body></html>"
    elif request.endswith((".png", ".jpg", ".jpeg")):
        return open(request[1:], "rb").read()


if __name__ == "__main__":
    pyMinServer.start()
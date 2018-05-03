# pyMinServer
A simple customisable web server with almost no boilerplate code


## Example program:

```python
import pyminserver

def main(request, **header):
  return "<html><h1>Hello World</h1></html>"
  
if __name__ == "__main__":
  pyminserver.start(port=5000) #default port is 80 if none is specified
```


## Another example with request processing

```python
import pyminserver	
	
def main(request, **header):	
    """A simple example site demo. main() handles all get requests.	
    'request' is the request path, '**header' is the header information with the request"""	
    print "Request: GET {}".format(request)	
    request = request[1:]	
    if request in ["", "index", "index.html", "index.htm"]:	
        return "<html><h1>Index of site</h1></html>"	
    elif request in ["about", "about.html", "about.htm"]:	
        return "<html><h1>About Page</h1><img src=\"image.jpg\"></html>"	
    elif request == "image.jpg":	
        return open("image.jpg", "rb")      #sample image processing	
    else:	
        return "<html><h1>Error 404</h1><br><p>File Not Found</p></html>"	
	
if __name__ == "__main__":	
    pyminserver.start()
```


## Important note:

there must be a function main(request, \**header) in your file, as well as a 'if \__name__ == "\__main__"' encapsulating your 'pyminserver.start() call, otherwise it will not work

# pyMinServer
A simple customisable web server with almost no boilerplate code

# About
PyMinServer is designed to be easy to implement in any situation. It is simple and intuitive, allowing for the creation of any webserver for any project, such as a dynamic website, a RESTful API etc.

# Current State
PyMinServer works for the dynamic generation of html. Currently it only supports HTTP GET methods, HEAD, and other requests are planned to be implemented soon. html can be generated dynamically based on the path of the request (/index, /about, /image.png etc), and the header information associated with that request (Accept-Language, Accept-Encoding, Host, Accept, User-Agent, DNT, Connection, Cache-Control, Upgrade-Insecure-Requests). If you want more information to process, it is very easy to add additional parameters by modifying `pyminserver.py` and adding additional options from the [basehttpserver documentation](https://docs.python.org/2/library/basehttpserver.html). Additionally, if you don't trust me, or think that you can do a better job, it is easy to add support for other http requests by modifying `pyminserver.py`. Support for head requests is easy to modify by updating `do_HEAD(self)` in the class `handle`. Feel free to contribute.

# Instalation
Instalation of pyMinServer is simple. Download, clone or paste `pyminserver.py` into your project directory, in another file, use `import pyminserver` to use.

# Usage
In order to minimise boilerplate code and make pyminserver as minimalist and intuitive as possible, only one function exists to modify output. `request` contains the GET path, (/index, /about, /image.jpg), and header contains header information associated with the request. To run the server, use `pyminserver.start()` and specify the port if needed. Here's a simple example:

```python
import pyminserver

def main(request, **header):
 return "<html><h1>Hello World</h1></html>
    
if __name__ == "__main__":
    pyminserver.start(port=5000) #default port is 80 if none is specified
````

`pyminserver.start()` does not necessarily have to be in a `if __name__ == "__main__"` conditional, but it it reccomended. Here is another simple example:

```python
def main(request, **header):		
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

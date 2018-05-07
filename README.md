# pyMinServer
A simple customisable web server with almost no boilerplate code

# About
PyMinServer is designed to be easy to implement in any situation. It is simple and intuitive, allowing for the creation of any webserver for any project, such as a dynamic website, a RESTful API etc.

# Current State
PyMinServer works for the dynamic generation of html. Currently it only supports HTTP GET methods, HEAD, and other requests are planned to be implemented soon. html can be generated dynamically based on the path of the request (/index, /about, /image.png etc), and the header information associated with that request (Accept-Language, Accept-Encoding, Host, Accept, User-Agent, DNT, Connection, Cache-Control, Upgrade-Insecure-Requests). If you want more information to process, it is very easy to add additional parameters by modifying `pyminserver.py` and adding additional options from the [basehttpserver documentation](https://docs.python.org/2/library/basehttpserver.html). Additionally, if you don't trust me, or think that you can do a better job, it is easy to add support for other http requests by modifying `pyminserver.py`. Support for head requests is easy to modify by updating `do_HEAD(self)` in the class `handle`. Feel free to contribute.

# Instalation
Instalation of pyMinServer is simple. Download, clone or paste `pyminserver.py` into your project directory, in another file, use `import pyminserver` to use.

# Usage
Here is an example of a simple website made in pyminserver.


    import pyminserver

    def main(request, **header):
	    return "<html><h1>Hello World</h1></html>
    
    if __name__ == "__main__":
        pyminserver.start(port=5000) #default port is 80 if none is specified

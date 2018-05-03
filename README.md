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



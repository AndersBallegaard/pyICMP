# pyICMP
## A ping implementation in python using native CLI clients


### Getting started

Install pyICMP
```bash
pip3 install pyICMP
```

Ping a single address
```python
#!/usr/bin/python3

#import pyICMP
import pyICMP

result = pyICMP.ping('1.1.1.1')

if result:
    print("OK")
else:
    print("fail")
```
# pyICMP
## A ping implementation in python using native CLI clients

[![Requirements Status](https://requires.io/github/AndersBallegaard/pyICMP/requirements.svg?branch=master)](https://requires.io/github/AndersBallegaard/pyICMP/requirements/?branch=master)

[![codecov](https://codecov.io/gh/AndersBallegaard/pyICMP/branch/master/graph/badge.svg)](https://codecov.io/gh/AndersBallegaard/pyICMP)

[![Build Status](https://travis-ci.org/AndersBallegaard/pyICMP.svg?branch=master)](https://travis-ci.org/AndersBallegaard/pyICMP)

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
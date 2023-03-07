#!/usr/bin/python
# for test purposes provide access to the package in the parent directory
import os
import sys

_parent_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src')
if _parent_dir not in sys.path:
    sys.path.insert(1, _parent_dir)

# now use pypackages to gain access to everything in the __pypackages__ directory
# this is all you need in a real application to use __pypackages__
import pypackages
from sanic import Sanic, Request
from sanic.response import text
app = Sanic('app')


@app.route('/')
async def hello(request: Request):
    return text('Hello, world')


if __name__ == '__main__':
    app.run(port=19999)

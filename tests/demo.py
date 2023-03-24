#!/usr/bin/python

# deal with src location
import os
import sys
_parent_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src')
if _parent_dir not in sys.path:
    sys.path.insert(1, _parent_dir)

# now use pypackages to install the requirements.txt locally into __packages__ and use it
import pypackages
pypackages.packages()


from sanic import Sanic, Request
from sanic.response import text
app = Sanic('app')


@app.route('/')
async def hello(request: Request):
    return text('Hello, world')


if __name__ == '__main__':
    app.run(port=19999)

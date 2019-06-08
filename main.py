import logging

import aiohttp
from src import create_app


# uvloop
try:
    import uvloop
    uvloop.install()
except ImportError:
    print('uvloop is not available')

# logging
logging.basicConfig(level=logging.DEBUG)

# app
app = create_app()

if __name__ == '__main__':
    aiohttp.web.run_app(app)

import argparse
import logging

import aiohttp
from src import create_app


# uvloop
try:
    import uvloop
    uvloop.install()
except ImportError:
    print('uvloop is not available')



# argument parser
parser = argparse.ArgumentParser(description='Demo project')
parser.add_argument(
    '--host',
    help='Host to listen',
    default='0.0.0.0'
)
parser.add_argument(
    '--port',
    help='Port to accept connections',
    default='5000'
)
parser.add_argument(
    '--reload',
    action='store_true',
    help='Autoreload code on change'
)
parser.add_argument(
    '--debug',
    action='store_true',
    help='Debug code'
)

args = parser.parse_args()

# reload
if args.reload:
    print('Start with code reload')
    import aioreloader
    aioreloader.start()

# logging
if args.debug:
    print('Start with debug')
    logging.basicConfig(level=logging.DEBUG)

# app
app = create_app()

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port)

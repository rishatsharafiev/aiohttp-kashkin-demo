import logging
import aiohttp

from src import create_app


logging.basicConfig(level=logging.DEBUG)
app = create_app()


if __name__ == '__main__':
    aiohttp.web.run_app(app)

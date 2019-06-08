import pathlib
import os

from aiohttp import web
import aiohttp_jinja2
import jinja2

import uvloop

from .routes import setup_routes


def create_app():
    BASE_PATH = pathlib.Path(__file__).parent
    TEMPLATE_PATH = os.path.join(BASE_PATH, 'templates')

    app = web.Application()

    # routes
    app = setup_routes(app)

    # jinja2 templates
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(TEMPLATE_PATH)
    )

    return app

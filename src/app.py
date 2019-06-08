from aiohttp import web

from .routes import setup_routes


def create_app():
    app = web.Application()

    app = setup_routes(app)

    return app

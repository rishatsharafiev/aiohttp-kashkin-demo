from aiohttp import web

from .views import frontend


def setup_routes(app):
    app.add_routes([
        web.get('/', frontend.index)
    ])
    return app

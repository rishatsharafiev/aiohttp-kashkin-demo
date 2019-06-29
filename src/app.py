import pathlib
import os

from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncpgsa

from .routes import setup_routes


def create_app(config: dict = None):
    BASE_PATH = pathlib.Path(__file__).parent
    TEMPLATE_PATH = os.path.join(BASE_PATH, 'templates')

    app = web.Application()

    app['config'] = config

    # routes
    app = setup_routes(app)

    # jinja2 templates
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(TEMPLATE_PATH)
    )

    app.on_startup.append(startup_db)
    app.on_shutdown.append(shutdown_db)

    return app


async def startup_db(app):
    config = app['config']
    app['db'] = await asyncpgsa.create_pool(dsn=config['database_dsn'])

async def shutdown_db(app):
    await app['db'].close()

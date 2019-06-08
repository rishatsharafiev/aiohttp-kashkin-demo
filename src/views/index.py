from aiohttp import web
from aiohttp_jinja2 import template


@template('index.jinja2')
async def handler(request):
    return {'name': 'Rishat', 'surname': 'Sharafiev'}

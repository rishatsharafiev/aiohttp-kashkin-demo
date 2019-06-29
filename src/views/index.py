from aiohttp import web
from aiohttp_jinja2 import template


@template('index.jinja2')
async def handler(request):
    site_name = request.app['config'].get('site_name')
    return {'site_name': site_name, 'name': 'Rishat', 'surname': 'Sharafiev'}

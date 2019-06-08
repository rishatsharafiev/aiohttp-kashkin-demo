from aiohttp import web
import aiohttp_jinja2
import jinja2


async def index(request):
    return web.Response(text='OK')

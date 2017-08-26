from sanic import Sanic
app = Sanic('app')
from . import views

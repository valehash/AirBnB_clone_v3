<<<<<<< HEAD
#!/usr/bin/python3
"""Flask Blueprint views"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")

=======
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
>>>>>>> master

from api.v1.views.index import *

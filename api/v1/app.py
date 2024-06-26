#!/usr/bin/python3
"""Flask API to return route status of my api"""
import os
from models import storage
from api.v1.views import app_views
from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Teardown function"""
    storage.close()


if __name__ == '__main__':
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)

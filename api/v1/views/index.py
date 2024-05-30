#!/usr/bin/python3

"""First page of the api"""
from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def get_status():
    """Return json status"""
    data = {
        "status": "OK"
    }
    resp = jsonify(data)
    resp.status_code =200

    retrun resp



"""
espelho da aplicação
"""
from flask import Blueprint
from flask_restful import Api

from .resources import ProductItemResource, ProductResource


bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(ProductResource, "/procuct/")
api.add_resource(ProductItemResource, "/procuct/<prouct_id>")

def init_app(app):
    app.register_blueprint(bp)
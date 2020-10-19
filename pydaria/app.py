from flask import Flask
from pydaria.extensions import configuration
from pydaria.extensions import appearance
from pydaria.extensions import database
from pydaria.extensions import auth
from pydaria.extensions import admin
from pydaria.extensions import commands
from pydaria.extensions import views


app = Flask(__name__)

configuration.init_app(app)
appearance.init_app(app)
database.init_app(app)
auth.init_app(app)
admin.init_app(app)
commands.init_app(app)
views.init_app(app)

"""
Codigo antes da modificação
"""

# from dynaconf import FlaskDynaconf
# from flask_admin import Admin 
# from flask_admin.base import AdminIndexView
# from flask_admin.contrib import sqla
# from flask_bootstrap import Bootstrap
# from flask_simplelogin import SimpleLogin, login_required
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)

# FlaskDynaconf(app)
# Bootstrap(app)
# db = SQLAlchemy(app)

# def verify_login(user):
#     return user.get("username") == "admin" and user.get("password") == "1234"
# SimpleLogin(app, login_checker=verify_login)

# # Proteger o admin com login via Monkey Patch
# AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
# sqla.ModelView._handle_view = login_required(AdminIndexView._handle_view)
# admin = Admin(app, name= app.config.TITLE, template_mode = "bootstrap3")


# class Products(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(140))
#     price = db.Column(db.Numeric())
#     description = db.Column(db.Text)
    
# admin.add_view(sqla.ModelView(Products, db.session))

# @app.cli.command()
# def createdb():
#     """ creates sqlite database """
#     db.create_all()
    
# @app.route("/")
# def index():
#     products = Products.query.all() #["prod_1", "prod_2", "prod_3", "prod_4"]
#     return render_template("index.html", products=products)

# @app.route("/product/<product_id>")
# def product(product_id):
#     product = Products.query.filter_by(id=product_id).first() or abort(
#         404, "Produto não encontrado"
#     )
#     return str(product) #render_template("product.html", product=product)


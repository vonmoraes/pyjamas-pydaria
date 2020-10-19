from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import SimpleLogin, login_required


# Proteger o admin com login via Monkey Patch
AdminIndexView._handle_view = login_required(AdminIndexView._handle_view)
sqla.ModelView._handle_view = login_required(AdminIndexView._handle_view)
admin = Admin(app, name= app.config.TITLE, template_mode = "bootstrap3")

def init_app(app):
    admin.name = app.config.TITLE
    admin.template_mode = "bootstrap3"
    admin.init_app(app)
    admin.add_view(sqla.ModelView(Products, db.session))
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    products = ["prod_1", "prod_2", "prod_3", "prod_4"]
    return render_template("index.html", products=products)
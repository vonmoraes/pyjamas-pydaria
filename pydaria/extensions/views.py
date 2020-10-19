from flask import, render_template

def init_app(app):
    pass

@app.route("/")
def index():
    products = Products.query.all() #["prod_1", "prod_2", "prod_3", "prod_4"]
    return render_template("index.html", products=products)

@app.route("/product/<product_id>")
def product(product_id):
    product = Products.query.filter_by(id=product_id).first() or abort(
        404, "Produto não encontrado"
    )
    return str(product) #render_template("product.html", product=product)
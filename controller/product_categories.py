from app import app

@app.route("/product/categories")
def pcat():
    return "We are at /product/categories endpoint"
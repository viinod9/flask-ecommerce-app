from app import app

@app.route("/user/signup")
def signup():
    return "We are at user signup endpoint"
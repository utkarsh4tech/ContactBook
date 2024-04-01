from __main__ import app

# with app.app_context():

@app.route("/")
def home():
    return "<h1>Contact Book</h1>"
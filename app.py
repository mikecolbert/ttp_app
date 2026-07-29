import flask
from flask import render_template
from flask_cors import CORS

app = flask.Flask(__name__)

app.config["SECRET_KEY"] = "sdfgsgsheryjw6qgbdtjr68w3456w3rgwyh"

CORS(app)


# main index page route
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)

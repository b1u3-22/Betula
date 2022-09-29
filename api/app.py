import flask
import database_controler
app = flask.Flask(__name__, static_folder = './build', static_url_path = '/')

@app.route("/", methods = ["GET"])
def index():
    return app.send_static_file("index.html")


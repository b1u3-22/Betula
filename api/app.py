import flask
import database_controller
from flask_cors import CORS

app = flask.Flask(__name__, static_folder = './build', static_url_path = '/')
cors = CORS(app)

@app.route("/", methods = ["GET"])
def index():
    return app.send_static_file("index.html")

@app.route("/getAllDebts", methods = ["GET"])
def get_all_debts():
    return database_controller.get_all_debts()

@app.route("/getGeneralInfo", methods = ["GET"])
def get_general_info():
    return database_controller.get_general_info()

database_controller.start_database()
app.run()
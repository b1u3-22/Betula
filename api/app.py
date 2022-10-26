import os
import io
import flask
import database_controller
import config_controller
from flask_cors import CORS
from PIL import Image

app = flask.Flask(__name__, static_folder = '../dist', static_url_path = '/')
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

@app.route("/getFinancialsGeneral", methods = ["GET"])
def get_financials_general():
    return database_controller.get_general_financials()

@app.route("/verifyUser", methods = ["POST"])
def verify_user():
    return database_controller.verify_user(flask.request.json["username"], flask.request.json["password"])

@app.route("/getUserPermissions", methods = ["POST"])
def get_user_permissions():
    return database_controller.get_user_permissions(flask.request.json["username"])

@app.route("/getConfig", methods=["GET"])
def get_config():
    return config_controller.get_config()


database_controller.start_database()

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0", 
        port = os.environ.get('PORT', 5000)
        )
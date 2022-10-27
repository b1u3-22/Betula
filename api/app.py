import os
import io
import flask
import re
import database_controller
import config_controller
from flask_cors import CORS
from PIL import Image

app = flask.Flask(__name__, static_folder = '../dist', static_url_path = '/')
cors = CORS(app)

@app.route("/", methods = ["GET"])
def index():
    return app.send_static_file("index.html")

@app.route("/verifyUser", methods = ["POST"])
def verify_user():
    return database_controller.verify_user(flask.request.json["username"], flask.request.json["password"])

@app.route("/getUserPermissions", methods = ["POST"])
def get_user_permissions():
    return database_controller.get_user_permissions(flask.request.json["username"])

@app.route("/getAllDebts", methods = ["GET"])
def get_all_debts():
    return database_controller.get_all_debts()

@app.route("/getAllUsers", methods=["GET"])
def get_all_users():
    return database_controller.get_all_users()

@app.route("/getAllImages", methods=["GET"])
def get_all_images():
    return database_controller.get_all_images()

@app.route("/getConfig", methods=["GET"])
def get_config():
    return config_controller.get_config()


@app.route("/updateDebts", methods=["PATCH"])
def update_debts():
    updated_debts = flask.request.json

    for key, debt in updated_debts.items():
        if key.startswith("deleted"):
            database_controller.delete_from_debts(re.findall(r'\d+', key)[0])

        elif key.startswith("new"):
            database_controller.insert_into_debts(
                debt["total"], 
                debt["remaining"], 
                debt["remainingPerFlat"], 
                debt["repaymentPerFlat"]
                )

        else:
            database_controller.patch_debt(
                key, 
                debt["total"], 
                debt["remaining"], 
                debt["remainingPerFlat"], 
                debt["repaymentPerFlat"]
                )

    return flask.Response(status=200)

database_controller.start_database()

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0", 
        port = os.environ.get('PORT', 5000)
        )
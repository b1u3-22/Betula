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

@app.route("/getFinancialsGeneral", methods = ["GET"])
def get_financials_general():
    return database_controller.get_general_financials()

@app.route("/verifyUser", methods = ["POST"])
def verify_user():
    return database_controller.verify_user(flask.request.json["username"], flask.request.json["password"])

@app.route("/getUserPermissions", methods = ["POST"])
def get_user_permissions():
    return database_controller.get_user_permissions(flask.request.json["username"])

@app.route("/getAllUsers", methods = ["GET"])
def get_all_users():
    return database_controller.get_all_users()

@app.route("/getAllPosts", methods = ["GET"])
def get_all_posts():
    return database_controller.get_all_posts()

@app.route("/patchGeneralInfo", methods = ["PATCH"])
def patch_general_info():
    for property, value in flask.request.json.items():
        database_controller.patch_general_info(property, value)

    return flask.Response(status=200)

@app.route("/patchFinancialsGeneral", methods = ["PATCH"])
def patch_financial_general():
    for property, value in flask.request.json.items():
        database_controller.patch_financials_general(property, value)

    return flask.Response(status=200)

@app.route("/patchUsers", methods = ["PATCH"])
def patch_users():
    for id, user in flask.request.json.items():
        if user == "deleted":
            database_controller.delete_from_users(id)

        elif database_controller.check_if_user_exists(id):
            database_controller.patch_user(id, user["username"], user["password"], user["permissions"], user["email"], user["status"])

        else:
            database_controller.insert_into_users(user["username"], user["password"], user["permissions"], user["email"], user["status"])

    return flask.Response(status=200)

@app.route("/patchDebts", methods = ["PATCH"])
def patch_debts():
    for id, debt in flask.request.json.items():
        if debt == "deleted":
            database_controller.delete_from_debts(id)

        elif database_controller.check_if_debt_exists(id):
            database_controller.patch_debt(id, debt["total_debt"], debt["remaining_debt"], debt["remaining_debt_per_flat"], debt["repainment_per_flat"])

        else:
            database_controller.insert_into_debts(debt["total_debt"], debt["remaining_debt"], debt["remaining_debt_per_flat"], debt["repainment_per_flat"])

    return flask.Response(status=200)

@app.route("/newPost", methods=["POST"])
def new_post():
    database_controller.insert_into_posts(flask.request.json.title, flask.request.json.text)

database_controller.start_database()
app.run()
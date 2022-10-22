import os
import io
import flask
import database_controller
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

@app.route("/getAllUsers", methods = ["GET"])
def get_all_users():
    return database_controller.get_all_users()

@app.route("/getAllPosts", methods = ["GET"])
def get_all_posts():
    return database_controller.get_all_posts()

@app.route("/getAllPictures", methods=["GET"])
def get_all_pictures():
    return database_controller.get_all_pictures()

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

@app.route('/images/<path:path>', methods=["GET"])
def send_image(path):
    return flask.send_from_directory(os.path.abspath('../../photos'), path)

@app.route('/uploadNewImages', methods=["PUT"])
def new_images():
    image = Image.open(io.BytesIO(flask.request.data))
    image_name = f"{database_controller.generate_picture_name()}.{image.format.lower()}"
    image_path = f"{os.path.abspath('../../photos')}/{image_name}"
    image_link = f"http://127.0.0.1:5000/images/{image_name}"
    database_controller.insert_into_pictures(image_link, image_path, "", "false", "false")
    image.save(image_path)
    
    return flask.Response(status=200)

@app.route("/patchImages", methods=["PATCH"])
def patch_images():
    for id, image in flask.request.json.items():
        if image == "deleted":
            database_controller.delete_from_pictures(id)

        else:
            database_controller.patch_picture(id, image["description"], image["is_background"], image["on_mainpage"])

    return flask.Response(status=200)

@app.route("/getBackgroundImage", methods=["GET"])
def get_background_image():
    return database_controller.get_background_picture()

@app.route("/getGalleryImages", methods=["GET"])
def get_gallery_image():
    return database_controller.get_gallery_pictures()

database_controller.start_database()
app.run(
    host = "0.0.0.0",
    port = os.environ.get("PORT", 5000)
)
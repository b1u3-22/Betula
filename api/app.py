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
@app.route("/home-gallery", methods = ["GET"])
@app.route("/home-contact", methods = ["GET"])
@app.route("/login", methods = ["GET"])
@app.route("/dashboard", methods = ["GET"])
@app.route("/gallery", methods = ["GET"])
@app.route("/settings-general", methods = ["GET"])
@app.route("/settings-finance", methods = ["GET"])
@app.route("/settings-users", methods = ["GET"])
def index():
    return app.send_static_file("index.html")

@app.route('/images/<path:path>', methods=["GET"])
def send_image(path):
    return flask.send_from_directory(os.path.abspath('../../photos'), path)

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

@app.route("/getHomePageConfig", methods=["GET"])
def get_homepage_config():
    return config_controller.get_homepage_config()

@app.route("/getDashboardPageConfig", methods=["GET"])
def get_dashboardpage_config():
    return config_controller.get_dashboardpage_config()

@app.route("/getGalleryPageConfig", methods=["GET"])
def get_gallerypage_config():
    return config_controller.get_gallerypage_config()

@app.route("/updateConfig", methods=["PATCH"])
def update_config():
    updated_config = flask.request.json
    config_controller.update_config(updated_config)
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

    return database_controller.get_all_debts()

@app.route("/updateUsers", methods=["PATCH"])
def update_users():
    updated_users = flask.request.json

    for key, user in updated_users.items():
        if key.startswith("deleted"):
            database_controller.delete_from_users(re.findall(r'\d+', key)[0])

        elif key.startswith("new"):
            database_controller.insert_into_users(
                user["username"],
                user["password"],
                "admin" if user["admin"] else "basic",
                user["email"],
                "active" if user["active"] else "disabled",
                "false"
                )

        else:
            database_controller.patch_user(
                key, 
                user["username"],
                user["password"],
                "admin" if user["admin"] else "basic",
                user["email"],
                "active" if user["active"] else "disabled"
                )

    return database_controller.get_all_users()

@app.route("/updateImages", methods=["PATCH"])
def update_images():
    updated_images = flask.request.json

    for key, image in updated_images.items():
        if key.startswith("deleted"):
            database_controller.delete_from_images(re.findall(r'\d+', key)[0])

        else:
            database_controller.patch_image(
                key, 
                image["description"],
                "true" if "isBackground" in image and image["isBackground"] else "false",
                "true" if "onHomepage" in image and image["onHomepage"] else "false"
                )

    return database_controller.get_all_images()

def upload_image(file, is_background = "false", on_homepage = "false"):
    image = Image.open(io.BytesIO(file))
    image_name = f"{database_controller.generate_image_name()}.{image.format.lower()}"
    image_path = f"{os.path.abspath('../../photos')}/{image_name}"
    image_link = f"/images/{image_name}"
    image.save(image_path)
    database_controller.insert_into_images(image_link, image_path, "", is_background, on_homepage)
    
    return image_link


@app.route("/uploadImage", methods=["PUT"])
def upload_gallery_image():
    return upload_image(flask.request.data)

@app.route("/uploadBackgroundImage", methods=["PUT"])
def upload_background_image():
    return upload_image(flask.request.data, is_background = "true")

@app.route("/uploadHomepageGalleryImage", methods=["PUT"])
def upload_homepage_gallery_image():
    return upload_image(flask.request.data, on_homepage = "true")


@app.route("/deleteImageByLink", methods=["PATCH"])
def delete_image_by_link():
    database_controller.delete_from_images_by_link(flask.request.json["link"])
    return flask.Response(status=200)

database_controller.start_database()
config_controller.init_config()

if __name__ == "__main__":
    app.run(
        host = "0.0.0.0", 
        port = os.environ.get('PORT', 5000)
        )
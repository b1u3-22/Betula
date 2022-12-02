from datetime import datetime
import sqlite3 as sqlite
import uuid
import os

database_path = f"{os.path.abspath('../../data')}/data.db"

def start_database():
    connection = sqlite.connect(database_path)
    connection.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT NOT NULL, password TEXT NOT NULL, permissions TEXT NOT NULL, email TEXT, status TEXT NOT NULL, dark_mode TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS images(id INTEGER PRIMARY KEY, link TEXT NOT NULL, location TEXT NOT NULL, description TEXT, is_background TEXT NOT NULL, on_homepage TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS debts(id INTEGER PRIMARY KEY, total_debt INTEGER NOT NULL, remaining_debt INTEGER NULL, remaining_debt_per_flat INTEGER NOT NULL, repayment_per_flat INTEGER NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY, timestamp TIMESTAMP, title TEXT NOT NULL, text TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS finus(id INTEGER PRIMARY KEY, link TEXT NOT NULL, location TEXT NOT NULL, timestamp TIMESTAMP)")
    connection.commit()
    connection.close()


def get_user_by_username(username):
    connection = sqlite.connect(database_path)

    try:
        result = connection.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()[0]
    except:
        return None

    if result == []:
        return None

    else:
        return {'id': result[0], 'username': result[1], 'password': result[2], 'permissions': result[3], 'email': result[4]}

def verify_user(username, password):
    connection = sqlite.connect(database_path)

    try:
        result = connection.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()[0]
    except:
        return {"verified": False}

    if result == []:
        return {"verified": False}

    elif result[2] == password and result[5] == "active":
        return {"verified": True}

    else:
        return {"verified": False}

def get_user_permissions(username):
    connection = sqlite.connect(database_path)
    try:
        result = connection.execute("SELECT * FROM users WHERE username = ?", (username, )).fetchall()[0]
    except:
        return {"permissions": "basic"}

    try:
        if result[3] == "admin":
            return {"permissions": "admin"}

        else:
            return {"permissions": "basic"}

    except:
        return {"permissions": "basic"}

def get_all_users():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM users").fetchall()
    users = {}

    for i in range(len(result)):
        users[result[i][0]] = {"password": result[i][2], "admin": True if result[i][3] == "admin" else False, "email": result[i][4], "active": True if result[i][5] == "active" else False, "username": result[i][1]}

    connection.close()
    return users

def insert_into_users(username, password, permissions, email, status, dark_mode):
    connection = sqlite.connect(database_path)
    connection.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?)", (username, password, permissions, email, status, dark_mode))
    connection.commit()
    connection.close()

def patch_user(user_id, username, password, permissions, email, status): 
    connection = sqlite.connect(database_path)
    connection.execute("UPDATE users SET username = ?, password = ?, permissions = ?, email = ?, status = ? WHERE id = ?", (username, password, permissions, email, status, user_id))
    connection.commit()
    connection.close()

def delete_from_users(id):
    connection = sqlite.connect(database_path)
    connection.execute("DELETE FROM users WHERE id = ?", (id, ))
    connection.commit()
    connection.close()


def check_if_user_exists(id):
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM users WHERE id = ?", (id, )).fetchall()
    
    if result == []:
        return False

    else:
        return True

#====================================================================================================================================

def get_all_phones():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM phones").fetchall()[0]
    phones = {}

    for phone in result:
        phones[phone[0]] = phone[1]

    connection.close()
    return phones

def delete_from_phones(id):
    connection = sqlite.connect(database_path)
    connection.execute("DELETE FROM phones WHERE id = ?", (id, ))
    connection.commit()
    connection.close()

#------------------------------------------------------------------------------------------------------------------------------------

def insert_into_phones(number):
    connection = sqlite.connect(database_path)
    connection.execute("INSERT INTO phones VALUES(NULL, ?)", (number))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_emails():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM phones").fetchall()[0]
    emails = {}

    for email in result:
        emails[email[0]] = email[1]

    connection.close()
    return emails

def delete_from_emails(id):
    connection = sqlite.connect(database_path)
    connection.execute("DELETE FROM emails WHERE id = ?", (id, ))
    connection.commit()
    connection.close()

#------------------------------------------------------------------------------------------------------------------------------------

def insert_into_emails(number):
    connection = sqlite.connect(database_path)
    connection.execute("INSERT INTO phones VALUES(NULL, ?)", (number))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_visibility():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM visiblity").fetchall()[0]
    visibilities = {}

    for visibility in result:
        visibilities[visibility[1]] = visibility[2]

    connection.close()
    return visibilities

#------------------------------------------------------------------------------------------------------------------------------------

def change_visibility(section, status):
    connection = sqlite.connect(database_path)
    connection.execute("UPDATE visibility SET status = ? WHERE section = ?", (status, section, ))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_texts():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM texts").fetchall()[0]
    texts = {}

    for text in result:
        texts[text[1]] = text[2]

    connection.close()
    return texts

#------------------------------------------------------------------------------------------------------------------------------------

def change_text(name, text):
    connection = sqlite.connect(database_path)
    connection.execute("UPDATE texts SET text = ? WHERE name = ?", (text, name, ))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_bank_account():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM bank_account").fetchall()[0]
    bank_account = {}

    for detail in bank_account:
        bank_account[detail[1]] = detail[2]

    connection.close()
    return bank_account

#------------------------------------------------------------------------------------------------------------------------------------

def change_bank_account(name, value):
    connection = sqlite.connect(database_path)
    connection.execute("UPDATE bank_account SET value = ? WHERE name = ?", (value, name, ))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_images():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM images").fetchall()
    images = {}

    for i in range(len(result)):
        if (result[i][4] != "true" and result[i][5] != "true"):
            images[result[i][0]] = {'link': result[i][1], 'description': result[i][3]}

    connection.close()
    return images

def get_image_by_id(id):
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM images WHERE id = ?", (id, )).fetchall()[0]
    image = {'id': result[0], 'link': result[1], 'location': result[2], 'description': result[3]}
    connection.close()
    return image

def get_image_by_link(link):
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM images WHERE link = ?", (link, )).fetchall()[0]
    image = {'id': result[0], 'link': result[1], 'location': result[2], 'description': result[3]}
    connection.close()
    return image

def get_background_image():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM images WHERE is_background = 'true'").fetchall()[0]
    image = {'link': result[1]}
    connection.close()
    return image

def get_gallery_images():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM images WHERE on_homepage = 'true'").fetchall()
    images = {}

    for i in range(len(result)):
        images[result[i][0]] = {'link': result[i][1]}

    connection.close()
    return images

#------------------------------------------------------------------------------------------------------------------------------------

def insert_into_images(link, location, description, is_background, on_homepage):
    connection = sqlite.connect(database_path)
    connection.execute("INSERT INTO images VALUES(NULL, ?, ?, ?, ?, ?)", (link, location, description, is_background, on_homepage))
    connection.commit()
    connection.close()

def delete_from_images(id):
    connection = sqlite.connect(database_path)

    location = connection.execute("SELECT location FROM images WHERE id = ?", (id, )).fetchone()[0]
    os.remove(location)

    connection.execute("DELETE FROM images WHERE id = ?", (id, ))
    connection.commit()
    connection.close()

def delete_from_images_by_link(link):
    connection = sqlite.connect(database_path)

    location = connection.execute("SELECT location FROM images WHERE link = ?", (link, )).fetchone()[0]
    os.remove(location)

    connection.execute("DELETE FROM images WHERE link = ?", (link, ))
    connection.commit()
    connection.close()

def patch_image(id, description, is_background, on_homepage):
    connection = sqlite.connect(database_path)
    connection.execute("UPDATE images SET description = ?, is_background = ?, on_homepage = ? WHERE id = ?", (description, is_background, on_homepage, id))
    connection.commit()
    connection.close()

def generate_image_name():
    return str(uuid.uuid1()).replace("-", "")

#====================================================================================================================================

def get_all_debts():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM debts").fetchall()
    debts = {}

    for i in range(len(result)):
        debts[result[i][0]] = {'total': result[i][1], 'remaining': result[i][2], 'remainingPerFlat': result[i][3], 'repaymentPerFlat': result[i][3]}

    connection.close()
    return debts

#------------------------------------------------------------------------------------------------------------------------------------

def insert_into_debts(total_debt, remaining_debt, remaining_debt_per_flat, repayment_per_flat):
    connection = sqlite.connect(database_path)
    connection.execute("INSERT INTO debts VALUES(NULL, ?, ?, ?, ?)", (total_debt, remaining_debt, remaining_debt_per_flat, repayment_per_flat))
    connection.commit()
    connection.close()

def patch_debt(id, total_debt, remaining_debt, remaining_debt_per_flat, repayment_per_flat): 
    connection = sqlite.connect(database_path)
    connection.execute("UPDATE debts SET total_debt = ?, remaining_debt = ?, remaining_debt_per_flat = ?, repayment_per_flat = ? WHERE id = ?", (total_debt, remaining_debt, remaining_debt_per_flat, repayment_per_flat, id))
    connection.commit()
    connection.close()

def delete_from_debts(id):
    connection = sqlite.connect(database_path)
    connection.execute("DELETE FROM debts WHERE id = ?", (id, ))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_posts():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM posts").fetchall()
    posts = {}

    for i in range(len(result)):
        posts[result[i][0]] = {'timestamp': result[i][1], 'postTitle': result[i][2], 'postText': result[i][3]}

    connection.close()
    return posts

def get_post_by_id(id):
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM posts WHERE id = ?", (id, )).fetchall()[0]
    post = {'id': result[0], 'timestamp': result[1], 'title': result[2], 'text': result[3]}
    connection.close()
    return post

#------------------------------------------------------------------------------------------------------------------------------------

def insert_into_posts(title, text):
    connection = sqlite.connect(database_path)
    connection.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (datetime.now().strftime("%d.%m. %Y  %H:%M:%S"), title, text))
    connection.commit()
    connection.close()

#====================================================================================================================================

def get_all_finus():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM finus").fetchall()
    finus = {}

    for i in range(len(result)):
        finus[result[i][0]] = {'link': result[i][1], 'location': result[i][2], 'timestamp': result[i][3]}

    connection.close()
    return finus

def get_latest_finu():
    connection = sqlite.connect(database_path)
    result = connection.execute("SELECT * FROM table ORDER BY id DESC LIMIT 1").fetchall()[0]
    finu = {'id': result[0], 'link': result[1], 'location': result[2], 'timestamp': result[3]}
    connection.close()
    return finu

#------------------------------------------------------------------------------------------------------------------------------------

def insert_into_finus(link, location):
    connection = sqlite.connect(database_path)
    connection.execute("INSERT INTO finus VALUES(NULL, ?, ?, ?)", (link, location, datetime.now()))
    connection.commit()
    connection.close()

#====================================================================================================================================

# FOR DEV PURPOSES ONLY
def custom_operation(operation):
    connection = sqlite.connect(database_path)
    connection.execute(f"{operation}")
    connection.commit()
    connection.close()
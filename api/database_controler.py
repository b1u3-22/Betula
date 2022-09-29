from datetime import datetime
import sqlite3 as sqlite

def start_database():
    connection = sqlite.connect("data.db")
    connection.execute("CREATE TABLE IF NOT EXISTS general_info(id INTEGER PRIMARY KEY, property TEXT NOT NULL, value TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS pictures(id INTEGER PRIMARY KEY, link TEXT NOT NULL, location TEXT NOT NULL, description TEXT)")
    connection.execute("CREATE TABLE IF NOT EXISTS financials_general(id INTEGER PRIMARY KEY, property TEXT NOT NULL, value TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS debts(id INTEGER PRIMARY KEY, total_debt INTEGER NOT NULL, remaining_debt INTEGER NULL, remaining_debt_per_flat INTEGER NOT NULL, repainment_per_flat INTEGER NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS posts(id INTEGER PRIMARY KEY, timestamp TIMESTAMP, title TEXT NOT NULL, text TEXT NOT NULL)")
    connection.execute("CREATE TABLE IF NOT EXISTS finus(id INTEGER PRIMARY KEY, link TEXT NOT NULL, location TEXT NOT NULL, timestamp TIMESTAMP)")
    connection.commit()
    connection.close()

def get_general_info():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM general_info").fetchall()
    financials_general = []

    for i in range(result):
        financials_general[i] = {result[i][1]: result[i][2]}

    connection.close()
    return financials_general

def get_general_financials():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM financials_general").fetchall()
    general_info = []

    for i in range(result):
        general_info[i] = {result[i][1]: result[i][2]}

    connection.close()
    return general_info

def get_all_pictures():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM pictures").fetchall()
    pictures = []

    for i in range(result):
        pictures[i] = {'id': result[i][0], 'link': result[i][1], 'location': result[i][2], 'description': result[i][3]}

    connection.close()
    return pictures

def get_picture_by_id(id):
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM pictures WHERE id = ?", (id, )).fetchall()[0]
    picture = {'id': result[0], 'link': result[1], 'location': result[2], 'description': result[3]}
    connection.close()
    return picture

def get_picture_by_link(link):
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM pictures WHERE link = ?", (link, )).fetchall()[0]
    picture = {'id': result[0], 'link': result[1], 'location': result[2], 'description': result[3]}
    connection.close()
    return picture

def get_all_debts():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM debts").fetchall()
    debts = []

    for i in range(result):
        debts[i] = {'id': result[i][0], 'total_debt': result[i][1], 'remaining_debt': result[i][2], 'remaining_debt_per_flat': result[i][3], 'repainment_per_flat': result[i][3]}

    connection.close()
    return debts

def get_all_posts():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM debts").fetchall()
    posts = []

    for i in range(result):
        posts[i] = {'id': result[i][0], 'timestamp': result[i][1], 'title': result[i][2], 'text': result[i][3]}

    connection.close()
    return posts

def get_post_by_id(id):
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM posts WHERE id = ?", (id, )).fetchall()[0]
    post = {'id': result[0], 'timestamp': result[1], 'title': result[2], 'text': result[3]}
    connection.close()
    return post

def get_all_finus():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM finus").fetchall()
    finus = []

    for i in range(result):
        finus[i] = {'id': result[i][0], 'link': result[i][1], 'location': result[i][2], 'timestamp': result[i][3]}

    connection.close()
    return finus

def get_latest_finu():
    connection = sqlite.connect("data.db")
    result = connection.execute("SELECT * FROM table ORDER BY id DESC LIMIT 1").fetchall()[0]
    finu = {'id': result[0], 'link': result[1], 'location': result[2], 'timestamp': result[3]}
    connection.close()
    return finu
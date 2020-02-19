import json
from flask import Flask
from flask import request
import MySQLdb
db = MySQLdb.connect(host='localhost', user='root', passwd='root')
cursor = db.cursor(cursorclass=MySQLdb.cursors.DictCursor)
app = Flask(__name__)

def list_allusers():  # Function used to return names of users in list
    cursor.execute('USE arcade')
    cursor.execute('SELECT username FROM arcade_player;')
    res = cursor.fetchall()
    names = []
    for i in res:
        names.append(i["username"])
    print(names)
    print(res)
    return names

@app.route("/")
def welcome():
    return str(list_allusers())


list_allusers()
app.run()

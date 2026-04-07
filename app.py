from flask import Flask 
from src.database.config import db
from src.models.UserModel import UserModel

app = Flask(__name__)

@app.before_request
def connect_db():
    if db.is_closed():
        db.connect()

@app.teardown_request
def close_db(exception):
    if not db.is_closed():
        db.close()

@app.route("/")
def index ():
    UserModel.create(username="test", name="Test User", password="password")
    return "OK"

with db:
    db.create_tables([UserModel])
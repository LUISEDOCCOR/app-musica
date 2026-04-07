from flask import Flask

# database
from src.database.config import db
from src.models.UserModel import UserModel

# routes
from src.routes.UserRoutes import bp as bp_users

app = Flask(__name__, template_folder="src/templates", static_folder="src/static")
app.secret_key = "secret-key"

app.register_blueprint(bp_users)


@app.before_request
def connect_db():
    if db.is_closed():
        db.connect()


@app.teardown_request
def close_db(e):
    if not db.is_closed():
        db.close()


@app.route("/ok")
def ok():
    return "OK"


with db:
    db.create_tables([UserModel])

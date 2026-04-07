from flask import Blueprint

from src.controllers.UserController import UserController

bp = Blueprint("users", __name__)


@bp.route("/auth", methods=["GET", "POST"])
def auth():
    return UserController.Auth()

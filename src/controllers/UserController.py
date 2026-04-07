import re

from flask import flash, redirect, render_template, request, session, url_for

from src.lib.bcrypt import hash_password, verify_password
from src.models.UserModel import UserModel


class UserController:
    @classmethod
    def Auth(cls):
        url = url_for("users.auth")

        if request.method == "POST":
            username = request.form.get("username", "").strip()
            password = request.form.get("password", "").strip()

            if not username or not password:
                flash("Todos los campos son obligatorios", "error")
                return redirect(url)

            if len(username) < 3:
                flash("El usuario debe tener al menos 3 caracteres", "error")
                return redirect(url)

            if len(password) < 6:
                flash("La contraseña debe tener al menos 6 caracteres", "error")
                return redirect(url)

            if not re.match("^[a-zA-Z0-9_]+$", username):
                flash(
                    "El usuario solo puede contener letras, números y guiones bajos",
                    "error",
                )
                return redirect(url)

            user = UserModel.get_or_none(UserModel.username == username)

            if not user:
                new_user = UserModel.create(
                    username=username, name=username, password=hash_password(password)
                )

                session["id"] = new_user.id
                session["usernmae"] = new_user.username

                return redirect("/")
            else:
                if verify_password(password, user.password):
                    session["id"] = user.id
                    session["usernmae"] = user.username

                    return redirect("/")
                else:
                    flash(
                        "Contraseña incorrecta",
                        "error",
                    )
                    return redirect(url)

        return render_template("users/index.html")

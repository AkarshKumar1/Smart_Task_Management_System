from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    login_required,
    logout_user
)

from .extensions import db, bcrypt

from .models import User

from .forms import (
    RegistrationForm,
    LoginForm
)


auth = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth"
)


# =========================
# REGISTER
# =========================
@auth.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():

        hashed_password = bcrypt.generate_password_hash(
            form.password.data
        ).decode("utf-8")

        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)

        db.session.commit()

        flash(
            "Account created successfully!",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/register.html",
        form=form
    )


# =========================
# LOGIN
# =========================
@auth.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.check_password_hash(
            user.password,
            form.password.data
        ):

            login_user(
                user,
                remember=form.remember.data
            )

            flash(
                "Login successful!",
                "success"
            )

            return redirect(
                url_for("main.dashboard")
            )

        else:

            flash(
                "Invalid email or password",
                "danger"
            )

    return render_template(
        "auth/login.html",
        form=form
    )


# =========================
# LOGOUT
# =========================
@auth.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Logged out successfully",
        "info"
    )

    return redirect(
        url_for("auth.login")
    )
from flask import Flask

from .config import Config

from .extensions import (
    db,
    bcrypt,
    login_manager,
    socketio
)

from .routes import main

from .auth import auth


def create_app():

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static"
    )

    app.config.from_object(Config)

    # Initialize Extensions
    db.init_app(app)

    bcrypt.init_app(app)

    login_manager.init_app(app)

    socketio.init_app(app)

    # Flask Login
    login_manager.login_view = "auth.login"

    login_manager.login_message = ""
    
    login_manager.login_message_category = ""

    # Register Blueprints
    app.register_blueprint(main)

    app.register_blueprint(auth)

    return app
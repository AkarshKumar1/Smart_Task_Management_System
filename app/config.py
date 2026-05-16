import os


class Config:

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "supersecretkey"
    )

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "connect_args": {
            "ssl": {
                "ssl_mode": "REQUIRED"
            }
        }
    }

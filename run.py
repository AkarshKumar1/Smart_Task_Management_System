import os

import pymysql

pymysql.install_as_MySQLdb()

from app import create_app, socketio

from app.extensions import db

app = create_app()


# Create database tables automatically
with app.app_context():

    db.create_all()


if __name__ == "__main__":

    port = int(
        os.environ.get("PORT", 5000)
    )

    socketio.run(
      app,
      host="0.0.0.0",
      port=port,
      debug=False,
      allow_unsafe_werkzeug=True
    )

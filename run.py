import pymysql

pymysql.install_as_MySQLdb()

from app import create_app, socketio


app = create_app()


if __name__ == "__main__":

    socketio.run(app, debug=True)
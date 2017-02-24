from flask.ext.sqlalchemy import SQLAlchemy
from server import app

db = SQLAlchemy()


def connect_to_db(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///gratitudes"
    app.config['SQLALCHEMY_ECHO'] = True
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    connect_to_db(app)
    print "Connected to db."

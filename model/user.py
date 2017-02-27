from model.model import connect_to_db, db
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask import flash


class User(db.Model):
    """Creating class for users."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    location = db.Column(db.String(64), nullable=True)
    profile_image = db.Column(db.Text, nullable=True)
    date_joined = db.Column(db.DateTime, nullable=False)

    following = db.relationship('User',
                                secondary='connections',
                                primaryjoin='Connection.follower_user_id == User.user_id',
                                secondaryjoin='Connection.following_user_id == User.user_id',
                                backref=db.backref('followers'),
                                )

    def __repr__(self):
        """For a more manageable way to print object's attributes."""

        return "{}'s Info: {} {}, {}".format(self.username, self.first_name, self.last_name, self.email)

    @classmethod
    def get_by_username(cls, username):
        """Gets the user object given a username."""

        try:
            return User.query.filter_by(username=username).one()
        except NoResultFound:
            print "No user found."

    @classmethod
    def add_new_user(cls,
                     first_name,
                     last_name,
                     username,
                     email,
                     password,
                     location=None,
                     profile_image=None):
        """Add new user to the db."""

        user = User(first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                    date_joined=datetime.today().date,
                    location=location,
                    profile_image=profile_image)

        db.session.add(user)
        db.session.commit()

        return user

    # WHERE DOES THIS ACTUALLY BELONG?
    def handle_signup_form_errors(cls, first_name, last_name, username, email, password, password_confirmed, location, profile_image):
        """Generates flash msgs depending on errors"""

        errors = []

        if first_name or last_name or username or email or password:
            pass
        else:
            errors.append("Your profile is incomplete.")
            if password != password_confirmed:
                errors.append("The passwords you've entered don't match.")

            elif username in users:
                errors.append("I'm sorry, it looks like that username is taken already. Please select a new one.")

        return errors


class Connection(db.Model):
    """Class for Connections; like an association table for Users to Users relationships?"""

    __tablename__ = "connections"

    connection_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    follower_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    following_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    def __repr__(self):
        return "<Connection ID: {}, Follower: {}, Following: {}>".format(self.connection_id,
                                                                         self.follower_user_id,
                                                                         self.following_user_id,
                                                                         )

    @classmethod
    def add_connection_to_db(cls, follower_user_id, following_user_id):
        """Given the follower and following user ids, adds connection to db."""

        try:
            connection = Connection.query.filter_by(follower_user_id=follower_user_id,
                                                    following_user_id=following_user_id,
                                                    ).one()
            flash("You're already following that user!")

        except NoResultFound:
            connection = Connection(follower_user_id=follower_user_id,
                                    following_user_id=following_user_id,
                                    )
            db.session.add(connection)
            db.session.commit()
            print "Added new connection object to the db."
            following = User.query.get(following_user_id)
            flash("You're now following {} {}".format(following.first_name, following.last_name))

    @classmethod
    def delete_connection(cls, follower_user_id, following_user_id):
        """Delete a connection between users."""

        try:
            connection = Connection.query.filter_by(follower_user_id=follower_user_id,
                                                    following_user_id=following_user_id,
                                                    ).one()
            db.session.delete(connection)
            db.session.commit()

        except NoResultFound:
            print "That connection was not in the db."


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."

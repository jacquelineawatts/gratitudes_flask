from model import db, connect_to_db
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound


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

    def __repr__(self):
        """For a more manageable way to print object's attributes."""

        return "{}'s Info: {} {}, {}".format(self.username, self.first_name, self.last_name, self.email)

    @classmethod
    def get_by_username(cls, user_id):
        """Gets the user object given a username."""

        try:
            return User.query.filter_by(user_id=user_id).one()
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


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."

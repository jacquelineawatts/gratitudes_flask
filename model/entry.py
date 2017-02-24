from model import db, connect_to_db
from user import User
import datetime


class Entry(db.Model):
    """Class for full entry, contains 3 gratitudes. """

    __tablename__ = "entries"

    entry_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False)
    date_updated = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    user = db.relationship('User', backref='entries')

    @classmethod
    def add_new_entry(cls, user_id, date_posted, date_updated):
        """Adds new entry to the db."""

        entry = Entry(user_id=user_id,
                      date_posted=date_posted,
                      date_updated=date_updated)

        db.session.add(entry)
        db.session.commit()

        return entry

    @classmethod
    def find_by_date(cls, date):
        """Return all entries for a provided date."""

        return Entry.query.filter(date_posted=date).all()

    @classmethod
    def find_by_user(cls, user_id):
        """ Return all entries for a provided username."""

        return Entry.query.filter_by(user=user_id).all()


class Gratitude(db.Model):
    """Creating class for gratitude entries."""

    __tablename__ = "gratitudes"

    gratitude_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    entry_id = db.Column(db.Integer, db.ForeignKey('entries.entry_id'), nullable=False)

    entry = db.relationship('Entry', backref='gratitudes')

    @classmethod
    def add_new_gratitude(cls, text, entry_id):
        """Adds new gratitude to the db. """

        gratitude = Gratitude(text=text,
                              entry_id=entry_id)

        db.session.add(gratitude)
        db.session.commit()

        return gratitude

    @classmethod
    def get_gratitudes_by_entry(cls, entry_id):
        """Returns all gratitudes associated with a given entry."""

        return Gratitude.query.filter_by(entry_id=entry_id).all()


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."

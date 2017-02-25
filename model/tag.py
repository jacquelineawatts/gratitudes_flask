from model.model import db, connect_to_db
from user import User
from entry import Gratitude


class Tag(db.Model):

    __tablename__ = "tags"

    tag_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    gratitude_id = db.Column(db.Integer, db.ForeignKey('gratitudes.gratitude_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    gratitude = db.relationship('Gratitude', backref='tags')
    user = db.relationship('User', backref="tags")

    @classmethod
    def add_new_tag(cls, gratitude_id, user_id):
        """Adds new tag to the db. """

        tag = Tag(gratitude_id=gratitude_id,
                  user_id=user_id)

        db.session.add(tag)
        db.session.commit()

        return tag

if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."

from model import db, connect_to_db
from entry import Gratitude
from user import User


class Comment(db.Model):
    """Class for user comments on gratitudes."""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    gratitude_id = db.Column(db.Integer, db.ForeignKey('gratitudes.gratitude_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    gratitude = db.relationship('Gratitude', backref='comments')
    user = db.relationship('User', backref='users')

    @classmethod
    def add_new_comment(cls, text, gratitude_id, user_id):
        """Adds new comment to the db."""

        comment = Comment(text=text,
                          gratitude_id=gratitude_id,
                          user_id=user_id)

        db.session.add(comment)
        db.session.commit()

        return comment


if __name__ == "__main__":

    from server import app
    connect_to_db(app)
    print "Connected to DB."

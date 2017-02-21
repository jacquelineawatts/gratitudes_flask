from model import db, connect_to_db
from user import User
from entry import Gratitude, Entry
from datetime import datetime

from server import app

connect_to_db(app)
print "Connected to db."


jacquelope = User(first_name='Jacqui',
                  last_name='Watts',
                  username='jacquelope',
                  email='jacquelineawatts@gmail.com',
                  password='tester',
                  location='San Francisco',
                  date_joined=datetime.today().date(),
                  profile_image='https://scontent-sjc2-1.xx.fbcdn.net/v/t1.0-1/p320x320/12928314_10103831599186320_7570467518951458496_n.jpg?oh=809c84d892fe71b3a0a721162f1cb309&oe=58A9E89E')

kaylala = User(first_name='Michaela',
               last_name='D\'Amico',
               username='kaylala',
               email='michaeladamico@gmail.com',
               password='testing',
               location='Tena, Ecuador',
               date_joined=datetime.today().date(),
               profile_image='https://scontent-sjc2-1.xx.fbcdn.net/v/t1.0-1/p320x320/10590394_10102505355658989_740112908400003827_n.jpg?oh=bec858284ab0f8f888b79a8aa0d0c70e&oe=58AB7845')

db.session.add(jacquelope)
db.session.add(kaylala)
db.session.commit()

entry1 = Entry(user_id=1,
               date_posted=datetime(2015, 12, 12),
               date_updated=datetime(2015, 12, 12),
               )


entry2 = Entry(user_id=2,
               date_posted=datetime(2015, 12, 21),
               date_updated=datetime(2015, 12, 21),
               )

db.session.add(entry1)
db.session.add(entry2)
db.session.commit()

grat1 = Gratitude(text="Setting up the xmas tree w/lights, the house smelling of pine, listening to Arcade Fire w/Geoff and Mike.",
                  entry_id=1)
grat2 = Gratitude(text="Awesome Bailee xmas party!",
                  entry_id=1)
grat3 = Gratitude(text="That I get to work next to Kristin on this website build, she rocks :)",
                  entry_id=1)


grat4 = Gratitude(text="The huge stack of crossword puzzles that mom's saved for me from the Projo.",
                  entry_id=2)
grat5 = Gratitude(text="Grandma getting so happy and excited to hear me play the piano.",
                  entry_id=2)
grat6 = Gratitude(text="Getting to sleep in the living room with my own christmas tree.",
                  entry_id=2)

db.session.add(grat1)
db.session.add(grat2)
db.session.add(grat3)
db.session.add(grat4)
db.session.add(grat5)
db.session.add(grat6)

db.session.commit()

# if __name__ == '__main__':

#     from server import app

#     connect_to_db(app)
#     print "Connected to db."

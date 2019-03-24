from pet_back_end import db
from sqlalchemy.dialects.postgresql import JSON


class Fans(db.Model):
    __tablename__ = "FanInfo"

    id = db.Column(db.Integer, primary_key=True) # these are called 'attributes'
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=False)
    name = db.Column(db.String(120), unique=False, nullable=False, primary_key=False)

# I didn't include the __init__ suggested in the Data Model portion of the tutorial
# b/c I'm jot using the JSON thing... db.Column(JSON)

    def __repr__(self):
        return "<Email: {self.email}, Name: {self.name}".format(self=self)
        # in the above line we define how to represent our fan object as a string.

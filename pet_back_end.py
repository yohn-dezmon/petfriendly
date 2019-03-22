import os

from flask import Flask, render_template, request, send_from_directory, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Integer)

project_dir = os.path.dirname(os.path.abspath(__file__))
# line 8 tells sqlite which db we are using
database_file= "sqlite:///{}".format(os.path.join(project_dir, "fandatabase.db"))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file # where the db is stored

db = SQLAlchemy(app) # initialize a connection to the database and keep it in the db variable

class Fans(db.Model):
    __tablename__ = "FanInfo"

    id = db.Column(db.Integer, primary_key=True) # these are called 'attributes'
    email = db.Column(db.String(120), unique=True, nullable=False, primary_key=False)
    name = db.Column(db.String(120), unique=False, nullable=False, primary_key=False)


    def __repr__(self):
        return "<Email: {self.email}, Name: {self.name}".format(self=self)
        # in the above line we define how to represent our fan object as a string.

# http://localhost:5000/
@app.route('/', methods=['POST', 'GET'])
def home():
    song_dict = {"Pumba":'PUMBA_1.mp3', "You're Feet":'youre feet mix 1.8.17_1.mp3',
     "ratatatatata":'ratatat.mp3',
    "12 | 8":'12_8 NO CLICK.mp3', "Sage to Your Internet" : 'sage to your internet .mp3',
    "EB":'EB DEMO MIX NO CLICK.mp3'}
    email = None
    name = None
    if request.method == "POST":
        email_name = Fans(email=request.form.get("email"), name=request.form.get("name"))
        db.session.add(email_name)
        db.session.commit()
        thank_u = "thank you!! <3"
        fans = Fans.query.all()
        return render_template("thank_u.html", thank_u=thank_u,
                                song_dict=song_dict, fans=fans)
    else:

        return render_template("pet_friend.html",
                                song_dict = song_dict
                                )

@app.route("/update", methods=["POST"])
def update():
    newemail = request.form.get("newemail")
    oldemail = request.form.get("oldemail")
    fans = Fans.query.filter_by(email=oldemail).first()
    fans.email = newemail
    newname = request.form.get("newname")
    oldname = request.form.get("oldname")
    fans = Fans.query.filter_by(name=oldname).first()
    fans.name = newname
    db.session.commit()
    return redirect("/")
# http://localhost:5000/delete
@app.route("/delete", methods=["POST", "GET"])
def delete():
    email = request.form.get("email")
    fans = Fans.query.filter_by(email=email).first()
    db.session.delete(fans)
    name = request.form.get("name")
    fans = Fans.query.filter_by(name=name).first()
    db.session.delete(fans)
    db.session.commit()
    return redirect("/")


# only run this script if python app.py is run in the command line
# serves the purpose of making this code snippet portable into
# other programs without opening up a server.
if __name__ == "__main__":
    app.run()

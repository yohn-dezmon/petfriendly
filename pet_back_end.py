# importing the flask class
from flask import Flask, render_template, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     __tablename__ = "fans"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True)
#     name = db.Column(db.string(200), unique=False)
#
#     def __init__(self, email, name):
#         self.email = email
#         self.name = name
# # repr returns '<E-mail email, name name>'
# # what's up with the <> ??
#     def __repr__(self):
#         return '<E-mail {self.email}, name {self.name}>'.format(self=self)

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
        email = request.form['email'] # this sets python email equal to the input named 'email'
        name = request.form['name']
        thank_u = "thank you!! <3"
        return render_template("thank_u.html", thank_u=thank_u,
                                song_dict=song_dict)
    else:
        return render_template("pet_friend.html",
                                song_dict = song_dict
                                )







#uhh... where is this page... OH!
# http://localhost:5000/hello
# got it!
# THIS IS REALLY COOL!
# This together with hello_form.html creates an official submit form! woo!
@app.route('/hello', methods=['POST', 'GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet}, {name}"
        return render_template("index_laid_out.html", greeting=greeting)
    else:
        return render_template("hello_form_laid_out.html")



# only run this script if python app.py is run in the command line
# serves the purpose of making this code snippet portable into
# other programs without opening up a server.
if __name__ == "__main__":
    app.run()

# importing the flask class
from flask import Flask
from flask import render_template
# for HTTP METHODS
from flask import request
from flask import send_from_directory

# instantiating the Flask class
# the first argument is the name of the application's module or package
# if you using a single module, you should use __name__

app = Flask(__name__)



# http://localhost:5000/home
@app.route('/home', methods=['POST', 'GET'])
def home():


    song_list = ["Pumba", "You're Feet", "ratatatatata",
    "12 | 8", "Sage to Your Internet","EB","Drunk Inside",
    "Newnewnew","Fuel Filter","Calling","tight fuck"]

    song_dict = {"Pumba":"/static/PUMBA_1.mp3", "You're Feet":"/static/youre feet mix 1.8.17_1.mp3",
     "ratatatatata":"/static/ratatat.mp3",
    "12 | 8":"/static/12_8 NO CLICK.mp3", "Sage to Your Internet":"/static/sage to your internet.mp3",
    "EB":"/static/EB DEMO MIX NO CLICK.mp3"}


    return render_template("pet_friend.html",
                            song_list = song_list,
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

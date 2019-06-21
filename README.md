### Website for my band, "Pet Friendly"

This is a basic website that hosts some of our songs, and provides a
form for fans to join our mailing list.

This project was setup using Flask, jinja2, HTML5, CSS, and Postgres.

**pet_back_end.py**: This file in the main directory is how you start up the web-page.

i.e. $ python3 pet_back_end.py on the command line.
This file is the Controller in the Model-View-Controller model. It also provides the connection
to the Postgres database.

To understand the **.env** and **config.py** files, please see this tutorial:

https://realpython.com/flask-by-example-part-1-project-setup/

The **requirements.txt** shows all of the dependencies for the project.

Within the **templates** directory are the HTML files I have for the web pages
structure/layout.

Within the **static** directory are the actual songs from my band, along with
the CSS file for the styling of the webpages.

Another tutorial that was very useful for updating the Postgres database:
https://www.codementor.io/garethdwyer/building-a-crud-application-with-flask-and-sqlalchemy-dm3wv7yu2

The docs, migrations, pet_web, sqlalchemy, csv_db, bin, and tracks directories **can be ignored**.

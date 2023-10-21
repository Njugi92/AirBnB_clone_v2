#!/usr/bin/python3
""" Start flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from sqlalchemy.orm import scoped_session, sessionmaker

# Creates an instance of flask class and assigns it to variable app
app = Flask(__name__)


#Tear down app context to remove current sqlalchemy session after each request
@app.teardown_appcontext
def teardown(exception):
    """remove current sqlalchemy session """
    storage.close()


# Defines the route for '/states_list'
@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Displays aHTML page with a list of all states objects in DBstorage
    States are sorted by name
    """
    states = sorted(storage.all(state).values(), key=lambda s: s.name)
    # render the template and pass the list of states to the template
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    # Start flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)

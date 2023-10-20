#!/usr/bin/python3
""" It starts Flask web application
"""


from flask import Flask, request


app = Flask(__name__)


# Define route to root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


# Define the route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return "HBNB"


# Defines rute for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Displays 'C' followed by value of <text>.
    Replases any underscores in <text> with slashes
    """
    # Replaces underscores in <text> variables with slashes
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


# Define the route for '/python/(<text>)'
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Displays 'python' followed by value of <text>.
    Replaces any value of underscore with slashes
    Replaces underscore with spaces in the text variables
    """
    formatted_text = text.replace('_', ' ')
    return "python {}".format(formatted_text)


if __name__ == "__main__":
    # Start flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)

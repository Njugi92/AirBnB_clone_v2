#!/usr/bin/python3
""" This starts flask web application
"""


from flask import Flask, request

app = Flask(__name__)


# Define the route for root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


# Defines the route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return "HBNB"


# Defines the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Displays 'C' followed by value of <text>
    Replaces any underscore in <text> with slashes
    Replaces underscores with spaces in text variables
    """
    formatted_text = text_replace('_', ' ')
    return "C {}".format(formatted_text)


# Defines route for '/python/(<text>)'
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Displays 'python' followed by value of <text>
    Replaces any underscore in <text> with slashes
    Replaces underscores with spaces in text variables
    """
    formarted_text = text.replace('_', ' ')
    return "Python{}".format(formatted_text)


# Define route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays n is a number only if n is an integer"""
    return "{} is a number".format(n)

if __name__ == "__main__":
    # Start the flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)

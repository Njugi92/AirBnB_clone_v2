#!/usr/bin/python3
""" This starts flask web application
"""


from flask import Flask, request, render_template

app = Flask(__name__)


# Define route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HHBNB!' """
    return "Hello HBNB!"


# Defines route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return "HBNB"


# Defines the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Displays 'C' followed by the value of <text>
    Replaces any value of underscores with slashes
    Replaces underscores with spaces in text variables
    """
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


# defines the route for '/python/(<text>)'
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """Displays 'Python' followed by values of <text>
    Replaces any value of <text> with slashes
    Replaces underscores with space in text variables
    """
    formatted_text = text.replace('_', ' ')
    return "Python{}".format(formatted_text)


# Defines the route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Displays n is a number only if n is an integer """
    return "{} is a number".format(n)


# Define the route for '/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Displays a HTML page only if ,n> is an integer"""
    # render the template and pass the value of n to template
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    # Start flask development server
    # Listen to all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)

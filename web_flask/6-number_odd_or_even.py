#!/usr/bin/python3
""" It starts flask web application
"""

from flask import Flask, request, render_template

app = Flask(__name__)


# Define route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


# Defines the route '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return "HBNB"


# Defines the route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ Displays 'C' followed by the value of <text>
    Replaces any underscores in <text> with slashes
    Replaces underscores with spaces in text variables
    """
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)


# Defines route for the '/python/(<text>)'
@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_with_text(text):
    """ Displays 'Pytho' followed by value of <text>
    Replaces any underscore in <text> with slashes
    Replaces underscores with spaces in text variables
    """
    formatted_text = text.replace('_', ' ')
    return "Python{}".format(formatted_text)


# Defines route for '/number_odd_or_even/<n>'
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Displays a HTML page only if n is an integer
    States whether n is odd or even in the body
    """
    # check if n is an integer
    if isinstance(n, int):
        # Determine whether n is even or odd
        even_or_odd = "even" if n % 2 == 0 else "odd"
        # render the template and pass the value of odd_or_even
        # to template
        return render_template('6-number_odd_or_even.html',
                                n=n, even_or_odd=even_or_odd)
    else:
        # if n not an integer return error message
        return "Invalid input. Pleaseprovide an integer."


# Define route for '/number/<n>'
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Displays n is a number only if n is an integer"""
    return "{} is a number".format(n)


# Defines route for '/number_template/<n>'
@app.route('/number_template/<int:n>', strict_slashes=False)
def nuber_template(n):
    """ Displays a HTML page only if n is an integer"""
    # render the template and pass the value of n to template
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    # start flask development server
    # listen to all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)

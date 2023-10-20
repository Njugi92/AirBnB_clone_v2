#!/sr/bin/pyhon3
""" This starts Flk web aption
"""

from flask import Flask

app = Flask(__name__)


# Define route for root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return "Hello HBNB!"


# Define the route for '/hbnb'
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return "HBNB"


# Defines route for '/c/<text>'
@app.route('/c/<text>', strict_slashes=False)
def c_with_text(text):
    """ This displays 'C' followed by the value of <text> """
    # Replacing underscores with spaces in text variables
    formatted_text = text.replace('_', ' ')
    return "C {}".format(formatted_text)

if __name__ == "__main__":
    # Start flask development server
    # Listen on all available network interfaces (0.0.0.0) and port 5000
    app.run(host='0.0.0.0', port=5000)

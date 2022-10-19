# import the Flask dependency
from flask import Flask

# create a new Flask instance called app
app = Flask(__name__)

# define the starting point (root)
@app.route('/')
def hello_world():
    return 'Hello world'


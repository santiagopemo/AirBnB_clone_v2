#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(db):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a states"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a states and cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(db):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display states and cities"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states', strict_slashes=False)
def states():
    """Display states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Display states"""
    states = storage.all(State).values()
    finded = False
    for state in states:
        if id == state.id:
            finded = True
            return render_template(
                '9-states.html', states=state, finded=finded)
    return render_template('9-states.html', states=states, finded=finded)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Display states"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities)


@app.route('/hbnb', strict_slashes=False)
def hbnb_is_alive():
    """Display states"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

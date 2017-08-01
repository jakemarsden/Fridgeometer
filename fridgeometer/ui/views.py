from flask import render_template

from fridgeometer import app
from fridgeometer.orm.models import FridgeEntry


@app.route('/')
@app.route('/index')
def get_index():
    fridge_entries = (FridgeEntry.query
                      .order_by(FridgeEntry.timestamp_stored)
                      .all())
    return render_template('index.html', fridge_entries=fridge_entries)

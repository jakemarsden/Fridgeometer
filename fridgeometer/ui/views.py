from flask import jsonify, render_template

from fridgeometer import app, db
from fridgeometer.orm.models import FridgeEntry


@app.route('/')
@app.route('/index')
def get_index():
    fridge_entries = (FridgeEntry.query
                      .order_by(FridgeEntry.timestamp_stored)
                      .all())
    return render_template('index.html', fridge_entries=fridge_entries)


@app.route('/fridge_entry/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id: int):
    fridge_entry = (FridgeEntry.query
                    .filter(FridgeEntry.id == entry_id)
                    .one_or_none())
    fridge_entry_exists = (fridge_entry is not None)
    if fridge_entry_exists:
        db.session.delete(fridge_entry)
        db.session.commit()
    return jsonify(success=fridge_entry_exists)

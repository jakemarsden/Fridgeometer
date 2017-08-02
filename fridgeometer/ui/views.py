from flask import jsonify, redirect, render_template

from fridgeometer import app, db
from fridgeometer.orm.models import FridgeEntry
from fridgeometer.ui.forms import AddFridgeEntryForm
from fridgeometer.util.datetimes import local_to_utc_datetime


@app.route('/')
@app.route('/index')
def get_index():
    fridge_entries = (FridgeEntry.query
                      .order_by(FridgeEntry.timestamp_stored)
                      .all())
    return render_template('index.html', fridge_entries=fridge_entries)


@app.route('/fridge_entry', methods=['GET', 'POST'])
def get_or_post_fridge_entry():
    form = AddFridgeEntryForm()
    if form.validate_on_submit():
        fridge_entry = FridgeEntry(foodstuff_id=form.foodstuff.data,
                                   timestamp_stored=local_to_utc_datetime(form.timestamp_stored.data))
        db.session.add(fridge_entry)
        db.session.commit()
        return redirect('/index')
    else:
        return render_template('add_fridge_entry.html', form=form)


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

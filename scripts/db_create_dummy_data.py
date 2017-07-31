#!venv/bin/python
from datetime import datetime, timedelta

from fridgeometer import db
from fridgeometer.orm.models import Foodstuff, FridgeEntry


def drop_all():
    print('Dropping all rows')
    Foodstuff.query.delete()
    FridgeEntry.query.delete()


def create_dummy_data():
    now = datetime.utcnow()

    foodstuffs = [
        Foodstuff(name='Kidney Beans', best_before=timedelta(days=4), use_by=timedelta(days=7)),
        Foodstuff(name='Chick Peas', best_before=timedelta(days=4), use_by=timedelta(days=7)),
        Foodstuff(name='Lamb Stew', best_before=timedelta(days=3), use_by=timedelta(days=5)),
        Foodstuff(name='Chicken Soup', best_before=timedelta(days=3), use_by=timedelta(days=4))
    ]

    db.session.add_all(foodstuffs)
    db.session.commit()

    fridge_entries = [
        FridgeEntry(foodstuff=foodstuffs[0], timestamp_stored=now - timedelta(days=0)),
        FridgeEntry(foodstuff=foodstuffs[1], timestamp_stored=now - timedelta(days=2)),
        FridgeEntry(foodstuff=foodstuffs[2], timestamp_stored=now - timedelta(days=4)),
        FridgeEntry(foodstuff=foodstuffs[3], timestamp_stored=now - timedelta(days=7))
    ]

    db.session.add_all(fridge_entries)
    db.session.commit()


drop_all()
create_dummy_data()

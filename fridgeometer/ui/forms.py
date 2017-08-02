from flask_wtf import FlaskForm
from sqlalchemy.sql import collate
from wtforms import SelectField
from wtforms.fields.html5 import DateTimeField
from wtforms.validators import DataRequired

from fridgeometer.orm.models import Foodstuff


class SelectFoodstuffField(SelectField):
    def __init__(self, label=None, validators=None, **kwargs):
        foodstuffs = (Foodstuff.query
                      .order_by(collate(Foodstuff.name, 'NOCASE'))
                      .all())
        choices = [(0, 'Choose an option...')] + [(f.id, f.name) for f in foodstuffs]
        super().__init__(label=label, validators=validators, coerce=int, choices=choices, **kwargs)


class AddFridgeEntryForm(FlaskForm):
    foodstuff = SelectFoodstuffField('Foodstuff', validators=[DataRequired()])
    timestamp_stored = DateTimeField('DateTime Stored', validators=[DataRequired()])

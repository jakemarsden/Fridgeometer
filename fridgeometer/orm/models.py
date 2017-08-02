from datetime import datetime, timedelta
from enum import Enum

from fridgeometer import db


class FridgeEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodstuff_id = db.Column(db.Integer, db.ForeignKey('foodstuff.id'))
    timestamp_stored = db.Column(db.DateTime, nullable=False)

    foodstuff = db.relationship('Foodstuff')

    @property
    def storage_time(self) -> timedelta:
        return datetime.utcnow() - self.timestamp_stored

    @property
    def freshness(self) -> 'FreshnessState':
        storage_time = self.storage_time
        foodstuff = self.foodstuff
        if storage_time > foodstuff.use_by:
            return FreshnessState.Unusable
        if storage_time > foodstuff.best_before:
            return FreshnessState.NotFresh
        return FreshnessState.Fresh


class Foodstuff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    best_before = db.Column(db.Interval, nullable=False)  # How long it takes for this food type to stop being fresh
    use_by = db.Column(db.Interval, nullable=False)  # How long it takes for this food type to stop being usable


class FreshnessState(Enum):
    Fresh = 1
    NotFresh = 2
    Unusable = 3

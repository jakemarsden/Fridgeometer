from datetime import timedelta

from fridgeometer import app
from fridgeometer.util import times


@app.template_filter()
def pretty_timedelta(delta: timedelta) -> str:
    return times.pretty_timedelta(delta)

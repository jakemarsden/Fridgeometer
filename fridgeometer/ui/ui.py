from datetime import timedelta

from fridgeometer import app
from fridgeometer.util import datetimes


@app.template_filter()
def pretty_timedelta(delta: timedelta) -> str:
    return datetimes.pretty_timedelta(delta)

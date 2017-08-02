from datetime import datetime, timedelta

from fridgeometer import app
from fridgeometer.util import datetimes


@app.context_processor
def utility_processor():
    return {'now': datetime.now}


@app.template_filter()
def pretty_timedelta(delta: timedelta) -> str:
    return datetimes.pretty_timedelta(delta)

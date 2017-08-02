from datetime import datetime, timedelta

import pytz
import tzlocal

_SECONDS_PER_MINUTE = 60
_SECONDS_PER_HOUR = _SECONDS_PER_MINUTE * 60
_SECONDS_PER_DAY = 24 * _SECONDS_PER_HOUR
_SECONDS_PER_YEAR = 365.25 * _SECONDS_PER_DAY
_SECONDS_PER_MONTH = _SECONDS_PER_YEAR / 12


def local_to_utc_datetime(dt: datetime):
    local_timezone = tzlocal.get_localzone()
    localized_dt = local_timezone.localize(dt)
    utc_dt = localized_dt.astimezone(pytz.utc)
    return utc_dt


def pretty_timedelta(td: timedelta) -> str:
    delta = abs(td.total_seconds())

    if round(delta) == 0:
        return 'now'

    if delta < _SECONDS_PER_MINUTE:
        seconds = round(delta)
        time_str = ('%d sec' if (seconds == 1) else '%d secs') % seconds

    elif delta < _SECONDS_PER_HOUR:
        minutes = round(delta / _SECONDS_PER_MINUTE)
        time_str = ('%d min' if (minutes == 1) else '%d mins') % minutes

    elif delta < _SECONDS_PER_DAY:
        hours = round(delta / _SECONDS_PER_HOUR)
        time_str = ('%d hour' if (hours == 1) else '%d hours') % hours

    elif delta < _SECONDS_PER_MONTH:
        days = round(delta / _SECONDS_PER_DAY)
        time_str = ('%d day' if (days == 1) else '%d days') % days

    elif delta < _SECONDS_PER_YEAR:
        months = round(delta / _SECONDS_PER_MONTH)
        time_str = ('%d month' if (months == 1) else '%d months') % months

    else:
        years = round(delta / _SECONDS_PER_YEAR)
        time_str = ('%d year' if (years == 1) else '%d years') % years

    if td.total_seconds() > 0:
        return 'in %s' % time_str
    else:
        return '%s ago' % time_str

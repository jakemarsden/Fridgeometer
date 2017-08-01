from datetime import timedelta

_SECONDS_PER_MINUTE = 60
_SECONDS_PER_HOUR = _SECONDS_PER_MINUTE * 60
_SECONDS_PER_DAY = 24 * _SECONDS_PER_HOUR
_SECONDS_PER_YEAR = 365.25 * _SECONDS_PER_DAY
_SECONDS_PER_MONTH = _SECONDS_PER_YEAR / 12


def pretty_timedelta(td: timedelta) -> str:
    delta = td.total_seconds()

    if delta < _SECONDS_PER_MINUTE:
        seconds = round(delta)
        return ('%d sec ago' if (seconds == 1) else '%d secs ago') % seconds

    if delta < _SECONDS_PER_HOUR:
        minutes = round(delta / _SECONDS_PER_MINUTE)
        return ('%d min ago' if (minutes == 1) else '%d mins ago') % minutes

    if delta < _SECONDS_PER_DAY:
        hours = round(delta / _SECONDS_PER_HOUR)
        return ('%d hour ago' if (hours == 1) else '%d hours ago') % hours

    if delta < _SECONDS_PER_MONTH:
        days = round(delta / _SECONDS_PER_DAY)
        return ('%d day ago' if (days == 1) else '%d days ago') % days

    if delta < _SECONDS_PER_YEAR:
        months = round(delta / _SECONDS_PER_MONTH)
        return ('%d month ago' if (months == 1) else '%d months ago') % months

    years = round(delta / _SECONDS_PER_YEAR)
    return ('%d year ago' if (years == 1) else '%d years ago') % years

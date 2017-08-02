import unittest
from datetime import timedelta

from fridgeometer.util import datetimes


class DateTimeUtilsTest(unittest.TestCase):
    def test_pretty_timedelta(self):
        one_milli = timedelta(milliseconds=1)
        one_year = timedelta(days=365.25)
        one_month = one_year / 12

        self.go('now', timedelta(seconds=0))

        self.go('in 1 sec', timedelta(seconds=1.5) - one_milli)
        self.go('in 2 secs', timedelta(seconds=1.5) + one_milli)
        self.go('1 sec ago', -timedelta(seconds=1.5) + one_milli)
        self.go('2 secs ago', -timedelta(seconds=1.5) - one_milli)

        self.go('in 1 min', timedelta(minutes=1.5) - one_milli)
        self.go('in 2 mins', timedelta(minutes=1.5) + one_milli)
        self.go('1 min ago', -timedelta(minutes=1.5) + one_milli)
        self.go('2 mins ago', -timedelta(minutes=1.5) - one_milli)

        self.go('in 1 hour', timedelta(hours=1.5) - one_milli)
        self.go('in 2 hours', timedelta(hours=1.5) + one_milli)
        self.go('1 hour ago', -timedelta(hours=1.5) + one_milli)
        self.go('2 hours ago', -timedelta(hours=1.5) - one_milli)

        self.go('in 1 day', timedelta(days=1.5) - one_milli)
        self.go('in 2 days', timedelta(days=1.5) + one_milli)
        self.go('1 day ago', -timedelta(days=1.5) + one_milli)
        self.go('2 days ago', -timedelta(days=1.5) - one_milli)

        self.go('in 1 month', (1.5 * one_month) - one_milli)
        self.go('in 2 months', (1.5 * one_month) + one_milli)
        self.go('1 month ago', -(1.5 * one_month) + one_milli)
        self.go('2 months ago', -(1.5 * one_month) - one_milli)

        self.go('in 1 year', (1.5 * one_year) - one_milli)
        self.go('in 2 years', (1.5 * one_year) + one_milli)
        self.go('1 year ago', -(1.5 * one_year) + one_milli)
        self.go('2 years ago', -(1.5 * one_year) - one_milli)

    def go(self, expected: str, td: timedelta):
        result = datetimes.pretty_timedelta(td)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

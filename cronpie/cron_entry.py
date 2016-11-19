from datetime import datetime
from itertools import cycle

import attr
from croniter import croniter

from .utils.validators import is_cron_time_expression, is_non_empty_list


@attr.s(slots=True)
class CronEntry:
    time = attr.ib(validator=is_cron_time_expression)
    command = attr.ib(validator=is_non_empty_list)
    _datetime_gen = attr.ib(init=False, default=None)

    @staticmethod
    def from_string(line):
        splitted_line = line.split(' ')
        time = ' '.join(splitted_line[:5])
        command = splitted_line[6:]
        return CronEntry(time, command)

    @property
    def cron_expression(self):
        return ' '.join(self.time)

    @property
    def next_run(self):
        if not self._datetime_gen:
            cron = croniter(self.time, datetime.now())
            self._datetime_gen = (
                cron.get_next(datetime)
                for _ in cycle([None])
            )
        return next(self._datetime_gen)

    def _match(self, value, field):
        valid_values = self._compute_valid_values(field)
        return value in valid_values

import pytest
from datetime import datetime, timedelta

from freezegun import freeze_time

import cronpie


class TestCronEntry:

    def test_rejects_wrong_entry(self):
        line = '* * * * * ls'
        with pytest.raises(ValueError):
            cronpie.CronEntry.from_string(line)

    def test_accepts_simple_entry(self, simple_cron_line):
        entry = cronpie.CronEntry.from_string(simple_cron_line)
        expected_time = '*/1 * * * *'
        expected_command = ['ls']
        assert entry.time == expected_time
        assert entry.command == expected_command

    def test_accepts_ranged_entry(self, ranged_cron_line):
        entry = cronpie.CronEntry.from_string(ranged_cron_line)
        expected_time = '2-30 1-5 2-7 * *'
        expected_command = ['ls']
        assert entry.time == expected_time
        assert entry.command == expected_command

    def test_accepts_additive_entry(self, additive_cron_line):
        entry = cronpie.CronEntry.from_string(additive_cron_line)
        expected_time = '1,30 1,5 2,7 * *'
        expected_command = ['ls']
        assert entry.time == expected_time
        assert entry.command == expected_command

    def test_accepts_frequency_entry(self, frequency_cron_line):
        entry = cronpie.CronEntry.from_string(frequency_cron_line)
        expected_time = '*/2 */5 * * *'
        expected_command = ['ls']
        assert entry.time == expected_time
        assert entry.command == expected_command

    def test_accepts_complex_entry(self, complex_cron_line):
        entry = cronpie.CronEntry.from_string(complex_cron_line)
        expected_time = '0,20-30/2 * * * *'
        expected_command = ['ls']
        assert entry.time == expected_time
        assert entry.command == expected_command

    @freeze_time("2016-08-26 23:03:00")
    def test_get_next_datetime(self, simple_cron_entry):
        expected_time = datetime(2016, 8, 26, 23, 4)
        assert simple_cron_entry.next_run == expected_time
        expected_time += timedelta(minutes=1)
        assert simple_cron_entry.next_run == expected_time

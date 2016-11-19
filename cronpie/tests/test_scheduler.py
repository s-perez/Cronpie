from datetime import datetime

from freezegun import freeze_time


class TestScheduler:

    def test_simple_entry_is_scheduled(self, scheduler, simple_cron_entry):
        scheduler.register(simple_cron_entry)
        _, entry = scheduler.next_scheduled
        assert entry == simple_cron_entry

    @freeze_time('2016-08-26 23:00:00')
    def test_schedule_is_ordered_properly(self, scheduler,
                                          simple_cron_entry,
                                          ranged_cron_entry):
        scheduler.register(ranged_cron_entry)
        scheduler.register(simple_cron_entry)
        _, entry = scheduler.next_scheduled
        assert entry == simple_cron_entry

    @freeze_time('2016-08-26 23:03:00')
    def test_requeues_entry(self, scheduler, simple_cron_entry):
        scheduler.register(simple_cron_entry)
        scheduler.return_next_and_reschedule()
        dt, entry = scheduler.next_scheduled
        assert dt == datetime(2016, 8, 26, 23, 5)
        assert entry == simple_cron_entry

import pytest

import cronpie

@pytest.fixture
def simple_cron_line():
    return '*/1 * * * * * ls'

@pytest.fixture
def simple_cron_entry(simple_cron_line):
    return cronpie.CronEntry.from_string(simple_cron_line)

@pytest.fixture
def ranged_cron_line():
    return '2-30 1-5 2-7 * * * ls'

@pytest.fixture
def ranged_cron_entry(ranged_cron_line):
    return cronpie.CronEntry.from_string(ranged_cron_line)

@pytest.fixture
def additive_cron_line():
    return '1,30 1,5 2,7 * * * ls'

@pytest.fixture
def frequency_cron_line():
    return '*/2 */5 * * * * ls'

@pytest.fixture
def complex_cron_line():
    return '0,20-30/2 * * * * * ls'

@pytest.fixture
def scheduler():
    yield cronpie.Scheduler.get_instance()
    cronpie.Scheduler.instance = None

@pytest.fixture
def runner(scheduler):
    runner = cronpie.Runner.get_instance()
    runner._scheduler = scheduler
    yield runner
    cronpie.Runner.instance = None

@pytest.fixture
def prober():
    yield cronpie.Prober.get_instance()
    cronpie.Prober.instance = None

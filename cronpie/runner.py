import multiprocessing
import os
import time
from datetime import datetime

import attr

from .utils.decorators import singleton


def _run_command(command):
    os.execlp(*command)


@singleton
@attr.s(slots=True)
class Runner:

    _scheduler = attr.ib(init=False)

    def _sleep_until_next_execution(self):
        scheduled_time, _ = self._scheduler.next_scheduled
        seconds = (scheduled_time - datetime.now()).total_seconds()
        time.sleep(seconds)

    def _run_task(self, command):
        process = multiprocessing.Process(target=_run_command, args=(command))
        process.run()
        return process.pid

import attr
from bintrees import FastAVLTree

from .decorators import singleton


@singleton
@attr.s(slots=True)
class Scheduler:
    _tree = attr.ib(
        init=False,
        default=attr.Factory(FastAVLTree),
        validator=attr.validators.instance_of(FastAVLTree)
    )

    def register(self, entry):
        self._tree.insert(entry.next_run, entry)

    def return_next_and_reschedule(self):
        _, entry = self._tree.pop_min()
        self.register(entry)

    @property
    def next_scheduled(self):
        return self._tree.min_item()

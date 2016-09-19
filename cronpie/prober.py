import attr

from .decorators import singleton


@singleton
@attr.s(slots=True)
class Prober:
    pass

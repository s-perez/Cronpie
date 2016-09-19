
def singleton(wrapped_cls):
    class _Singleton:
        def __init__(self, *args, **kwargs):
            raise NotImplementedError()

        @classmethod
        def get_instance(cls):
            if not getattr(cls, 'instance', False):
                cls.instance = wrapped_cls()
            return cls.instance

    return _Singleton

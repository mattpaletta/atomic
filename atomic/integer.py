from atomic.atomic import Atomic


class Integer(Atomic):
    def __init__(self, initial=0):
        super().__init__()
        self._value = initial

    def __getattr__(self, item):
        with self._lock:
            return self._value

    def __set__(self, instance, value):
        with self._lock:
            self._value = value

    def increment(self, by=1):
        with self._lock:
            self._value += by

    def decrement(self, by=1):
        with self._lock:
            self._value -= by

    def __add__(self, other):
        with self._lock:
            return self._value + other

    def __sub__(self, other):
        with self._lock:
            return self._value - other

import threading
from typing import TypeVar, Dict

from atomic.atomic import Atomic

K = TypeVar('K')
V = TypeVar('V')


class ThreadSafeDict(Atomic):
    def __init__(self):
        super().__init__()
        self._values: Dict[K, V] = {}

    def get(self, key: K):
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return self._values[key]
        else:
            return self._values[key]

    def set(self, key: K, value: V):
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return self._values.update({key: value})
        else:
            return self._values.update({key: value})

import threading
from typing import TypeVar, Dict, Optional, Iterator, Tuple

from atomic.atomic import Atomic

K = TypeVar('K')
V = TypeVar('V')


class ThreadSafeDict(Atomic):
    def __init__(self):
        super().__init__()
        self._values: Dict[K, V] = {}

    def __getitem__(self, item) -> Optional[V]:
        return self.get(item)

    def __setitem__(self, key, value) -> None:
        return self.set(key, value)

    def __contains__(self, item):
        return self.contains(item)

    def items(self) -> Iterator[Tuple[K, V]]:
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                for k, v in self._values.items():
                    yield k, v
        else:
            for k, v in self._values.items():
                yield k, v

    def contains(self, key: K) -> bool:
        return self.get(key) is not None

    def get(self, key: K) -> Optional[V]:
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return self._values.get(key, None)
        else:
            return self._values.get(key, None)

    def set(self, key: K, value: V) -> None:
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                self._values.update({key: value})
        else:
            self._values.update({key: value})

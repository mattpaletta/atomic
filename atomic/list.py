import threading
from typing import TypeVar, List

from atomic.atomic import Atomic

T = TypeVar('T')


class AtomicList(Atomic):
    def __init__(self, initial = None):
        super().__init__()
        self._value: List[T] = [] if initial is None else initial

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._value)

    def __len__(self):
        """List length"""
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return len(self._value)
        else:
            return len(self._value)

    def __getitem__(self, ii):
        """Get a list item"""
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return self._value[ii]
        else:
            return self._value[ii]

    def __delitem__(self, ii):
        """Delete an item"""
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                del self._value[ii]
        else:
            del self._value[ii]

    def __setitem__(self, ii, val):
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                if not self._in_transaction:
                    self._value[ii] = val
        else:
            self._value[ii] = val

    def __str__(self):
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return str(self._value)
        else:
            return str(self._value)

    def insert(self, ii, val):
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                self._value.insert(ii, val)
        else:
            self._value.insert(ii, val)

    def __add__(self, other):
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return self._value + other
        else:
            return self._value + other

    def __sub__(self, other):
        if not self._in_transaction or threading.current_thread() != self._transaction_thread:
            with self._lock:
                return [x for x in self._value not in other]
        else:
            return [x for x in self._value not in other]

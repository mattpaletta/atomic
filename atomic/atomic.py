import threading
from multiprocessing import Lock


class Atomic(object):
    def __init__(self):
        self._lock = Lock()
        self._in_transaction = False
        self._transaction_thread = None

    def __enter__(self):
        self.begin_transaction()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_transaction()
        return self

    def in_transaction(self):
        return self._in_transaction

    def begin_transaction(self):
        self._in_transaction = True
        self._transaction_thread = threading.current_thread()
        self._lock.acquire()

    def end_transaction(self):
        self._in_transaction = False
        self._transaction_thread = None
        self._lock.release()

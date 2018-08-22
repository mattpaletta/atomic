from multiprocessing import Lock


class Atomic(object):
    def __init__(self):
        self._lock = Lock()

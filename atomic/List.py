from Atomic import Atomic


class List(Atomic):
    def __init__(self, initial=[]):
        super().__init__()
        self._value = initial
        self._key_locks = []
        self._transation = False

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._value)

    def __len__(self):
        """List length"""
        if not self._transation:
            with self._lock:
                return len(self._value)
        else:
            return len(self._value)

    def __getitem__(self, ii):
        """Get a list item"""
        if not self._transation:
            with self._lock:
                return self._value[ii]
        else:
            return self._value[ii]

    def __delitem__(self, ii):
        """Delete an item"""
        if not self._transation:
            with self._lock:
                del self._value[ii]
        else:
            del self._value[ii]

    def __setitem__(self, ii, val):
        if not self._transation:
            with self._lock:
                self._value[ii] = val
        else:
            self._value[ii] = val

    def __str__(self):
        if not self._transation:
            with self._lock:
                return str(self._value)
        else:
            return str(self._value)

    def __enter__(self):
        with self._lock:
            self._transation = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        with self._lock:
            self._transation = False

    def insert(self, ii, val):
        if not self._transation:
            with self._lock:
                self._value.insert(ii, val)
        else:
            self._value.insert(ii, val)

    def __add__(self, other):
        if not self._transation:
            with self._lock:
                return self._value + other
        else:
            return self._value + other

    def __sub__(self, other):
        if not self._transation:
            with self._lock:
                return [x for x in self._value not in other]
        else:
            return [x for x in self._value not in other]
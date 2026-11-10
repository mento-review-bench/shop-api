import threading

class Counter:
    def __init__(self):
        self._lock = threading.Lock()
        self.value = 0

    def incr(self, n=1):
        with self._lock:
            self.value += n
            return self.value

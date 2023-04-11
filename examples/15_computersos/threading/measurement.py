import threading
from threading import Lock


class Measurement:

    def __init__(self):
        self.current_temp = 0.0
        self.min_temp = 0.0
        self.max_temp = 0.0
        # self.lock = Lock()
        # self.updated = threading.Condition()

    def update(self, new_current_temp):
        # self.lock.acquire()

        self.current_temp = new_current_temp
        self.max_temp = max(self.max_temp, self.current_temp)
        self.min_temp = min(self.min_temp, self.current_temp)

        # self.lock.release()

        # notify/signal that measurements has been updated
        # with self.updated:
        #    self.updated.notify_all()
        #    self.updated.notify()

    def get(self):

        # with self.updated:
        #    self.updated.wait()

        # self.lock.acquire()

        current_temp = self.current_temp
        min_temp = self.min_temp
        max_temp = self.max_temp

        # self.lock.release()

        return current_temp, min_temp, max_temp

    def __str__(self):

        current_temp, max_temp, min_temp = self.get()

        temp_str = f'({current_temp})[{max_temp};{min_temp}]'

        return temp_str



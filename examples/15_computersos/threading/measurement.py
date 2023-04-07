from threading import Lock


class Measurement:

    def __init__(self):
        self.current_temp = 0.0
        self.min_temp = 0.0
        self.max_temp = 0.0
        self.lock = Lock()

    def update(self, new_current_temp):
        self.lock.acquire()

        self.current_temp = new_current_temp
        self.max_temp = max(self.max_temp, self.current_temp)
        self.min_temp = min(self.min_temp, self.current_temp)

        self.lock.release()

        # TODO: signal any waiting display threads

    # TODO: introduce read method that returns a tuple and which is locked
    # wait here for signal

    def __str__(self):

        return f'({self.current_temp})[{self.max_temp};{self.min_temp}]'


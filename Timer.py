from time import time


class Timer:
    """ This is a timer that is used for the state system
    time is in milliseconds
    """

    def __init__(self):
        self.start_time = 0
        self.time = time

    def start(self):
        self.start_time = self.time()

    def elapsed_time(self):
        return int((self.time() - self.start_time)*1000)
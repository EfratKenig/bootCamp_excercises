import time


def slow_down(func):
    def inner():
        time.sleep(1)
    return inner()


slow_down(sum(range(3)))

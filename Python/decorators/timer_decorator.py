import time


def timer_decorator(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print("function runtime: " + str(end - start))
    return inner()


@timer_decorator
def sum1():
    return sum(range(10000000))


@timer_decorator
def sum2():
    return sum(range(50000000))

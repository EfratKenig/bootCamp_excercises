def cache_decorator(func):
    def inner(*args):
        if not inner.prev_results.__contains__(str(args)):
            ret = func(*args)
            inner.prev_results[str(args)] = ret
        else:
            return inner.prev_results[str(args)]
        return ret
    inner.prev_results = {}
    return inner


@cache_decorator
def rec_fib(num):
    print("calculating: " + str(num))
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return rec_fib(num - 1) + rec_fib(num - 2)


rec_fib(1)
rec_fib(4)

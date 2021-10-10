def count_calls(func):
    def inner(*args, **kwargs):
        inner.calls += 1
        print("Number of calls: " + str(inner.calls))
        return func(*args, **kwargs)
    inner.calls = 0
    return inner


@count_calls
def count():
    return 1


count()
count()
count()
count()
count()
count()


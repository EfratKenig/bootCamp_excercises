def func_info(func):
    def inner(*args, **kwargs):
        ret = func(*args, **kwargs)
        print("Function name: {}\nArgs: {}\nKwargs: {}\nReturn value: {}\nReturn type: {}"
              "".format(func.__name__, args, kwargs, ret, type(ret)))
    return inner


@func_info
def add(n1, n2, age, text):
    return n1+n2


add(1, 2, age=3, text="hello")

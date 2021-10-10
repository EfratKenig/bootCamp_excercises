def my_enumerate(iterable, start=0):
    obj_to_ret = ((i, iterable[i-start]) for i in range(start, start + len(iterable)))
    return obj_to_ret

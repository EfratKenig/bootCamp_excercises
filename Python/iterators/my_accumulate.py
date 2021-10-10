def my_accumulate(iterable):
    if iterable[0] is None:
        return 0
    obj_to_ret = [iterable[0]]
    for i in range(1, len(iterable)):
        obj_to_ret.append(iterable[i] + iterable[i - 1])
        iterable[i] = obj_to_ret[-1]
    return obj_to_ret

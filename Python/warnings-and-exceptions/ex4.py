def divide(x, y):
    try:
      print(f'{x}/{y} is {x / y}')
    except NameError as name_exc:
        print(name_exc)
    except ZeroDivisionError as zero_exc:
        print(zero_exc)
    except TypeError as type_exc:
        print(str(type_exc))
    except ValueError as val_exc:
        print(str(val_exc))

def exc_one_block(x, y):
    try:
      print(f'{x}/{y} is {x / y}')
    except (NameError, ZeroDivisionError, TypeError, ValueError) as exc:
        print(exc)
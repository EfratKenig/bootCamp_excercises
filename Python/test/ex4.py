def my_reduce(function, sequence, initial=None):
    if initial is not None:
        sequence = [initial] + sequence

    for i in range(len(sequence)-2):
        sequence[0] = function(sequence[0], sequence[1])
        sequence.pop(1)
    try:
        return function(sequence[0], sequence[1])
    except IndexError:
        print("The function '"+str(function.__name__) + "' requires at least two arguments")

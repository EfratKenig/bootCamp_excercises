def handle_exceptions():
    try:
        age = int(input("How old are you? "))
    except ValueError as exception:
        print(exception)
    except EOFError as exception:
        print(exception)

# EOFError: on ^D

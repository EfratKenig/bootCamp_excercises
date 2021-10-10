# Add a try-except statement to
# the body of this function which
# handles a possible IndexError
# and print an error message accordingly:

def get_list_element(my_list, index):
    try: print(my_list[index])
    except IndexError as exception:
        print(exception)

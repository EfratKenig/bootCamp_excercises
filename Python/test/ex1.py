import json


def combine_lines(source1, source2, dest, lines1=None, lines2=None):
    if lines1 is None:
        lines1 = []
    if lines2 is None:
        lines2 = []
    combined_lines = {}
    with open(source1, 'r') as file_a:
        file_lines = list(enumerate(file_a))
        for i in range(len(lines1)):
            try:
                num_line = lines1[i]
                combined_lines['line' + str(i + 1)] = [file_lines[num_line][1].strip('\n')]
            except IndexError:
                print('Line index out of range in ' + source1)
    with open(source2, 'r') as file_b:
        file_lines = list(enumerate(file_b))
        for i in range(len(lines2)):
            num_line = lines2[i]
            try:
                if combined_lines.__contains__('line' + str(i + 1)):
                    combined_lines['line' + str(i + 1)].append(file_lines[num_line][1].strip('\n'))
                else:
                    # add a new key to the dictionary:
                    combined_lines['line' + str(i + 1)] = [file_lines[num_line][1].strip('\n')]
            except IndexError:
                print('Line index out of range in ' + source2)
        with open(dest, 'w') as json_file:
            json.dump(combined_lines, json_file)

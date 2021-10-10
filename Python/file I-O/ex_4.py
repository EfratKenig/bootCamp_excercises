import json
import csv


def check_empty_values(dictionary):
    """
    auxiliary function for handling empty values
    in a dictionary gets a dict object
    :returns: a new dictionary with "***" replacing
    its empty values if any exist
    """
    for i in list(dictionary.keys()):
        if dictionary[i] == "":
            dictionary[i] = "***"
    return dictionary


def merge_files(json_file, csv_file):
    with open(json_file, 'r') as json_f:
        data_dict = json.load(json_f)
        tags = list(data_dict[0].keys())  # save the keys names for the csv data,
        # because there are different names there
    with open(csv_file, 'r') as csv_f:
        reader = csv.reader(csv_f)
        for rows in reader:
            break # advance to the second line
        dicts_list = []
        for rows in reader:
            my_dict = {str(tags[i]): rows[i] for i in range(len(tags))}
            dicts_list.append(my_dict)
        # generates a list of all dictionaries from both json and csv file:
        merged_dict = [check_empty_values(i) for i in data_dict] + [check_empty_values(i) for i in dicts_list]
    with open("merged_data.txt", 'w') as txt_f:
        counter = 1
        for i in merged_dict:
            str_to_write = "Report: {}\n" \
                           "Number: {}\n-----\n" \
                           "Time: {}\nOwner: {}\n" \
                           "Category: {} - {}\nFAIL/PASS {}\n" \
                           "======================================\n" \
                           "======================================\n".format(i['name'],
                                                                             counter, i['time'], i['owner'], i['cat'],
                                                                             i['sub-cat'], i['status'])
            counter += 1
            txt_f.write(str_to_write)


merge_files("test_reports.json", "test_reports.csv")

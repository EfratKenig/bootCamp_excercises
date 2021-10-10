import json


def dict_2_json(dictionary):
    """
    Converts the dict into a JSON file
    """
    with open("dict_2_json.json", 'w') as json_file:
        json.dump(dictionary, json_file)


my_dict = [
    {"name": "Afghanistan", "code": "AF"},
    {"name": "Åland Islands", "code": "AX"},
    {"name": "Albania", "code": "AL"},
    {"name": "Algeria", "code": "DZ"},
    {"name": "American Samoa", "code": "AS"},
    {"name": "Western Sahara", "code": "EH"},
    {"name": "Yemen", "code": "YE"},
    {"name": "Zambia", "code": "ZM"},
    {"name": "Zimbabwe", "code": "ZW"}
]
dict_2_json(my_dict)

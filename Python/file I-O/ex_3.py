import json


def create_ikea_files(path):
    with open(path, 'r') as data_file:
        l = []
        with open("ikea.json", 'w') as json_file:
            data_list = []
            for line in data_file:
                line = line.replace("\n", "")
                res = tuple(map(str, line.split(' - ')))
                data_dict = {str(res[0]): str(res[1])}
                data_list.append(data_dict)
            json.dump(data_list, json_file)
        with open("ikea.csv", 'w') as csv_file:
            data_file.seek(0, 0)
            csv_file.write('item, price\n')

            for line in data_file:
                line = line.replace("\n", "")
                res = str(line.split(' - ')).strip('[').replace(']', '\n').replace("'", '')
                csv_file.write(res)


create_ikea_files("ikea.txt")

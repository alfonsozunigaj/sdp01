import sys
from os import listdir
from os.path import isfile, join
from datetime import datetime as dt


def sort_elems(elem):
    return elem[1]


def parse_goals(file_name):
    goals = []
    tmp_file = open(file_name, "r")
    for line in tmp_file:
        temp_line = line.strip().split()
        goals.append([temp_line[0], int(temp_line[1]), temp_line[2], map(int, temp_line[3:])])
    tmp_file.close()
    return goals


def process_data():
    file_list = [f for f in listdir("data/") if isfile(join("data/", f))]
    data = {}
    for file in file_list:
        tmp_file = open("data/" + file, "r")
        tmp_file.readline()
        data[file] = {}
        for line in tmp_file:
            temp_line = line.strip().split(";")
            data[file][temp_line[0]] = map(int, temp_line[1:])
    return data


def get_element(goal):
    index = goal[1]
    direction = goal[2]
    parameters = goal[3]

    order = []

    data_file = open("data/" + goal[0], "r")
    data_file.readline()

    for line in data_file:
        l = line.strip().split(";")
        value = [l[0], sum([a * b for a, b in zip(parameters, map(float, l[1:]))])]
        order.append(value)
    data_file.close()

    order.sort(key=sort_elems, reverse=direction=="DESC")
    return order[index-1][0]


def get_preprocessed_element(goal, data):
    file_search = goal[0]
    index = goal[1]
    direction = goal[2]
    parameters = goal[3]

    order = []

    data_dictionary = data[file_search]

    for key in data_dictionary:
        value = [key, sum([a * b for a, b in zip(parameters, map(int, data_dictionary[key]))])]
        order.append(value)

    order.sort(key=sort_elems, reverse=direction == "DESC")
    return order[index-1][0]





print dt.now()

results = ""
if len(sys.argv) > 1 and sys.argv[1] == "-p":
    data = process_data()
    print dt.now()
    print "\n"

    file_name = raw_input()

    print dt.now()

    goals = parse_goals(file_name)
    for goal in goals:
        results += get_preprocessed_element(goal, data) + "\n"
else:
    goals = parse_goals("goals.txt")
    for goal in goals:
        results += get_element(goal) + "\n"

destination_file = open("results2.txt", "w")
destination_file.write(results)
destination_file.close()

print dt.now()

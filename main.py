import sys


def parse_goals(file_name):
    goals = []
    tmp_file = open(file_name, "r")
    for line in tmp_file:
        temp_line = line.strip().split()
        goals.append([temp_line[0], int(temp_line[1]), temp_line[2], map(int, temp_line[3:])])
    tmp_file.close()
    return goals


def swap(ordered_list, index):
    aux = ordered_list[index]
    ordered_list[index] = ordered_list[index - 1]
    ordered_list[index - 1] = aux


def order_elements(ordered_list, direction, index):
    j = index
    if direction == "ASC":
        while j > 0 and ordered_list[j - 1][1] > ordered_list[j][1]:
            swap(ordered_list, j)
            j -= 1
    else:
        while j > 0 and ordered_list[j - 1][1] < ordered_list[j][1]:
            swap(ordered_list, j)
            j -= 1
    return None


def get_element(goal):
    file_search = goal[0]
    index = goal[1]
    direction = goal[2]
    parameters = goal[3]

    order = [None] * (index + 1)

    data_file = open("data/" + file_search, "r")
    data_file.readline()

    iterator = 0
    for line in data_file:
        l = line.strip().split(";")
        value = [l[0], sum([a * b for a, b in zip(parameters, map(int, l[1:]))])]
        order[min(iterator, index)] = value
        order_elements(order, direction, min(iterator, index))
        iterator += 1
    data_file.close()
    return order[-2][0]


def save_results():
    global results
    destination_file = open("results2.txt", "w")
    for result in results:
        destination_file.write(result + "\n")
    destination_file.close()


if len(sys.argv) > 1 and sys.argv[1] == "-p":
    file_name = raw_input()
    goals = parse_goals(file_name)
else:
    goals = parse_goals("goals.txt")
results = []
for goal in goals:
    results.append(get_element(goal))
save_results()

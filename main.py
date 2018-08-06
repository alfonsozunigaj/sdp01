def parse_goals():
	goals = []

	tmp_file = open("goals.txt", "r")
	for line in tmp_file:
		temp_line = line.strip().split()
		goals.append([temp_line[0], int(temp_line[1]), temp_line[2],  map(int, temp_line[3:])])

	return goals


def swap(ordered_list, index):
	aux = ordered_list[index]
	ordered_list[index] = ordered_list[index-1]
	ordered_list[index-1] = aux


def order_elements(ordered_list, direction, index):
	i = 0
	while i <= index:
		j = i
		if ordered_list[j] == None: break
		if direction == "ASC":
			while j > 0 and ordered_list[j-1][1] > ordered_list[j][1]:
				swap(ordered_list, j)
				j -= 1
		else:
			while j > 0 and ordered_list[j-1][1] < ordered_list[j][1]:
				swap(ordered_list, j)
				j -= 1
		i += 1
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
		value = [l[0], sum([a*b for a,b in zip(parameters,map(int,l[1:]))])]
		order[min(iterator, index)] = value
		iterator += 1
		order_elements(order, direction, min(iterator, index))
	print(order[-2][0])










goals = parse_goals()
for goal in goals:
	get_element(goal)
import collections

file ='a.txt'

def change_path(path):
    node_path = []
    for location in path[1:]:
        for intersection in directory:
            if location == intersection[2]:
                node_path.append(int(intersection[1]))
    return node_path

def conflict_finder():
    conflicts = [item for item, count in collections.Counter(current_pos).items() if count > 1]
    return conflicts

with open(file, "r+") as f:
    data_set_example = f.read()
    f.close()

data_set_example = data_set_example.split("\n")
length = len(data_set_example)

for i in range(length):
    data_set_example[i] = data_set_example[i].split(" ")

duration = int(data_set_example[0][0])
intersections = int(data_set_example[0][1])
streets = int(data_set_example[0][2])
cars = int(data_set_example[0][3])
score = int(data_set_example[0][4])

directory = []
paths = []

i = 1
while i < length-1:
    if i < 1+streets:
        directory.append(data_set_example[i])
        i += 1
    else:
        paths.append(data_set_example[i])
        i += 1

node_path = []
for path in paths:
    node_path.append(change_path(path))

edge_list = []
for item in directory:
    edge_list.append(list((int(item[0]), int(item[1]), int(item[3]))))

travel = [[0 for i in range(intersections)] for j in range(intersections)]
for i in range(intersections):
    for j in range(intersections):
        if i == j:
            travel[j][i] = 1
for row, col, weight in edge_list:
    travel[row][col] = weight

starting_pos = []
for i in range(cars):
    starting_pos.append(int(paths[i][0]))

current_pos = starting_pos

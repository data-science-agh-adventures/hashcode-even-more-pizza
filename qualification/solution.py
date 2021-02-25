from collections import defaultdict

filename = 'f.txt'
with open(filename) as input_data:
    simulationTime, intersectionsCount, streetsCount, carsCount, bonus = \
    list(map(int, input_data.readline().split()))


    crossroads = []
    for i in range(intersectionsCount):
        crossroads.append([i, []])

    streets_dict = {}


    for i in range(streetsCount):
        start, end, name, weight = input_data.readline().strip().split(' ')
        crossroads[int(end)][1].append(name)
        streets_dict[name] = {'start': int(start), 'end': int(end), 'weight': int(weight), 'cars': [], 'isRed': True}


    cars_list = []
    for i in range(carsCount):
        items = input_data.readline().strip().split(' ')
        street_count = int(items[0])
        route = items[1:]
        start_street = route[0]
        streets_dict[start_street]['cars'].append(i)
        cars_list.append({'street_count': street_count, 'route': route, 'path_index': 0})


streets_points = defaultdict(int)

for car in cars_list:
    for road in car['route']:
        routeLength = 0
        streets_points[road] += 1

crossroads_points = []


for i in range(len(crossroads)):
    crossroads_points.append(defaultdict(int))
    # temporaryList = []
    minimum = -1
    for element in crossroads[i][1]:
        # temporaryList.append(streets_points[element])
        current_points = streets_points[element]
        if minimum == -1 or current_points < minimum and current_points != 0:
            minimum = current_points
    if minimum in [0, -1]:
        continue

    for street in crossroads[i][1]:
        if streets_points[street] != 0:
            crossroads_points[i][street] = streets_points[element] // minimum
    # minimum = min(temporaryList)
    # if minimum > 0:
    #    crossroads_points[i][element] = streets_points[element] // minimum

# print(streets_points)
# print(crossroads_points)

with open(filename.replace('.txt', '.out'), 'w') as output_data:
    total = len(crossroads_points)
    output_data.write(f'{total}\n')
    for i, crossroad in enumerate(crossroads_points):
        crossroad_keys = list(filter(lambda x: crossroad[x] > 0, crossroad))
        streets_count = len(crossroad_keys)
        if streets_count == 0:
            continue

        output_data.write(f'{i}\n')
        output_data.write(f'{streets_count}\n')
        for street in crossroad_keys:
            output_data.write(f'{street} {crossroad[street]}\n')

print('END')


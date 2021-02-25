with open("a.txt") as input_data:
    simulationTime, intersectionsCount, streetsCount, carsCount, bonus = \
        list(map(int, input_data.readline().split()))



"""
from collections import defaultdict

crossroads = defaultdict(defaultdict(list))
streets_dict = {}

for _ in range(streets):
    start, end, name, weight = input_data.readline()
    crossroads[int(end)]['in'].append(name)
    crossroads[int(start)]['out'].append(name)
    streets_dict[name] = {'start': int(start), 'end': int(end), 'weight': int(weight), 'cars': []}

cars_list = []
for i in range(cars):
    items = input_data.readline().split(' ')
    street_count = int(items[0])
    route = items[1:]
    start_street = route[0]
    streets_dict[start_street]['cars'].append(i)
    cars_list.append({'street_count': street_count, 'route': route})
"""

with open("a.txt") as input_data:
    simulationTime, intersectionsCount, streetsCount, carsCount, bonus = \
        list(map(int, input_data.readline().split()))


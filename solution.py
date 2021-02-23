from copy import deepcopy
import sys
import logging

# xdddddddd
def get_problem_solution_output(pizza_list, two_teams, three_teams, four_teams):
    team_divisions = divide_for_sum_of_team_sizes(len(pizza_list), \
        two_teams, three_teams, four_teams)
    
    points = 0
    result = []
    team_sizes = (4, 3, 2)
    pizza_list_temp = deepcopy(pizza_list)
    for team_division, team_size in zip(team_divisions, team_sizes):
        if team_division < 1:
            continue

        for _ in range(team_division):
            team_pizzas = (team_size, [])
            pizzas = get_max_pizzas_for_team(pizza_list_temp, team_size)
            for element in pizzas[0]:
                pizza_list_temp.pop(element)
                team_pizzas[1].append(element)
            points += pizzas[1]
            result.append(team_pizzas)
    
    logging.debug(points)
    return result
    # return [
    #     (2, [1, 4]),
    #     (3, [0, 2, 3])
    # ]


def divide_for_sum_of_team_sizes(pizza_count, t2, t3, t4):
    fours, threes, twos = 0, 0, 0
    while (pizza_count >= 6 or pizza_count == 4) and fours < t4:
        fours += 1
        pizza_count -= 4
    
    while (pizza_count >= 5 or pizza_count == 3) and threes < t3:
        threes += 1
        pizza_count -= 3
    
    while (pizza_count >= 4 or pizza_count == 2) and twos < t2:
        twos += 1
        pizza_count -= 2
    
    return fours, threes, twos


def get_max_pizzas_for_team(pizza_list, pizza_count_for_team):
    result = {}
    pizza_list_temp = deepcopy(pizza_list)
    points = 0
    for _ in range(pizza_count_for_team):
        max_pizza_index = max(pizza_list_temp, key = lambda x: pizza_list_temp[x][0])
        points += len(pizza_list_temp[max_pizza_index][1])
        ingredients = pizza_list_temp.pop(max_pizza_index)
        for line in pizza_list_temp:
            pizza_list_temp[line][1].difference_update(ingredients[1])
            pizza_list_temp[line][0] = len(pizza_list_temp[line][1])
        result[max_pizza_index] = pizza_list[max_pizza_index]
    return result, points ** 2


def write_output(path_to_base_on, solution_output):
    no_ext_path = path_to_base_on.replace('.in', '')
    target_path = no_ext_path + '.out'
    with open(target_path, 'w') as target_file:
        teams_count = len(solution_output)
        line = f'{teams_count}\n'
        target_file.write(line)
        for i, (team_size, pizzas) in enumerate(solution_output):
            line = f'{team_size} {" ".join(map(str, pizzas))}'
            if i < teams_count - 1:
                line += '\n'
            target_file.write(line)


def solve_file_input(path):
    with open(path) as input_data:
        pizza_count, two_teams, three_teams, four_teams = \
            list(map(int, input_data.readline().split()))
        
        pizza_list = {}
        for i, line in enumerate(input_data):
            if not line:
                continue
            if i >= pizza_count:
                break
            items = line.split()
            result_line = [int(items[0]), set(items[1:])]
            pizza_list[i] = result_line
        
    solution_output = get_problem_solution_output(pizza_list, \
            two_teams, three_teams, four_teams)
    write_output(path, solution_output)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    for path in sys.argv[1:]:
        solve_file_input(path)

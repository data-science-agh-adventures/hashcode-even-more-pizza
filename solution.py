from copy import deepcopy
import sys


def get_problem_solution_output(pizza_list, two_teams, three_teams, four_teams):
    return [
        (2, [1, 4]),
        (3, [0, 2, 3])
    ]


def write_output(path_to_base_on, solution_output):
    no_ext_path = path_to_base_on.replace('.in', '')
    target_path = no_ext_path + '.out'
    with open(target_path, 'w') as target_file:
        teams_count = len(solution_output)
        line = f'{teams_count}\n'
        target_file.write(line)
        for team_size, pizzas in solution_output:
            line = f'{team_size} {" ".join(map(str, pizzas))}\n'
            target_file.write(line)


if __name__ == '__main__':
    path = sys.argv[1]
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
            result_line = [int(items[0]), items[1:]]
            pizza_list[i] = result_line
        
    solution_output = get_problem_solution_output(pizza_list, \
            two_teams, three_teams, four_teams)
    write_output(path, solution_output)

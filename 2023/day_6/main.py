import math

# Setup
with open('2023/day_6/input.txt') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]

# Part 1
time_list = lines[0]
distance_list = lines[1]

def clean_input_list(input_list):
    new_list = input_list.split(":")[1]
    new_list = new_list.split(" ")
    new_list = list(filter(None, new_list))
    new_list = [int(x) for x in new_list]

    return new_list


time_list = clean_input_list(time_list)
distance_list = clean_input_list(distance_list)

def check_conditions(my_time, my_distance, my_time_held):
    time_after = my_time - my_time_held
    distance_travelled = my_time_held * time_after

    if distance_travelled > my_distance:
        return 1
    else:
        return 0


def solve_part_1(my_time_list, my_distance_list):
    answer_list = []
    for ind, time in enumerate(my_time_list):
        count = 0
        for t in range(0, time + 1): # t ~ time held
            count += check_conditions(time, my_distance_list[ind], t)
        answer_list.append(count)
    
    answer = math.prod(answer_list)

    return answer


answer_1 = solve_part_1(time_list, distance_list)

# Part 2
def find_combined_variable(input_list):
    new_input_list = [str(x) for x in input_list]
    variable = ""
    for var in new_input_list:
        variable += var

    variable = int(variable)

    return variable


new_time = find_combined_variable(time_list)
new_distance = find_combined_variable(distance_list)


# It is worth noting for this solution that after the first solution is found
# all subsequent answers work except until it doesn't, then all subsequent
# solutions don't work

def solve_part_2(my_time, my_distance):
    solution_index = 0

    for ind, time in enumerate(range(0, my_time + 1)):
        # time ~ time held
        # my_time is total_time

        time_after = my_time - time # time left after being held
        if time_after * time > my_distance:
            solution_index += ind
            break

    answer = my_time - (solution_index*2) + 1

    return answer


answer_2 = solve_part_2(new_time, new_distance)

print(answer_1)
print(answer_2)
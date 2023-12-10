import numpy as np
import string
import math

# Create list of sybmols and numbers
symbols = list(string.punctuation)
symbols.remove(".")
nums = list(string.digits)

with open('input.txt') as f:
    lines = f.readlines()
lines = [word.strip() for word in lines]

# Part 1
# Replace any symbol in strings with a "*"
lines_star = []
for line in lines:
    new_line = line
    for sym in symbols:
        new_line = new_line.replace(sym, "*")
    lines_star.append(new_line)


# Now check if number is connected to a "*"
num_coords = []
star_coords = []
for idx, line in enumerate(lines_star):

    for i, char in enumerate(line):
        x = i
        y = idx
        if char in nums:
            num_coords.append([x, y])

        if char == "*":
            star_coords.append([x, y])


# Combine each number into a list if the next number is connected
combined_num_coords = []
coord_sublist = []
for idx, coord in enumerate(num_coords):

    if len(coord_sublist) == 0:
        coord_sublist.append(num_coords[idx])

    elif num_coords[idx] == num_coords[-1] and num_coords[
        idx][0] == coord_sublist[-1][0] + 1:

        coord_sublist.append(num_coords[idx])
        combined_num_coords.append(coord_sublist)

    elif num_coords[idx][0] == coord_sublist[-1][0] + 1:
        coord_sublist.append(num_coords[idx])

    else:
        combined_num_coords.append(coord_sublist)
        coord_sublist = [num_coords[idx]]


# Create a list of same length full of True or False based on whether
#   it connects to a "*" or not --> Do this by checking if in star_coords
# Finally add up the numbers where it is True

true_false_list = []
for coord_set in combined_num_coords:
    check = False

    coord_check_list = []
    for coord in coord_set:
        for x in range(-1, 2):
            for y in range(-1, 2):
                coord_check_list.append([x + coord[0], y + coord[1]])
    
    for coord_test in coord_check_list:
        if coord_test in star_coords:
            check = True

    true_false_list.append(check)


answer_1 = 0
for idx, check in enumerate(true_false_list):
    sum_str = ""
    if check == True:
        for coord in combined_num_coords[idx]:
            sum_str += lines[coord[1]][coord[0]]
        
        sum_int = int(sum_str)
        answer_1 += sum_int


# Part 2
# Now check if number is connected to a "*"
real_star_coords = []
for idx, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == "*":
            real_star_coords.append([i, idx])


coord_check_lists = []
for idx, coord_set in enumerate(combined_num_coords):

    coord_check_list = []
    for coord in coord_set:
        for x in range(-1, 2):
            for y in range(-1, 2):
                coord_check_list.append([x + coord[0], y + coord[1]])
    
    coord_check_lists.append(coord_check_list)


answer_2_ind_list = []
for star_coords in real_star_coords:

    answer_2_ind = []
    for idx, coords in enumerate(coord_check_lists):
        for coord in coords:
            if coord == star_coords:
                answer_2_ind.append(idx)
                break
    if len(answer_2_ind) > 1: # Remove stars with only 1 matching number
        answer_2_ind_list.append(answer_2_ind)


number_set_list = []
for indices_list in answer_2_ind_list:

    number_sublist = []
    for index in indices_list:
        # This gets us a list of coords
        coord_list = combined_num_coords[index]

        num_str = ""
        for coord in coord_list:
            num_str += lines[coord[1]][coord[0]]
            
        number_sublist.append(int(num_str))
    number_set_list.append(number_sublist)


answer_2_list = []
for number_set in number_set_list:
    answer_2_list.append(math.prod(number_set))

answer_2 = sum(answer_2_list)


print(answer_1)
print(answer_2)
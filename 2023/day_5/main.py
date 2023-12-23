# Setup
with open('2023/day_5/input.txt') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]


# Part 1
# Split out each section of the input
master_list = []
section_list = []
for ind, line in enumerate(lines):

    if line != "" and ind == len(lines)-1:
        section_list.append(line)
        master_list.append(section_list)

    elif line != "":
        section_list.append(line)

    elif line == "":
        master_list.append(section_list)
        section_list = []


# Turn seeds into an input list
seeds = (lines[0]).split(": ")[1]
seeds = seeds.split(" ")
seeds = [int(x) for x in seeds]

def fix_map_input(map_list):
    '''
    Function that cleans the maps in the Almanac
        - Removes the first elt in the list
        - Turns other elts into lists with integers
    '''
    new_map_list = []
    
    for ind, n in enumerate(map_list):
        if ind == 0:
            pass
        else:
            map_fixed = n.split(" ")
            map_fixed = [int(x) for x in map_fixed]
            new_map_list.append(map_fixed)

    return new_map_list

# Fix all the inputs
list_of_map_inputs = []
for ind, lst in enumerate(master_list):
    if ind > 0:
        list_of_map_inputs.append(fix_map_input(lst))

# Put the seeds through the Almanac maps
location_list = []
for seed in seeds:
    n = seed
    for map_input in list_of_map_inputs:
        for sub_map in map_input:
            range_length = sub_map[2] - 1
            if n >= sub_map[1] and n <= sub_map[1] + range_length:
                n = sub_map[0] + (n-sub_map[1])
                break
            
    location_list.append(n)


answer_1 = min(location_list)


# Part 2
# Create list of seed pairs (i.e. start of range and length of range)
seeds_pair_list = []
for i in range(0, len(seeds), 2):
    seeds_pair_list.append([seeds[i], seeds[i+1]])

# Idea --> Work completely backwards
smallest_location = 0
answer_flag = False
while answer_flag != True:
    n = smallest_location
    for map_input in reversed(list_of_map_inputs):
        for sub_map in map_input:
            range_length = sub_map[2] - 1
            if n >= sub_map[0] and n <= sub_map[0] + range_length:
                n = sub_map[1] + (n-sub_map[0])
                break

    for seed_pair in seeds_pair_list:
        if n >= seed_pair[0] and n <= seed_pair[0] + seed_pair[1] - 1:
            answer_flag = True
    
    if answer_flag == False:
        smallest_location += 1
        

answer_2 = smallest_location


print(answer_1)
print(answer_2)
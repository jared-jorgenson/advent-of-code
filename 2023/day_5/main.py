# Setup
with open('example.txt') as f:
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



print(answer_1)
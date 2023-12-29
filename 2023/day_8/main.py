import math

# Setup
with open('2023/day_8/input.txt') as f:
    lines = f.readlines()
lines = [word.strip() for word in lines]

# Part 1
    
turn_instructions = lines[0]

network_input = lines[2:]
network_input = [x.replace("(", "") for x in network_input]
network_input = [x.replace(")", "") for x in network_input]

def go_left(node):
    path = node.split(" = ")[1]
    path = path.split(", ")[0]
    return path


def go_right(node):
    path = node.split(" = ")[1]
    path = path.split(", ")[1]
    return path


def find_node(path, network):
    node = "".join(filter(lambda x: x.startswith(path), network))
    return node


def count_number_turns(my_instructions, my_network_input):
    # Set current node at first node
    starting_path = "AAA"
    current_node = find_node(starting_path, my_network_input)
    count = 0

    while current_node.startswith("ZZZ") == False:
        for instruction in my_instructions:
            if current_node.startswith("ZZZ"):
                break

            elif instruction == "L":
                new_path = go_left(current_node)
                current_node = find_node(new_path, my_network_input)
                count += 1
            elif instruction == "R":
                new_path = go_right(current_node)
                current_node = find_node(new_path, my_network_input)
                count += 1

    return count
            

# Part 2
def find_start_nodes(my_network):
    starting_nodes = []
    for node in my_network:
        if node[2] == "A":
            node_path = node[:3]
            starting_nodes.append(node_path)

    return starting_nodes


def count_steps_simultaneous(my_instructions, my_network_input):
    starting_paths = find_start_nodes(my_network_input)
    starting_nodes = [find_node(s, my_network_input) for s in starting_paths]

    answer_list = []
    for node in starting_nodes:
        count = 0
        current_node = node
        while current_node[2] != "Z":
            for instruction in my_instructions:

                if current_node[2] == "Z":
                    break

                elif instruction == "L":
                    new_path = go_left(current_node)
                    current_node = find_node(new_path, my_network_input)
                    count += 1

                elif instruction == "R":
                    new_path = go_right(current_node)
                    current_node = find_node(new_path, my_network_input)
                    count += 1

        answer_list.append(count)
        answer = math.lcm(*answer_list)

    return answer


answer_1 = count_number_turns(turn_instructions, network_input)
answer_2 = count_steps_simultaneous(turn_instructions, network_input)

print(answer_1)
print(answer_2)
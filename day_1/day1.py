# Part 1

with open('day1.txt') as f:
    lines = f.readlines()


new_lines = [element.replace('\n', '0') for element in lines]

integer_list = [int(int(element)/10) for element in new_lines]

integer_list[-1] = integer_list[-1]*10


solution_list = []
index = 0
current_sum = 0

while index < len(integer_list):
    if integer_list[index] != 0 and index == len(integer_list) - 1:
        current_sum += integer_list[index]
        solution_list.append(current_sum)
        index += 1
    elif integer_list[index] != 0:
        current_sum += integer_list[index]
        index += 1
    else:
        solution_list.append(current_sum)
        index += 1
        current_sum = 0

print(max(solution_list))

# Part 2

solution_list.sort(reverse=True)

print(solution_list)

part_2_answer = solution_list[0] + solution_list[1] + solution_list[2]

print(part_2_answer)

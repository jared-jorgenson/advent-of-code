with open('puzzle_1_input.txt') as f:
    lines = f.readlines()

# Setup
lines = [word.strip() for word in lines]
lines = [line.split("   ") for line in lines]


# Part 1
left_input = [int(line[0]) for line in lines]
right_input = [int(line[1]) for line in lines]

left_input.sort()
right_input.sort()

answer_1_list = []
for index, left_num in enumerate(left_input):
    right_num = right_input[index]
    calc_number = abs(left_num - right_num)
    answer_1_list.append(calc_number)

answer_1 = sum(answer_1_list)

print(f'Answer 1: {answer_1}')


# Part 2

answer_2_list = []
for left_num in left_input:
    count_left_in_right = right_input.count(left_num)
    calc_number_2 = count_left_in_right * left_num

    answer_2_list.append(calc_number_2)

answer_2 = sum(answer_2_list)

print(f'Answer 2: {answer_2}')
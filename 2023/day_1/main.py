import re

with open('input.txt') as f:
    lines = f.readlines()

# Setup
lines_s = [word.strip() for word in lines]
lines = [list(word.strip()) for word in lines]
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
string_nums = ['one', 'two', 'three', 'four', 'five',
               'six', 'seven', 'eight', 'nine']

num_dict = {(string_nums+nums)[i]: (nums+nums)[i] for i in range(len(nums)*2)}

# Part 1
answer_list = []

for input_list in lines:

    for char in input_list:
        if char in nums:
            char1 = char
            break

    for char in reversed(input_list):
        if char in nums:
            char2 = char
            break

    answer_list.append(int(char1 + char2))

answer = sum(answer_list)

# Part 2
answer2_list = []

pattern_nums = r'(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))'

for input_s in lines_s:
    decrypted_list = re.findall(pattern_nums, input_s)
    output_list = []
    for elt in decrypted_list:
        output = num_dict[elt]
        output_list.append(output)
        final_output = int(output_list[0] + output_list[-1])
    answer2_list.append(final_output)

answer_2 = sum(answer2_list)


# Answers
print(answer)
print(answer_2)
import string

with open('day3.txt') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]
full_letters = string.ascii_lowercase + string.ascii_uppercase
full_dict = {letters: idx for idx,
             letters in enumerate(full_letters, start=1)}

pt1_answer = 0
pt2_answer = 0

for i in range(0, len(lines)):
    first_half = lines[i][:int(len(lines[i])/2)]
    second_half = lines[i][int(len(lines[i])/2):]

    pt1_answer += full_dict[list(set(first_half).intersection(second_half))[0]]


index = 0

while index < len(lines):
    first_line = lines[index]
    second_line = lines[index + 1]
    third_line = lines[index + 2]

    pt2_answer += full_dict[list(set(first_line) &
                                 set(second_line) & set(third_line))[0]]

    index += 3


print(pt1_answer)
print(pt2_answer)

with open('day4.txt') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]


pt1_answer = 0
for i in range(0, len(lines)):
    A = lines[i].split(',')

    first_nums = A[0].split('-')
    second_nums = A[1].split('-')

    first_list = [x for x in range(int(first_nums[0]), int(first_nums[1])+1)]
    second_list = [x for x in range(
        int(second_nums[0]), int(second_nums[1])+1)]

    first_set = set(first_list)
    second_set = set(second_list)

    if first_set.issubset(second_set) == True:
        pt1_answer += 1
    elif second_set.issubset(first_set) == True:
        pt1_answer += 1

pt2_answer = 0
for i in range(0, len(lines)):
    A = lines[i].split(',')

    first_nums = A[0].split('-')
    second_nums = A[1].split('-')

    first_list = [x for x in range(int(first_nums[0]), int(first_nums[1])+1)]
    second_list = [x for x in range(
        int(second_nums[0]), int(second_nums[1])+1)]

    first_set = set(first_list)
    second_set = set(second_list)

    if not first_set.isdisjoint(second_set) == True:
        pt2_answer += 1


print(pt1_answer)
print(pt2_answer)

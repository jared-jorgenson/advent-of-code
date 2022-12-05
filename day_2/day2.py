with open('day2.txt') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]

my_score = 0

for i in lines:
    if i[0] == "A":
        if i[2] == "X":
            my_score += 4
        elif i[2] == "Y":
            my_score += 8
        else:
            my_score += 3
    elif i[0] == "B":
        if i[2] == "X":
            my_score += 1
        elif i[2] == "Y":
            my_score += 5
        else:
            my_score += 9
    else:
        if i[2] == "X":
            my_score += 7
        elif i[2] == "Y":
            my_score += 2
        else:
            my_score += 6

print(my_score)

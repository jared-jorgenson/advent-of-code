# Setup
with open('input.txt') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]


# Part 1
answer_1 = 0
for ind, line in enumerate(lines):
    games_list = line.rsplit(': ')[1].split('; ')
    games_ind = ind + 1

    game_possible = True

    for game in games_list:
        game_hand_list = game.split(", ")

        for colour_cubes in game_hand_list:
            number = int(colour_cubes.split(" ")[0])
            colour = colour_cubes.split(" ")[1]

            if colour == "red" and number > 12:
                game_possible = False
            
            if colour == "green" and number > 13:
                game_possible = False

            if colour == "blue" and number > 14:
                game_possible = False
    
    if game_possible:
        answer_1 += games_ind


# Part 2
answer_2_list = []

for line in lines:
    games_list = line.rsplit(': ')[1].split('; ')
    all_game_hands = []

    for game in games_list:
        game_hand_list = game.split(", ")
        all_game_hands = all_game_hands + game_hand_list

    red_num = 0
    green_num = 0
    blue_num = 0

    for colour_cubes in all_game_hands:
        number = int(colour_cubes.split(" ")[0])
        colour = colour_cubes.split(" ")[1]

        if colour == "red" and red_num < number:
            red_num = number

        if colour == "green" and green_num < number:
            green_num = number

        if colour == "blue" and blue_num < number:
            blue_num = number

    product_colour_cubes = red_num * green_num * blue_num
    answer_2_list.append(product_colour_cubes)

answer_2 = sum(answer_2_list)


print(answer_1)
print(answer_2)
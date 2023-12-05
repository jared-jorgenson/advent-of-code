# Setup
with open('input.txt') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]


# Part 1
games_list = []
for line in lines:
    game = line.split(": ")[1]
    games_list.append(game)

answer_1 = 0
for game in games_list:
    winning_nums = game.split(" | ")[0]
    game_nums = game.split(" | ")[1]

    winning_nums_list = winning_nums.split(" ")
    game_nums_list = game_nums.split(" ")

    while "" in winning_nums_list:
        winning_nums_list.remove("")

    while "" in game_nums_list:
        game_nums_list.remove("")

    count = 0
    for num in game_nums_list:
        if num in winning_nums_list:
            count += 1

    if count > 1:
        answer_1 += 1 * (2**(count - 1))
    else:
        answer_1 += count


# Part 2
num_cards = [1] * len(lines)

for ind, game in enumerate(games_list):
    winning_nums = game.split(" | ")[0]
    game_nums = game.split(" | ")[1]

    winning_nums_list = winning_nums.split(" ")
    game_nums_list = game_nums.split(" ")

    while "" in winning_nums_list:
        winning_nums_list.remove("")

    while "" in game_nums_list:
        game_nums_list.remove("")

    number_of_games = num_cards[ind]

    count = 0
    for num in game_nums_list:
        if num in winning_nums_list:
            count += 1
    
    for card_add in range(count):
        num_cards[card_add + ind + 1] += 1 * number_of_games

answer_2 = sum(num_cards)


print(answer_1)
print(answer_2)
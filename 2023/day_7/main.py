import math

# Setup
with open('2023/day_7/input.txt') as f:
    lines = f.readlines()
lines = [word.strip() for word in lines]

# Part 1
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
cards_dict = {x:ind for ind, x in enumerate(cards)}

card_hand_list = [x.split(" ")[0] for x in lines]
bid_hand_list = [int(x.split(" ")[1]) for x in lines]


def group_card_hand(x): # x ~ the cards in a hand
    # This function finds if its 5 of a kind, 4 of a kind, ..., then
    # gives a value, higher value means better group of hand
    if len(set(x)) == 1:
        return 6
    elif len(set(x)) == 2 and (x.count(x[0]) == 1 or x.count(x[0]) == 4):
        return 5
    elif len(set(x)) == 2:
        return 4
    elif len(set(x)) == 3 and (
        x.count(x[0]) == 3 or x.count(x[1]) == 3 or x.count(x[2]) == 3):
        return 3
    elif len(set(x)) == 3:
        return 2
    elif len(set(x)) == 4:
        return 1
    elif len(set(x)) == 5:
        return 0


def is_hand_higher(my_hand_1, my_hand_2, my_cards_dict):
    for ind, card in enumerate(my_hand_1):
        card_2 = my_hand_2[ind]
        if my_cards_dict[card] > my_cards_dict[card_2]:
            return True
        elif my_cards_dict[card] < my_cards_dict[card_2]:
            return False


# higher rank = higher number so lowest rank goes first in the list
def solve_camel_game(my_card_hand_list, my_bid_hand_list, card_dic, group_fn):
    bid_list = []
    hand_placement_list = []

    for ind, my_card_hand in enumerate(my_card_hand_list):
        check_group = group_fn(my_card_hand)

        card_check = False
        if hand_placement_list != []:
            if is_hand_higher(my_card_hand, hand_placement_list[-1], card_dic):
                card_check = True

        if hand_placement_list == []: # base case
            hand_placement_list.append(my_card_hand)
            bid_list.append(my_bid_hand_list[ind])

        elif check_group > group_fn(hand_placement_list[-1]):
            hand_placement_list.append(my_card_hand)
            bid_list.append(my_bid_hand_list[ind])

        elif check_group >= group_fn(
            hand_placement_list[-1]) and card_check:

            hand_placement_list.append(my_card_hand)
            bid_list.append(my_bid_hand_list[ind])

        else:
            for ind2, my_hand in enumerate(hand_placement_list):
                break_flag = False
                if group_fn(my_hand) > check_group:
                    hand_placement_list.insert(ind2, my_card_hand)
                    bid_list.insert(ind2, my_bid_hand_list[ind])
                    break

                elif group_fn(my_hand) == check_group:
                    if is_hand_higher(my_hand, my_card_hand, card_dic):
                        hand_placement_list.insert(ind2, my_card_hand)
                        bid_list.insert(ind2, my_bid_hand_list[ind])
                        break_flag = True
                if break_flag:
                    break

    answer_list = [(ind+1)*x for ind, x in enumerate(bid_list)]
    answer = sum(answer_list)

    return answer


# Part 2
cards2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
cards_dict_2 = {x:ind for ind, x in enumerate(cards2)}

def group_card_hand_2(x): # x ~ the cards in a hand
    if "J" not in x:
        return group_card_hand(x)
    
    else:
        group_value = group_card_hand(x)

        for card in cards2:
            new_hand = x.replace("J", card)
            if group_card_hand(new_hand) == 6:
                group_value = 6
                break
            elif group_card_hand(new_hand) > group_value:
                group_value = group_card_hand(new_hand)

        return group_value


answer_1 = solve_camel_game(card_hand_list,
                        bid_hand_list,
                        cards_dict,
                        group_card_hand)

answer_2 = solve_camel_game(card_hand_list,
                        bid_hand_list,
                        cards_dict_2,
                        group_card_hand_2)


print(answer_1)
print(answer_2)
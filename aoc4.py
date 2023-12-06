
cards = []
with open('aoc4.txt', 'r') as file:
    for line in file:
        card, line = line.split(':')
        win_num, my_num = line.split(' | ')
        win_num = list(map(lambda x: int(x), win_num.split()))
        my_num = list(map(lambda x: int(x), my_num.strip('\n').split()))
        card = [win_num, my_num]
        cards.append(card)

total_points = 0
# Part 1
for win_list, num_list in cards:
    match = 0
    match = len(set(win_list) & set(num_list))
    point = lambda x: 0 if x == 0 else 2**(x - 1)
    # print(match)
    # for win in win_list:
    #     if win in num_list:
    #         match +=1
    # if match == 0:
    
    #     point = 0
    # else:
    #     point = 2**(match - 1)
    total_points += point(match)
print(total_points)

scratchcards = []
i = 0
# for win_list, num_list in cards:
#     i += 1
#     if i < 3:
#         instance = []
#         match = 0
#         for win in win_list:
#             if win in num_list:
#                 match +=1
#         og_card = [win_list, num_list]
#         instance.append(og_card)
#         copies  = cards[i+1:match]
#         instance.append(copies)
#         scratchcards.append(instance)
# print(scratchcards)   
            
        
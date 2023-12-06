import re

# 0|1|2|3|4|5|6|7|8|9|
pattern = r'\d{1,2} green|\d{1,2} red|\d{1,2} blue'

class BagGamePart1:
    def __init__(self, red, green, blue, file):
        self.RED_MAX = red
        self.GREEN_MAX = green
        self.BLUE_MAX = blue
        self.INPUT = file

    def get_data(self, file):
        with open(file, 'r') as data:
            return data.readlines()

    def processed_data(self):
        info = self.get_data(self.INPUT)
        return list(map(lambda x: re.findall(pattern, x), info))

    def find_num_possible_games(self):
        count = 0
        for i, game in enumerate(self.processed_data()):
            nums_and_colors = list(map(lambda x: x.split(), game))
            poss_or_imposs = list(map(lambda x: 1\
                    if 'red' == x[1] and int(x[0]) < self.RED_MAX or \
                    'green' == x[1] and int(x[0]) < self.GREEN_MAX or \
                    'blue' == x[1] and int(x[0]) < self.BLUE_MAX else 0, nums_and_colors))
            if 0 not in poss_or_imposs:
                count += i+1
        return count 
        #     for cube in game:
        #         num, color = cube.split()
        #         if 'red' == color and int(num) < self.RED_MAX:
        #             count += 1
        #         elif 'green' == color and int(num) < self.GREEN_MAX:
        #             count += 1
        #         elif 'blue' == color and int(num) < self.BLUE_MAX:
        #             count +=1
        # return count

if __name__ == '__main__':
    bag_game = BagGamePart1(red=12, green=13, blue=14, file='aoc2.txt')
    print(bag_game.find_num_possible_games())

    # for line in file:
    #     game_cubes = re.findall(pattern, line)
    #     # cubes_and_colors = [cubes.split() for cubes in game_cubes]
    #     cubes_and_colors = list(map(lambda x: x.split(), game_cubes))
    #     for cubes in cubes_and_colors:
    #         pass
        # x, game_id = game.split()
        # info_list = info.split(';')
        # game_handful_list = []
        # for handful in info_list:
        #     handful = handful.strip(',').split()
        # win_num, my_num = line.split(' | ')
        # win_num = list(map(lambda x: int(x), win_num.split()))
        # my_num = list(map(lambda x: int(x), my_num.strip('\n').split()))
        # game = [win_num, my_num]
        # games.append(game)

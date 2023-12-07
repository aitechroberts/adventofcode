import time
start = time.time()
import re

'''
Today I am practicing using regex, OOP, and lambda functions
'''
pattern = r'\d{1,2} green|\d{1,2} red|\d{1,2} blue'

# easier regex pattern r'(\d+) (\w)'
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
            nums_and_colors = [(int(x.split()[0]), x.split()[1]) for x in game]
            poss_or_imposs = set(list(map(lambda draw: True \
                    if 'red' == draw[1] and draw[0] <= self.RED_MAX or \
                    'green' == draw[1] and draw[0] <= self.GREEN_MAX or \
                    'blue' == draw[1] and draw[0] <= self.BLUE_MAX else False, nums_and_colors)))
            if False not in poss_or_imposs:
                count += (i+1)
 
        return count 


    def find_game_set_powers(self):
        total_power = 0
        for game in self.processed_data():
            nums_and_colors = [(int(x.split()[0]), x.split()[1]) for x in game]
            power = {}
            for draw in nums_and_colors:  
                match draw[1]:
                    case 'red':
                        try: 
                            power['red'] = max(draw[0], power['red'])
                        except:
                            power['red'] = draw[0]
                    case 'green': 
                        try: 
                            power['green'] = max(draw[0], power['green'])
                        except:
                            power['green'] = draw[0]
                    case 'blue':
                        try: 
                            power['blue'] = max(draw[0], power['blue'])
                        except:
                            power['blue'] = draw[0]
            total_power += power['red'] * power['green'] * power['blue']
        return total_power
           

if __name__ == '__main__':
    bag_game = BagGamePart1(red=12, green=13, blue=14, file='aoc2.txt')
    print(bag_game.find_game_set_powers())
    print(time.time()-start)


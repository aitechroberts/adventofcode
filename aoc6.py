import re, time
from functools import reduce
start = time.time()
INPUT = 'aoc6.txt'
PATTERN = r'\d+|Time|Distance'

'''
More practice using OOP and functools.reduce this time
found that making the processed_data a property helped a ton

Also found that my get_possible_distances function 
was very useful as a helper function
'''
class Race:
    def __init__(self, file) -> None:
        self.INPUT = file
        self.data = self.processed_data()

    def get_data(self, file):
        with open(file, 'r') as file:
            return file.readlines()

    def processed_data(self):
        processed = {x[0]: [int(y) for y in x[1:]] for x in [re.findall(PATTERN, line) for line in self.get_data(self.INPUT)]}
        return processed

    def get_possible_distances(self, race_time:int):
        return [(race_time-hold_time)*hold_time for hold_time in range(race_time+1)]

    def get_num_ways_multiple_races(self):
        num_ways = []
        for i, time in enumerate(self.data['Time']):
            distances = self.get_possible_distances(time)
            ways = sum(list(map(lambda dist: 1 if dist > self.data['Distance'][i] else 0, distances)))
            num_ways.append(ways)
            # Use functools reduce and lambda to iteratively reduce a list wihtout for loop
        return reduce(lambda x, y: x*y, num_ways)
    
    def get_num_ways_one_big_race(self):
        total_time = int(reduce(lambda x, y: str(x) + str(y), self.data['Time']))
        total_dist = int(reduce(lambda x, y: str(x) + str(y), self.data['Distance']))
        poss_dist = self.get_possible_distances(total_time)
        ways = sum(list(map(lambda dist: 1 if dist > total_dist else 0, poss_dist)))
        return ways



if __name__ == '__main__':
    race = Race(file=INPUT)
    print(race.get_num_ways_one_big_race())
    # print(race.processed_data())
    # print(race.find_num_ways_to_beat_record())
    print(time.time()-start)

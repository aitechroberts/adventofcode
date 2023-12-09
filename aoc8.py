import re

INPUT = 'aoc8.txt'
PATTERN = r'\w+'
'''
Practice using OOP and ensuring separation of concerns

'''
class LandNav:
    def __init__(self, file) -> None:
        self.__INPUT = file
        self.__directions = self.get_directions()
        self.__dirs_dict = self.get_data_dict()


    def retrieve_data(self):
        with open(self.__INPUT, 'r') as file:
            raw_data = file.readlines()
        return raw_data
    
    def get_directions(self):
        return self.retrieve_data()[0].strip('\n')

    def get_data_dict(self):
        raw_data = self.retrieve_data()[1:]
        processed_data = {x: (y, z) for x, y, z in \
                          [re.findall(PATTERN, line) for line in raw_data]}
        return processed_data
    
    def follow_directions(self):
        dirs_dict = self.__dirs_dict.copy()
        steps_key = 'AAA'
        steps_counter = 0
        while steps_key != 'ZZZ':
            for dir in self.__directions:
                steps_counter += 1
                match dir:
                    case 'L':
                        steps_key = dirs_dict[steps_key][0]
                    case 'R':
                        steps_key = dirs_dict[steps_key][1]
                print(steps_key)
        return steps_counter

if __name__ == '__main__':
    ln = LandNav(file=INPUT)
    print(ln.get_directions())
    print(ln.get_data_dict())
    print(ln.follow_directions())

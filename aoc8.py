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
        self.__node_dict = self.get_data_dict()


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
        node_dict = self.__node_dict.copy()
        steps_key = 'AAA'
        steps_counter = 0
        while steps_key != 'ZZZ':
            for dir in self.__directions:
                steps_counter += 1
                match dir:
                    case 'L':
                        steps_key = node_dict[steps_key][0]
                    case 'R':
                        steps_key = node_dict[steps_key][1]
                print(steps_key)
        # while steps_key != 'ZZZ':
        #     for dir in self.__directions:
        #         steps_counter += 1
        #         match dir:
        #             case 'L':
        #                 steps_key = node_dict[steps_key][0]
        #             case 'R':
        #                 steps_key = node_dict[steps_key][1]
        #         print(steps_key)
        return steps_counter

    def get_ghost_start_point(self):
        return [key for key in list(self.__node_dict.keys()) if key[2] == 'A']

    def ghost_mode(self):
        '''
        This solution technically works, but it takes
        FAR too long.
        '''
        node_dict = self.__node_dict.copy()
        steps_node = self.get_ghost_start_point() # Sets start point at all nodes ending in 'A'
        steps_counter = 0
        dirs_counter = 0
        while not all(node.endswith('Z') for node in steps_node):
        # while steps_counter <6:
            for i, node in enumerate(steps_node):
                match self.__directions[dirs_counter]:
                    case 'L':
                        steps_node[i] = node_dict[node][0]
                    case 'R':
                        steps_node[i] = node_dict[node][1]
            dirs_counter += 1
            '''
            To start over with the directions and not cause
            an IndexError, the dirs_counter is reset to 0
            allowing me to iterate over the directions list
            using list indexing rather than a nested for loop
            which should at least be more readable
            '''
            if dirs_counter == len(self.__directions):
                dirs_counter = 0
            steps_counter += 1
            # if 'Z' in steps_node[0][2] and 'Z' in steps_node[1][2] or 'Z' in steps_node[2][2] and 'Z' in steps_node[3][2] or 'Z' in steps_node[4][2] and 'Z' in steps_node[5][2]:
            #     print(steps_node)
        return steps_counter

    def lcm_mode(self):
        pass

if __name__ == '__main__':
    ln = LandNav(file=INPUT)
    print(ln.get_directions())
    print(ln.get_data_dict())
    print(ln.get_ghost_start_point())
    print(ln.ghost_mode())

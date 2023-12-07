import re, time
start = time.time()
INPUT = 'aoc5.txt'
PATTERN = r'seeds|seed-to-soil map|soil-to-fertilizer map|fertilizer-to-water map|water-to-light map|light-to-temperature map|temperature-to-humidity map|humidity-to-location map|\d+'

'''
More practice using OOP and functools.reduce this time
found that making the processed_data a property helped a ton

Also found that my get_possible_distances function 
was very useful as a helper function
'''
class SeedMap:
    def __init__(self, file) -> None:
        self.__INPUT = file
        self.__data = self.get_processed_data()
        self.__seeds_dict = self.get_data_dict()
        self.__max_num = self.get_max_num()
        self.__max_list = [i for i in range(self.__max_num + 1)]
        self.__loc_map = self.build_location_maps()

    def retrieve_data(self, file):
        with open(file, 'r') as file:
            return file.readlines()

    def get_processed_data(self):
        processed_data = [re.findall(PATTERN, line) for line in self.retrieve_data(self.__INPUT)]
        filtered_data = [non_empty for non_empty in processed_data if non_empty]
        return filtered_data
    
    def get_max_num(self):
        data = self.get_processed_data()
        max_num = []
        for i, item in enumerate(data):
            if i == 0:
                max_num.append(max(item[1:]))
            if item[0].isdigit():
                max_num.append(max(item))
            else:
                pass
        return int(max(max_num))
    
    def get_data_dict(self):
        seeds_dict = {self.__data[0][0]: [int(seed) for seed in self.__data[0][1:]]}
        for i, item in enumerate(self.__data[1:], start=1):
            if not item[0].isdigit():
                seeds_dict[item[0]] = [[int(seed) for seed in self.__data[i+1]], [int(seed) for seed in self.__data[i+2]]]
            else:
                pass
        return seeds_dict

    def build_location_maps(self):
        loc_map = {}
        maps = list(self.__seeds_dict.keys())[1:]
        for key in maps:
            if key == 'seeds':
                loc_map['seeds'] = self.__seeds_dict['seeds']
            dest_range_start1 = self.__seeds_dict[key][0][0]
            dest_range_start2 = self.__seeds_dict[key][1][0]
            source_range_start1 = self.__seeds_dict[key][0][1]
            source_range_start2 = self.__seeds_dict[key][1][1]
            range_len1 = self.__seeds_dict[key][0][2]
            range_len2 = self.__seeds_dict[key][1][2]
            map_list = self.__max_list.copy()
            for i, x in enumerate(self.__max_list):
                if (dest_range_start1 + range_len1) >= x >= dest_range_start1:
                    map_list[source_range_start1 + (i - dest_range_start1)] = x
                elif (dest_range_start2 + range_len2) >= x >= dest_range_start2:
                    map_list[source_range_start2 + (i - dest_range_start1)] = x
                else:
                    pass
            loc_map[key] = map_list
        return loc_map

                 

if __name__ == '__main__':
    sm = SeedMap(file=INPUT)
    print(sm.build_location_maps())
    print(time.time()-start)
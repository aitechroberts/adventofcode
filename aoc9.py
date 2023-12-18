# from functools 
INPUT = 'aoc9.txt'
'''
Practice using OOP and ensuring separation of concerns

'''
class Histories:
    def __init__(self, file) -> None:
        self.__INPUT = file
        self.__hist_lists = self.retrieve_data()
        self.values = []

    def retrieve_data(self):
        with open(self.__INPUT, 'r') as file:
            raw_data = [[int(char) for char in line.split()] for line in file.readlines()]
        return raw_data

    def create_sequence_list(self, hist):
        # Creates a lower level sequence of differences from a list
        return [int(hist[i + 1]) - int(hist[i]) for i in range(len(hist) - 1)]
    
    def create_reverse_sequence(self, hist):
        # 
        return [int(hist[i + 1]) - int(hist[i]) for i in range(len(hist) - 1)]

    def find_extrapolated_values(self):
        hist_lists = self.__hist_lists.copy()
        vals_list = []
        # Iterate over history lists
        for hist in hist_lists:
            # Initiate list of sequences with history first
            list_of_seqs = [hist]
            # Create seq list for history
            sequence_list = self.create_sequence_list(hist)
            # Append to list of seqs
            list_of_seqs.append(sequence_list)
            # Continue until all items in seq_list are 0
            while not all(item == 0 for item in sequence_list):
                sequence_list = self.create_sequence_list(sequence_list)
                list_of_seqs.append(sequence_list)
            sequence_list = self.create_sequence_list(sequence_list)
            list_of_seqs.append(sequence_list)
            # reverse list_of_seqs just because I like ascending order
            list_of_seqs = list_of_seqs[::-1]
            print(list_of_seqs)
            # finding the sum of all last values, could be list comp maybe, but this is more readable
            for i in range(len(list_of_seqs) - 1):
                list_of_seqs[i+1].append(list_of_seqs[i + 1][-1] + list_of_seqs[i][-1])
            vals_list.append(list_of_seqs[-1][-1])
        print(sum(vals_list))
        return 
    
    def find_reverse_values(self):
        vals_list = []
        hist_lists = self.__hist_lists.copy()
        # Iterate over history lists
        for hist in hist_lists:
            # Initiate list of sequences with history first
            list_of_seqs = [hist]
            # Create seq list for history
            sequence_list = self.create_sequence_list(hist)
            # Append to list of seqs
            list_of_seqs.append(sequence_list)
            # Continue until all items in seq_list are 0
            while not all(item == 0 for item in sequence_list):
                sequence_list = self.create_sequence_list(sequence_list)
                list_of_seqs.append(sequence_list)
            # reverse list_of_seqs just because I like ascending order
            list_of_seqs = list_of_seqs[::-1]
            print(list_of_seqs)
            for i in range(len(list_of_seqs) - 1):
                if i == 0:
                    list_of_seqs[0].insert(0, 0)
                list_of_seqs[i+1].insert(0, list_of_seqs[i + 1][0] - list_of_seqs[i][0])
            vals_list.append(list_of_seqs[-1][0])
            print(list_of_seqs)
        print(vals_list)
        return sum(vals_list)
            


if __name__ == '__main__':
    history = Histories(file=INPUT)
    # print(all(item == 0 for item in [0,0,1,1,1]))
    # print(history.retrieve_data())
    print(history.find_reverse_values())
    # print(history.create_sequence_list(history.retrieve_data()[0]))
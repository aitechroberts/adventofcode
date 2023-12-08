INPUT = 'aoc7.txt'

'''
Practice using OOP and ensuring separation of concerns

'''
class CamelCards:
    def __init__(self, file, joker=False) -> None:
        self.__INPUT = file
        self.__cards_dict = self.get_data_dict()
        if joker:
            self.__card_ranking = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        else:
            self.__card_ranking = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.__rank_map = {char: index for index, char in enumerate(self.__card_ranking)}

    def retrieve_data(self, file):
        with open(file, 'r') as file:
            raw_data = file.readlines()
        processed_data = [line.strip('\n').split() for line in raw_data]
        # filtered_data only needed on testing data that doesn't have enough hands
        # filtered_data = [non_empty for non_empty in processed_data if non_empty]
        return processed_data
    
    def get_data_dict(self):
        return {hand: [int(bid)] for hand, bid in self.retrieve_data(self.__INPUT)}
    
    def process_hand(self, hand):
        '''
        This is a bit of a superfluous functinon which could
        be done inline in the identify_hand_types fn
        '''
        return [hand.count(item) for item in hand]

    def hand_sorter(self, hand):
        '''
        The sorted function takes a tuple so each hand is converted to a tuple
        where each char is assigned a value according to rank_map. Then, the 
        hands are sorted according to their tuple values where for example
        'KKK3K' = (12,12,12,1,12)
        '''
        return tuple(self.__rank_map[char] for char in hand if char in self.__rank_map)
        
    def identify_hand_types(self):
        hand_types = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': []}
        for hand in list(self.__cards_dict.keys()):
            hand_type = self.process_hand(hand)
            # Append to five of a kind rank
            if hand_type.count(5) in hand_type:
                hand_types['7'].append(hand)
            # Append to four of a kind rank
            elif hand_type.count(4) in hand_type:
                hand_types['6'].append(hand)
            # Append to full house rank
            elif sum(hand_type) == 13:
                hand_types['5'].append(hand)
            # Append to three of a kind rank
            elif hand_type.count(3) in hand_type:
                hand_types['4'].append(hand)
            # Append to 2 pair rank
            elif hand_type.count(2) == 4:
                hand_types['3'].append(hand)
            # Append to 1 pair rank
            elif hand_type.count(2) == 2:
                hand_types['2'].append(hand)
            # Append to high card rank
            else:
                hand_types['1'].append(hand)
        return hand_types
    
    def sort_ranks(self, hand_types):
        return {rank: sorted(hand_types[rank], key=lambda x: self.hand_sorter(x)) for rank in hand_types}

    def rank_hands(self, hand_types):
        cards_dict = self.__cards_dict.copy() # structure {hand: [bid]}
        length = []
        for rank in list(hand_types.keys()):
            if len(hand_types[rank]) != 0:
                    for i, hand in enumerate(hand_types[rank], start=1):
                        cards_dict[hand].append(i + sum(length)) # structure {hand: [bid]}
            length.append(len(hand_types[rank]))
        return cards_dict

    def get_total_winnings(self, ranked_hands):
        return sum(bid * rank for hand, (bid, rank) in ranked_hands.items())
        # return sum([ranked_hands[hand][0] * ranked_hands[hand][1] for hand in ranked_hands])

if __name__ == '__main__':
    cc = CamelCards(file=INPUT)
    print(cc.get_total_winnings(cc.rank_hands(cc.sort_ranks(cc.identify_hand_types()))))


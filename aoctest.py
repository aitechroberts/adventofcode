import re
nums = []
word_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine|']

with open('aoc1.txt', 'r') as file:
    for i, line in enumerate(file):
        line_nums = []
        words = []
        pattern = r'' + '|'.join(word_nums) + '|'.join(['1', '2', '3', '4', '5', '6', '7', '8', '9'])
        line_nums_re = re.findall(pattern, line)
        # print(line_nums_re)
        for item in line_nums_re:
            if item.isdigit():
                line_nums.append(int(item))
            else:
                match item:
                    case 'one':
                        num = 1
                        line_nums.append(num)
                    case 'two':
                        num = 2
                        line_nums.append(num)

                    case 'three':
                        num = 3
                        line_nums.append(num)

                    case 'four':
                        num = 4
                        line_nums.append(num)

                    case 'five':
                        num = 5
                        line_nums.append(num)

                    case 'six':
                        num = 6
                        line_nums.append(num)

                    case 'seven':
                        num = 7
                        line_nums.append(num)

                    case 'eight':
                        num = 8
                        line_nums.append(num)

                    case 'nine':
                        num = 9
                        line_nums.append(num)
    
    
        if len(line_nums) == 1:
            line_total = int(str(line_nums[0])*2)
            nums.append(line_total)
        elif len(line_nums) > 1:
            line_total = int(str(line_nums[0]) + str(line_nums[-1]))
            nums.append(line_total)
        else:
            pass
print(nums[777])
print(sum(nums))
lines = []
nums = []

string = '''
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''

with open('aoc3.txt', 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))
    for i, line in enumerate(lines):
        number = []
        
        for i, item in enumerate(line):
            if not item.isdigit() and item != '.':
                if line[i-3].isdigit() and line[i-2].isdigit() and line[i-1].isdigit():
                    number.append(line[i-2] + line[i-1])
                elif line[i-2].isdigit() and line[i-1].isdigit():
                    number.append(line[i-2] + line[i-1])
                elif line[i-1].isdigit():
                    number.append(line[i-1])
 
            if number:
                nums.append(int(''.join(number)))
                number = []
            else:
                number = []

    print(nums)
total = sum(nums)
print(total)
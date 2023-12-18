# ll = [x for x in open("aoc8.txt").read().strip().split('\n\n')]
# import math
# inst = list(ll[0])
# conn = {}
# for l in ll[1].split("\n"):
# 	a = l.split(" ")[0]
# 	b = l.split("(")[1].split(",")[0]
# 	c = l.split(" ")[3].split(")")[0]
# 	conn[a] = (b, c)
# pos = 'AAA'
# idx = 0
# while pos != 'ZZZ':
# 	d = inst[idx%len(inst)]
# 	pos = conn[pos][0 if d=='L' else 1]
# 	idx += 1
# print("p1", idx)
# def solvesteps(start):
# 	pos = start
# 	idx = 0
# 	while not pos.endswith('Z'):
# 		d = inst[idx%len(inst)]
# 		pos = conn[pos][0 if d=='L' else 1]
# 		idx += 1
# 	return idx
# ret = 1
# for start in conn:
# 	if start.endswith('A'):
# 		ret = math.lcm(ret, solvesteps(start))
# print("p2", ret)

import math

def read_input(file_path):
    """Reads the puzzle input from the file."""
    with open(file_path, 'r') as file:
        parts = file.read().strip().split('\n\n')
    return parts

def parse_connections(connections_list):
    """Parses the connections into a dictionary."""
    connections = {}
    for line in connections_list.split("\n"):
        node, (left, right) = line.split(" = ")
        connections[node] = (left.strip("()"), right.strip("()"))
    return connections

def follow_instructions(start_node, instructions, connections):
    """Follows the instructions from the start node and returns the number of steps."""
    position = start_node
    steps = 0
    while position != 'ZZZ':
        direction = instructions[steps % len(instructions)]
        position = connections[position][0 if direction == 'L' else 1]
        steps += 1
    return steps

def solve_part_2(connections, instructions):
    """Solves part 2 by finding the LCM of steps for each path starting with 'A'."""
    lcm_steps = 1
    for start_node in connections:
        if start_node.endswith('A'):
            steps = follow_instructions(start_node, instructions, connections)
            lcm_steps = math.lcm(lcm_steps, steps)
    return lcm_steps

# Read and parse the input
input_data = read_input("aoc8.txt")
instructions, connections_data = input_data[0], input_data[1]
connections = parse_connections(connections_data)

# Solve Part 1
steps_part_1 = follow_instructions('AAA', instructions, connections)
print("Part 1:", steps_part_1)

# Solve Part 2
steps_part_2 = solve_part_2(connections, instructions)
print("Part 2:", steps_part_2)

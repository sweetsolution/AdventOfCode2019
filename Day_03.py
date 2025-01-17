# Advent of Code 2019
# Day 3
# Part 1: 2025-01-12 Matthias Suess
# Part 2: 2025-01-17 Matthias Suess

import math
import re, sys
print("-- AdventOfCode 2019 Day 3 --")

def load(file):
  with open(file) as f:
    rows = f.read().strip().split('\n')
    return [row.split(',') for row in rows]

directions = load("input_day3.txt")

direction_delta={'R': 1+0j, 'L': -1+0j, 'U': 0+1j, 'D': 0+-1j}

def get_grid_elements(locations):
    position = complex(0, 0)
    stepcount = 0
    elements = {}
    for location in locations:
        direction = location[:1]
        length = int(location[1:])
        delta = direction_delta[direction]
        for _ in range(0, length):
            position += delta
            stepcount+=1
            elements[position] = stepcount
    return elements

## Part 1: Manhattan distance from the central port to the closest intersection
wire_1 = get_grid_elements(directions[0])
wire_2 = get_grid_elements(directions[1])
interset = set(wire_1.keys()).intersection(set(wire_2.keys()))
a = int(min([abs(elem.real)+abs(elem.imag) for elem in interset]))
print(f"Result part 1 = {a}")

## Part 2: Fewest combined steps the wires must take to reach an intersection
minimal_steps = sys.maxsize
for intersection in interset:
    stepcount_1 = wire_1[intersection]
    stepcount_2 = wire_2[intersection]
    minimal_steps = min(minimal_steps, (stepcount_1 + stepcount_2))

print(f"Result part 2 = {minimal_steps}")
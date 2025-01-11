# Advent of Code 2019
# Day 2
# 2025-01-11, Matthias Suess

import math
import re
print("-- AdventOfCode 2019 Day 2 --")

def load(file):
  with open(file) as f:
    return [int(e) for e in f.read().split(',')]

instructions = load("input_day2.txt")

def program(noun, verb, prog):
    pointer = 0
    prog[1] = noun
    prog[2] = verb
    while True:
        opcode = prog[pointer]
        if opcode == 99:
            break
        if opcode == 1:
            prog[prog[pointer+3]] = prog[prog[pointer+1]] + prog[prog[pointer+2]]
        elif opcode == 2:
            prog[prog[pointer+3]] = prog[prog[pointer+1]] * prog[prog[pointer+2]]
        else:
            print("Error, unknown opcode")
            break
        pointer += 4
    return prog[0]

## Part 1
print(f"Result part 1 = {program(12, 2, instructions.copy())}")

## Part 2 brute force
for noun in range(100):
   for verb in range(100):
      result = program(noun, verb, instructions.copy())
      if result ==19690720:
          print(f"Result part 2 = {100 * noun + verb}")
          break
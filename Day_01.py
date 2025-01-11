# Advent of Code 2019
# Day 1
# 2025-01-10, Matthias Suess

import math
import re
print("-- AdventOfCode 2019 Day 1 --")

def load(file):
  with open(file) as f:
    return [int(e) for e in f.read().split('\n')]

masses = load("input.txt")

## Part 1
result = sum([mass // 3 - 2 for mass in masses])
print(f"Result part 1 = {result}")

## Part 2
def caluclate_total_fuel(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + caluclate_total_fuel(fuel)

result = sum([caluclate_total_fuel(mass) for mass in masses])
print(f"Result part 1 = {result}")
     

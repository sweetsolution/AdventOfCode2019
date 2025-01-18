# Advent of Code 2019
# Day 4
# 2025-01-18 Matthias Suess


import math
import re, sys
print("-- AdventOfCode 2019 Day 4 --")

pattern_never_decrease = r'^0*1*2*3*4*5*6*7*8*9*$'
pattern_two_adjacent_digits = r'(\d)\1'
pattern_all_charcters_in_row = r'(\w)\1+'

def check_number(number):
  if re.match(pattern_never_decrease, str(number)) == None:
    return False
  return re.search(pattern_two_adjacent_digits, str(number)) != None

def check_numberPart2(number):
  found_groups = re.finditer(pattern_all_charcters_in_row, str(number))
  for found in found_groups:
    if found.span()[1]-found.span()[0] == 2:
      return True
  return False

## Part 1: How many different passwords
count = 0
for num in range(153517, 630395+1):
  erg = check_number(num)
  if erg == True:
    count+=1
print(f"Result part 1 = {count}")

## Part 2: How many different passwords
count = 0
for num in range(153517, 630395+1):
  erg = check_number(num)
  erg2 = check_numberPart2(num)
  if (erg == True) and (erg2==True):
    count+=1
print(f"Result part 2 = {count}")
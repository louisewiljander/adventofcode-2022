#------  DATA INPUT ZONE ------#
import string
input_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 3\input.txt", "r")
test_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 3\test.txt", "r")

rucksacks = input_file.read().splitlines()
test_rucksacks = test_file.read().splitlines()

######################## Task 1 ########################

#------ FUNCTIONS ------#

# Function to check for common items in rucksacks
def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    if (a_set & b_set):
        return a_set & b_set
    else:
        return "No common elements"

# Function to get priority value from rucksack item
def getPriority(item):
    lowercase_letters = dict()
    for index, letter in enumerate(string.ascii_lowercase):
        lowercase_letters[letter] = index + 1

    uppercase_letters = dict()
    for index, letter in enumerate(string.ascii_uppercase):
        uppercase_letters[letter] = index + 27

    if item.islower():
        return lowercase_letters[item]
    else:
        return uppercase_letters[item]

#------ RUNNING SOLUTION ------#
sum_priorities = 0

for i in rucksacks:
    half_length = len(i) // 2
    first_half, second_half = i[:half_length], i[half_length:]
    item = ', '.join(common_member(first_half, second_half))

    priority = getPriority(item)
    sum_priorities += priority

print(sum_priorities)

######################## Task 2 ########################

#------ FUNCTIONS ------#
def get_badge(a, b, c):
    a_set = set(a)
    b_set = set(b)
    c_set = set(c)

    if (a_set & b_set & c_set):
        return a_set & b_set & c_set
    else:
        return "No common elements"

#------ RUNNING SOLUTION ------#
sum_priorities = 0

# Split elves into groups of three
start = 0
end = len(rucksacks)
step = 3
for i in range(start, end, step):
    x = i
    elf_group = rucksacks[x:x+step]
    badge = ', '.join(get_badge(elf_group[0], elf_group[1], elf_group[2]))
    priority = getPriority(badge)
    sum_priorities += priority

print(sum_priorities)


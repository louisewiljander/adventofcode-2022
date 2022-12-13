#------  DATA INPUT ZONE ------#
input_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 5\input.txt", "r").read()
test_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 5\test.txt", "r")

input_file,instructions = input_file.split("\n\n")
input_file,instructions = input_file.splitlines(),instructions.splitlines()

crates = [""]*9

for i in range(len(input_file)-2, -1, -1):
    for a in range(1, len(input_file[0]), 4):
        if input_file[i][a].isupper():
            crates[a//4] += input_file[i][a]

test_instructions = test_file.read().splitlines()

test_crates = ["ZN", "MCD", "P"]

######################## Task 1 ########################

#------ RUNNING SOLUTION ------#
for line in instructions: # for each instruction
    a,b,c,d,e,f = line.split() # split the instructions in chunks to extract the numbers b (no of crates), d (from pile), f (to pile)
        
    # Assign number values to variables     
    nr_of_crates = int(b)
    source_pile, dest_pile = int(d)-1, int(f)-1

    # Move crate
    for i in range(nr_of_crates):
        crates[dest_pile] += crates[source_pile][-1]
        crates[source_pile] = crates[source_pile][:-1]

# Get the top crate of each pile
top_crates = ""
for x in crates:
    top_crates += x[-1]

print(top_crates)

######################## Task 2 ########################

#------ RUNNING SOLUTION ------#
crates = [""]*9

for i in range(len(input_file)-2, -1, -1):
    for a in range(1, len(input_file[0]), 4):
        if input_file[i][a].isupper():
            crates[a//4] += input_file[i][a]

for line in instructions: # for each instruction
    a,b,c,d,e,f = line.split() # split the instructions in chunks to extract the numbers b (no of crates), d (from pile), f (to pile)
    
    # Assign number values to variables     
    nr_of_crates = int(b)
    source_pile, dest_pile = int(d)-1, int(f)-1

    # Move crates
    pile = crates[source_pile][-nr_of_crates:]
    crates[dest_pile] += pile
    crates[source_pile] = crates[source_pile][:-nr_of_crates]

# Get the top crate of each pile
top_crates = ""
for x in crates:
    top_crates += x[-1]

print(top_crates)
    
#------  DATA INPUT ZONE ------#
input_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 4\input.txt", "r")
test_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 4\test.txt", "r")

assignment_pairs = input_file.read().splitlines()
test_pairs = test_file.read().splitlines()

######################## Task 1 ########################

#------ FUNCTIONS ------#


#------ RUNNING SOLUTION ------#
counter = 0

for i in assignment_pairs:    
    i = i.split(",")
    pair1 = i[0].split("-")
    a = int(pair1[0])
    b = int(pair1[1])
    pair2 = i[1].split("-")
    x = int(pair2[0])
    y = int(pair2[1])

    if a <= x and b >= y:
        counter += 1

    elif a >= x and b <= y:
        counter += 1

    else:
        continue

print(counter)

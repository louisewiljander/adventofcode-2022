# Opening data file in read mode
inputFile = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 1\input.txt", "r")

# Opening test file in readmode
testFile = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 1\test.txt", "r")

# Creating list of food items (calorie count) from file
data = inputFile.read().splitlines()
testData = testFile.read().splitlines()

# Create variable to represent elf
elf = 0

# Create variable to hold sum of calories of one elf's food items
elfCalSum = 0

# Create variable to hold the largest calorie sum
mostCalories = 0

################################# TASK 1 #################################

# Go through list and sum up all food items per elf, and then check if that sum is higher than the current highest calorie sum value
for i in testData:
    if i == '':
        elf += 1
        # print("Elf " + str(elf) + "is carrying " + str(elfCalSum) + " calories.")
        if elfCalSum > mostCalories:
            mostCalories = elfCalSum
            # print("The heaviest load is:" + str(mostCalories) + " calories.")
            elfCalSum = 0
        else:
            elfCalSum = 0
    else:
        elfCalSum += int(i)

# Printing mostCalories
print("mostCalories is: " + str(mostCalories))

################################# TASK 2 #################################

# Reset Calorie Sum variable 
elfCalSum = 0

# Create variables to hold top 3 calorie loads
top3List = [0,0,0]

def checkTopThree(sum, list):
    """
    Function to take a sum and update list of top 3 values

    """
    if sum > list[0]:
        list[2] = list[1]
        list[1] = list[0]
        list[0] = sum

    elif sum > list[1]:
        list[2] = list[1]
        list[1] = sum

    elif sum > list[2]:
        list[2] = sum
    
    return list

# Loop through data
for i in testData:
    if i == '':
        checkTopThree(elfCalSum, top3List)
        elfCalSum = 0

    elif i == testData[-1]:
        elfCalSum += int(i)
        checkTopThree(elfCalSum, top3List)
    
    else:
        elfCalSum += int(i)

sum = 0

for i in top3List:
    sum += i

print(top3List)
print(sum)
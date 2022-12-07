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
top1 = 0
top2 = 0
top3 = 0

"""
def checkTopThree(sum, top3List):
    if sum > var1:
        var3 = var2
        var2 = var1
        var1 = sum

    elif sum > var2:
        var3 = var2
        var2 = sum

    elif sum > var3:
        var3 = sum
"""

# Loop through data
for i in testData:
    if i == '':
        if elfCalSum > top1:
            top3 = top2
            top2 = top1
            top1 = elfCalSum

        elif elfCalSum > top2:
            top3 = top2
            top2 = elfCalSum

        elif elfCalSum > top3:
            top3 = elfCalSum

        elfCalSum = 0

    elif i == testData[-1]:
        elfCalSum += int(i)

        if elfCalSum > top1:
            top3 = top2
            top2 = top1
            top1 = elfCalSum

        elif elfCalSum > top2:
            top3 = top2
            top2 = elfCalSum

        elif elfCalSum > top3:
            top3 = elfCalSum
    
    else:
        elfCalSum += int(i)

print(top1)
print(top2)
print(top3)
print(top1+top2+top3)
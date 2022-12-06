# Opening file in read mode
inputFile = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 1\input.txt", "r")

# Creating list of food items (calorie count) from file
data = inputFile.read().splitlines()

# Create variable to represent elf
elf = 0

# Create variable to hold sum of calories of one elf's food items
elfCalSum = 0

# Create variable to hold the largest calorie sum
mostCalories = 0

for i in data:
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

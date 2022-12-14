#------  DATA INPUT ZONE ------#
input_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 6\input.txt", "r")
test_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 6\test.txt", "r")

subroutine = input_file.read()
test_subroutine = test_file.read()

######################## Task 1 ########################

#------ FUNCTIONS ------#
def isUniqueChars(string):
    x = ""

    for i in string:
        if i not in x:
            x += i
    
    if ( x==string):
        return True
    else:
        return False


#------ RUNNING SOLUTION ------#

letters_to_check = subroutine[0:3]
subroutine = subroutine[3:]

counter = 3

for i in subroutine:
    counter += 1
    letters_to_check = letters_to_check + i

    if isUniqueChars(letters_to_check):
        break

    else:
        letters_to_check = letters_to_check[1:]
        
print(counter)
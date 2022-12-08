#------  DATA INPUT ZONE ------#

#player_input = input("Player, choose your shape:")
#opponent_input = input("Opponent, choose your shape:")

input_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 2\input.txt", "r")
test_file = open(r"C:\Users\lwiljander\VS Code Lab\adventofcode-2022\adventofcode-2022\Day 2\test.txt", "r")

game = input_file.read().splitlines()
test_game = test_file.read().splitlines()

######################## Task 1 ########################

#------ FUNCTIONS ------#

# Function to convert encrypted hand value to shape
def checkShape(hand):
    switch = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }

    return switch.get(hand, "Wrong encryption input.")

# Function to convert shape to points
def shapeToPoints(shape):
    switch = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }

    return switch.get(shape, "Wrong shape input")

# A game round function generating a round result
def gameRound(player_input, opponent_input):
    player_hand = checkShape(player_input)
    opponent_hand = checkShape(opponent_input)

    round_result = ""

    if player_hand == opponent_hand:
        round_result = "Draw"

    elif player_hand == "Rock" and opponent_hand == "Scissors":
        round_result = "Win"

    elif player_hand == "Rock" and opponent_hand == "Paper":
        round_result = "Loss"

    elif player_hand == "Scissors" and opponent_hand == "Paper":
        round_result = "Win"

    elif player_hand == "Scissors" and opponent_hand == "Rock":
        round_result = "Loss"
    
    elif player_hand == "Paper" and opponent_hand == "Rock":
        round_result = "Win"
    
    elif player_hand == "Paper" and opponent_hand == "Scissors":
        round_result = "Loss"
    
    return round_result

# Function to convert round result to points
def resultToPoints(result):
    switch = {
        "Win": 6,
        "Draw": 3,
        "Loss": 0
    }

    return switch.get(result, "Wrong result input.")

#------ RUNNING SOLUTION ------#
points = 0

for i in game:
    opponent_hand = i[0]
    player_hand = i[2]

    player_shape = checkShape(player_hand)
    points += shapeToPoints(player_shape)

    result = gameRound(player_hand, opponent_hand)
    points += resultToPoints(result)

print(points)

######################## Task 2 ########################

#------ FUNCTIONS ------#
def checkStrategy(code):
    switch = {
        "X": "Loss",
        "Y": "Draw",
        "Z": "Win"
    }

    return switch.get(code, "Wrong strategy input.")

def pickLosingShape(opponent_shape):
    switch = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper"
    }

    return switch.get(opponent_shape, "Wrong shape input.")

def pickWinningShape(opponent_shape):
    switch = {
        "Rock": "Paper",
        "Paper": "Scissors",
        "Scissors": "Rock"
    }

    return switch.get(opponent_shape, "Wrong shape input.")

#------ RUNNING SOLUTION ------#
points = 0

for i in game:
    opponent_hand = i[0]
    inputStrategy = i[2]

    strategy = checkStrategy(inputStrategy)

    if strategy == "Loss":
        opponent_shape = checkShape(opponent_hand)
        player_shape = pickLosingShape(opponent_shape)
        points += shapeToPoints(player_shape)
        points += resultToPoints("Loss")

    elif strategy == "Win":
        opponent_shape = checkShape(opponent_hand)
        player_shape = pickWinningShape(opponent_shape)
        points += shapeToPoints(player_shape)
        points += resultToPoints("Win")
    
    elif strategy == "Draw":
        opponent_shape = checkShape(opponent_hand)
        player_shape = opponent_shape
        points += shapeToPoints(player_shape)
        points += resultToPoints("Draw")

print(points)

#------ TEST/PRINTING AREA ------#

#print(test_game)

#print(checkShape(player_input))
#print(shapeToPoints(checkShape(player_input)))

#print(checkShape(opponent_input))
#print(shapeToPoints(checkShape(opponent_input)))

#round_result = gameRound(player_input, opponent_input)
#print(round_result)

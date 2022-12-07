######################## Task 1 ########################

# Player input
player_input = input("Player, choose your shape:")
opponent_input = input("Opponent, choose your shape:")

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

    return switch.get(hand, "Wrong input.")

def checkShapePoints(hand):
    switch = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors"
    }

    return switch.get(hand, "Wrong input.")

# Function to convert shape to points
def shapeToPoints(shape):
    switch = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3
    }

    return switch.get(shape, "Wrong input")

# A round of Rock, Paper, Scissors
def gameRound(player_input, opponent_input):
    player_hand = checkShape(player_input)
    opponent_hand = checkShape(opponent_input)

    round_result = ""

    if player_hand == opponent_hand:
        round_result = "Draw"

    elif player_hand == "Rock" and opponent_hand == "Scissors":
        round_result = "Win"

    elif player_hand == "Scissors" and opponent_hand == "Paper":
        round_result = "Win"
    
    elif player_hand == "Paper" and opponent_hand == "Rock":
        round_result = "Win"

    elif player_hand == "Rock" and opponent_hand == "Scissors":
        round_result = "Win"
    
    elif player_hand == "Rock" and opponent_hand == "Scissors":
        round_result = "Win"
    
    elif player_hand == "Rock" and opponent_hand == "Scissors":
        round_result = "Win"

# Testing solution
print(checkShape(player1))
print(shapeToPoints(checkShape(player1)))
print(checkShape(player2))
print(shapeToPoints(checkShape(player2)))



        

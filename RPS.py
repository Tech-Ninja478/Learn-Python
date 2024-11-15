import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")

print("Welcome to Rock, Paper, Scissors!")
playerchoice = input("Enter the following: \n1 For Rock\n2 For Paper\n3 For Scissors\n\n")

player = int(playerchoice)

if player < 1 | player > 3:
    sys.exit("Please enter value from 1, 2 or 3")

computerchoice = random.choice("123")

computer = int(computerchoice)

print("")

print("You chose " + str(RPS(player)).replace('RPS.', "") + ".")
print("Computer chose " + str(RPS(computer)).replace('RPS.', "") + ".")

print("")

if player == 1 and computer == 3:
    print("🎉Player Wins!")
elif player == 2 and computer == 1:
    print("🎉Player Wins!")
elif player == 3 and computer == 2:
    print("🎉Player Wins!")
elif player == computer:
    print("Tie Game 😮")
else:
    print("💻 Computer Wins!")

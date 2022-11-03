# WORK CITED 
# Excersies Day 8 
# https://realpython.com/python-rock-paper-scissors/ 

from random import randint, random 
while True: 
# returns an intenger # from the selected element from the specific range 
    print ("Hello User! Let's play rock/paper/scissors!")
# displays word into terminal 
    user = input("Enter your option of (rock, paper, or scissors): ") 
# allows for user input 
    while (user != "rock" and user != "paper" and user != "scissors"):
        user = input("choose your fate")
# sets aside a block of code, to be repeated until the condition is falsified 
# can only put the selected option, if they don't, the game will keep going on until they select a choice 
    myList = ["rock", "paper", "scissors"]
# can store any type of value inside the "list"
    def randChoice(): 
        return(myList[randint(0,len(myList)-1)])
# returns randonly selected element from the specific sequence 
# from the specific integers specified (ex. 0,2)

    mrcomputer = randChoice()

# runs without any conditions until the break statement executed inside the loop
    if user == mrcomputer:
        print(f"Both players selected {user}. IT'S A TIEEEEE!!!!")
    elif user == "rock":
        if mrcomputer == "scissors":
            print("Rock SMASHES scissors! YOU WINNNNNN!")
        else:
            print("Paper COVERS rock! You LOSEEEE.")
    elif user == "paper":
        if mrcomputer == "rock":
            print("Paper COVERS rock! You WINNNNN!")
        else:
            print("Scissors CUTSSSSS paper! You LOSEEEEE.")
    elif user == "scissors":
        if mrcomputer == "paper":
            print("Scissors CUTSSSSS paper! You WINNNNN!")
        else:
            print("Rock SMASHES scissors! You LOSEEEEE.")
# loop - to check if the player wants to play again or break the loop if they don't want to 
    play_again = input("Play again (come onnnn)? (yes/no): ")
    if play_again.lower() != "yes":
        print("thanks for playing")
        break   
    
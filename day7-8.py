from random import randint 

myList = ["one", "two", "three"]
print(myList[randint(0, len(myList)-1)])


from random import randint

print("Hello Player 1!") 
# Question = input("Let's play.").lower()
    # https://www.codegrepper.com/code-examples/python/how+to+make+a+yes+or+no+question+in+python
    # Yes or No question
myList = ["rock", "paper", "scissors"]
while True: 
    computer = myList[randint(0,2)]
    player = input("rock, paper, or scissors?").lower()


    # if player == "rock": 
    # print ("AI has beat you with Paper") 

# playerChoice = input ("Choose either rock, paper, or scissors.")
# computerchoice = random.choice(choices)
# player = None 
# while player not in choices: 
    # player == input("rock paper or scissors?")
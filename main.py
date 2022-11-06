from getpass import getpass as input
import time

print("Welcome to the epic 2 player game of 🪨  📄 ✂️")
print()
print("If you manage to break the code and an error message displays, please inbox me and I will fix the error. Your feedback is highly appreciated. Enjoy the game!")
print()
print("""Rock wins against scissors; 
paper wins against rock; 
and scissors wins against paper. 
If both players throw the same hand signal, it is considered a tie, and play resumes until there is a clear winner""")
print()
print("""Please enter R, P, or S for rock, paper, or scissors and then press enter. 
Each player cannot see what the other player typed in 😉.
Type in your answer and press enter.""")
print()

guessList = ['rock', 'paper', 'scissors', 'r', 'p', 's']

def endGame():
  while True:
    x= input("""Thank you for playing 🪨  📄 ✂️  !
To play again please click Stop on top right page and click Run """)
    print()
    continue


def getPlayer1Name():
  print("Player1: ")
  while True:
    name = input("What is your name?: ")
    print()
    if name.isnumeric() == True:
      print()
      print("Please enter your real name not numbers.")
      print()
      continue
    else:
      return name


def getPlayer2Name():
  print("Player2: ")
  while True:
    name = input("What is your name?: ")
    print()
    if name.isnumeric() == True:
      print()
      print("Please enter your real name not numbers.")
      print()
      continue
    else:
      return name


def getPlayer1Guess(player1):
  print(player1.upper())
  while True:
    guess1 = input("R, P, or S?: ")
    print()
    if guess1.lower() in guessList:  
      return guess1
    else:
      print()
      print("Please enter R, P, or S for Rock, Paper or Scissors .")
      print()
      continue


def getPlayer2Guess(player2):
  print(player2.upper())
  while True:
    guess2 = input("R, P, or S?: ")
    print()
    if guess2.lower() in guessList: 
      return guess2
    else:
      print()
      print("Please enter R, P, or S for Rock, Paper or Scissors .")
      print()
      continue
      
def displayWinner(guess1, guess2, player1, player2):
  r = ['rock', 'r']
  p = ['paper', 'p']
  s = ['scissors', 's']
  if guess1 in r and guess2 in s:
    print()
    print(player1,"wins! Rock wins against scissors.")
    print()
  elif guess1 in p and guess2 in r:
    print()
    print(player1,"wins! Paper wins against rock.")
    print() 
  elif guess1 in s and guess2 in p:
    print()
    print(player1,"wins! Scissors wins against paper.")
    print()  
  elif guess1 == guess2:
    print()
    print("Its a tie! Please continue playing until a winner is decided.")
    print() 
    while True:
      guess1 = getPlayer1Guess(player1)
      guess2 = getPlayer2Guess(player2)
      if guess1 == guess2:
        print("Its a tie! Please continue playing until a winner is decided.")
        continue
      else:
        displayWinner(guess1, guess2, player1, player2)
        break
        
      
  elif guess2 in r and guess1 in s:
    print()
    print(player1,"wins! Rock wins against scissors.")
    print()
  elif guess2 in p and guess1 in r:
    print()
    print(player2,"wins! Paper wins against rock.")
    print() 
  elif guess2 in s and guess1 in p:
    print()
    print(player2,"wins! Scissors wins against paper.")
    print()   

player1 = getPlayer1Name()
player2 = getPlayer2Name()
count = 0
while True:
  count+=1
  if count < 4:
    guess1 = getPlayer1Guess(player1)
    guess2 = getPlayer2Guess(player2)
    displayWinner(guess1, guess2, player1, player2)
    
    print("Round",count)
    print()
  
  exit = input("Would like to exit? ")
  if exit.lower() == 'yes':
    
    
    
  
  
  


if __name__ == "__main__":
  endGame()

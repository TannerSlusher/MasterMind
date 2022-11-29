#Tanner Slusher 2/16/22

import random

#This is the list that the program randomly chooses from.
colors = ["Blue", "Red", "Green", "Yellow"]

#This is the code segment that compares the user guess with the actual answer and gives the user feedback on how correct they are. 
def compare(color1,color2,x,y,z):
    if color1 == color2:
        print("That is the correct color and correct position.")
    elif color1 != color2 and secretCode[x] == color2:
        print("That is a correct color but not the correct position.")
    elif color1 != color2 and secretCode[y] == color2:
        print("That is a correct color but not the correct position.")
    elif color1 != color2 and secretCode[z] == color2:
        print("That is a correct color but not the correct position.")
    elif color1 != color2 and secretCode[x] != color2 and secretCode[y] != color2 and secretCode[z] != color2 and colors[1] != color2 and colors[0] != color2 and colors[2] != color2 and colors[3] != color2:
      print("That is either not a valid color or not a color at all")
    else:
        print("That is not the correct color or position.")

#These lines of code set the random choice to values. They then add the values to a list.
true_color1 = random.choice(colors)
true_color2 = random.choice(colors)
true_color3 = random.choice(colors)
true_color4 = random.choice(colors)
secretCode = []
secretCode.append(true_color1)
secretCode.append(true_color2)
secretCode.append(true_color3)
secretCode.append(true_color4)

#This is the list that holds user's four answers.
color_guess = []

#This the introduction of the program and what it does.
print("This is a program which is a recreation of a board game called MasterMind. The user is to guess a secret code of colors made randomly by this program. The program will then ask the user for a color at a time and give the user feedback on how correct they are. After they figure it out or fail ten times, they will be given a message to tell how they did and what the code was.")

#This tells the user their color choices.
print("Your color choices are blue, red, green, and yellow. \n \n")

#This is the holder of how many are the guesses the user has done
count = 1

#This is the variable of how tries the user did.
tries = 0

#This is the code thats asks for the colors, compares them, and keeps count of tries
while count <= 10:
  guess1 = input("What color is the first position? ")
  guess1 = guess1.capitalize()
  compare(true_color1,guess1,1,2,3)
  color_guess.append(guess1)
  print("\n")

  guess2 = input("What color is the second position? ")
  guess2 = guess2.capitalize()
  compare(true_color2,guess2,0,2,3)
  color_guess.append(guess2)
  print("\n")

  guess3 = input("What color is the third position? ")
  guess3 = guess3.capitalize()
  compare(true_color3,guess3,0,1,3)
  color_guess.append(guess3)
  print("\n")

  guess4 = input("What color is the fourth position? ")
  guess4 = guess4.capitalize()
  compare(true_color4,guess4,0,1,2)
  color_guess.append(guess4)
  print("\n")

  tries = tries + 1

  #The following lines decide whether they have figure it or have to keep on going
  if color_guess == secretCode:
    count = 11
  else:
    count = count + 1

  #This takes everything from the list of color guesses so the user can try again  
  for i in range(4):
    color_guess.pop()

print("\n\n")

#Tells the user the secret code
print("The secret code was " + str(secretCode) + "\n")

#Gives feedback on how well the user did
if tries == 1:
  print("It took you " + str(tries) + " try to crack the secret code. You're an amazing guesser but let's see if you can do it again.")
elif tries > 1 and tries <= 6:
  print("It took you " + str(tries) + " tries to crack the secret code. You did a good job.")
else: 
  print("It took you " + str(tries) + " tries to crack the secret code. You will do better next time.")

#This asks if the user wants to play again
answer = input("Do you wish to play again? ")
answer = answer.capitalize()

#If the user says yes then it will continuously repeat

while answer == "Yes":
  #These lines of code set the random choice to values. They then add the values to a list.
  true_color1 = random.choice(colors)
  true_color2 = random.choice(colors)
  true_color3 = random.choice(colors)
  true_color4 = random.choice(colors)
  secretCode = []
  secretCode.append(true_color1)
  secretCode.append(true_color2)
  secretCode.append(true_color3)
  secretCode.append(true_color4)

  #This is the list that holds user's four answers.
  color_guess = []

  #This tells the user their color choices.
  print("Your color choices are blue, red, green, and yellow. \n \n")

  #This is the holder of how many is the guesses run
  count = 1

  #This the variable of how tries the user did.
  tries = 0

  #This the code thats asks for the colors, compares     them, and keeps count of tries
  while count <= 10:
    guess1 = input("What color is the first position? ")
    guess1 = guess1.capitalize()
    compare(true_color1,guess1,1,2,3)
    color_guess.append(guess1)
    print("\n")

    guess2 = input("What color is the second position? ")
    guess2 = guess2.capitalize()
    compare(true_color2,guess2,0,2,3)
    color_guess.append(guess2)
    print("\n")

    guess3 = input("What color is the third position? ")
    guess3 = guess3.capitalize()
    compare(true_color3,guess3,0,1,3)
    color_guess.append(guess3)
    print("\n")

    guess4 = input("What color is the fourth position? ")
    guess4 = guess4.capitalize()
    compare(true_color4,guess4,0,1,2)
    color_guess.append(guess4)
    print("\n")

    tries = tries + 1

    #The following lines decide whether they have figure it or have to keep on going
    if color_guess == secretCode:
      count = 11
    else:
      count = count + 1

  #This takes everything from the list of color guesses so the user can try again  
    for i in range(4):
      color_guess.pop()

  print("\n\n")

  #Tells the user the secret code
  print("The secret code was " + str(secretCode) + "\n")

  #Gives feedback on how well the user did
  if tries == 1:
    print("It took you " + str(tries) + " try to crack the secret code. You're an amazing guesser but let's see if you can do it again.")
  elif tries > 1 or tries <= 6:
    print("It took you " + str(tries) + " tries to crack the secret code. You did a good job.")
  else: 
    print("It took you " + str(tries) + " tries to crack the secret code. You will do better next time.")
  
  print("\n \n")

  #This asks if the user wants to play again
  answer = input("Do you wish to play again? ") 
  answer = answer.capitalize()

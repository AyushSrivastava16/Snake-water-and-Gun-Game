import time
initial = time.time()




print("You have 10 Chances and the among you and your computer who scores more will win.\n")
nogu = 10
i = 1
yom = 0
cmpm = 0

while (i <= nogu) :

  bo = f"Number Of Rounds = {i}\n"
  print(bo)
  choices = ["Snake", "Water", "Gun"]
  import random
  computer_Choice = random.choice(choices)


  print("You have to select from Snake, Water and Gun.\n")
  print("Type 1 to choose Snake, 2 for Water and 3 for Gun.\n" )
  your_Choice = int(input())
  print("\n")
  print("----------------------------------------------------------------------------------------------------------------------")


  if your_Choice == 1 :
    print(f"Your Choice is Snake and computer guess is {computer_Choice}\n")

  elif your_Choice == 2 :
    print(f"Your Choice is Water and computer guess is {computer_Choice}\n")

  elif your_Choice == 3 :
    print(f"Your Choice is Gun and computer guess is {computer_Choice}\n")




  else :
    print("Error Invalid Input")


  
  if computer_Choice == "Snake" and your_Choice == 1 :
    print("Nobody won, You both guessed the Same\n")

    print("Tie both got zero point this round.\n")
  
  elif computer_Choice == "Water" and your_Choice == 1 :
    print("You won this round.\n")

    yom = yom + 1
    

  elif computer_Choice == "Gun" and your_Choice == 1 :
    print("Computer Wins this round.\n")

    cmpm = cmpm + 1





  elif computer_Choice == "Snake" and your_Choice == 2 :
    print("Computer wins this round.\n")

    cmpm = cmpm + 1

  elif computer_Choice == "Water" and your_Choice == 2 :
    print("Nobody won, You both guessed the Same\n")

    print("Tie both got zero point in this round.\n")

  elif computer_Choice == "Gun" and your_Choice == 2 :
    print("You won this round.\n")
    yom = yom + 1

  





  elif computer_Choice == "Snake" and your_Choice == 3 :
    print("You won this round. \n")
    yom = yom + 1
  
  elif computer_Choice == "Water" and your_Choice == 3 :
    print("Computer wins this round. \n")

    cmpm = cmpm + 1

  elif computer_Choice == "Gun" and your_Choice == 3 :
    print("Nobody won, You both guessed the Same")
    print("Both got zero point in this round.\n")

  




  else :
    print("Invalid")

  


  



  i = i+1


  user_point = f"Your point = {yom}"
  computer_point = f"Computer point = {cmpm}\n"


  print(user_point)
  print(computer_point)
  

  print("\n")

print("Game Over.\n")
if yom > cmpm :
  print("Congratulations, You won")

elif yom < cmpm :
  print("You Lose, Computer wins.")

elif yom == cmpm :
  print("Game Tied.")
print("\n")
print("\n")
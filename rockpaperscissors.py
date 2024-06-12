import random
Rock ="""
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper="""

   _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list=[Paper,Rock,Scissors]
nums=len(list)
random_choice=random.randint(0,nums-1)
computer_choice=list[random_choice]
your_choice=int(input("Press 0 for Paper, Press 1 for Rock, Press 2 for Scissors.\n"))
your_outcome=list[your_choice]
print("You choice is : \n")
print(your_outcome)
print("Computer Choice is :\n")
print(computer_choice)
if(your_outcome==list[0] and computer_choice==list[0]):
    print("Match Drawn")
if(your_outcome==list[1] and computer_choice==list[1]):
    print("Match Drawn")
if(your_outcome==list[2] and computer_choice==list[2]):
    print("Match Drawn")
if(your_outcome==list[0] and computer_choice==list[1]):
    print("You Outsmarted Computer.")
if(your_outcome==list[0] and computer_choice==list[2]):
    print("OOPS! Better luck next time.")
if(your_outcome==list[1] and computer_choice==list[0]):
    print("OOPS! Better luck next time.")
if(your_outcome==list[1] and computer_choice==list[2]):
    print("You Outsmarted Computer.")
if(your_outcome==list[2] and computer_choice==list[0]):
    print("You Outsmarted Computer.")
if(your_outcome==list[2] and computer_choice==list[1]):
    print("OOPS! Better luck next time.")

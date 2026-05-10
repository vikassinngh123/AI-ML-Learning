'''
simple Rock , Paper and Scissors Logic
Uses basics python function like input , random logics , while/if loops etc.

'''
import random
import time

def play_game():
  print('We are Playing Rock(🪨),Paper(📄) and Scissors(✂️)')
  print("\nYour Options \n 🪨 : 1 \n 📄 : 2 \n ✂️ : 3")
  time.sleep(1)

  #score traker variable
  user_win=0
  computer_win=0
  draw=0

  #dict for maping num to emojis
  dict_option={1:"🪨" , 2:"📄" , 3:"✂️"}


  while True:
    try:
      #user choice
      User_input=int(input("\nEnter Your choice : "))

      if User_input not in dict_option:
              print("\nInvalid choice! Please enter 1, 2, or 3.")
              continue

      #computer choise
      computer_input=random.randint(1,3)

      print(f"Computer -> {dict_option[computer_input]} V/S Your's -> {dict_option[User_input]}")
      time.sleep(1)

      #Win Logic
      if computer_input==User_input :
        print("\nDRAW")
        draw+=1
      elif (computer_input==1 and User_input==2) or (computer_input==2 and User_input==3) or (computer_input==3 and User_input==1) :
        print("\nYou Win")
        user_win+=1
      else:
        print("\nComputer Win")
        computer_win+=1

      #Score
      print(f"\nScore \n User:{user_win} \n Computer:{computer_win} \n Draw:{draw}")
      print("Good Game")
      time.sleep(1)

      # continue or break logic
      play_more=input("\nWant to play more (y/n) : ").lower()
      time.sleep(1)
      if play_more=="n":
        print("\nThanks for playing! ")
        break

    except ValueError:
      print("Please enter a number,not text")


if __name__=="__main__":
  play_game()


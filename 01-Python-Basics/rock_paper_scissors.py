'''
simple Rock , Paper and Scissors Logic
Uses basics python input , random logics

'''
import random
import time
import json
import os

SCORE_FILE="score.json"

def load_scores():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            return json.load(f)
    return {"user": 0 , "computer": 0}

def save_scores(scores):
    with open(SCORE_FILE, "w") as f:
        json.dump(scores, f)

def play_game():
  print('We are Playing Rock(🪨),Paper(📄) and Scissors(✂️)')
  print("\nYour Options \n 🪨 : 1 \n 📄 : 2 \n ✂️ : 3")
  time.sleep(1)

  #local score traker variable
  user_win=0
  computer_win=0
  draw=0

  #Universal score traker
  scores=load_scores()
  print(f"\nUniversal Score \n User:{scores['user']} \n Computer:{scores['computer']}")
  time.sleep(1)
  #dict for maping num to emojis
  dict_option={1:"🪨" , 2:"📄" , 3:"✂️"}


  while True:
    try:
      #user choice
      User_input=int(input("\nEnter Your choice : "))

      if User_input not in dict_option:
              print("\nInvalid choice! Please enter 1, 2, or 3.")
              break

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

        scores["user"] += 1
        save_scores(scores)

      else:
        print("\nComputer Win")
        computer_win+=1

        scores["computer"] += 1
        save_scores(scores)


      # continue or break logic
      play_more=input("\nWant to play more (y/n) : ").lower()
      time.sleep(1)
      if play_more=="n":
        print("\nThanks for playing! ")
        print(f"\nYour Score \n User:{user_win} \n Computer:{computer_win} \n Draw:{draw}")
        time.sleep(1)
        print(f"\nUniversal Score \n User:{scores['user']} \n Computer:{scores['computer']}")
        time.sleep(1)
        break

    except ValueError:
      print("Please enter a number,not text")


if __name__=="__main":
  play_game()


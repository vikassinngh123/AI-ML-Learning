"""
Guess the Number Game
Description: A multi-mode interactive guessing game featuring:
             1. User vs. Computer (Standard)
             2. Computer vs. User (Randomized Search)
             3. User 1 vs. User 2 (Local Multiplayer)
Features: Input validation, score tracking, and dramatic timing effects
"""

import random
import time

def is_input_valid(mini=None,maxi=None,msg="input"):
  while True:
    try:
      value=int(input(f"{msg}"))
      if mini<=value<=maxi:
          return value
      else:
          print(f"Invalid Input enter a value between {mini} and {maxi}")
    except ValueError:
        print("invalid Input! please enter a number not text.")

def Guess_game():
  print("This is a guessing game")

  while True:
    pick_gamemode=is_input_valid(1,3,'Choice \n 1-User V/s Computer\n 2-Computer V/s User \n 3-User_1 V/s User_2 \n Enter you pick : ')

    # Gamemode User V/S Computer
    if pick_gamemode==1:

      Score=1

      print("Computer is picking a number b/w 1-100")

      print('.' ,end=" ",flush=True)
      time.sleep(0.7)
      print('.',end=" ",flush=True)
      time.sleep(0.6)
      print('.',end=" ",flush=True)
      time.sleep(0.7)

      computer_pick=random.randint(1,100)

      user_guess=is_input_valid(1,100,"Enter you guess(1-100) : ")
      
      while user_guess!=computer_pick:
        
        if user_guess>computer_pick :
          Score+=1
          print("Pick a lower number")
        else:
          Score+=1
          print("Pick a higher number")

        user_guess=is_input_valid(1,100,"Enter you guess(1-100) : ")

      print(f"\nCongrats \nYou have guessed the number {computer_pick} in {Score} guesses")

    # Gamemode Computer V/s User
    if pick_gamemode==2:
      computer_score=1

      print("\nYou will be seeing guessing a number you choice")
      user_pick_number=is_input_valid(1,100,'\nEnter a number(1-100) : ')

      computer_guess=random.randint(1,100)
      print(f"\nComputer has picked {computer_guess}")
      min_bound=1
      max_bound=100
      
      while computer_guess!=user_pick_number:
    
        if computer_guess>user_pick_number :
          computer_score+=1
          print("\nComputer pick a lower number")
          max_bound=computer_guess-1
          computer_guess=random.randint(min_bound,max_bound)
          time.sleep(0.5)
          print(f"\nComputer has picked {computer_guess}")
          time.sleep(0.5)

        else:
          computer_score+=1
          print("Computer pick a higher number")
          min_bound=computer_guess+1
          computer_guess = random.randint(min_bound, max_bound)
          time.sleep(0.5)
          print(f"Computer has picked {computer_guess}")
          time.sleep(0.5)

      print(f"\nCongrats \n Computer has guessed the number {user_pick_number} in {computer_score} guesses")

    # Gamemode User_1 V/s User_2
    if pick_gamemode==3:
      user_1_score=1
      user_2_score=1
      print("\nFirst User_1 will be picking a number b/w 1-100")
      print("\nThen User_2 will be picking a number b/w 1-100")

      user_1_pick=is_input_valid(1,100,'\nUser_1 Enter a number(1-100) : ')
      user_2_pick=is_input_valid(1,100,'\nUser_2 Enter a number(1-100) : ')

      while True:
        user_1_guess=is_input_valid(1,100,'\nUser_1 Enter your guess(1-100) : ')
        if user_1_guess==user_2_pick:
          print(f"\nCongrats \nUser_1 has guessed the number {user_2_pick} in {user_1_score} guesses")
          break

        user_2_guess=is_input_valid(1,100,'\nUser_2 Enter your guess(1-100) : ')

        if user_2_guess==user_1_pick:
          print(f"\nCongrats \nUser_2 has guessed the number {user_1_pick} in {user_2_score} guesses")
          break
        
        if user_1_guess>user_2_pick:
          user_1_score+=1
          print("\nUser_1 pick a higher number")
        else:
          user_1_score+=1
          print("\nUser_1 pick a lower number")

        if user_2_guess>user_1_pick:
          user_2_score+=1
          print("\nUser_2 pick a higher number")
        else:
          user_2_score+=1
          print("\nUser_2 pick a lower number")

    print('\nWant to Play more ?')
    play_more=is_input_valid(1,2,'\n 1-Yes 2-No : ')
    if play_more==2:
      break

if __name__=="__main__":
  Guess_game()

'''
Slot Machine Simulator (Casino Suite)
-------------------------------------
Features:
- 3-Reel weighted probability logic (64 stops per reel).
- Interactive betting system with balance tracking.
- Automated input validation for secure betting.
- Symbolic payout system for Emojis (Jackpots, Multipliers).
'''

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


def slot_machine():

  reel_1=(["❌"] * 30) + (["🍒"] * 16) + (["💵"] * 9) + (["🪙"] * 5) + (["💰"] * 3) + (["7️⃣"] * 1)
  reel_2=(["❌"] * 30) + (["🍒"] * 16) + (["💵"] * 9) + (["🪙"] * 5) + (["💰"] * 3) + (["7️⃣"] * 1)
  reel_3=(["❌"] * 30) + (["🍒"] * 16) + (["💵"] * 9) + (["🪙"] * 5) + (["💰"] * 3) + (["7️⃣"] * 1)
     

  print(f"Max money limit : 10000000 ")
  money=is_input_valid(0,10000000,"Enter Your starting money : ")

  while money>=10:
    

    #----Get User Bet----
    print(f"\nCurrent Balance : ${money}")

    bet=is_input_valid(10,money,"Enter your bet(Min 10) : ")

    money=money-bet
    time.sleep(1)


    #-----Spin Result----
    stop_r_1=random.choice(reel_1)
    stop_r_2=random.choice(reel_2)
    stop_r_3=random.choice(reel_3)

    result=(stop_r_1,stop_r_2,stop_r_3)

    print("Spinning....")
    time.sleep(1)


    #----Animated Display----
    print(f"[{result[0]}]", end=" ", flush=True)
    time.sleep(0.7)
    print(f"[{result[1]}]", end=" ", flush=True)
    time.sleep(0.7)
    print(f"[{result[2]}]")
    time.sleep(0.5)

    
    #----Win Logic----
    win=0
    if result[0]==result[1]==result[2]=="7️⃣":
      print("🎉 JACKPOT! 🎉")
      win=bet*1000
    elif result[0]==result[1]==result[2]=="💰" :
      print("🎉 FANTASTIC WIN!!! 🎉")
      win=bet*150
    elif result[0]==result[1]==result[2]=="🪙" :
      print("🎉 RAINING GOLD!!! 🎉")
      win=bet*60
    elif result[0]==result[1]==result[2]=="💵" :
      print("🎉 BIG WIN!!! 🎉")
      win=bet*40
    elif result[0]==result[1]==result[2]=="🍒" :
      print("🎉 WIN!! 🎉")
      win=bet*10
    elif result.count("🍒")==2:
      print("🎉 Small WIN! 🎉")
      win=bet*5
    elif "🍒"in result:
      print("🎉 WIN! 🎉")
      win=bet*1
    

    #----Update Balance----
    if win > 0:
      print(f"You Won ${win}")
      money+=win
    else :
      print("You Lose!!!")
      print("You can win MORE!!!")


    #----Spin More Prompt-----
    play_more=input("\nWants to play more(y/n) : ").lower()
    if play_more!="y":
      time.sleep(1)
      break


  #----Game over----
  if money<10:
    print(f"\nYou're out of money!")
  print(f"Final Balance: {money}")
  print("Thanks for playing")


if __name__ == "__main__":
  slot_machine()

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
def roulette():
  ring_setup = [
      (0, 'green'), (32, 'red'), (15, 'black'), (19, 'red'), (4, 'black'),
      (21, 'red'), (2, 'black'), (25, 'red'), (17, 'black'), (34, 'red'),
      (6, 'black'), (27, 'red'), (13, 'black'), (36, 'red'), (11, 'black'),
      (30, 'red'), (8, 'black'), (23, 'red'), (10, 'black'), (5, 'red'),
      (24, 'black'), (16, 'red'), (33, 'black'), (1, 'red'), (20, 'black'),
      (14, 'red'), (31, 'black'), (9, 'red'), (22, 'black'), (18, 'red'),
      (29, 'black'), (7, 'red'), (28, 'black'), (12, 'red'), (35, 'black'),
      (3, 'red'), (26, 'black')
  ]

  while True:

    spin_result=random.choice(ring_setup)

    user_bet=is_input_valid(1,10,'''\nBetting Option \n1 : Straight \n2 : Split
                                  \n3 : Street\n4 : Corner \n5 : Six Line\n6 : Red|Black
                                  \n7 : Odd|Even \n8 : High|Low \n9 : Dozen\n10 : Exit\n Enter Your Choise : ''')

    print("Spining.",end='',flush=True)
    time.sleep(1)
    print(".",end='',flush=True)
    time.sleep(1)
    print(".",end='',flush=True)
    time.sleep(1)


    if user_bet==1:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")
      user_choisen_number=is_input_valid(1,36,"Enter your choisen number(1-36): ")

      print(f"The Spin Result is {spin_result}")

      if spin_result[0]==user_choisen_number:
        print(f"Congratulations You Win {user_bet_amount*35}")
      else:
        print(f"You Lose {user_bet_amount}")


    elif user_bet==2:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")

      user_numbers=[]
      count=0
      while count<=2:
        user_choisen_number=is_input_valid(1,36,"Enter your choisen number(1-36): ")
        user_numbers.append(user_choisen_number)
        time+=1


      print(f"The Spin Result is {spin_result}")
      if spin_result[0]==user_numbers[0] or spin_result[0]==user_numbers[1]:
        print(f"Congratulations You Win {user_bet_amount*17}")
      else:
        print(f"You Lose {user_bet_amount}")


    elif user_bet==3:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")

      user_numbers=[]
      count=0
      while count<=3:
        user_choisen_number=is_input_valid(1,36,"Enter your choisen number(1-36): ")
        user_numbers.append(user_choisen_number)
        time+=1

      print(f"The Spin Result is {spin_result}")
      if spin_result[0]==user_numbers[0] or spin_result[0]==user_numbers[1] or spin_result[0]==user_numbers[2]:
        print(f"Congratulations You Win {user_bet_amount*11}")
      else:
        print(f"You Lose {user_bet_amount}")



    elif user_bet==4:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")

      user_numbers=[]
      count=0
      while count<=4:
        user_choisen_number=is_input_valid(1,36,"Enter your choisen number(1-36): ")
        user_numbers.append(user_choisen_number)
        time+=1


      print(f"The Spin Result is {spin_result}")
      if spin_result[0]==user_choisen_number[0] or spin_result[0]==user_choisen_number[1] or spin_result[0]==user_choisen_number[2] or spin_result[0]==user_choisen_number[3]:
        print(f"Congratulations You Win {user_bet_amount*8}")
      else:
        print(f"You Lose {user_bet_amount}")


    elif user_bet==5:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")

      user_numbers=[]
      count=0
      while count<=6:
        user_choisen_number=is_input_valid(1,36,"Enter your choisen number(1-36): ")
        user_numbers.append(user_choisen_number)
        time+=1


      print(f"The Spin Result is {spin_result}")
      if spin_result[0]==user_choisen_number[0] or spin_result[0]==user_choisen_number[1] or spin_result[0]==user_choisen_number[2] or spin_result[0]==user_choisen_number[3] or spin_result[0]==user_choisen_number[4] or spin_result[0]==user_choisen_number[5]:
        print(f"Congratulations You Win {user_bet_amount*5}")
      else:
        print(f"You Lose {user_bet_amount}")


    elif user_bet==6:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")
      user_choisen_color=input("Enter your choisen Color(Red|Black): ")


      print(f"The Spin Result is {spin_result}")
      if spin_result[1]==user_choisen_color.lower():
        print(f"Congratulations You Win {user_bet_amount*2}")
      else:
        print(f"You Lose {user_bet_amount}")

    elif user_bet==7:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")
      user_choise_O_E=input("Enter your choise (Odd|Even): ")


      print(f"The Spin Result is {spin_result}")
      if spin_result[0]%2==0 and user_choise_O_E.lower()=="even":
        print(f"Congratulations You Win {user_bet_amount*2}")
      elif spin_result[0]%2!=0 and user_choise_O_E.lower()=="odd":
        print(f"Congratulations You Win {user_bet_amount*2}")
      else:
        print(f"You Lose {user_bet_amount}")

    elif user_bet==8:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")
      user_choise_H_L=input("Enter your choise (High|Low): ")
      print(f"The Spin Result is {spin_result}")
      if spin_result[0]>18 and user_choise_H_L.lower()=="high":
        print(f"Congratulations You Win {user_bet_amount*2}")
      elif spin_result[0]<19 and user_choise_H_L.lower()=="low":
        print(f"Congratulations You Win {user_bet_amount*2}")
      else:
        print(f"You Lose {user_bet_amount}")

    elif user_bet==9:
      user_bet_amount=is_input_valid(10,10000,"Enter your Bet(min->10 , max->10000): ")
      user_choise_dozen=is_input_valid(1,3,"\n1-(1-12)\n2-(13-24)\n3-(25-36)\nEnter your choise : ")
      print(f"The Spin Result is {spin_result}")
      if user_choise_dozen==1 and 1<=spin_result[0]<=12:
        print(f"Congratulations You Win {user_bet_amount*3}")
      elif user_choise_dozen==2 and 13<=spin_result[0]<=24:
        print(f"Congratulations You Win {user_bet_amount*3}")
      elif user_choise_dozen==3 and 25<=spin_result[0]<=36:
        print(f"Congratulations You Win {user_bet_amount*3}")
      else:
        print(f"You Lose {user_bet_amount}")

    elif user_bet==10:
      print("Thanks For Playing")
      break

if __name__=="__main__":
  roulette()

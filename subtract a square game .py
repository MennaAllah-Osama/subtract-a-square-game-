# Purpose:" Subtract a square.It is a two-player mathematical game.
         # It is played by two people with a pile of coins between them.
         # The players take turns removing coins from the pile, always removing a non-zero square number of coins.
         # The player who removes the last coin wins."
# Author: MennaAllah Osama Mohammad Ali.

import random
import math


print('Welcome in Subtract a square game.')         # A welcome message in the beginning of the game.
while True:
  print("Choose an Option:\nA)choose your own number of coins\nB)Random number of coins\n")
  choice = input("Enter your choice")
  if choice == "A" or choice == "a":
    n_coins = int(input("Enter your non_perfect square number of coins\n"))
    while n_coins == 0 or math.sqrt(n_coins) % 1 == 0:
       n_coins = int(input('WRONG!! , please enter a non_perfect square number of coins '))
    break

# Let number of coins random number from 1 to 1000.
  elif choice == "B" or choice == "b":
    n_coins = random.randint(10, 1000)
    while math.sqrt(n_coins) % 1 == 0:
        if math.sqrt(n_coins) % 1 == 0:
            n_coins = random.randint(10, 1000)
            continue
    break
  else:
    print("Invalid")
    continue

print ('The number of total coins is : ',n_coins)                              #Telling the users obout the total numbers of coins.

while n_coins > 0 :
    player1 = int(input('player1 , please enter a non-zero perfect square number'))                  #Let the first player to enter a valid number.
    while player1 == 0 or math.sqrt(player1)% 1 !=0  :                                                # Make a contition that the number should be non-zero square number.
            player1 = int(input('WRONG!!!!! , please enter a perfect square number'))
    n_coins -= player1

    while n_coins < 0:
     if n_coins < 0 :
        n_coins += player1
        player1 = int(input('please , choose a number that makes the number of the coins > 0'))
        while player1 == 0 or math.sqrt(player1) % 1 != 0:
            player1 = int(input('WRONG!!!!! , please enter a perfect square number'))
        n_coins -= player1
    print('the current number of coins is' , n_coins)

#Check the statue of the game if there is a winner or not.
    if n_coins == 0 :
        print('player1 wins')
        break

    player2 = int(input('player2 , please enter a non-zero perfect square number'))                  #Let the second player to enter a valid number.
    while player2 == 0 or math.sqrt(player2) % 1 != 0:                                               # Make a contition that the number should be non-zero square number.
            player2 = int(input('WRONG!!!!! , please enter a perfect square number'))
    n_coins -= player2

    while n_coins < 0 :
      if  n_coins < 0 :
          n_coins += player2 
          player2 = int(input('please , choose a number that makes the number of the coins > 0'))
          while player2 == 0 or math.sqrt(player1) % 1 != 0:
              player2 = int(input('WRONG!!!!! , please enter a perfect square number'))
          n_coins -= player2
    print('the current number of coins is' , n_coins)

#Check the statue of the game if there is a winner or not.
    if n_coins == 0:
        print('player2 wins')
        break

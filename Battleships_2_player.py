import random

def print_board(board):
  for row in board:
    print(" ".join(row))

#Subroutine to process player 1's input
def player1(ship1_row, ship1_col, hit):
    legit_move = False
    while legit_move == False:
      print("Player 1:   ")
      print_board(board1)
      print("")
      guess1_row = int(input("Player 1 guess row:   ")) - 1
      guess1_col = int(input("Player 1 guess column:   ")) - 1
      if ship_len == 1:
        if guess1_row == ship2_row and guess1_col == ship2_col:
          print("")
          print("Congratulations! You sank Player 2's battleship!")
          board1[guess1_row][guess1_col] = "!"
          print("")
          print("Player 1's Final Board:")
          print_board(board1)
          print("")
          print("Player 1 wins! Well done! You won in " + str(turn_count) + " moves!")
          print("")
          print("Player 1's ship was in row " + str((ship1_row) + 1) + ", col " + str((ship1_col) + 1))
          print("Player 2's ship was in row " + str((ship2_row) + 1) + ", col " + str((ship2_col) + 1))
          quit()
          winner1 = True
          legit_move = True
          break
        else:
          if guess1_row not in range(10) or guess1_col not in range(10):
              print("Oops, that's not even in the ocean.")
              print("")
          elif board1[guess1_row][guess1_col] == "X":
              print("You guessed that one already.")
              print("")
          else:
              print("You missed Player 2's battleship!")
              board1[guess1_row][guess1_col] = "X"
              legit_move = True
      #If statement deciding whether or not player 2's ship was sunk     
      elif ship_len == 2:
        if (guess1_row == ship2_row and guess1_col == ship2_col) or (guess1_row == ship2_row2 and guess1_col == ship2_col2):
          if hit == ship_len:
            print("")
            print("Congratulations! You sank Player 1's battleship!")
            board1[guess1_row][guess1_col] = "!"
            print("")
            print("Player 1's Final Board:")
            print_board(board2)
            print("Player 1 wins! Well done! You won in " + str(turn_count) + " moves!")
            print("")
            print("Player 1's ship was in row " + str((ship1_row) + 1) + " and " + str((ship1_row2) + 1) + ", col " + str((ship1_col) + 1) + " and " + str((ship1_col2) + 1))
            print("Player 2's ship was in row " + str((ship2_row) + 1) + " and " + str((ship2_col2) + 1) + ", col " + str((ship2_col) + 1) + " and " + str((ship2_col2) + 1))
            quit()
            winner1 = True
            legit_move = True
            break
          else:
            print("")
            print("Congratulations! You hit Player 2's battleship!")
            board1[guess1_row][guess1_col] = "!"
            print_board(board1)
            hit = hit + 1
            if hit == ship_len:
              quit()
        else:
          if guess1_row not in range(10) or guess1_col not in range(10):
              print("Oops, that's not even in the ocean.")
              print("")
          elif (board1[guess1_row][guess1_col] == "X") or (board1[guess1_row][guess1_col] == "!"):
              print("You guessed that one already.")
              print("")
          else:
              print("You missed Player 2's battleship!")
              board1[guess1_row][guess1_col] = "X"
              print_board(board1)
              legit_move = True

      #Same code but for different lengthed ships                                               
      elif ship_len == 3:
        if (guess1_row == ship2_row and guess1_col == ship2_col) or (guess1_row == ship2_row2 and guess1_col == ship2_col2) or (guess1_row == ship2_row3 and guess1_col == ship2_col3):
          if hit == ship_len:
            print("")
            print("Congratulations! You sank Player 2's battleship!")
            board1[guess1_row][guess1_col] = "!"
            print("")
            print("Player 1's Final Board:")
            print_board(board1)
            print("Player 1 wins! Well done! You won in " + str(turn_count) + " moves!")
            print("")
            print("Player 1's ship was in row " + str((ship1_row) + 1) + ", " + str((ship1_row2) + 1) + " and " + str((ship1_row3) + 1) + ", col " + str((ship1_col) + 1) + ", " + str((ship1_col2) + 1) + " and " + str((ship1_col3) + 1))
            print("Player 2's ship was in row " + str((ship2_row) + 1) + ", " + str((ship2_row2) + 1) + " and " + str((ship2_col3) + 1) + ", col " + str((ship2_col) + 1) + ", " + str((ship2_col2) + 1) + " and " + str((ship2_col3) + 1))
            quit()
            winner1 = True
            legit_move = True
            break
          else:
            print("")
            print("Congratulations! You hit Player 1's battleship!")
            board1[guess1_row][guess1_col] = "!"
            print_board(board1)
            hit = hit + 1
            if hit == ship_len:
              quit()
        else:
          if guess1_row not in range(10) or guess1_col not in range(10):
              print("Oops, that's not even in the ocean.")
              print("")
          elif (board1[guess1_row][guess1_col] == "X") or (board1[guess1_row][guess1_col] == "!"):
              print("You guessed that one already.")
              print("")
          else:
              print("You missed Player 1's battleship!")
              board1[guess1_row][guess1_col] = "X"
              print_board(board1)
              legit_move = True

#Subroutine for processing player 2's input(Similar code but for player 2 instead)           
def player2(ship2_row, ship2_col, hit):
    legit_move = False
    while legit_move == False:
      print("Player 2:   ")
      print("")
      guess2_row = int(input("Player 2 guess row:   ")) - 1
      guess2_col = int(input("Player 2 guess column:   ")) - 1
      if ship_len == 1:
        if guess2_row == ship1_row and guess2_col == ship1_col:
          print("")
          print("Congratulations! You sank my battleship!")
          board2[guess2_row][guess2_col] = "!"
          print("")
          print("Player 2's Final Board:")
          print_board(board2)
          print("Player 2 wins! Well done! You won in " + str(turn_count) + " moves!")
          print("")
          print("Player 1's ship was in row " + str((ship1_row) + 1) + ", col " + str((ship1_col) + 1))
          print("Player 2's ship was in row " + str((ship2_row) + 1) + ", col " + str((ship2_col) + 1))
          quit()
          winner2 = True
          legit_move = True
          break
        else:
          if guess2_row not in range(10) or guess2_col not in range(10):
              print("Oops, that's not even in the ocean.")
              print("")
          elif board2[guess2_row][guess2_col] == "X":
              print("You guessed that one already.")
              print("")
          else:
              print("You missed my battleship!")
              board2[guess2_row][guess2_col] = "X"
              print_board(board2)
              legit_move = True

      elif ship_len == 2:
        if (guess2_row == ship1_row and guess2_col == ship1_col) or (guess2_row == ship1_row2 and guess2_col == ship1_col2):
          if hit == ship_len:
            print("")
            print("Congratulations! You sank Player 1's battleship!")
            board2[guess2_row][guess2_col] = "!"
            print("")
            print("Player 2's Final Board:")
            print_board(board2)
            print("Player 2 wins! Well done! You won in " + str(turn_count) + " moves!")
            print("")
            print("Player 1's ship was in row " + str((ship1_row) + 1) + " and " + str((ship1_row2) + 1) + ", col " + str((ship1_col) + 1) + " and " + str((ship1_col2) + 1))
            print("Player 2's ship was in row " + str((ship2_row) + 1) + " and " + str((ship2_col2) + 1) + ", col " + str((ship2_col) + 1) + " and " + str((ship2_col2) + 1))
            quit()
            winner2 = True
            legit_move = True
            break
          else:
            print("")
            print("Congratulations! You hit Player 1's battleship!")
            board2[guess2_row][guess2_col] = "!"
            print_board(board2)
            hit = hit + 1
            if hit == ship_len:
              quit()
        else:
          if guess2_row not in range(10) or guess2_col not in range(10):
              print("Oops, that's not even in the ocean.")
              print("")
          elif (board2[guess2_row][guess2_col] == "X") or (board2[guess2_row][guess2_col] == "!"):
              print("You guessed that one already.")
              print("")
          else:
              print("You missed Player 1's battleship!")
              board2[guess2_row][guess2_col] = "X"
              print_board(board2)
              legit_move = True
                                                      
      elif ship_len == 3:
        if (guess2_row == ship1_row and guess2_col == ship1_col) or (guess2_row == ship1_row2 and guess2_col == ship1_col2) or (guess2_row == ship1_row3 and guess2_col == ship1_col3):
          if hit == ship_len:
            print("")
            print("Congratulations! You sank Player 1's battleship!")
            board2[guess2_row][guess2_col] = "!"
            print("")
            print("Player 2's Final Board:")
            print_board(board2)
            print("Player 2 wins! Well done! You won in " + str(turn_count) + " moves!")
            print("")
            print("Player 1's ship was in row " + str((ship1_row) + 1) + ", " + str((ship1_row2) + 1) + " and " + str((ship1_row3) + 1) + ", col " + str((ship1_col) + 1) + ", " + str((ship1_col2) + 1) + " and " + str((ship1_col3) + 1))
            print("Player 2's ship was in row " + str((ship2_row) + 1) + ", " + str((ship2_row2) + 1) + " and " + str((ship2_col3) + 1) + ", col " + str((ship2_col) + 1) + ", " + str((ship2_col2) + 1) + " and " + str((ship2_col3) + 1))
            quit()
            winner2 = True
            legit_move = True
            break
          else:
            print("")
            print("Congratulations! You hit Player 1's battleship!")
            board2[guess2_row][guess2_col] = "!"
            print_board(board2)
            hit = hit + 1
            if hit == ship_len:

              quit()
        else:
          if guess2_row not in range(10) or guess2_col not in range(10):
              print("Oops, that's not even in the ocean.")
              print("")
          elif (board2[guess2_row][guess2_col] == "X") or (board2[guess2_row][guess2_col] == "!"):
              print("You guessed that one already.")
              print("")
          else:
              print("You missed Player 1's battleship!")
              board2[guess2_row][guess2_col] = "X"
              print_board(board2)
              legit_move = True
        
#Creating the board and certain global variables                                         
board1 = []
board2 = []
for x in range(0, 10):
  board1.append(["O"] * 10)

for x in range(0, 10):
  board2.append(["O"] * 10)
  
winner1 = False
winner2 = False
turn_count = 1
hit = 0
diff = 0

#Difficulty selected by players judges how many turns they have
while diff != "easy" and diff != "medium" and diff != "hard" and diff != "extreme" and diff != "unlimited":
  diff = input("Enter difficulty: easy, medium, hard, extreme or unlimited   ")
  diff = diff.lower()
  if diff == "easy":
    turn_numb = 20
  elif diff == "medium":
    turn_numb = 15
  elif diff == "hard":
    turn_numb = 10
  elif diff == "extreme":
    turn_numb = 5
  elif diff == "unlimited":
    turn_numb = 101
  else:
    print("Invalid difficulty")

#While loop and IF statements to decide on length of ships
length = 0
while length != "short" and length != "medium" and length != "long":
    length = input("Enter ship length: short, medium or long   ")
    length = length.lower()
    if length == "short":
        ship_len = 1
    elif length == "medium":
        ship_len = 2
    elif length == "long":
        ship_len = 3
    else:
        print("Invalid length")
        print("")
    
ship1_row = 10
ship1_col = 10
ship2_row = 10
ship2_col = 10

#Players entering their placement of their ships
while ship1_row < 0 or ship1_row > 9:
  ship1_row = int(input("Player 1 enter ship row (1-10):   ")) - 1
while ship1_col < 0 or ship1_col > 9:
  ship1_col = int(input("Player 1 enter ship column (1-10):   ")) -1
while ship2_row < 0 or ship2_row > 9:
  ship2_row = int(input("Player 2 enter ship row (1-10):   ")) - 1
while ship2_col < 0 or ship2_col > 9:
  ship2_col = int(input("Player 2 enter ship column (1-10):   ")) -1

#All this code checks the placements and sees if it fits on the board (for player 1)
fit = False
if ship_len == 2 or ship_len == 3:
    while fit == False:
        direction = "no direction"
        while direction != "up" and direction != "down" and direction != "left" and direction != "right" and direction != "u" and direction != "d" and direction != "l" and direction != "r":
            direction = input("Player 1, enter direction - up, down, left or right - of your ship from starting point (" + str((ship1_row) + 1) + "," + str((ship1_col) + 1) + "):   ")
            direction = direction.lower()
            if ship_len == 3:
                if direction == "up":
                    ship1_row2 = ship1_row - 1
                    ship1_row3 = ship1_row - 2
                    ship1_col2 = ship1_col
                    ship1_col3 = ship1_col
                    if ship1_row3 <= 0 or ship1_row3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                    
                elif direction == "down":
                    ship1_row2 = ship1_row + 1
                    ship1_row3 = ship1_row + 2
                    ship1_col2 = ship1_col                                                 
                    ship1_col3 = ship1_col
                    if ship1_row3 <= 0 or ship1_row3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "left":
                    ship1_col2 = ship1_col - 1
                    ship1_col3 = ship1_col - 2
                    ship1_row2 = ship1_row
                    ship1_row3 = ship1_row
                    if ship1_col3 <= 0 or ship1_col3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "right":
                    ship1_col2 = ship1_col + 1
                    ship1_col3 = ship1_col + 2
                    ship1_row2 = ship1_row
                    ship1_row3 = ship1_row
                    if ship1_col3 <= 0 or ship1_col3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                else:
                    fit = False
                    print("Invalid direction")
                    print("")
                
            elif ship_len == 2:
                if direction == "up":
                    ship1_row2 = ship1_row - 1
                    ship1_col2 = ship1_col
                    if ship1_row2 <= 0 or ship1_row2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "down":
                    ship1_row2 = ship1_row + 1
                    ship1_col2 = ship1_col
                    if ship1_row2 <= 0 or ship1_row2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "left":
                    ship1_col2 = ship1_col - 1
                    ship1_row2 = ship1_row
                    if ship1_col2 <= 0 or ship1_col2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "right":
                    ship1_col2 = ship1_col + 1
                    ship1_row2 = ship1_row
                    if ship1_col2 <= 0 or ship1_col2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                else:
                    print("Invalid direction")
                    print("")
                    
#Same code but for player 2's placements
fit = False
if ship_len == 2 or ship_len == 3:
    while fit == False:
        direction = "no direction"
        while direction != "up" and direction != "down" and direction != "left" and direction != "right" and direction != "u" and direction != "d" and direction != "l" and direction != "r":
            direction = input("Player 2, enter direction - up, down, left or right - of your ship from starting point (" + str((ship1_row) + 1) + "," + str((ship1_col) + 1) + "):   ")
            direction = direction.lower()
            if ship_len == 3:
                if direction == "up":
                    ship2_row2 = ship2_row - 1
                    ship2_row3 = ship2_row - 2
                    ship2_col2 = ship2_col
                    ship2_col3 = ship2_col
                    if ship2_row3 <= 0 or ship2_row3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                    
                elif direction == "down":
                    ship2_row2 = ship2_row + 1
                    ship2_row3 = ship2_row + 2
                    ship2_col2 = ship2_col                                                 
                    ship2_col3 = ship2_col
                    if ship2_row3 <= 0 or ship2_row3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "left":
                    ship2_col2 = ship2_col - 1
                    ship2_col3 = ship2_col - 2
                    ship2_row2 = ship2_row
                    ship2_row3 = ship2_row
                    if ship2_col3 <= 0 or ship2_col3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "right":
                    ship2_col2 = ship2_col + 1
                    ship2_col3 = ship2_col + 2
                    ship2_row2 = ship2_row
                    ship2_row3 = ship2_row
                    if ship2_col3 <= 0 or ship2_col3 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                else:
                    fit = False
                    print("Invalid direction")
                    print("")
                
            elif ship_len == 2:
                if direction == "up":
                    ship2_row2 = ship2_row - 1
                    ship2_col2 = ship2_col
                    if ship2_row2 <= 0 or ship2_row2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "down":
                    ship2_row2 = ship2_row + 1
                    ship2_col2 = ship2_col
                    if ship2_row2 <= 0 or ship1_row2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "left":
                    ship2_col2 = ship2_col - 1
                    ship2_row2 = ship2_row
                    if ship2_col2 <= 0 or ship2_col2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "right":
                    ship2_col2 = ship2_col + 1
                    ship2_row2 = ship2_row
                    if ship2_col2 <= 0 or ship2_col2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                else:
                    print("Invalid direction")
                    print("")

#################################
if ship_len == 1:
    print(ship1_row, ship1_col)
    print("")
    print(ship2_row, ship2_col)
elif ship_len == 2:
    print(ship1_row, ship1_col)
    print(ship1_row2, ship1_col2)
    print("")
    print(ship2_row, ship2_col)
    print(ship2_row2, ship2_col2)
elif ship_len == 3:
    print(ship1_row, ship1_col)
    print(ship1_row2, ship1_col2)
    print(ship1_row3, ship1_col3)
    print("")
    print(ship2_row, ship2_col)
    print(ship2_row2, ship2_col2)
    print(ship2_row3, ship2_col3)
#################################

#"Game Over" screen and information displayed on that screen
for x in range(turn_numb):
    print("")
    print("Turn:   " + str(turn_count))
    if winner1 == False and winner2 == False:
      (player1(ship1_row, ship1_col, hit))
      print("")
      (player2(ship2_row, ship2_col, hit))
    turn_count = turn_count + 1
    x = x + 1

print("")
print("")
print("Game Over!")
if diff == "extreme":
  print("You are not as good as you think! Chose an easier difficulty ;)")
elif diff == "hard":
  print("Should have picked an easier difficulty!")
elif diff == "medium":
  print("Perhaps you could try the easier difficulty next time")
elif diff == "easy":
  print("At least you tried :(")
else:
  print("Now try a mode with limited moves")

print("")  
if ship_len == 1:
    print("Your ship was in row " + str((ship1_row) + 1) + ", col " + str((ship1_col) + 1))
    print("CPU's ship was in row " + str((ship2_row) + 1) + ", col " + str((ship2_col) + 1))
elif ship_len == 2:
    print("Your ship was in row " + str((ship1_row) + 1) + " and " + str((ship1_row2) + 1) + ", col " + str((ship1_col) + 1) + " and " + str((ship1_col2) + 1))
    print("CPU's ship was in row " + str((ship2_row) + 1) + " and " + str((ship2_row2) + 1) + ", col " + str((ship2_col) + 1) + " and " + str((ship2_col2) + 1))
elif ship_len == 3:
    print("Your ship was in row " + str((ship1_row) + 1) + ", " + str((ship1_row2) + 1) + " and " + str((ship1_row3) + 1) + ", col " + str((ship1_col) + 1) + ", " + str((ship1_col2) + 1) + " and " + str((ship1_col3) + 1))
    print("CPU's ship was in row " + str((ship2_row) + 1) + ", " + str((ship2_row2) + 1) + " and " + str((ship2_row3) + 1) + ", col " + str((ship2_col) + 1) + ", " + str((ship2_col2) + 1) + " and " + str((ship2_col3) + 1))    

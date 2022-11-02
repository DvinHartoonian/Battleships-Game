from random import randint
import time

#Subroutines to print the board
def print_board(board):
    print("")
    for row in board:
        print(" ".join(row))
    print("")

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

def half_chance():
    return randint(1,2)

#Whether or not the move from player 1 hit the CPU's ship(s)
def player1(ship1_row, ship1_col, hit):
    legit_move = False
    while legit_move == False:
      print("Player 1:   ")
      print("")
      guess1_row = int(input("Player 1 guess row:   ")) - 1
      guess1_col = int(input("Player 1 guess column:   ")) - 1
      if ship_len == 1:
          if guess1_row == shipc_row and guess1_col == shipc_col:
            print("")
            print("Congratulations! You sank CPU's battleship!")
            board1[guess1_row][guess1_col] = "!"
            print("")
            print("Player 1's Final Board:") 
            print_board(board1)
            print("")
            print("You win! Well done! You won in " + str(turn_count) + " moves!")
            print("")
            print("Your ship was in row " + str((ship1_row) + 1) + ", col " + str((ship1_col) + 1))
            print("CPU's ship was in row " + str((shipc_row) + 1) + ", col " + str((shipc_col) + 1))
            quit()
            winner = True
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
                print("You missed CPU's battleship!")
                board1[guess1_row][guess1_col] = "X"
                print_board(board1)
                legit_move = True

      #Same code but for multiple ships           
      elif ship_len == 2:
          if (guess1_row == shipc_row and guess1_col == shipc_col) or (guess1_row == shipc_row2 and guess1_col == shipc_col2):
              if hit == ship_len:
                print("")
                print("Congratulations! You sank my battleship!")
                board1[guess1_row][guess1_col] = "!"
                print("")
                print("Player 1's Final Board:") 
                print_board(board1)
                print("")
                print("You win! Well done! You won in " + str(turn_count) + " moves!")
                print("")
                print("Your ship was in row " + str((ship1_row) + 1) + " and " + str((ship1_row2) + 1) + ", col " + str((ship1_col) + 1) + " and " + str((ship1_col2) + 1))
                print("CPU's ship was in row " + str((shipc_row) + 1) + " and " + str((shipc_row2) + 1) + ", col " + str((shipc_col) + 1) + " and " + str((shipc_col2) + 1))
                quit()
                winner = True
                legit_move = True
                break
              else:
                print("")
                print("Congratulations! You hit CPU's battleship!")
                board1[guess1_row][guess1_col] = "!"
                print_board(board1)
                hit = hit + 1
                if hit == 3:
                  quit()
          else:
            if guess1_row not in range(10) or guess1_col not in range(10):
                print("Oops, that's not even in the ocean.")
                print("")
            elif (board1[guess1_row][guess1_col] == "X") or (board1[guess1_row][guess1_col] == "!"):
                print("You guessed that one already.")
                print("")
            else:
                print("You missed CPU's battleship!")
                board1[guess1_row][guess1_col] = "X"
                print_board(board1)
                legit_move = True
                                                             
      elif ship_len == 3:
        if (guess1_row == shipc_row and guess1_col == shipc_col) or (guess1_row == shipc_row2 and guess1_col == shipc_col2) or (guess1_row == shipc_row3 and guess1_col == shipc_col3):
            if hit == ship_len:
                print("")
                print("Congratulations! You sank CPU's battleship!")
                board1[guess1_row][guess1_col] = "!"
                print("")
                print("Player 1's Final Board:") 
                print_board(board1)
                print("")
                print("You win! Well done! You won in " + str(turn_count) + " moves!")
                print("")
                print("Your ship was in row " + str((ship1_row) + 1) + ", " + str((ship1_row2) + 1) + " and " + str((ship1_row3) + 1) + ", col " + str((ship1_col) + 1) + ", " + str((ship1_col2) + 1) + " and " + str((ship1_col3) + 1))
                print("CPU's ship was in row " + str((shipc_row) + 1) + ", " + str((shipc_row2) + 1) + " and " + str((shipc_row3) + 1) + ", col " + str((shipc_col) + 1) + ", " + str((shipc_col2) + 1) + " and " + str((shipc_col3) + 1))
                quit()
                winner = True
                legit_move = True
                break
            else:
                print("")
                print("Congratulations! You hit CPU's battleship!")
                board1[guess1_row][guess1_col] = "!"
                print_board(board1)
                hit = hit + 1
                if hit == 3:
                  quit()
        else:
            if guess1_row not in range(10) or guess1_col not in range(10):
                print("Oops, that's not even in the ocean.")
                print("")
            elif (board1[guess1_row][guess1_col] == "X") or (board1[guess1_row][guess1_col] == "!"):
                print("You guessed that one already.")
                print("")
            else:
                print("You missed CPU's battleship!")
                board1[guess1_row][guess1_col] = "X"
                print_board(board1)
                legit_move = True

#The CPU entering its move and whether or not it hits player 1's ship(s)           
def cpu(shipc_row, shipc_col, hit):
    legit_move = False
    while legit_move == False:
        print("CPU is making a move, please wait...")
        time.sleep(2)
        print("")
        guessc_row = random_row(boardc)
        guessc_col = random_col(boardc)
        if ship_len == 1:
            if guessc_row == ship1_row and guessc_col == ship1_col:
                print("")
                print("Unlucky, CPU sank your battleship!")
                boardc[guessc_row][guessc_col] = "!"
                print("")
                print("CPU's Final Board:")
                print_board(boardc)
                print("")
                print("CPU wins in " + str(turn_count) + " moves!")
                print("Bad luck :(")
                print("")
                print("Your ship was in row " + str((ship1_row) + 1) + ", col " + str((ship1_col) + 1))
                print("CPU's ship was in row " + str((shipc_row) + 1) + ", col " + str((shipc_col) + 1))
                quit()
                loser = True
                legit_move = True
                break
            else:
                if guessc_row not in range(10) or guessc_col not in range(10):
                    legit_move = False
                elif boardc[guessc_row][guessc_col] == "X":
                    legit_move = False
                else:
                    ("Fortunately, CPU missed your battlehsip!")
                    boardc[guessc_row][guessc_col] = "X"
                    print("CPU:   ")
                    print_board(boardc)
                    print("")
                    print("CPU guessed row " + str(guessc_row) + ", column " + str(guessc_col))
                    legit_move = True
                                    
        elif ship_len == 2:
            if (guessc_row == ship1_row and guessc_col == ship1_col) or (guessc_row == ship1_row2 and guessc_col == ship1_col2):
                if hit == ship_len:
                    print("")
                    print("Unlucky, CPU sank your battleship!")
                    boardc[guessc_row][guessc_col] = "!"
                    print("")
                    print("CPU's Final Board:")
                    print_board(boardc)
                    print("")
                    print("CPU wins in " + str(turn_count) + " moves!")
                    print("Bad luck :(")
                    print("")
                    print("Your ship was in row " + str((ship1_row) + 1) + " and " + str((ship1_row2) + 1) + ", col " + str((ship1_col) + 1) + " and " + str((ship1_col2) + 1))
                    print("CPU's ship was in row " + str((shipc_row) + 1) + "and " + str((shipc_row2) + 1) + ", col " + str((shipc_col) + 1) + " and " + str((shipc_col2) + 1))
                    quit()
                    loser = True
                    legit_move = True
                    break
                else:
                    print("")
                    print("Congratulations! You hit CPU's battleship!")
                    boardc[guess_row][guess_col] = "!"
                    print_board(board)
                    hit = hit + 1
                    if hit == 3:
                      quit()
            else:
                if guessc_row not in range(10) or guessc_col not in range(10):
                    legit_move = False
                elif (boardc[guessc_row][guessc_col] == "X") or (boardc[guessc_row][guessc_col] == "!"):
                    legit_move = False
                else:
                    ("Fortunately, CPU missed your battlehsip!")
                    boardc[guessc_row][guessc_col] = "X"
                    print("CPU:   ")
                    print_board(boardc)
                    print("")
                    print("CPU guessed row " + str(guessc_row) + ", column " + str(guessc_col))
                    legit_move = True
                                                                 
        elif ship_len == 3:
            if (guessc_row == ship1_row and guessc_col == ship1_col) or (guessc_row == ship1_row2 and guessc_col == ship1_col2) or (guessc_row == ship1_row3 and guessc_col == ship1_col3):
                if hit == ship_len:
                    print("")
                    print("Unlucky, CPU sank your battleship!")
                    boardc[guessc_row][guessc_col] = "!"
                    print("")
                    print("CPU's Final Board:")
                    print_board(boardc)
                    print("")
                    print("CPU wins in " + str(turn_count) + " moves!")
                    print("Bad luck :(")
                    print("")
                    print("Your ship was in row " + str((ship1_row) + 1) + ", " + str((ship1_row2) + 1) + " and " + str((ship1_row3) + 1) + ", col " + str((ship1_col) + 1) + ", " + str((ship1_col2) + 1) + " and " + str((ship1_col3) + 1))
                    print("CPU's ship was in row " + str((shipc_row) + 1) + ", " + str((shipc_row2) + 1) + " and " + str((shipc_row3) + 1) + ", col " + str((shipc_col) + 1) + ", " + str((shipc_col2) + 1) + " and " + str((shipc_col3) + 1))
                    quit()
                    loser = True
                    legit_move = True
                    break
                else:
                    print("")
                    print("Congratulations! You hit CPU's battleship!")
                    boardc[guess_row][guess_col] = "!"
                    print_board(board)
                    hit = hit + 1
                    if hit == 3:
                      quit()
            else:
                if guessc_row not in range(10) or guessc_col not in range(10):
                    legit_move = False
                elif (boardc[guessc_row][guessc_col] == "X") or (boardc[guessc_row][guessc_col] == "!"):
                    legit_move = False
                else:
                    ("Fortunately, CPU missed your battlehsip!")
                    boardc[guessc_row][guessc_col] = "X"
                    print("CPU:   ")
                    print_board(boardc)
                    print("")
                    print("CPU guessed row " + str(guessc_row) + ", column " + str(guessc_col))
                    legit_move = True

#The creation of the board                                                                 
board1 = []
boardc = []
for x in range(0, 10):
    board1.append(["O"] * 10)

for x in range(0, 10):
    boardc.append(["O"] * 10)

#Creation of certain global variables
hit = 0    
turn_count = 1
winner = False
loser = False
fit = False
diff = 0

#Difficulty selection and what this equates to
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
        print("Invaild difficulty")
        print("")

#Selection of the size of the ship(s) 
print("")
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

#Checks the ship position so that it is valid for the board
ship1_row = 10
ship1_col = 10
print("")                                                                
while ship1_row < 0 or ship1_row > 9:
    ship1_row = int(input("Enter row of ship's starting point (1-10):   ")) - 1
    print("")
    if ship1_row < 0 or ship1_row > 9:
        print("Invalid coordinate")
        print("")
while ship1_col < 0 or ship1_col > 9:
    ship1_col = int(input("Enter column of ship's starting point (1-10):   ")) - 1
    print("")
    if ship1_col < 0 or ship1_col > 9:
        print("Invalid coordinate")
        print("")                                                             
if ship_len == 2 or ship_len == 3:
    while fit == False:
        direction = "no direction"
        while direction != "up" and direction != "down" and direction != "left" and direction != "right" and direction != "u" and direction != "d" and direction != "l" and direction != "r":
            direction = input("Enter direction - up, down, left or right - of ship from starting point (" + str((ship1_row) + 1) + "," + str((ship1_col) + 1) + "):   ")
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
                    if ship1_row3 <= 0 or ship1_row3 >= 9:
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
                    if ship1_row2 <= 0 or ship1_row2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                elif direction == "right":
                    ship1_col2 = ship1_col + 1
                    ship1_row2 = ship1_row
                    if ship1_row2 <= 0 or ship1_row2 >= 9:
                        print("Ship does not fit on board. Try again")
                        fit = False
                    else:
                        fit = True
                        
                else:
                    print("Invalid direction")
                    print("")

shipc_row = random_row(boardc)
shipc_col = random_col(boardc)

if ship_len == 3:
  if shipc_row <= 2 or shipc_row >= 7:
    chance = half_chance
    if chance == 1:
        chance = half_chance()
        if chance == 1:
          shipc_row2 = shipc_row
          shipc_row3 = shipc_row
          shipc_col2 = shipc_col + 1
          shipc_col3 = shipc_col + 2
        else:
          shipc_row2 = shipc_row
          shipc_row3 = shipc_row
          shipc_col2 = shipc_col - 1
          shipc_col3 = shipc_col - 2
    else:
        if shipc_row <= 2:
            shipc_row2 = shipc_row + 1
            shipc_row3 = shipc_row + 2
            shipc_col2 = shipc_col
            shipc_col3 = shipc_col
        elif shipc_row >= 7:
            shipc_row2 = shipc_row - 1
            shipc_row3 = shipc_row - 2
            shipc_col2 = shipc_col
            shipc_col3 = shipc_col

  elif shipc_col <= 2 or shipc_col >= 7:
    chance = half_chance() 
    if chance == 1:
        chance = half_chance()
        if chance == 1:
          shipc_row2 = shipc_row + 1
          shipc_row3 = shipc_row + 2
          shipc_col2 = shipc_col
          shipc_col3 = shipc_col
        else:
          shipc_row2 = shipc_row - 1
          shipc_row3 = shipc_row - 2
          shipc_col2 = shipc_col
          shipc_col3 = shipc_col
    else:
        if shipc_col <= 2:
            shipc_col2 = shipc_col + 1
            shipc_col3 = shipc_col + 2
            shipc_row2 = shipc_row
            shipc_row3 = shipc_row
        elif shipc_col >= 7:
            shipc_col2 = shipc_col - 1
            shipc_col3 = shipc_col - 2
            shipc_row2 = shipc_row
            shipc_row2 = shipc_row
        
  else:
      chance = half_chance()
      if chance == 1:
          chance == half_chance()
          if chance == 1:
            shipc_row2 = shipc_row + 1
            shipc_row3 = shipc_row + 2
            shipc_col2 = shipc_col
            shipc_col3 = shipc_col
          else:
            shipc_row2 = shipc_row - 1
            shipc_row3 = shipc_row - 2
            shipc_col2 = shipc_col
            shipc_col3 = shipc_col 
      else:
          chance = half_chance()
          if half_chance() == 1:
            shipc_col2 = shipc_col + 1
            shipc_col3 = shipc_col + 2
            shipc_row2 = shipc_row
            shipc_row3 = shipc_row
          else:
            shipc_col2 = shipc_col - 1
            shipc_col3 = shipc_col - 2
            shipc_row2 = shipc_row
            shipc_row3 = shipc_row

elif ship_len == 2:
  if shipc_row <= 2 or shipc_row >= 7:
    chance = half_chance
    if chance == 1:
        chance = half_chance()
        if chance == 1:
          shipc_row2 = shipc_row
          shipc_col2 = shipc_col + 1
        else:
          shipc_row2 = shipc_row
          shipc_col2 = shipc_col - 1
    else:
        if shipc_row <= 2:
            shipc_row2 = shipc_row + 1
            shipc_col2 = shipc_col
        elif shipc_row >= 7:
            shipc_row2 = shipc_row - 1
            shipc_col2 = shipc_col
  else:    
    chance = half_chance()
    if chance == 1:
      chance == half_chance()
      if chance == 1:
        shipc_row2 = shipc_row + 1
        shipc_col2 = shipc_col
      else:
        shipc_row2 = shipc_row - 1
        shipc_col2 = shipc_col
    else:
      chance = half_chance()
      if half_chance() == 1:
        shipc_col2 = shipc_col + 1
        shipc_row2 = shipc_row
      else:
        shipc_col2 = shipc_col - 1
        shipc_row2 = shipc_row

#################################
if ship_len == 1:
    print(ship1_row, ship1_col)
    print("")
    print(shipc_row, shipc_col)
elif ship_len == 2:
    print(ship1_row, ship1_col)
    print(ship1_row2, ship1_col2)
    print("")
    print(shipc_row, shipc_col)
    print(shipc_row2, shipc_col2)
elif ship_len == 3:
    print(ship1_row, ship1_col)
    print(ship1_row2, ship1_col2)
    print(ship1_row3, ship1_col3)
    print("")
    print(shipc_row, shipc_col)
    print(shipc_row2, shipc_col2)
    print(shipc_row3, shipc_col3)
#################################

for x in range(turn_numb):
    print("")
    print("")
    print("Turn:   " + str(turn_count))
    if winner == False and loser == False:
      (player1(ship1_row, ship1_col, hit))
      print("")
      (cpu(shipc_row, shipc_col, hit))
    turn_count = turn_count + 1
    x = x + 1

#"Game Over" screen and what information is displayed on this screen
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
    print("CPU's ship was in row " + str((shipc_row) + 1) + ", col " + str((shipc_col) + 1))
elif ship_len == 2:
    print("Your ship was in row " + str((ship1_row) + 1) + " and " + str((ship1_row2) + 1) + ", col " + str((ship1_col) + 1) + " and " + str((ship1_col2) + 1))
    print("CPU's ship was in row " + str((shipc_row) + 1) + " and " + str((shipc_row2) + 1) + ", col " + str((shipc_col) + 1) + " and " + str((shipc_col2) + 1))
elif ship_len == 3:
    print("Your ship was in row " + str((ship1_row) + 1) + ", " + str((ship1_row2) + 1) + " and " + str((ship1_row3) + 1) + ", col " + str((ship1_col) + 1) + ", " + str((ship1_col2) + 1) + " and " + str((ship1_col3) + 1))
    print("CPU's ship was in row " + str((shipc_row) + 1) + ", " + str((shipc_row2) + 1) + " and " + str((shipc_row3) + 1) + ", col " + str((shipc_col) + 1) + ", " + str((shipc_col2) + 1) + " and " + str((shipc_col3) + 1))

    
        

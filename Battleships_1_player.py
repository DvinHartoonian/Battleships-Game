from random import randint

#Sunbroutines for the board
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
#Array for board aesthetic
board = []
for x in range(0, 10):
  board.append(["O"] * 10)

hit = 0
ship_down = 0
ship_numb = 0
turn_count = 1
diff = 0

#Number of turns depending on choice of difficulty
while diff != "easy" and diff != "medium" and diff != "hard" and diff != "extreme" and diff != "20" and diff != "15" and diff != "10" and diff != "5":
  diff = input("Enter difficulty / number of moves: easy(20), medium(15), hard(10) or extreme(5)   ")
  diff = diff.lower()
  if diff == "easy" or diff == "20":
    turn_numb = 20
  elif diff == "medium" or diff == "15":
    turn_numb = 15
  elif diff == "hard" or diff == "10":
    turn_numb = 10
  elif diff == "extreme" or diff == "5":
    turn_numb = 5
  else:
    print("Invalid difficulty")
    print("")

#Asking the player for number of ships in the game
while ship_numb != 1 and ship_numb != 2 and ship_numb != 3:
  ship_numb = int(input("Enter number of ships (1, 2 or 3):   "))

#Asking player for length of ships
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

#Creates a random ship for the player to attack
if ship_numb == 1:
  ship_row = random_row(board)
  ship_col = random_col(board)
  
  if ship_len == 3:
    if ship_row == 0 or ship_row == 9:
      chance = half_chance
      if chance == 1:
        ship_row2 = ship_row
        ship_row3 = ship_row
        ship_col2 = ship_col + 1
        ship_col3 = ship_col + 2
      else:
        ship_row2 = ship_row
        ship_row3 = ship_row
        ship_col2 = ship_col - 1
        ship_col3 = ship_col - 2
      
    elif ship_col == 0 or ship_col == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2 = ship_row + 1
        ship_row3 = ship_row + 2
        ship_col2 = ship_col
        ship_col3 = ship_col
      else:
        ship_row2 = ship_row - 1
        ship_row3 = ship_row - 2
        ship_col2 = ship_col
        ship_col3 = ship_col
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2 = ship_row + 1
          ship_row3 = ship_row + 2
          ship_col2 = ship_col
          ship_col3 = ship_col
        else:
          ship_row2 = ship_row - 1
          ship_row3 = ship_row - 2
          ship_col2 = ship_col
          ship_col3 = ship_col 
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2 = ship_col + 1
          ship_col3 = ship_col + 2
          ship_row2 = ship_row
          ship_row3 = ship_row
        else:
          ship_col2 = ship_col - 1
          ship_col3 = ship_col - 2
          ship_row2 = ship_row
          ship_row3 = ship_row

  elif ship_len == 2:
    if ship_row == 0 or ship_row == 9:
      chance = half_chance
      if chance == 1:
        ship_row2 = ship_row
        ship_col2 = ship_col + 1
      else:
        ship_row2 = ship_row
        ship_col2 = ship_col - 1
    elif ship_col == 0 or ship_col == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2 = ship_row + 1
        ship_col2 = ship_col
      else:
        ship_row2 = ship_row - 1
        ship_col2 = ship_col
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2 = ship_row + 1
          ship_col2 = ship_col
        else:
          ship_row2 = ship_row - 1
          ship_col2 = ship_col
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2 = ship_col + 1
          ship_row2 = ship_row
        else:
          ship_col2 = ship_col - 1
          ship_row2 = ship_row

####################################
          
#Same code, but for 2 ships
elif ship_numb == 2:
  ship_row = random_row(board)
  ship_col = random_col(board)
  ship_row_2 = random_row(board)
  ship_col_2 = random_col(board)
  
  if ship_len == 3:
    if ship_row == 0 or ship_row == 9:
      chance = half_chance
      if chance == 1:
        ship_row2 = ship_row
        ship_row3 = ship_row
        ship_col2 = ship_col + 1
        ship_col3 = ship_col + 2
      else:
        ship_row2 = ship_row
        ship_row3 = ship_row
        ship_col2 = ship_col - 1
        ship_col3 = ship_col - 2
      
    elif ship_col == 0 or ship_col == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2 = ship_row + 1
        ship_row3 = ship_row + 2
        ship_col2 = ship_col
        ship_col3 = ship_col
      else:
        ship_row2 = ship_row - 1
        ship_row3 = ship_row - 2
        ship_col2 = ship_col
        ship_col3 = ship_col
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2 = ship_row + 1
          ship_row3 = ship_row + 2
          ship_col2 = ship_col
          ship_col3 = ship_col
        else:
          ship_row2 = ship_row - 1
          ship_row3 = ship_row - 2
          ship_col2 = ship_col
          ship_col3 = ship_col 
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2 = ship_col + 1
          ship_col3 = ship_col + 2
          ship_row2 = ship_row
          ship_row3 = ship_row
        else:
          ship_col2 = ship_col - 1
          ship_col3 = ship_col - 2
          ship_row2 = ship_row
          ship_row3 = ship_row

  elif ship_len == 2:
    if ship_row == 0 or ship_row == 9:
      chance = half_chance
      if chance == 1:
        ship_row2 = ship_row
        ship_col2 = ship_col + 1
      else:
        ship_row2 = ship_row
        ship_col2 = ship_col - 1
    elif ship_col == 0 or ship_col == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2 = ship_row + 1
        ship_col2 = ship_col
      else:
        ship_row2 = ship_row - 1
        ship_col2 = ship_col
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2 = ship_row + 1
          ship_col2 = ship_col
        else:
          ship_row2 = ship_row - 1
          ship_col2 = ship_col
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2 = ship_col + 1
          ship_row2 = ship_row
        else:
          ship_col2 = ship_col - 1
          ship_row2 = ship_row
          
  ##############################################
  #The code for applying the length of the ship(s)
  if ship_len == 3:
    if ship_row_2 == 0 or ship_row_2 == 9:
      chance = half_chance
      if chance == 1:
        ship_row2_2 = ship_row_2
        ship_row3_2 = ship_row_2
        ship_col2_2 = ship_col_2 + 1
        ship_col3_2 = ship_col_2 + 2
      else:
        ship_row2_2 = ship_row_2
        ship_row3_2 = ship_row_2
        ship_col2_2 = ship_col_2 - 1
        ship_col3_2 = ship_col_2 - 2
      
    elif ship_col == 0 or ship_col == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2_2 = ship_row_2 + 1
        ship_row3_2 = ship_row_2 + 2
        ship_col2_2 = ship_col_2
        ship_col3_2 = ship_col_2
      else:
        ship_row2_2 = ship_row_2 - 1
        ship_row3_2 = ship_row_2 - 2
        ship_col2_2 = ship_col_2
        ship_col3_2 = ship_col_2
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2_2 = ship_row_2 + 1
          ship_row3_2 = ship_row_2 + 2
          ship_col2_2 = ship_col_2
          ship_col3_2 = ship_col_2
        else:
          ship_row2_2 = ship_row_2 - 1
          ship_row3_2 = ship_row_2 - 2
          ship_col2_2 = ship_col_2
          ship_col3_2 = ship_col_2
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2_2 = ship_col_2 + 1
          ship_col3_2 = ship_col_2 + 2
          ship_row2_2 = ship_row_2
          ship_row3_2 = ship_row_2
        else:
          ship_col2_2 = ship_col_2 - 1
          ship_col3_2 = ship_col_2 - 2
          ship_row2_2 = ship_row_2
          ship_row3_2 = ship_row_2

  elif ship_len == 2:
    if ship_row_2 == 0 or ship_row_2 == 9:
      chance = half_chance
      if chance == 1:
        ship_row2_2 = ship_row_2
        ship_col2_2 = ship_col_2 + 1
      else:
        ship_row2_2 = ship_row_2
        ship_col2_2 = ship_col_2 - 1
    elif ship_col_2 == 0 or ship_col_2 == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2_2 = ship_row_2 + 1
        ship_col2_2 = ship_col_2
      else:
        ship_row2_2 = ship_row_2 - 1
        ship_col2_2 = ship_col_2
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2_2 = ship_row_2 + 1
          ship_col2_2 = ship_col_2
        else:
          ship_row2_2 = ship_row_2 - 1
          ship_col2_2 = ship_col_2
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2_2 = ship_col_2 + 1
          ship_row2_2 = ship_row_2
        else:
          ship_col2_2 = ship_col_2 - 1
          ship_row2_2 = ship_row_2

#########################################
#Same as before, but for 3 ships
elif ship_numb == 3:
  ship_row = random_row(board)
  ship_col = random_col(board)
  ship_row_2 = random_row(board)
  ship_col_2 = random_col(board)
  ship_row_3 = random_row(board)
  ship_col_3 = random_col(board)
  
  if ship_len == 3:
    if ship_row == 0 or ship_row == 9:
      chance = half_chance
      if chance == 1:
        ship_row2 = ship_row
        ship_row3 = ship_row
        ship_col2 = ship_col + 1
        ship_col3 = ship_col + 2
      else:
        ship_row2 = ship_row
        ship_row3 = ship_row
        ship_col2 = ship_col - 1
        ship_col3 = ship_col - 2
      
    elif ship_col == 0 or ship_col == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2 = ship_row + 1
        ship_row3 = ship_row + 2
        ship_col2 = ship_col
        ship_col3 = ship_col
      else:
        ship_row2 = ship_row - 1
        ship_row3 = ship_row - 2
        ship_col2 = ship_col
        ship_col3 = ship_col
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2 = ship_row + 1
          ship_row3 = ship_row + 2
          ship_col2 = ship_col
          ship_col3 = ship_col
        else:
          ship_row2 = ship_row - 1
          ship_row3 = ship_row - 2
          ship_col2 = ship_col
          ship_col3 = ship_col 
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2 = ship_col + 1
          ship_col3 = ship_col + 2
          ship_row2 = ship_row
          ship_row3 = ship_row
        else:
          ship_col2 = ship_col - 1
          ship_col3 = ship_col - 2
          ship_row2 = ship_row
          ship_row3 = ship_row

  elif ship_len == 2:
    if ship_row == 0 or ship_row == 9:
      chance = half_chance
      if chance == 1:
        ship_row2 = ship_row
        ship_col2 = ship_col + 1
      else:
        ship_row2 = ship_row
        ship_col2 = ship_col - 1
    elif ship_col == 0 or ship_col == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2 = ship_row + 1
        ship_col2 = ship_col
      else:
        ship_row2 = ship_row - 1
        ship_col2 = ship_col
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2 = ship_row + 1
          ship_col2 = ship_col
        else:
          ship_row2 = ship_row - 1
          ship_col2 = ship_col
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2 = ship_col + 1
          ship_row2 = ship_row
        else:
          ship_col2 = ship_col - 1
          ship_row2 = ship_row
          
  ##########################################        
  if ship_len == 3:
    if ship_row_2 == 0 or ship_row_2 == 9:
      chance = half_chance
      if chance == 1:
        ship_row2_2 = ship_row_2
        ship_row3_2 = ship_row_2
        ship_col2_2 = ship_col_2 + 1
        ship_col3_2 = ship_col_2 + 2
      else:
        ship_row2_2 = ship_row_2
        ship_row3_2 = ship_row_2
        ship_col2_2 = ship_col_2 - 1
        ship_col3_2 = ship_col_2 - 2
      
    elif ship_col_2 == 0 or ship_col_2 == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2_2 = ship_row_2 + 1
        ship_row3_2 = ship_row_2 + 2
        ship_col2_2 = ship_col_2
        ship_col3_2 = ship_col_2
      else:
        ship_row2_2 = ship_row_2 - 1
        ship_row3_2 = ship_row_2 - 2
        ship_col2_2 = ship_col_2
        ship_col3_2 = ship_col_2
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2_2 = ship_row_2 + 1
          ship_row3_2 = ship_row_2 + 2
          ship_col2_2 = ship_col_2
          ship_col3_2 = ship_col_2
        else:
          ship_row2_2 = ship_row_2 - 1
          ship_row3_2 = ship_row_2 - 2
          ship_col2_2 = ship_col_2
          ship_col3_2 = ship_col_2 
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2_2 = ship_col_2 + 1
          ship_col3_2 = ship_col_2 + 2
          ship_row2_2 = ship_row_2
          ship_row3_2 = ship_row_2
        else:
          ship_col2_2 = ship_col_2 - 1
          ship_col3_2 = ship_col_2 - 2
          ship_row2_2 = ship_row_2
          ship_row3_2 = ship_row_2

  elif ship_len == 2:
    if ship_row_2 == 0 or ship_row_2 == 9:
      chance = half_chance
      if chance == 1:
        ship_row2_2 = ship_row_2
        ship_col2_2 = ship_col_2 + 1
      else:
        ship_row2_2 = ship_row_2
        ship_col2_2 = ship_col_2 - 1
    elif ship_col_2 == 0 or ship_col_2 == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2_2 = ship_row_2 + 1
        ship_col2_2 = ship_col_2
      else:
        ship_row2_2 = ship_row_2 - 1
        ship_col2_2 = ship_col_2
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2_2 = ship_row_2 + 1
          ship_col2_2 = ship_col_2
        else:
          ship_row2_2 = ship_row_2 - 1
          ship_col2_2 = ship_col_2
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2_2 = ship_col_2 + 1
          ship_row2_2 = ship_row_2
        else:
          ship_col2_2 = ship_col_2 - 1
          ship_row2_2 = ship_row_2
  #######################################
  if ship_len == 3:
    if ship_row_3 == 0 or ship_row_3 == 9:
      chance = half_chance
      if chance == 1:
        ship_row2_3 = ship_row_3
        ship_row3_3 = ship_row_3
        ship_col2_3 = ship_col_3 + 1
        ship_col3_3 = ship_col_3 + 2
      else:
        ship_row2_3 = ship_row_3
        ship_row3_3 = ship_row_3
        ship_col2_3 = ship_col_3 - 1
        ship_col3_3 = ship_col_3 - 2
      
    elif ship_col_3 == 0 or ship_col_3 == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2_3 = ship_row_3 + 1
        ship_row3_3 = ship_row_3 + 2
        ship_col2_3 = ship_col_3
        ship_col3_3 = ship_col_3
      else:
        ship_row2_3 = ship_row_3 - 1
        ship_row3_3 = ship_row_3 - 2
        ship_col2_3 = ship_col_3
        ship_col3_3 = ship_col_3
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2_3 = ship_row_3 + 1
          ship_row3_3 = ship_row_3 + 2
          ship_col2_3 = ship_col_3
          ship_col3_3 = ship_col_3
        else:
          ship_row2_3 = ship_row_3 - 1
          ship_row3_3 = ship_row_3 - 2
          ship_col2_3 = ship_col_3
          ship_col3_3 = ship_col_3 
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2_3 = ship_col_3 + 1
          ship_col3_3 = ship_col_3 + 2
          ship_row2_3 = ship_row_3
          ship_row3_3 = ship_row_3
        else:
          ship_col2_3 = ship_col_3 - 1
          ship_col3_3 = ship_col_3 - 2
          ship_row2_3 = ship_row_3
          ship_row3_3 = ship_row_3

  elif ship_len == 2:
    if ship_row_3 == 0 or ship_row_3 == 9:
      chance = half_chance
      if chance == 1:
        ship_row2_3 = ship_row_3
        ship_col2_3 = ship_col_3 + 1
      else:
        ship_row2_3 = ship_row_3
        ship_col2_3 = ship_col_3 - 1
    elif ship_col_3 == 0 or ship_col_3 == 9:
      chance = half_chance() 
      if chance == 1:
        ship_row2_3 = ship_row_3 + 1
        ship_col2_3 = ship_col_3
      else:
        ship_row2_3 = ship_row_3 - 1
        ship_col2_3 = ship_col_3
    else:    
      chance = half_chance()
      if chance == 1:
        chance == half_chance()
        if chance == 1:
          ship_row2_3 = ship_row_3 + 1
          ship_col2_3 = ship_col_3
        else:
          ship_row2_3 = ship_row_3 - 1
          ship_col2_3 = ship_col_3
      else:
        chance = half_chance()
        if half_chance() == 1:
          ship_col2_3 = ship_col_3 + 1
          ship_row2_3 = ship_row_3
        else:
          ship_col2_3 = ship_col_3 - 1
          ship_row2_3 = ship_row_3
          
###################################
#The debug code that displays the location of the ship to the player
if ship_numb == 1:
  if ship_len == 1:
    print(ship_row, ship_col)
  elif ship_len == 2:
    print(ship_row, ship_col)
    print(ship_row2, ship_col2)
  elif ship_len == 3:
    print(ship_row, ship_col)
    print(ship_row2, ship_col2)
    print(ship_row3, ship_col3)
    
elif ship_numb == 2:
  if ship_len == 1:
    print(ship_row, ship_col)
    print("")
    print(ship_row_2, ship_col_2)
  elif ship_len == 2:
    print(ship_row, ship_col)
    print(ship_row2, ship_col2)
    print("")
    print(ship_row_2, ship_col_2)
    print(ship_row2_2, ship_col2_2)
  elif ship_len == 3:
    print(ship_row, ship_col)
    print(ship_row2, ship_col2)
    print(ship_row3, ship_col3)
    print("")
    print(ship_row_2, ship_col_2)
    print(ship_row2_2, ship_col2_2)
    print(ship_row3_2, ship_col3_2)
    
elif ship_numb == 3:
  if ship_len == 1:
    print(ship_row, ship_col)
    print("")
    print(ship_row_2, ship_col_2)
    print("")
    print(ship_row_3, ship_col_3)
  elif ship_len == 2:
    print(ship_row, ship_col)
    print(ship_row2, ship_col2)
    print("")
    print(ship_row_2, ship_col_2)
    print(ship_row2_2, ship_col2_2)
    print("")
    print(ship_row_3, ship_col_3)
    print(ship_row2_3, ship_col2_3)
  elif ship_len == 3:
    print(ship_row, ship_col)
    print(ship_row2, ship_col2)
    print(ship_row3, ship_col3)
    print("")
    print(ship_row_2, ship_col_2)
    print(ship_row2_2, ship_col2_2)
    print(ship_row3_2, ship_col3_2)
    print("")
    print(ship_row_3, ship_col_3)
    print(ship_row2_3, ship_col2_3)
    print(ship_row3_3, ship_col3_3)
###################################

print_board(board)

#While loop to display the number of guesses and turns left
while turn_count <= turn_numb:
    print("")
    print("Turn = " + str(turn_count))
    print("")

    #Variables to store the guess of the player
    guess_row = int(input("Guess Row: ")) - 1
    guess_col = int(input("Guess Col: ")) - 1
    if ship_numb == 1:
      if ship_len == 1:

        #What happens if the guess is correct and the ship is sunk
        if (guess_row == ship_row and guess_col == ship_col):
          print("")
          print("Congratulations! You sunk the battleship!")
          board[guess_row][guess_col] = "!"
          if diff == "easy":
            print("Try a more difficult level now!")
          elif diff == "medium":
            print("Perhaps you could try a harder level now!")
          elif diff == "hard":
            print("You are really good at this! Now try our hardest level!")
          else:
            print("You are a master at this game!")
                
          print("")
          print("Final Board:")
          print_board(board)
          break

        #What happens if the guess is not correct
        else:
            if guess_row not in range(10) or guess_col not in range(10):
                print("Oops, that's not even in the ocean.")
                turn_count = turn_count - 1
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
                turn_count = turn_count - 1
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)

      #The same code but for different lengthed ships        
      elif ship_len == 2:
        if ((guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row2 and guess_col == ship_col2)) and (board[guess_row][guess_col] != "!"):
          print("")
          print("Congratulations! You hit the battleship!")
          board[guess_row][guess_col] = "!"
          print_board(board)
          hit = hit + 1
          if hit == ship_len:
            print("")
            print("Congratulations! You sunk a battleship!")
            board[guess_row][guess_col] = "!"
            if ship_down == ship_numb:
              print("")
              print("Well done! You sunk all the ships!")
              if diff == "easy":
                print("Try a more difficult level now!")
              elif diff == "medium":
                print("Perhaps you could try a harder level now!")
              elif diff == "hard":
                print("You are really good at this! Now try our hardest level!")
              else:
                print("You are a master at this game!")
                  
              print("")
              print("Final Board:")
              print_board(board)
              break
              quit()
        else:
        
            if guess_row not in range(10) or guess_col not in range(10):
                print("Oops, that's not even in the ocean.")
                turn_count = turn_count - 1
            elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!"):
                print("You guessed that one already.")
                turn_count = turn_count - 1
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)
            
      elif ship_len == 3:
        if ((guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row2 and guess_col == ship_col2) or (guess_row == ship_row3 and guess_col == ship_col3)) and (board[guess_row][guess_col] != "!"):
          print("")
          print("Congratulations! You hit the battleship!")
          board[guess_row][guess_col] = "!"
          print_board(board)
          hit = hit + 1
          if hit == ship_len:
            print("")
            print("Congratulations! You sunk a battleship!")
            board[guess_row][guess_col] = "!"
            if ship_down == ship_numb:
              print("")
              print("Well done! You sunk all the ships!")
              if diff == "easy":
                print("Try a more difficult level now!")
              elif diff == "medium":
                print("Perhaps you could try a harder level now!")
              elif diff == "hard":
                print("You are really good at this! Now try our hardest level!")
              else:
                print("You are a master at this game!")
                  
              print("")
              print("Final Board:")
              print_board(board)
              break
              quit()
        else:
            if guess_row not in range(10) or guess_col not in range(10):
              print("Oops, that's not even in the ocean.")
              turn_count = turn_count - 1
            elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!"):
              print("You guessed that one already.")
              turn_count = turn_count - 1
            else:
              print("You missed the battleship!")
              board[guess_row][guess_col] = "X"
              print_board(board)
              
#################################################################################################################
    #Same code but for a different amount of ships
    elif ship_numb == 2:
      if ship_len == 1:
        if (guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row_2 and guess_col == ship_col_2):
          print("")
          print("Congratulations! You sunk a battleship!")
          board[guess_row][guess_col] = "!"
          ship_down = ship_down + 1
          
          if ship_down == ship_numb:
            print("")
            print("Well done! You sunk all the ships!")
            if diff == "easy":
              print("Try a more difficult level now!")
            elif diff == "medium":
              print("Perhaps you could try a harder level now!")
            elif diff == "hard":
              print("You are really good at this! Now try our hardest level!")
            else:
              print("You are a master at this game!")
              
            print("")
            print("Final Board:")
            print_board(board)
            break
          
        else:
            if guess_row not in range(10) or guess_col not in range(10):
                print("Oops, that's not even in the ocean.")
                turn_count = turn_count - 1
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
                turn_count = turn_count - 1
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)
              
      elif ship_len == 2:
        if (((guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row2 and guess_col == ship_col2)) or ((guess_row == ship_row_2 and guess_col == ship_col_2) or (guess_row == ship_row2_2) and guess_col == ship_col2_2)) and (board[guess_row][guess_col] != "!"):
          print("")
          print("Congratulations! You hit the battleship!")
          board[guess_row][guess_col] = "!"
          print_board(board)
          hit = hit + 1
          if hit == ship_len:
            print("")
            print("Congratulations! You sunk a battleship!")
            board[guess_row][guess_col] = "!"
            if ship_down == ship_numb:
              print("")
              print("Well done! You sunk all the ships!")
              if diff == "easy":
                print("Try a more difficult level now!")
              elif diff == "medium":
                print("Perhaps you could try a harder level now!")
              elif diff == "hard":
                print("You are really good at this! Now try our hardest level!")
              else:
                print("You are a master at this game!")
                  
              print("")
              print("Final Board:")
              print_board(board)
              break
              quit()
        else:
        
            if guess_row not in range(10) or guess_col not in range(10):
                print("Oops, that's not even in the ocean.")
                turn_count = turn_count - 1
            elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!"):
                print("You guessed that one already.")
                turn_count = turn_count - 1
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)
            
      elif ship_len == 3:
        if ((guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row2 and guess_col == ship_col2) or (guess_row == ship_row3 and guess_col == ship_col3)) or ((guess_row == ship_row_2 and guess_col == ship_col_2) or (guess_row == ship_row_2 and guess_col == ship_col_2) or (guess_row == ship_row3_2 and guess_col == ship_col3_2)) and (board[guess_row][guess_col] != "!"):
          print("")
          print("Congratulations! You hit the battleship!")
          board[guess_row][guess_col] = "!"
          print_board(board)
          hit = hit + 1
          if hit == ship_len:
            print("")
            print("Congratulations! You sunk a battleship!")
            board[guess_row][guess_col] = "!"
            if ship_down == ship_numb:
              print("")
              print("Well done! You sunk all the ships!")
              if diff == "easy":
                print("Try a more difficult level now!")
              elif diff == "medium":
                print("Perhaps you could try a harder level now!")
              elif diff == "hard":
                print("You are really good at this! Now try our hardest level!")
              else:
                print("You are a master at this game!")
                  
              print("")
              print("Final Board:")
              print_board(board)
              break
              quit()
        else:
            if guess_row not in range(10) or guess_col not in range(10):
              print("Oops, that's not even in the ocean.")
              turn_count = turn_count - 1
            elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!"):
              print("You guessed that one already.")
              turn_count = turn_count - 1
            else:
              print("You missed the battleship!")
              board[guess_row][guess_col] = "X"
              print_board(board)
              
#######################################################################################################
    elif ship_numb == 3:
      if ship_len == 1:
        if (guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row_2 and guess_col == ship_col_2) or (guess_row == ship_row_3 and guess_col == ship_col_3):
          print("")
          print("Congratulations! You sunk a battleship!")
          board[guess_row][guess_col] = "!"
          ship_down = ship_down + 1
            
          if ship_down == ship_numb:
            print("")
            print("Well done! You sunk all the ships!")
            if diff == "easy":
              print("Try a more difficult level now!")
            elif diff == "medium":
              print("Perhaps you could try a harder level now!")
            elif diff == "hard":
              print("You are really good at this! Now try our hardest level!")
            else:
              print("You are a master at this game!")
              
            print("")
            print("Final Board:")
            print_board(board)
            break
          
        else:
            if guess_row not in range(10) or guess_col not in range(10):
                print("Oops, that's not even in the ocean.")
                turn_count = turn_count - 1
            elif board[guess_row][guess_col] == "X":
                print("You guessed that one already.")
                turn_count = turn_count - 1
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)
              
      elif ship_len == 2:
        if (((guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row2 and guess_col == ship_col2)) or ((guess_row == ship_row_2 and guess_col == ship_col_2) or (guess_row == ship_row2_2 and guess_col == ship_col2_2)) or ((guess_row == ship_row_3 and guess_col == ship_col_3) or (guess_row == ship_row2_3 and guess_col == ship_col2_3))) and (board[guess_row][guess_col] != "!"):
          print("")
          print("Congratulations! You hit the battleship!")
          board[guess_row][guess_col] = "!"
          print_board(board)
          hit = hit + 1
          if hit == ship_len:
            print("")
            print("Congratulations! You sunk a battleship!")
            board[guess_row][guess_col] = "!"
            if ship_down == ship_numb:
              print("")
              print("Well done! You sunk all the ships!")
              if diff == "easy":
                print("Try a more difficult level now!")
              elif diff == "medium":
                print("Perhaps you could try a harder level now!")
              elif diff == "hard":
                print("You are really good at this! Now try our hardest level!")
              else:
                print("You are a master at this game!")
                  
              print("")
              print("Final Board:")
              print_board(board)
              break
              quit()
        else:
        
            if guess_row not in range(10) or guess_col not in range(10):
                print("Oops, that's not even in the ocean.")
                turn_count = turn_count - 1
            elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!"):
                print("You guessed that one already.")
                turn_count = turn_count - 1
            else:
                print("You missed the battleship!")
                board[guess_row][guess_col] = "X"
                print_board(board)
            
      elif ship_len == 3:
        if (((guess_row == ship_row and guess_col == ship_col) or (guess_row == ship_row2 and guess_col == ship_col2) or (guess_row == ship_row3 and guess_col == ship_col3)) or ((guess_row == ship_row_2 and guess_col == ship_col_2) or (guess_row == ship_row2_2 and guess_col == ship_col2_2) or (guess_row == ship_row3_2 and guess_col == ship_col3_2)) or ((guess_row == ship_row_3 and guess_col == ship_col_3) or (guess_row == ship_row2_3 and guess_col == ship_col2_3) or (guess_row == ship_row3_3 and guess_col == ship_col3_3))) and (board[guess_row][guess_col] != "!"):
          print("")
          print("Congratulations! You hit the battleship!")
          board[guess_row][guess_col] = "!"
          print_board(board)
          hit = hit + 1
          if hit == ship_len:
            print("")
          print("Congratulations! You sunk a battleship!")
          board[guess_row][guess_col] = "!"
          if ship_down == ship_numb:
            print("")
            print("Well done! You sunk all the ships!")
            if diff == "easy":
              print("Try a more difficult level now!")
            elif diff == "medium":
              print("Perhaps you could try a harder level now!")
            elif diff == "hard":
              print("You are really good at this! Now try our hardest level!")
            else:
              print("You are a master at this game!")
                  
            print("")
            print("Final Board:")
            print_board(board)
            break
            quit()
        else:
            if guess_row not in range(10) or guess_col not in range(10):
              print("Oops, that's not even in the ocean.")
              turn_count = turn_count - 1
            elif (board[guess_row][guess_col] == "X") or (board[guess_row][guess_col] == "!"):
              print("You guessed that one already.")
              turn_count = turn_count - 1
            else:
              print("You missed the battleship!")
              board[guess_row][guess_col] = "X"
              print_board(board)

    #The "Game Over" screen and what information it displays        
    if turn_count == turn_numb:
        print("")
        print("")
        print("Game Over")
        if ship_numb == 1:
          if ship_len == 1:
            print("The ship was in row " + str((ship_row) + 1) + ", col " + str((ship_col) + 1))
          elif ship_len == 2:
            print("The ship was in row " + str((ship_row) + 1) + " and " + str((ship_row2) + 1) + ", col " + str((ship_col) + 1) + " and " + str((ship_col2)+ 1))
          elif ship_len == 3:
            print("The ship was in row " + str((ship_row) + 1) + ", " + str((ship_row2) + 1) + " and " + str((ship_row3) + 1) + ", col " + str((ship_col) + 1) + ", " + str((ship_col2) + 1) + " and " + str((ship_col3) + 1))

        elif ship_numb == 2:
          if ship_len == 1:
            print("The first ship was in row " + str((ship_row) + 1) + ", col " + str((ship_col) + 1))
            print("The second ship was in row " + str((ship_row_2) + 1) + ", col " + str((ship_col_2) + 1))
          elif ship_len == 2:
            print("The first ship was in row " + str((ship_row) + 1) + " and " + str((ship_row2) + 1) + ", col " + str((ship_col) + 1) + " and " + str((ship_col2) + 1))
            print("The second ship was in row " + str((ship_row_2) + 1) + " and " + str((ship_row2_2) + 1) + ", col " + str((ship_col_2) + 1) + " and " + str((ship_col2_2) + 1))
          elif ship_len == 3:
            print("The first ship was in row " + str((ship_row) + 1) + ", " + str((ship_row2) + 1) + " and " + str((ship_row3) + 1) + ", col " + str((ship_col) + 1) + ", " + str((ship_col2) + 1) + " and " + str((ship_col3) + 1))
            print("The second ship was in row " + str((ship_row_2) + 1) + ", " + str((ship_row2_2) + 1) + " and " + str((ship_row3_2) + 1) + ", col " + str((ship_col_2) + 1) + ", " + str((ship_col2_2) + 1) + " and " + str((ship_col3_2) + 1))

        elif ship_numb == 3:
          if ship_len == 1:
            print("The first ship was in row " + str((ship_row) + 1) + ", col " + str((ship_col) + 1))
            print("The second ship was in row " + str((ship_row_2) + 1) + ", col " + str((ship_col_2) + 1))
            print("The third ship was in row " + str((ship_row_3) + 1) + ", col " + str((ship_col_3) + 1))
          elif ship_len == 2:
            print("The first ship was in row " + str((ship_row) + 1) + " and " + str((ship_row2) + 1) + ", col " + str((ship_col) + 1) + " and " + str((ship_col2) + 1))
            print("The second ship was in row " + str((ship_row_2) + 1) + " and " + str((ship_row2_2) + 1) + ", col " + str((ship_col_2) + 1) + " and " + str((ship_col2_2) + 1))
            print("The third ship was in row " + str((ship_row_3) + 1) + " and " + str((ship_row2_3) + 1) + ", col " + str((ship_col_3) + 1) + " and " + str((ship_col2_3) + 1))
          elif ship_len == 3:
            print("The first ship was in row " + str((ship_row) + 1) + ", " + str((ship_row2) + 1) + " and " + str((ship_row3) + 1) + ", col " + str((ship_col) + 1) + ", " + str((ship_col2) + 1) + " and " + str((ship_col3) + 1))
            print("The second ship was in row " + str((ship_row_2) + 1) + ", " + str((ship_row2_2) + 1) + " and " + str((ship_row3_2) + 1) + ", col " + str((ship_col_2) + 1) + ", " + str((ship_col2_2) + 1) + " and " + str((ship_col3_2) + 1))
            print("The third ship was in row " + str((ship_row_3) + 1) + ", " + str((ship_row2_3) + 1) + " and " + str((ship_row3_3) + 1) + ", col " + str((ship_col_3) + 1) + ", " + str((ship_col2_3) + 1) + " and " + str((ship_col3_3) + 1))

        
        if diff == "extreme" or diff == "5":
          print("You are not as good as you think! Chose an easier difficulty ;)")
        elif diff == "hard" or diff == "10":
          print("Should have picked an easier difficulty!")
        elif diff == "medium" or diff == "15":
          print("Perhaps you could try the easier difficulty next time")
        elif diff == "easy" or diff == "20":
          print("At least you tried :(")
        
    turn_count = turn_count + 1

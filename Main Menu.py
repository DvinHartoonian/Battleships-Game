
print("BATTLESHIPS\n\n\n\n\n\n\n\n\n\n\n\n\n")




choice = 0
while choice != "CPU" or "SOLO" or "2 PLAYER" or "2PLAYER":

    choice = input("Please enter if you would like to play solo, 2 player or CPU: ")
    choice = choice.upper()

    if choice == "CPU":
        import Battleships_CPU
    elif choice == "SOLO":
        import Battleships_1_player
    elif choice == "2 PLAYER" or "2PLAYER":
        import Battleships_2_player
    else:
        print("Invalid Input")
        

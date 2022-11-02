# Prints title
print("BATTLESHIPS")
print("")
print("")
print("")
play = "o"
play_again = True
while play_again == True:
    choice = 0
    # Loop for player to choose what mode they want to play
    while choice != "solo" and choice != "2player" and choice != "2 player" and choice != "two player" and choice != "cpu":
        choice = input("Please enter your mode: solo, 2 player or CPU   ")
        choice = choice.lower()
        # What happens when the player chooses "cpu"
        if choice == "cpu":
            import Battleships_CPU
            while play != "y" and play != "yes" and play != "n" and play != "no":
                play = input("Do you want to play again?   ")
                play = play.lower()
                if play == "y" or play == "yes":
                    play_again = True
                elif play == "n" or play == "no":
                    play_again = False
                else:
                    print("Invalid answer")
                    print("")
        # What happens when the player chooses "solo"
        elif choice == "solo":
            import Battleships_1_player
            while play != "y" and play != "yes" and play != "n" and play != "no":
                play = input("Do you want to play again?   ")
                play = play.lower()
                if play == "y" or play == "yes":
                    play_again = True
                elif play == "n" or play == "no":
                    play_again = False
                else:
                    print("Invalid answer")
                    print("")
        # What happens when the player chooses "2 player"
        elif choice == "2 player" or choice == "2player" or choice == "two player":
            import Battleships_2_player
            while play != "y" and play != "yes" and play != "n" and play != "no":
                play = input("Do you want to play again?   ")
                play = play.lower()
                if play == "y" or play == "yes":
                    play_again = True
                elif play == "n" or play == "no":
                    play_again = False
                else:
                    print("Invalid answer")
                    print("")
        else:
            print("Invalid Input")
        # If the player doesn't input something

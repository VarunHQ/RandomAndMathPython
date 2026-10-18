import random

while True:
    user_action = input("Enter a choice (Rock, Paper, Scissors): ")
    possible_action = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(possible_action)
    print("User choosen number is ", user_action , "Computer Choosen number is ", computer_choice)

    if user_action == computer_choice:
        print("Computer and User have choosen the same option. This game is a Tie!")

    elif user_action == "Rock":
        if computer_choice == "Scissors":
            print("User wins the game because rock smashes scissors")
        else:
            print("Computer wins the game because paper covers rock")

    elif user_action == "Paper":
        if computer_choice == "Rock":
            print("User wins the game because paper covers rock")
        else:
            print("Computer wins the Game because scisscors cut paper")
    elif user_action == "Scissors":
        if computer_choice == "Paper":
            print("User wins the game because scissors cut paper")
        else:
            print("Compuer wins the game because rock smashes scissors")

    play_again = input("Play again (Y/N): ")
    if play_again != "Y":
        break
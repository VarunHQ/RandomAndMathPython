import random
playing = True
number = str(random.randint(0,9))

print("I will generate a number between 0 - 9. You have to guess it!")
print("The game ends when you guess the correct number.")

while playing:
    guess = int(input("Enter your best guess: "))
    if number == guess:
        print("You have guessed the number correctly!")
        print("The number was ", number)
        break
    else:
        print("Wrong number please try again!")
import random
import math

print("Lucky number guessing")
lucky_number = random.randint(1, 10)
print("Your lucky number is:", lucky_number)

fun_choices = ["Play Nintendogs game", "Solve a math problem", "Play with toys", "Eat snacks"]
random_activity = random.choice(fun_choices)
print("Random activity for today:", random_activity)

print("\nGuess the secret number from 1 to 5!")
secret_number = random.randint(1, 5)

while True:
    guess = int(input("Enter your guess: "))

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess. Try again!")

decimal_number = float(input("\nEnter a decimal number: "))

print("Ceiling value:", math.ceil(decimal_number))
print("Floor value:", math.floor(decimal_number))

x = 5
y = -7
print("Copy sign result:", math.copysign(x, y))

negative_number = int(input("Enter a negative number: "))
print("Absolute value:", math.fabs(negative_number))

num1 = int(input("Enter first number for HCF: "))
num2 = int(input("Enter second number for HCF: "))

print("HCF is:", math.gcd(num1, num2))
print("\nLucky number guessing game summary")
print("Lucky Number:", lucky_number)
print("Random Activity:", random_activity)
print("Secret Number:", secret_number)
print("============================")
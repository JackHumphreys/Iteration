import random
guessed = False
number = random.randint(1,101)
noOfTurns = 0
while guessed == False:
    noOfTurns = noOfTurns + 1
    userGuess =int(input("Enter your guess for the number: "))
    if userGuess == number:
        guessed = True
    elif userGuess > number:
        print("The number you guessed is too high")
    else:
        print("The number you have guessed is too low")
print("You took {0} turns to guess the number".format(noOfTurns))
print("The number was: {0}".format(number))

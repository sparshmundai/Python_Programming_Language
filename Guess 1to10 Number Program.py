#Ask python program to imagine a random number
import random
print("""****Random number guess****
***** To win, guess a number between 1 and 10 ******
******in five turns****\n""")
def guessANumber():
    imagine = random.randrange(1,11)
    #Ask for the first guess from user
    noofturns = 1
    while noofturns <=5:
        guess = int(input("Provide your guess: "))
        if guess == imagine:
            print("You won the game, guessed number {} in {} turns!!!".format(guess, noofturns))
            break
        else:
            print("Try again")
        noofturns += 1
    print("Game over")

cont = input("\n Do you want to play, type y or n \n")
while cont != 'n':
    if cont == 'y':
        guessANumber()
    cont = input("\n Do you want to play, type y or n \n")

print("\n\nHave a good day\n")

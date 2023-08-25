#Ask python program to image a radom number
import random
print("""***Random Number Guess
        ***to win guess a word in list
        ***in five turns***\n""")
def guessword():
    imagine  = random.randrange(1,11)
    no_turns = 1
    while no_turns <=5:
        guess = int(input("guess a word: "))
        if guess == imagine:
            print("you won the game, guessed word {} in {} turns!!!!".format(guess,no_turns))
            break
        else:
            print("Better Luck Next Time")
        no_turns =+ 1
    

#Write a python program to guess a pronoun word
import random

print("""****Guess the Pronoun Word****
**** To Win The Game in four turns****\n""")

def guessword():
      wordlist = ["i", "you", "he", "she", "it", "we", "they", "me", "him", "her", "them"]
      imagine = random.randrange(12)
      wordguess = wordlist[imagine]
      #Ask for the user to guess the word
      noturns = 1
      while noturns <= 4:
            guess = input("Guess a word: ")
            if guess == wordguess:
                  print("You won the game, guessed word {} in {} turns!!!".format(guess, noturns))
                  break
            else:
                  print("Try again")
                  noturns += 1
                  print("Game Over, you lose the game")

conti = input("\n Do you want to play game, type yes or no \n")
while conti != 'no':
    if conti == 'yes':
          guessword()
          conti = input("\n Do you want to play game, type y or n \n")
    else:
          input("Do you want to exit the game? ")



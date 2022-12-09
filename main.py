import random
from lives import livesGuesses

print(
    "The hangman game has begun and a word has been choosen. You have 6 lives.")
  
list = [
    "penguin", "food", "animals", "location", "ghost", "fire", "heart", "meter", "rizz"
  ]
word = random.choice(list)
lives = 6
guess = ""
  
while len(guess) < len(word) - 1:
  guess += "_"
print(''.join(guess))

guess = guess.split("_")
livesGuesses(lives, word, guess)



 


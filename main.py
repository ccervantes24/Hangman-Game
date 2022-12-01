from random import random 
import random

print("The hangman game will begin and a word has been choosen. You will have 6 lives.")


list = ["penguin", "food", "animals", "location", "ghost"]
word = random.choice(list)
print(word)
lives = 6


while True:
  letter= input("Enter a letter:")
  for i in word.split():
    if i == letter:
      print(i)
    else:
      print("You lost a live. Try again.")
      lives -= 1
  if lives == 0:
    print("You lost")
    break

    
     
    
  





def livesGuesses(lives, word, guess):
  while lives > 0:
    letter = input("guess a character: ")  #if letter is found in word
    if letter in word:
      for index in (idx for idx,l in enumerate(word) if l == letter):
        guess[index] = letter
    # index = word.index(letter)
    # #index1 = word.rindex(letter,index)
    # del guess[index]
    # #del guess[index1]
    # guess.insert(index, letter)
    # #guess.insert(index1, letter)
        print(guess)
    elif letter not in word:  #if letter not in word
      lives -= 1
      print("Wrong ")
      print(f"You have {lives} lives left")
    # elif lives == 0:
    #       print("You have lost, better luck next time")
    #       print(f"The word was {word}")
    #       break
    # elif guess == word:
    #       print("You Win This Time")
    # break

    if lives == 0:
      print("You lost, better luck next time ")  #defeat message
      print(f"The word was {word} ")
      break



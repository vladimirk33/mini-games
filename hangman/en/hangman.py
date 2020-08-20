import random

def start_game():
  guess = input('Type "play" to play the game, "exit" to quit: ')
  if guess == "play":
    play()
  elif guess == "exit":
    return False
  else:
    start_game()

def play():
  MAX_WRONG = 8
  WORDS = ('python', 'java', 'kotlin', 'javascript')
  correct_word = random.choice(WORDS)
  cypher_word = '-' * len(correct_word)
  wrong = 0
  used = set()
  while wrong != MAX_WRONG:
    print(f"\n{cypher_word}")
    guess = input('Input a letter: ')
    if guess in used:
      print("You already typed this letter")
      continue
    elif len(guess) != 1:
      print("You should input a single letter")
      continue
    elif guess.isupper() or not guess.isalpha():
      print("It is not an ASCII lowercase letter")
      continue
    if guess in correct_word:
        new = ''
        for i in range(len(correct_word)):
            if guess == correct_word[i]:
                new += guess
            else:
                new += cypher_word[i]
        cypher_word = new
        if cypher_word == correct_word:
          break
    else:
      print("No such letter in the word")
      wrong += 1
    used.add(guess)
  if wrong == MAX_WRONG:
    print("You are hanged!")
  else:
    print(f"You guessed the word {correct_word}!\nYou survived!")

def main():
  print("H A N G M A N")
  start_game()

if __name__ == "__main__":
  main()
import random
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = '''
88                                                                            
88                                                                            
88                                                                            
88,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYb,d8 88,dPYba,,adPYba,  ,adPPYYba,  8b,dPPYba, 
88P'    "8a ""     `Y8 88P'   `"8a a8"    `Y88 88P'   "88"    "8a ""     `Y8  88P'   `"8a 
88       88 ,adPPPPP88 88       88 8b       88 88      88      88 ,adPPPPP88  88       88 
88       88 88,    ,88 88       88 "8a,   ,d88 88      88      88 88,    ,88  88       88 
88       88 `"8bbdP"Y8 88       88  `"YbbdP"Y8 88      88      88 `"8bbdP"Y8  88       88 
                                    aa,    ,88                                
                                     "Y8bbdP"                                 
'''

word_list = ["spaghetti", "pizza", "hamburger", "chocolate", "broccoli", "germany", "japan", "brazil", "australia", "canada", "argentina", "portugal", "strawberry", "blueberry", "raspberry", "watermelon", "pineapple", "elephant", "giraffe", "kangaroo", "hippopotamus", "butterfly", "dolphin", "table", "chair", "computer", "window", "garden", "picture", "music", "travel", "family", "friend", "school", "planet", "flower", "animal", "country"]


lives = 6


print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print("Word to guess: " + display)


    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a LIFE!!")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"the correct word you trying to guess is: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])

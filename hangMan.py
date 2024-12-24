import random

hangman = '''
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

print(hangman)

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
# print(chosen_word)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print(f"Word Of Guess!  {placeholder}\n")

game_over = False

correct_guess = []

while not game_over:

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guess.append(letter)
        elif letter in correct_guess:
            display += letter
        else:
            display += " _ "

    print(f" {display} ")

    #for game over
    if "_" not in display:
        game_over = True
        print("Win!!")

# Word guessing game!! Guess The Word & be the winner
# M N Makola 2023 (Python)

from random import randrange #I import randrange to randomize the secret word
from words import secret_words, clues


print("\t***************** Hello And Welcome To My Word Guessing Game.************")
print("\t***************** Guess The Word And Be A The Winner ************\n")


# Assigning variables and lists to be used
random = randrange(3)               #I assign a random number to the variable random
current_word = secret_words[random] #I use random to index a word from the list of secret words
user_guess = ""
chances = 10
game_on = False
clue = clues[random]    
player = input("Enter Your Name: ").title().strip()
word_state = len(current_word) * "_"
letters = []

print("")

# Functions
# Checking the secret word's legnth to give a clue to player
def word_lenght():
    current_word_length = len(current_word)
    print(f"{player} the word has {current_word_length} characters\n")

# Function to check if the letters are in the secret word
def check_letters():
    for letter in user_guess:
        if letter in current_word:
            if letter not in letters:
                letters.append(letter)
    

# Function to print hints for player
def get_hint():
    print(f"Here is a clue {player}: {clue}\n")
     

# checking if the users guess is correct 
def check_guess():
    if user_guess == current_word:
        print(f"Correct Word {player}. You win\n")   
    else:
        print(f"Sorry {player}, Wrong Guess, You have {chances - 1} chances left to play\n")


# User interaction. Start Game

while not game_on:
    start = input(f"{player} Begin [y/n]: ")
    if start == "y":
        game_on = True
        print(f"\t\t\tLets Get Started {player}\n")
    elif start == "n":
        game_on = False
    else:
        print(f"{player} enter y for yes and n for no.\n")     

print(f"\t*********** Welcome {player}. You Can Now Begin **********")
print(f"\t\t\t*********** Goodluck ********** \n")

# game loop with conditions on when the game should play
while chances != 0 and game_on:
        
        print(f"\t***********{player}. You Have {chances} Chances To Guess The Word**********")
        
        get_hint()
        word_lenght()
        check_letters()
        print(f"{player} These letters are in the word: {letters} ")
        print(word_state)

        user_guess = input(f"Enter your guess\n{player}: ").title().strip()    
        check_guess()
        chances -= 1
        
        if user_guess == current_word:
            game_on = False
            break
        
        
        
                 
        
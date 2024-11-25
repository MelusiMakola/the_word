# M N Makola
# Hangman(Beginner Project #2)

import random

#List of words
words = ["python","elonmusk", "desire", "love", "human", "time", "space", "grow"] 

# Randomly selecting words from list
chosen_word = random.choice(words)

# player attempt
attempts = 10

# Substitute for letters player has not guessed
word_subsitute = ["_" for _ in chosen_word]

print(f"Welcome To My Hangman Game")

# Game loop
while (attempts != 0) and ("_" in word_subsitute):
#     \n to go to a new line and " ".join(word_subsitute) 
#      is to join and separate the strings in word_substitute 
#     using " " an empty String
    print("\n" + " ".join(word_subsitute))

    print(f"\nHere is a clue: \nThis word has the letter {chosen_word[random.randint(0,len(chosen_word)-1)]}\n")

    print("1. Exit")

    guess = input("Guess a Letter: ").strip().lower()
    
    



    if guess in chosen_word:
        
        guess_index = chosen_word.index(guess)    
            
        # codition to check the player guess
        if len(guess) > 1:
            print("Please Enter One Character At A Time!!")
        
        elif guess not in word_subsitute:        
            word_subsitute.pop(guess_index)
            word_subsitute.insert(guess_index, guess)
            print(f"\nGuessed Letter: {guess}. Great Guess!!\n")

        else:
            attempts -= 1
            print(f"\n-1 Attempt Sorry The Letter {guess} has already been guessed. Attempts: {attempts} \n")
        

    elif guess == "1":
        break

    else:
        attempts -= 1
        print(f"\nSorry Try Again. You Have {attempts} Remaining\n")

if (attempts != 0) and ("_" not in word_subsitute):
    print(f"\nCongratulations. The Word Is '{chosen_word.title()}'. You Guessed All The Letters With {attempts} Attempts Left\n")

elif guess == "1":
    print(f"\nYou should atleast have finished the game. You had {attempts} attempts Left\n")

else:
    print(f"\n{attempts} Left You Lose. The word is '{chosen_word.title()}'. Better Luck Next Time\n")


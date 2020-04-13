"""
   Miranda Lassar and Sonia Presti and Charisma Chauhan hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app

"""

#the function generate_random_word, choses a random word from a list of words
import random
def generate_random_word():
    words = ['dog','cat','watermelon','animal','jumping','flying','swim','fish','food',
            'elephant','pig','farm','stick', 'magnet','cards','bears','camera','pencil','bread',
            'clothes','banana','light','coffee', 'chocolate', 'couch', 'television', 'radio', 'star',
            'airport', 'landscape','button','puzzle','glasses','rainbow','waterfall','backpack','gym',
            'flashlight','soccer','tennis','suitcase','socks','video','trumpet','guitar','piano','shoes',
            'paper','money','alien','unicorn','mermaid','key']
    word = random.choice(words)
    return word

#the function print_word prints the guessed letters in the correct places with underscores for letters that have not been guessed yet
def print_word(word, guessed_letter, blank):
    if guessed_letter in word:
        for n in range(0,len(word)):
            if word[n] == guessed_letter:
                blank[n] = guessed_letter
        seperator = ' '
        x = seperator.join(blank)
    else:
        seperator = ' '
        x = seperator.join(blank)
    print(x)
    return x



def play_hangman():

    while True:
        guessed_letters = []
        guesses_left = 6
        word = generate_random_word()
        blank = list(len(word)*'_')
        letter = input("Guess a letter")
        done = False
        while done==False:
            if letter in guessed_letters:
                guesses_left = guesses_left - 1
                print("You already guessed", letter)
            elif letter not in word:
                guessed_letters.append(letter)
                guesses_left = guesses_left - 1
                print(letter, 'is not in the word.')
            else:
                guessed_letters.append(letter)
                print(letter, 'is in the word!')

            #the function letters_in_word() returns a list of the letters in the word
            def letters_in_word():
                letters_in_word = []
                for i in range(0,len(word)):
                    letters_in_word.append(word[i])
                return letters_in_word

            letters_in_word = letters_in_word()

            #the list guess_all keeps track of what letters in the word were already guessed
            guess_all = []

            for i in range(0,len(word)):
                if word[i] in guessed_letters:
                    guess_all.append(word[i])

            #if all the letters in the word have been guessed, then you win
            #else if there are no more guesses left then you lose
            #the else statement lets you guess another letter if you haven't won yet and you still have guesses remaining
            if guess_all == letters_in_word:
                print_word(word,letter,blank)
                print('you win')
                done=True
            elif guesses_left == 0:
                print('you lose :(')
                print('the answer was,', word)
                done=True
            else:
                print_word(word,letter,blank)
                letter = input('Guess a letter')

        #the code below asks the player if they want to play again
        #depending on their answer the game either restarts or the program ends
        want_to_play = input('Do you want to play another game?')
        if want_to_play == 'no':
            print("Thanks for playing!")
            break
        elif want_to_play == 'yes':
            continue



play_hangman()

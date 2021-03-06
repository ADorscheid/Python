import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
    #return 'fetlocks'
# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word = choose_word(wordlist)


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word = ''
    for a in range(len(letters_guessed)):
        word = word + letters_guessed[a]
        
    if word == secret_word:
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word=''
    counter=0
    secret_word_list=list(secret_word)
    if (len(letters_guessed)==0):
        letters_guessed.append(' ')
    for a in range(len(secret_word)):
        for b in range(len(letters_guessed)):
            if secret_word_list[a] == letters_guessed[b]:
                word = word + letters_guessed[b] + ' '
                break
            if b == (len(letters_guessed)-1) and counter == b:
                word = word + '_ '
            counter+=1
            if b == len(letters_guessed)-1:
                counter = 0
    return word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    str = string.ascii_lowercase
    str_list = list(str)
    for a in range(len(letters_guessed)):
        for b in range(len(str_list)):
            if letters_guessed[a] == str_list[b]:
                del(str_list[b])
                break
    return_str = ''.join(str_list)
    return return_str
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses=6
    letters_guessed=[]
    unique_letters = 'abc'
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    
    while ((is_word_guessed(secret_word,letters_guessed) == False) and guesses!=0):
        print("----------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        old_guessed_word = get_guessed_word(secret_word,letters_guessed)
        letter_guess = str(input("Please guess a letter: "))
        letters_guessed.append(letter_guess)
        guessed_word = get_guessed_word(secret_word,letters_guessed)
        
        if (old_guessed_word == guessed_word):
            print("Oops!  That letter is not in my word: ", old_guessed_word)
            guesses-=1
        else:
            print("Good guess: ", guessed_word)
            
    print("----------------")
    if (is_word_guessed(secret_word,letters_guessed) == True):
        print("Congratulations, you won!")
        print("Your total score for this game is: ", (6-guesses*len(unique_letters)))
    else:
        print("Sorry, you ran out of guesses.  The word was", secret_word)

if __name__ == "__main__":
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)


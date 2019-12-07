'''
Created on Nov 23, 2019

@author: ITAUser
'''
# import the random library

#def a function called pick_random_word():
    #open and read word dictionary/list(words.txt)
    
    #variable called index = select random word
    #variable called word -= strip the randomly selected word
    #return variable word

#define a function called ask for_next_letter():
    #variable called letter = input that asks user to select a letter
    #return the letter selected

#generate_word_string(word,letters_guessed)
    #variable called output = empty list
    #make a for loop that goes through each letter in the variable 'word'
        #if statement that checks if letter is in letters_guessed
            #append letter to output
        #else: 
            #append ("_")
        #return output as a string
        
#create a main module
    #variable called WORD = pick _random_word()

    #variable called letter_to_guess = set of Word
    #variable called correct_letters_guessed = empty set
    #variable called incorrect_letters_guessed = empty set
    #variable called number_of_guesses = number of guess I choose
    
    #print statement that welcomes the user to hangman
    
    #while loop that runs until number_of_guess is less than 1 or letters_to_guess is equal to 0
        #variable called guess = ask_for_next_letter() and turn into lower case
        
        #if statement that checks if guess is in correct_letters_guessed or guess is in incorrect_letters_guessed
            #print "you already guessed that"
        
        #if statement checks if guess is in letter_to_guess
            #remove guess from letter_to_guess
            #add guess to correct_letters_guessed
        #else:
            #add guess to incorrect_letters_guessed
            #number_of_guess goes down by one
            
    #variable called word string = generate_-word_string(WORD, correct_letters_guessed)
    #print statement that prints word string
    #print statement that prints how many guesses you have left
    
    #if statement to check if numbers of guesses is less than one
        #print "congratulations you guessed the word correctly"
    #else:
        #print "sorry you lost the word was " + WORD
    
    
    
    
    
    
    
    
    
    
    
    
    
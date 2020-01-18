'''random word generator'''
#this program generates a random noun, verb, or adjective from 18 possible results.
#the program will greet the user, then ask them which type of word they'd like to generate
#based on the user input, the program generates the appropriate type of word
#then the program asks the user if they want to repeat or if they want to end

import random #imports random numbers for the functions to pick from

'''functions'''

#choose random number and print out a noun based on which # chosen
def generate_noun():
    random_number = random.randint(1,6)
    
    if (random_number == 1):
        print("vortex")
    elif(random_number == 2):
        print("elbow")
    elif(random_number == 3):
        print("icicle")
    elif(random_number == 4):
        print("frigate")
    elif(random_number == 5):
        print("oatmeal")
    elif(random_number == 6):
        print("canopy")

#choose random number and print out a verb based on which # chosen
def generate_verb():
    random_number = random.randint(1,6)
    
    if (random_number == 1):
        print("prance")
    elif(random_number == 2):
        print("wallow")
    elif(random_number == 3):
        print("absorb")
    elif(random_number == 4):
        print("deflect")
    elif(random_number == 5):
        print("slosh")
    elif(random_number == 6):
        print("reverberate")

#choose random number and print out a adjective based on which # chosen
def generate_adjective():
    random_number = random.randint(1,6)

    if (random_number == 1):
        print("starchy")
    elif(random_number == 2):
        print("vibrant")
    elif(random_number == 3):
        print("plaintive")
    elif(random_number == 4):
        print("bountiful")
    elif(random_number == 5):
        print("brassy")
    elif(random_number == 6):
        print("omnivorous")

#contains the different selection conditionals.
def type_selection():
    word_type = input(str("What type of word would you like to generate? "))
    #word_type is a user-inputted variable. answers should be be noun, verb, or adjective. the inputted value will determine which random number generator is run
    if word_type == "noun":
        generate_noun()
    elif word_type == "verb":
        generate_verb()
    elif word_type == "adjective":
        generate_adjective()
    else:
        print("Sorry, I don't understand. Please enter noun, verb, or adjective when prompted.")

#ask the use if they want to generate another word.
#having this as a function rather than a variable allows the program to continue running if the user enters something other than yes or no
def repeat_program():
    repeat_query = str(input("Would you like to generate another word? "))
    #user-input variable to determine if the user wants to generate another word. answers should be yes or no.

    if repeat_query == "yes":
        process() #repeats word generation
    elif repeat_query == "no":
        exit()
    else:
        print("Sorry, I don't understand. Please enter yes or no when prompted.")
        repeat_program() #repeats inquiry about whether or not user wants to repeat word generation

#process contains the steps the program will run after greeting the user. By containing these steps in a function, the program can repeat.
def process():
    type_selection() #ask the user what type of word they want to generate, then give them a word

    repeat_program() #ask the user if they want to generate another word

'''main'''

#greet user
print("Welcome! \nThis program will generate a random noun, verb, or adjective.\n")

process()
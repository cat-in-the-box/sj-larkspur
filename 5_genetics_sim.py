'''this program  calculates how likely a child is to have sickle cell anemia (SCA) given the genetic makeup of two parents'''

'''variables'''

#there are 3 total variables.
#parent1: the 1st variable is the genetic makeup of parent 1
#parent 2: the 2nd variable is the genetic makeup of parent 2
#number_B: the 3rd variable is the total number of B's in the parents' genetic makeup.

'''variables: parent 1 and parent 2'''
#are input by the user.
#are strings with two characters each.
#the two characters for either variable can be any combination of B and/or b.
#B (upercase letter) is the dominant trait (red blood cells with a round shape)
#b (lowercase letter) is the recessive trait (reb blood cells with sickle cell anemia)

'''variable: number_B'''
#is an integer and can equal 0, 1, or 2.
#represents the total number of B's (dominant trait) in either parent's genetic makeup.
#this variable is initially set to 0.

'''results'''
#if parent1 or parent2 has type BB, nothing is added to number_B. the result is 0% likelihood
#OTHERWISE, for each B in parent1 or parent2, 1 is added to number_B
#if number_B = 2, result is 25% likelihood
#if number_B = 1, result is 50% likelihood
#if number_B = 0, result is 100% likelihood

'''program'''

#introduction for user
print("This program calculates how likely a child is to have sickle cell anemia given the genetic makeup of two parents.\n")
print("In this program, you will be asked to provide the genetic makeup of each parent.\n")
print("Use the letters B and b to describe the genetic makeup. B (uppercase letter) designates the dominant trait. b (lowercase letter) designates the recessive trait.\n")
print("At the end, you'll be given a percentage indicating how likely it is that the child of these parents will have sickle cell anemia. \n Let's begin.\n")

#setting variables
parent1 = str(input("What is the genetic makeup of the first parent? Enter BB, Bb, or bb. "))
parent2 = str(input("What is the genetic makeup of the second parent? Enter BB, Bb, or bb. "))

number_B = 0

#deciding result
if(parent1 == "BB" or parent2 == "BB"):
    print("The child of these parents will not have sickle cell anemia.")
    exit()

if(parent1[0] == "B"):
    number_B = number_B + 1

if(parent1[1] == "B"):
    number_B = number_B + 1

if(parent2[0] == "B"):
    number_B = number_B + 1
    
if(parent2[1] == "B"):
    number_B = number_B + 1
        
#printing result
if(number_B == 2):
    print("The child of these parents is 25% likely to have sickle cell anemia.")
    
elif(number_B == 1):
    print("The child of these parents is 50% likely to have sickle cell anemia.")
    
elif(number_B == 0):
    print("The child of these parents will have sickle cell anemia.")
    
'''future editing'''
#else condition should be added but will require some troubleshooting.
#currently the program only looks for B's and will generate results regardless of what is actually entered, since it has conditions for any number of Bs (0 to infinity)
    
'''check your results'''
#if variables are BB and BB, result is 0%
#if variables are [BB and bb] or [bb and BB], result is 0%
#if variables are [BB and Bb] or [Bb and BB], result is 0%
#if variables are Bb and Bb, result is 25%
#if variables are [Bb and bb] or [bb and Bb], result is 50%
#if variables are bb and bb, result is 100%
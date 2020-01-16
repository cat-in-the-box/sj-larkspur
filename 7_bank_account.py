'''Bank Account Simulator'''
#this program simulates a bank account for a user. the user can add and take away money from the account. the user can also check the balance of the account.
#every time the user selects what they want to do, a nuew function is called in. at its completion, the user is again prompted to define what they want to do
#this process can be repeated as many times as desired or the program can be exited

'''VARIABLES'''

#defines starting amount in bank account. 
account_balance = 0

'''FUNCTIONS'''

#gives account balance. result should be a float. it can be negative.
def give_balance (account_balance):
    print("\nYour account balance is $" + str(account_balance) + "\n")
    options_menu(account_balance) #calls in menu of user options

#asks user to define the amount to add to their account, adds this amount, then gives the new balance
def deposit(account_balance):
    deposit_amount = float(input("How much do you want to deposit? $")) #should be a number
    account_balance = account_balance + deposit_amount #adds deposit amount to the account and redefines the account balance with this new number
    give_balance(account_balance) #returns the new account balance

#asks user to define the amount to take out of their account, subtracts this amount, then gives the new balance
def withdrawal(account_balance):
    withdrawal_amount = float(input("How much do you want to withdraw? $")) #should be a number
    account_balance = account_balance - withdrawal_amount #subtracts withdrawal amount from the account and redefines the account balance with this new number
    give_balance(account_balance) #returns the new account balance

#defines the set of options the user has
def options_menu(account_balance):
    user_choice = str(input("What would you like to do? \n\t Enter 1 to check your balance. \n\t Enter 2 to make a deposit. \n\t Enter 3 to make a withdrawal. \n\t Enter 4 to exit this program.\n\t "))
    
    if user_choice == "1":
        give_balance(account_balance)
    elif user_choice == "2":
        deposit(account_balance)
    elif user_choice == "3":
        withdrawal(account_balance)
    elif user_choice == "4":
        exit
    else:
        print("I'm sorry, I don't understand.")
        options_menu(account_balance)

'''MAIN'''

#greet user
print("Thank you for banking with Peppermint Piggy Bank. /n")
username = str(input("Please enter your username. "))
str(input("Please enter your password. ")) #this is only for simulation purposes :)
print("Welcome, " + username + "!")

options_menu(account_balance)
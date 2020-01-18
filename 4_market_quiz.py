#children's book suggestor

#books to suggest
Thisby = 0
Midnight = 0
Artemis = 0
Westing = 0
Greenglass = 0
Horse = 0

#define genre (yes or no questions)
#fantasy
fantasy = input("Do you like fantasy books? yes/no ")
if (fantasy == "yes"):
    Thisby = Thisby + 1
    Midnight = Midnight + 1
    Artemis = Artemis + 1
    Greenglass = Greenglass + 1
    Horse = Horse + 1
elif (fantasy == "no"):
    Westing = Westing + 1
else:
    print("Please try again and answer yes or no.")

#mystery
mystery = input("Do you like mystery books? yes/no ")
if (mystery == "yes"):
    Midnight = Midnight + 1
    Artemis = Artemis + 1
    Greenglass = Greenglass + 1
    Westing = Westing + 1
elif (mystery == "no"):
    Thisby = Thisby + 1
    Horse = Horse + 1
else:
    print("Please try again and answer yes or no.")

#action
action = input("Do you like books with a lot of action? yes/no ")
if (action == "yes"):
    Artemis = Artemis + 1    
elif (action == "no"):
    Thisby = Thisby + 1
    Horse = Horse + 1
    Greenglass = Greenglass + 1
    Westing = Westing + 1
    Midnight = Midnight + 1
else:
    print("Please try again and answer yes or no.")
    
#fairytale
fairytale = input("Do you like fairytales? yes/no ")
if (fairytale == "yes"):
    Horse = Horse + 1
    Midnight = Midnight + 1
elif (fairytale == "no"):
    Artemis = Artemis + 1
    Thisby = Thisby + 1
    Greenglass = Greenglass + 1
    Westing = Westing + 1
else:
    print("Please try again and answer yes or no.")
    
#coming of age
age = input("Do you like coming of age stories? yes/no ")
if (age == "yes"):
    Horse = Horse + 1
    Westing = Westing + 1
elif (age == "no"):
    Artemis = Artemis + 1
    Thisby = Thisby + 1
    Greenglass = Greenglass + 1
    Midnight = Midnight + 1
else:
    print("Please try again and answer yes or no.") 

#weigh value defined by yes or no questions above
#suggest book title with the highest value
#choose from Thisby, Midnight, Artemis, Westing, Greenglass, or Horse

if (Thisby >= max(Thisby, Midnight, Artemis, Westing, Greenglass, Horse)):
    print("You should read \"Thisby Thestoop and the Black Mountain\" by Zac Gorman!")
    
if (Midnight >= max(Thisby, Midnight, Artemis, Westing, Greenglass, Horse)):
    print("You should read \"The Midnight Folk\" by John Masefield!")
    
if (Artemis >= max(Thisby, Midnight, Artemis, Westing, Greenglass, Horse)):
    print("You should read \"Artemis Fowl\" by Eoin Colfer!")
    
if (Westing >= max(Thisby, Midnight, Artemis, Westing, Greenglass, Horse)):
    print("You should read \"The Westing Game\" by Ellen Raskin!")

if (Greenglass >= max(Thisby, Midnight, Artemis, Westing, Greenglass, Horse)):
    print("You should read \"Greenglass House\" by Kate Milford!")
    
if (Horse >= max(Thisby, Midnight, Artemis, Westing, Greenglass, Horse)):
    print("You should read \"The Little White Horse\" by Elizabeth Goudge!")

#have the program run the line below if you want to check the answers
#print(Thisby, Midnight, Artemis, Westing, Greenglass, Horse)
    
#didn't have time to get to these ones but it might be fun some day!
#define setting (yes or no questions)
#define tone (yes or no questions)
#define fantasy creature preference (yes or no questions)
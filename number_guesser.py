import random
#Asking use to enter random number
top_of_range = input("Type a number:  ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    #If number is below 0, user aked to enter a larger number.
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time. ")
        quit()
else:
    #asks user to enter a number if number was not entered 
    print("Please type a number next time. ")
    quit()

# Getting a random number  above 0 
random_number = random.randint(0, top_of_range)
#print(random_number)
# User number of guesses
guesses = 0



while True:
    #Counts number of guesses
    guesses += 1
    # Aksing user to make a guess
    user_guess = input("Make a new guess: ")
    if user_guess.isdigit():
        user_guess =int(user_guess)

    else:
        print("Please type a number next time. ")
        continue
    if user_guess == random_number:
        print("You got it! Your number is", user_guess)
        #Asks user if wants to continue playing
        keep_going = input("Keep going? (y/n)")
        if keep_going != "y":

            break
    #Letting user know if number entered is above or below ramdom number.
    elif user_guess > random_number:
        print("You were above the number! ")
    else:
        print("You are below the number")

        
# Prints number of guesses before user got it right
print("You got it in ", guesses, "guesses")

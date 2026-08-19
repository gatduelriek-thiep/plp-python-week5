# Secret number between 1 and 20 guess game
secret_number = 12

# Create a counter variable for attempts
attempts = 0

# Variable that will control the loop iteration
guessed = False

print("__Let me think between number 1 and 20__")

# While loop that will evaluate to true when user guessed the number

while not guessed:
    
    guess = int(input("Take a guess: "))
    attempts += 1
    
    if guess < secret_number:
        print("It is too low. Please try again")
    
    elif guess > secret_number:
        print("Too high. Please try again")
    
    else:
        print("Congratulations! You guessed it. ")
        guessed = True

# Report of number of trial
print(f"You got it in {attempts} attempts!")


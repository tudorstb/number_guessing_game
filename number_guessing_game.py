import random
#i choose to implement a verification for the number in order to enter only intigers
def verify_int(guess):
        while True:
            try:
                guess = int(guess)
            except:
                print("invalid option choose")
                guess = input('Guess an integer between 1 and 20:')
            else:
                return guess
rand_number=random.randrange(1,20)
start_nr = 1
end_nr = 20
while True:
    guess=input(f"Guess an integer between {start_nr} and {end_nr}:")
    guess=verify_int(guess)
    if guess==rand_number:
        print("You got it!")
        break
    elif guess>rand_number:
        print("The guess is too high!")
        if end_nr > guess:
            end_nr=guess
    else:
        print("The guess is too low!")
        if start_nr < guess:
            start_nr=guess


import random
#i choose to implement a verification for the number in order to enter only intigers and numbers between a set numbers
def verify_int(guess,start_nr,end_nr):
        while True:
            try:
                guess = int(guess)
                assert guess >= start_nr and guess <= end_nr
            except:
                if isinstance(guess, int):
                    if guess <1:
                        print("invalid option choose,number too lower then the limit")
                    else:
                        print("invalid option choose,number too largeer then the limit")
                else:
                    print("Error ,did not entered a intiger")
                guess = input(f'Guess an integer between {start_nr} and {end_nr}:')

            else:
                return guess
rand_number=random.randrange(1,20)
start_nr = 1
end_nr = 20
list_of_attempt=[]
number_of_attempt=0
while True:
    guess=input(f"Guess an integer between {start_nr} and {end_nr}:")
    guess=verify_int(guess,start_nr,end_nr)
    list_of_attempt.append(guess)
    number_of_attempt+=1
    if guess==rand_number:
        print("You got it!")
        print(f'You had {number_of_attempt} attempt :{list_of_attempt}')
        break
    elif guess>rand_number:
        print("The guess is too high!")
        if end_nr > guess:
            end_nr=guess
    else:
        print("The guess is too low!")
        if start_nr < guess:
            start_nr=guess


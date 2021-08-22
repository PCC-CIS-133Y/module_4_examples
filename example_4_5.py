# example 4.5
import random # you must add this at the top of your program to use the random functions

def main():
    answer = random.randint(1, 10)
    guess = 0
    tooHigh = 0
    tooLow = 0
    valid = False

    print("Guess a number between 1 and 10!")
    while guess != answer:
        valid = False # reset the flag before prompting for guess
        while not valid:
            try:
                guess = int(input("\nEnter guess: "))
                if guess < 1 or guess > 10:
                    print("Guess must be 1-10")
                else:
                    valid = True
            except:
                print("Not an integer!")

        if guess == answer:
            print("Correct!!")
        elif guess > answer:
            print("Too high!")
            tooHigh += 1
        else:
            print("Too low!")
            tooLow += 1

    print(tooHigh, "of your guess were too high.")
    print(tooLow, "of your guess were too low.")
    print("\nThank you for playing!")  

main()




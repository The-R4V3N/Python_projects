import random

MAX_ATTEMPTS = 10


def main():
    choice = ''
    random.seed()
    while choice != 'n':
        print("*******************************************")
        print("************Let the Game begin!************")
        print("*******************************************\n")
        print("I am thinking of a number between 0 and 99.")
        print("Can you guess what it is?\n")
        print("You have 10 attempts :\t ")

        num = random.randint(0, 99)
        for i in range(MAX_ATTEMPTS):
            try:
                guess = int(input())
                if guess > 99:
                    print("Error please enter a valid number")
                elif guess == num:
                    print("\nCongratulations! You have guessed correctly.")
                    print("The secret number was {}\t\n".format(num))
                    break
                elif guess > num:
                    print("Sorry your guess was too high!\n")
                else:
                    print("Sorry your guess was too low!\n")
            except ValueError:
                print("Error please enter a number")

        while choice != 'y' and choice != 'n':
            choice = input("Do you want to play again? (y/n): ").lower()
            if choice != 'y' and choice != 'n':
                print("Invalid Input! Please enter Y or N: ")


if __name__ == "__main__":
    main()

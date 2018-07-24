import random

number = random.randint(1, 100)


def main():

    print("Welcome to the HI - LO game")

    guess = 0

    while guess != number:
        guess = int(input("Guess a number between 1 & 100: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")

    print("Got it: The number is {}".format(number))


if __name__ == '__main__':
    main()
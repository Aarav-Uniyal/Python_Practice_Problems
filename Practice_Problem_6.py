import random


def number_guess():
    p1 = input("Enter the name of player 1.\n")
    p2 = input("Enter the name of player 2.\n")
    try:
        a = int(input("Enter the minimum range of the random number.\n"))
        b = int(input("Enter the maximum range of the random number.\n"))

    except ValueError:
        print("Enter numbers only.\n")
        number_guess()
    n = random.randrange(a, b)
    i = 0
    print(f"{p1}'s turn.\n")
    while True:
        try:
            c = int(input(f"Guess the number between {a} and {b}.\n"))

        except ValueError:
            print("Enter a number only.\n")
            number_guess()

        i += 1
        if i == 5:
            v = "GAME OVER"
            print(v)
            break
        elif c == n:
            print(f"Congrats you have guessed the number in {i} tries!\n")
            break

        elif c < n:
            print(f"Just a little bit more. You have {5 - i} tries left.\n")

        elif c > n:
            print(f"Just a little bit lower. You have {5 - i} tries left.\n")

    print(f"{p2}'s turn.\n")
    e = random.randrange(a, b)
    j = 0
    while True:
        try:
            d = int(input(f"Guess the number between {a} and {b}.\n"))

        except ValueError:
            print("Enter a number only.\n")
            number_guess()

        j += 1
        if j == 5:
            z = "GAME OVER"
            print(z)
            break
        elif d == e:
            print(f"Congrats you have guessed the number in {j} tries!\n")
            break

        elif d < e:
            print(f"Just a little bit more. You have {5 - j} tries left.\n")

        elif d > e:
            print(f"Just a little bit lower. You have {5 - j} tries left.\n")

    if j < i:
        print(f"{p2} wins!!!")

    elif j > i:
        print(f"{p1} wins!!!")

    elif j == i:
        print(f"This match was a tie.")

    else:
        print("Something went wrong.\n")
        number_guess()


if __name__ == '__main__':
    number_guess()

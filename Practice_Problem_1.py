def age_akinator(d, f):
    if f == 2:
        if d < 2020 or d > 1920:
            f = 2020 - d
            b = f + 100
            print(f"You will be of 100 years old in {b}.\n")

        elif d >= 2020:
            print("You are not yet born.\n")

        elif d < 1920:
            print("You seem to be the oldest programmer in the world.\n")

    elif f == 4:
        if d < 100 or d > 0:
            b = d + 100
            print(f"You will be of 100 years old in {b}.\n")

        elif d < 1:
            print("You are not yet born.\n")

        elif d > 100:
            print("You seem to be the oldest programmer in the world.\n")

    else:
        print("Invalid input. Please try again.\n")
        b = input("Tell me your age or your year of birth and I will tell you when you will turn 100 years old.\n")
        c = len(b)
        b = int(b)
        age_akinator(b, c)


def choicer():
    choice = input("Do you want to know your age in a particular year?(y/n)\n")
    choice = choice.lower()
    if choice == "y":
        g = input("Enter the year.\n")
        g = int(g)
        re_age_akinator(g)

    elif choice == "n":
        exit()

    else:
        print("Invalid input. Please try again.\n")
        choicer()


def re_age_akinator(d):
    if e == 4:
        if d > 2020:
            o = 2020 - a
            i = d - 2020
            b = o + i
            print(f"You will be of {b} years old in {d}.\n")

        elif d <= 2020:
            print("Cannot take input for the past or present.\n")

    elif e == 2:
        if d > 2020:
            j = d - 2020
            b = a + j
            print(f"You will be of {b} years old in {d}.\n")

        elif d <= 2020:
            print("Cannot take input for the past or present.\n")

    else:
        print("Invalid input. Please try again.\n")
        g = input("Enter the year.\n")
        re_age_akinator(g)


if __name__ == '__main__':
    a = input("Tell me your age or your year of birth and I will tell you when you will turn 100 years old.\n")
    e = len(a)
    a = int(a)
    age_akinator(a, e)
    choicer()

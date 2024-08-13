import random


def jumble():
    try:
        n = int(input("Enter the number of persons.\n"))
    except ValueError:
        print("Enter a number only.\n")
        exit()
    first_names = []
    last_names = []
    for i in range(n):
        names1 = input("Enter the name(separate the first name with the last name using a space).\n")
        split = names1.split(" ")
        first_names.append(split[0])
        for e, iw in enumerate(split):
            if e == 0:
                continue
            elif e > 0:
                last_names.append(split[e])

    for c, item in enumerate(first_names):
        r = random.choice(last_names)
        print(item, r)


if __name__ == '__main__':
    jumble()

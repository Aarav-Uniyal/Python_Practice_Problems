def apple_ranger():
    try:
        a = int(input("Enter the number of apples Harry has.\n"))
        if a < 1:
            print("At least one apple is required.\n")
            apple_ranger()

        mn = int(input("Enter the minimum number.\n"))
        mx = int(input("Enter the maximum number.\n"))

    except Exception:
        print("Enter numbers only.")
        apple_ranger()

    if mn == 0 or mx == 0:
        print("Can't divide with zero.\n")
        apple_ranger()

    elif mn > mx:
        print("mn cannot be greater than mx.")
        apple_ranger()

    elif mn != mx:
        mx = mx + 1
        for i in range(mn, mx):
            if a % i == 0:
                print(f"{i} is a divisor of {a}.")

            elif a % i != 0:
                print(f"{i} is not a divisor of {a}.")

            else:
                print("Something went wrong. Please try again.\n")
                apple_ranger()

    elif mn == mx:
        print("This is not a range as mn and mx are equal.")
        mx = mx + 1
        for i in range(mn, mx):
            if a % i == 0:
                print(f"{i} is a divisor of {a}.")

            elif a % i != 0:
                print(f"{i} is not a divisor of {a}.")

            else:
                print("Something went wrong. Please try again.\n")
                apple_ranger()

    exit()


if __name__ == '__main__':
    apple_ranger()

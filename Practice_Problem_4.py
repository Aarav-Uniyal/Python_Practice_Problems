def next_palindrome():
    try:
        a = int(input("Enter the number of numbers you want to get the next palindrome of.\n"))

    except ValueError:
        print("Enter a number only.\n")
        next_palindrome()

    p = []
    for i in range(a):
        try:
            e = int(input("Enter the numbers.\n"))
        except ValueError:
            print("Enter numbers only.\n")
            next_palindrome()
        p.append(str(e))

    for f in p:
        if f == f[::-1]:
            print(f"{f} is already a palindrome.")
        else:
            j = f
            while True:
                f = int(f)
                k = f + 1
                f = str(k)
                if f == f[::-1]:
                    break

            print(f"The nearest palindrome for {j} is {k}.")

    exit()


if __name__ == '__main__':
    next_palindrome()

def list_next_palindrome():
    try:
        a = int(input("Enter the number of numbers you want to get the next palindrome of.\n"))

    except ValueError:
        print("Enter a number only.\n")
        list_next_palindrome()

    p = []
    for i in range(a):
        try:
            e = int(input("Enter the numbers.\n"))
        except ValueError:
            print("Enter numbers only.\n")
            list_next_palindrome()
        p.append(str(e))

    for i, w in enumerate(p):
        if w == w[::-1] or int(w) < 10:
            pass
        elif w != w[::-1] and int(w) > 10:
            while True:
                w = int(w)
                w += 1
                w = str(w)
                if w == w[::-1]:
                    p[i] = w
                    break

    print(f"Here is your list ---> {p}.")
    exit()


if __name__ == '__main__':
    list_next_palindrome()

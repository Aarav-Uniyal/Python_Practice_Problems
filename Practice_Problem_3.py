def list_reverser():
    try:
        n = int(input("How many food items do you want to add in your list.\n"))

    except ValueError:
        print("Please enter a number.\n")
        list_reverser()

    print("Enter the names of the food items one by one.")
    list1 = []
    for i in range(n):
        a = input()
        list1.append(a)
        pass

    list2 = list1.copy()
    list2.reverse()

    list3 = list1.copy()
    list3 = list3[::-1]

    list4 = list1.copy()
    e = len(list4) - 1
    for i in range(len(list4)//2):
        list4[i], list4[e - i] = list4[e - i], list4[i]
        pass

    if list2 == list3 == list4:
        print("Your list =", list1)
        print("List1 =", list2)
        print("List2 =", list3)
        print("List3 =", list4)

    else:
        print("Something went wrong.\n")
        list_reverser()


if __name__ == '__main__':
    list_reverser()

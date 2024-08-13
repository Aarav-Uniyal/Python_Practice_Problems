import random


def aditya_multiplication(n):
    global multiplication
    multiplication = []
    for i in range(11):
        if n * i == 0:
            continue
        multiplication.append(n * i)
    for it in range(1):
        r = random.randint(0, 9)
        multiplication.remove(multiplication[r])
        multiplication.insert(r, random.randint(n, n * 10))
    return multiplication


def is_correct(table, number):
    i = 0
    for item in table:
        i += 1
        if i == 11:
            break
        if item != number*i:
            return f"Problem found at position {number}*{i} with result value {item}. "
        elif item == number*i:
            pass
    for n in range(len(table)):
        return None


if __name__ == '__main__':
    try:
        num = int(input("Enter the number you want to get table of.\n"))
    except ValueError:
        print("Enter a number only\n")
    else:
        print(aditya_multiplication(num))
        print(is_correct(multiplication, num))

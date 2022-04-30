a = input("Enter input: ")


def integer(a):
    count = 0
    for i in range(len(a)):
        if a[i].isdigit():
            count = count + 1
    if count == len(a):
        print("It is an integer")
    else:
        print("It is not an integer")


def check(num):
    try:
        float(num)
        return print("It is float value")
    except ValueError:
        return print("It is not a float value")


def alphabet(a):
    x = a.isalpha()
    if x:
        print("It is an Alphabet")
    else:
        print("It is not an Alphabet")


def uplo(text):
    x = text.isalpha()
    if x:
        if text.islower():
            print("Lower Case Alphabet")
        elif text.isupper():
            print("Upper Case Alphabet")
        else:
            print("Both Uppercase and Lowercase alphabets are involved")
    else:
        print("It is not an Alphabet")


def arithmetic(n):
    A = ["+", "-", "*", "%", "/", "="]
    if n in A:
        print("It is an arithmetic operator")
    else:
        print("Not an arithmetic operator")


def special(n):
    if 31 < ord(n) < 48 or 57 < ord(n) < 65 or 90 < ord(n) < 97 or 122 < ord(n) < 127:
        print("It is a Special character")
    else:
        print("It is not an Special character")


def switch():
    print(
        "1 : Integer or not\n2 : FLOAT or not\n3 : Alphabet or not\n4 : Upper Case or Lower Case\n5 : Arithmetic "
        "operator or not\n6 : Special character or not")
    option = int(input("enter your option from 1-6: "))
    if option == 1:
        integer(a)
    elif option == 2:
        check(a)
    elif option == 3:
        alphabet(a)
    elif option == 4:
        uplo(a)
    elif option == 5:
        arithmetic(a)
    elif option == 6:
        special(a)
    else:
        print("Incorrect option")


switch()

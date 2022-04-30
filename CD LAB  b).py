# Write a program to check whether given input is float or not
a = input("Enter input: ")


def check(num):
    try:
        float(num)
        return print("It is float value")
    except ValueError:
        return print("It is not a float value")


check(a)

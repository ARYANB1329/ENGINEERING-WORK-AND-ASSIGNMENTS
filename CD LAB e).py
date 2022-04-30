# Write a program to check whether given input is arithmetic operator or not
A = ["+", "-", "*", "%", "/", "="]
n = input("Enter a arithmetic Operator:")
if n in A:
    print("It is an arithmetic operator")
else:
    print("Not an arithmetic operator")

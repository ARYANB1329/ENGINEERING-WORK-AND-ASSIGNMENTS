# Write a program to check whether given input is special character or not
n = input("Enter a character:")
if 31 < ord(n) < 48 or 57 < ord(n) < 65 or 90 < ord(n) < 97 or 122 < ord(n) < 127:
    print("It is a Special character")
else:
    print("It is not an Special character")

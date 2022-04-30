# Write a program to check whether given input is lowercase or UPPERCASE
text = input("Enter input: ")
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

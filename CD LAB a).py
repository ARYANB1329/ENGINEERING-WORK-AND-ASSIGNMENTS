# Write a program to check whether given input is integer or not

a = input("Enter input: ")
count = 0
for i in range(len(a)):
    if a[i].isdigit():
        count = count + 1
if count == len(a):
    print("It is an integer")
else:
    print("It is not an integer")
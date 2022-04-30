String1 = list(str(input("Enter your string1:")))
String2 = list(str(input("Enter your string2:")))
a = sorted(String1)
b = sorted(String2)

if(a == b):
    print("It is an anagram")
else:
    print("It is not an anagram")

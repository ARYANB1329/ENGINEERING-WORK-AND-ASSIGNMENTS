str_input = input("Enter string: ")
flag = 0
count = 0
for i in range(len(str_input)):
    if 65 <= ord(str_input[i]) <= 122:
        count = count + 1
if len(str_input) > 1:
    if count == len(str_input):
        print("It is a word")
    else:
        print("It is not a word")
else:
    print("It is not a word")

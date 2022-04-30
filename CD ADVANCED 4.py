# No of Epsilon Productions
print("For Epsilon Productions, use '#' as ")
print(" After '->' : ")
print(" To enter next production rule - 'y' ")
print(" Else, Press on Enter key")

count = 0
while input() == 'y':
    k = input("Enter production rule: ")
    l, r = k.split('->')
    x = r.split("/")
    arr = []
    flag = 0

    for i in x:
        if i != '':
            arr.append(i)

    for i in range(len(arr)):
        if arr[i] == '#':
            flag = 1
            break
    if k[1] == '-' and k[2] == '>' and k[0].isupper() and len(k) > 3 and flag == 1:
        count = count + 1

print("No of Epsilon production: ", count)

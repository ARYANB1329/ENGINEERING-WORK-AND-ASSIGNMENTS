# No of UNIT productions, For example: A->a

c = 0
while input() == 'y':
    k = input("Enter production rule: ")
    l, r = k.split('->')
    x = r.split("/")
    arr = []

    for i in x:
        if i != '':
            arr.append(i)

    for i in range(len(arr)):
        if len(arr[i]) == 1 and k[1] == '-' and k[2] == '>' and k[0].isupper():
            c = c + 1

print("No of Unit Productions", c)


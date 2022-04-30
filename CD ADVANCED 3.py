k = input("Enter CFG: ")
l, r = k.split('->')
x = r.split("/")
arr = []
for i in x:
    if i != '':
        arr.append(i)
count = 0
m = []


def NT():
    global count
    for i in range(len(arr)):
        a = arr[i]
        for j in range(len(a)):
            if a[j].isupper():
                count = count + 1
                m.append(a[j])
    print("Number of Non-Terminals in RHS", count)


def Terminal():
    global count
    for i in range(len(arr)):
        a = arr[i]
        for j in range(len(a)):
            if not a[j].isupper():
                count = count + 1
    print("No of Terminals", count)


m = input(" 1 - No of Non-Terminals  2 - No of Terminals")

if m == 1:
    NT()
elif m == 2:
    Terminal()
else:
    print("Enter 1 or 2")
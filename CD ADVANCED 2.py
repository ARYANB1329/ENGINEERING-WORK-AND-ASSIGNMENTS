# No of Non-Terminals in RHS (A-Z)
k = input("Enter CFG: ")
l, r = k.split('->')
x = r.split("/")
arr = []
for i in x:
    if i != '':
        arr.append(i)
count = 0
m = []

for i in range(len(arr)):
    a = arr[i]
    for j in range(len(a)):
        if a[j].isupper():
            count = count + 1
            m.append(a[j])
print("Number of Non-Terminals in RHS", count)

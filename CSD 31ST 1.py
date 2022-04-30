# Rotation Groups
# ARYAN B13 29
k = list(map(str, input("Enter input: ").split()))
l = []
for i in range(len(k)):
    m = ''.join((sorted(k[i])))
    l.append(m)
count = 0

for i in range(len(l)):
    if len(l[i]) == 1:
        count = count + 1
    for j in range(len(l)):
        if i > j and (l[i] == l[j]):
            count = count + 1
            continue
print(count)

l = int(input())
r = int(input())
c = 0
for i in range(l, r):
    z = str(i)
    if len(z) % 2 == 0:
        n = len(z) // 2
        s1 = z[:n]
        s2 = z[n:]
        l1 = list(map(int, s1))
        l2 = list(map(int, s2))
        if sum(l1) == sum(l2):
            c = c + 1
print(c)

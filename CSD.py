# SAME SIZES
def getMedian(ar1, ar2, n):
    i = 0
    j = 0
    m1 = -1
    m2 = -1
    count = 0
    while count < (n + 1):
        count += 1
        if i == n:
            m1 = m2
            m2 = ar2[0]
            break
        elif (j == n):
            m1 = m2
            m2 = ar1[0]
            break
        if (ar1[i] <= ar2[j]):
            m1 = m2
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2
            m2 = ar2[j]
            j += 1
    return (m1 + m2) / 2


# DIFFERENT SIZES
def getMedian2(ar1, ar2, n, m):
    i = 0
    j = 0
    m1, m2 = -1, -1
    if ((m + n) % 2 == 1):
        for count in range(((n + m) // 2) + 1):
            if (i != n and j != m):
                if ar1[i] > ar2[j]:
                    m1 = ar2[j]
                    j += 1
                else:
                    m1 = ar1[i]
                    i += 1
            elif (i < n):
                m1 = ar1[i]
                i += 1
            # for case when j<m,
            else:
                m1 = ar2[j]
                j += 1
        return m1
    else:
        for count in range(((n + m) // 2) + 1):
            m2 = m1
            if (i != n and j != m):
                if ar1[i] > ar2[j]:
                    m1 = ar2[j]
                    j += 1
                else:
                    m1 = ar1[i]
                    i += 1
            elif (i < n):
                m1 = ar1[i]
                i += 1
            else:
                m1 = ar2[j]
                j += 1
        return (m1 + m2) // 2


ar1 = []
ar2 = []

n = int(input("Length of first array: "))
for i in range(0, n):
    a = int(input())
    ar1.append(a)

m = int(input("Length of second array: "))
for i in range(0, m):
    a = int(input())
    ar2.append(a)

if n == m:
    print("Median is ", getMedian(ar1, ar2, n))
else:
    print("Median is ", getMedian2(ar1, ar2, n, m))

def distancesum(x, y, n):
    sum = 0

    # for each point, finding distance
    # to rest of the point
    for i in range(n):
        for j in range(i + 1, n):
            sum += (abs(x[i] - x[j]) +
                    abs(y[i] - y[j]))

    return sum


n = int(input("Enter number of elements : "))
a = list(map(int, input("\nEnter the x co-ordinates: ").strip().split()))[:n]
b = list(map(int, input("\nEnter the y co-ordinates: ").strip().split()))[:n]

print(distancesum(a, b, n))
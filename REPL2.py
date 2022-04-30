def LowerArray(arr, countSmaller, n):
    # initialize all the counts in countSmaller array as 0
    for i in range(n):
        countSmaller[i] = 0

    for i in range(n):
        for j in range(i + 1, n):
            if (arr[j] < arr[i]):
                countSmaller[i] += 1


# Utility function that prints out an array on a line
def printArray(arr, size):
    for i in range(size):
        print(arr[i], end=" ")
    print()

arr = []
n = len(arr)
for i in range(0,n):
    x = int(input("Enter"))
    arr.append(x)
low = [0] * n
LowerArray(arr, low, n)
printArray(low, n)
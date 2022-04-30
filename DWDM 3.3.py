# Normalization by Decimal Scaling
def decNor(num, maxNum):
    digit = len(str(maxNum))
    div = pow(10, digit)
    return num / div


n = int(input("Enter number of elements : "))
data = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

num = int(input("Enter an item from data: "))
print(decNor(num, max(data)))

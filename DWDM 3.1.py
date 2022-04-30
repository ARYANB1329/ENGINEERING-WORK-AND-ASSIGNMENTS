# To perform min max normalization of the entered values in a given range
n = int(input("Enter number of elements : "))
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]
k = max(a)
j = min(a)
l = int(input("enter the new maximum:"))
m = int(input("enter the new minimum:"))
final = []
for i in a:
    new = ((i - j) / (k - j)) * (l - m) + m
    final.append(new)
print(final)

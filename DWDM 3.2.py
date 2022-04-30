# Calculate the z-score from with scipy
n = int(input("Enter number of elements : "))
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]


mean = sum(a) / len(a)
differences = [(value - mean)**2 for value in a]
sum_of_differences = sum(differences)
standard_deviation = (sum_of_differences / (len(a) - 1)) ** 0.5
z_scores = [(value - mean) / standard_deviation for value in a]

print(z_scores)

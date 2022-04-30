# take CFGs as input
# Display no of productions

print(" After '->' : ")
print(" To enter next production rule - 'y' ")
print(" Else, Press on Enter key")

count = 0
while input() == 'y':
    k = input("Enter production rule: ")
    if k[1] == '-' and k[2] == '>' and k[0].isupper() and len(k) > 3:
        count = count + 1

print("No of production Rules: ", count)

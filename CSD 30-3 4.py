# ARYAN SHIV SIDDHABATHULA 121910313029 (B13 29)
# Given a string s, return its run-length encoding. You can assume the string to be encoded have no digits and
# consists solely of alphabetic characters.


k = input("Enter input:")
count = 0

n = len(k)
i = 0
while i < n - 1:
    count = 1
    while i < n - 1 and k[i] == k[i + 1]:
        count += 1
        i += 1
    i += 1
    print(k[i - 1] + str(count), end="")

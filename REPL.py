my_dict = {}
key = list(map(int, input("KEY:").split()))
print("Assign value to each key:")
for x in key:
    val = input("Value of Key: ")
    my_dict[x] = val
print(my_dict)
key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

print('Maximum Value: ',my_dict[key_max])
print('Minimum Value: ',my_dict[key_min])
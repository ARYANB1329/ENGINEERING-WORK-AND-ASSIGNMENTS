a_file = open("words.txt", "r")
lines = a_file.readlines()
last_lines = lines[-5:]

print(last_lines)
a_file.close()
file1 = open("words.txt", "r")
str1 = file1.read()
vowel_count = 0
for i in str1:
    if (i == 'A' or i == 'a' or i == 'E' or i == 'e' or i == 'I'
            or i == 'i' or i == 'O' or i == 'o'
            or i == 'U' or i == 'u'):
        vowel_count += 1

print('The Number of Vowels in text file :', vowel_count)

file1.close()
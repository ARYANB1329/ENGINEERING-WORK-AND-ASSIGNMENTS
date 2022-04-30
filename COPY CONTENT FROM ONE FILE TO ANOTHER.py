# open both files
with open('words.txt', 'r') as firstfile, open('words2.txt', 'a') as secondfile:
    # read content from first file
    for line in firstfile:
        # write content to second file
        secondfile.write(line)

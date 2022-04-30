# Maximum Repeating Substring For a string sequence, a string word is
# k-repeating if word concatenated k times is a substring of sequence. The word's
# maximum k-repeating value is the highest value k where word is k-repeating in sequence.
# If word is not a substring of sequence, word's maximum k-repeating value is 0.

str_input = input("Enter string: ")
word = input("Enter substring: ")
k = 0
n = len(word)
for i in range(len(str_input)):
    if word in str_input[i:i+n]:
        k = k+1
print(k)

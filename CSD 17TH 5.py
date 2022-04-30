# Given a string s, repeatedly delete the earliest
# consecutive duplicate characters.
str_input = input("Enter string: ")


def solve(s):
    stack = []

    def delete_earliest_consecutive_duplicate_characters():
        while len(stack) > 1 and stack[-1] == stack[-2]:
            end = stack[-1]
            while stack and stack[-1] == end:
                stack.pop()

    for c in s:
        if stack and stack[-1] != c:
            delete_earliest_consecutive_duplicate_characters()
        stack.append(c)

    delete_earliest_consecutive_duplicate_characters()

    return "".join(stack)


print(solve(str_input))

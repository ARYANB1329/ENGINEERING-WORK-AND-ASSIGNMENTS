# Length of Longest Balanced Subsequence

def solve(s):
    res = o = 0
    for i in s:
        if i == "(":
            o += 1
        else:
            if o != 0:
                o -= 1
                res += 2
    return res


user_input = input("Enter: ")
print(solve(user_input))

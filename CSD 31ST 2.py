# Multiple parentheses
# ARYAN B13 29
def Parentheses(s):
    list1 = []
    list1.append(-1)
    ln = 0
    for i in range(len(s)):
        if s[i] == "(":
            list1.append(i)
        else:
            del list1[-1]
            if len(list1) == 0:
                list1.append(i)
            else:
                if (i - list1[-1]) > ln:
                    ln = i - list1[-1]
    return ln


k = input("Enter:")
print(Parentheses(k))

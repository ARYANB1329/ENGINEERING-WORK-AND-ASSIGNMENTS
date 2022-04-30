def evaluate(lhs, rhs, op):
    if op == '>':
        return lhs > rhs
    elif op == '<':
        return lhs < rhs
    elif op == '==':
        return lhs == rhs
    elif op == '<=':
        return lhs <= rhs
    elif op == '>=':
        return lhs >= rhs
    else:
        return None


s = input("Enter expression:")
l = ["<", ">", "="]
count = 0
k = 0
for i in s:
    if i in l:
        count += 1  # Only 1 operator in given expression
    else:
        if not i.isdigit():
            k = 1
            break
if count > 2 or k == 1:
    print("Not a valid expression")
else:
    print("It is a valid expression")
    if count == 1:
        if '<' in s:
            h = s.split("<")
            print(evaluate(int(h[0]), int(h[1]), '<'))
        elif '>' in s:
            h = s.split(">")
            print(evaluate(int(h[0]), int(h[1]), '>'))
    else:
        if '<=' in s:
            h = s.split("<=")
            print(evaluate(int(h[0]), int(h[1]), '<='))
        elif '>=' in s:
            h = s.split(">=")
            print(evaluate(int(h[0]), int(h[1]), '>='))
        else:
            h = s.split("==")
            print(evaluate(int(h[0]), int(h[1]), '=='))

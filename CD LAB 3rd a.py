a = input("enter the sentence:").split()
k = 0
if len(a) > 1:
    print(" ".join(a), "is a sentence")
    for i in a:
        for j in i:
            if not j.isupper():
                k = 1
                break
        if k == 1:
            print(" ".join(a), "is not uppercase sentence")
            break
    if k == 0:
        print(" ".join(a), "is an uppercase sentence")
else:
    print(" ".join(a), "is not a sentence")

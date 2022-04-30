a = input("enter the sentence:").split()
k = 0
if len(a) > 0:
    print(" ".join(a), "is a sentence")
    for i in a:
        for j in i:
            if not j.islower():
                k = 1
                break
        if k == 1:
            print(" ".join(a), "is not lowercase sentence")
    if k == 0:
        print(" ".join(a), "is a lowercase sentence")
else:
    print(" ".join(a), "is not a lowercase sentence")

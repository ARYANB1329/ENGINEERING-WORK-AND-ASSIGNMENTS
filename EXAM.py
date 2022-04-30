x=1
y=2
z=3

def add(x,y):
    z=multiply (x, y)
    x=x+z
    return x

def multiply(x, y) :
    x=x*y
    return x

z=add(1, 1)

print(x, y, z)
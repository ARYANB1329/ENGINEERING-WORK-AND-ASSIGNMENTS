import numpy

n , m = input().split()
x = list(map(int, input().split()))
y = list(map(int, input().split()))

my_array = []
my_array.append(x)
my_array.append(y)
print(numpy.mean(my_array, axis=1))
print(numpy.var(my_array, axis=0))
king = numpy.std(my_array)
ping = round(king,11)
print(ping)

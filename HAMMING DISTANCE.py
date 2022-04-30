#ARYAN SIDDHABATHULA 121910313029
# B13 29

class Program(object):
   def hammingDistance(self, a, b):

      x = 0
      for i in range(31,-1,-1):
         h1= a>>i&1
         h2 = b>>i&1
         x+= not(h1==h2)

      return x
Hamming = Program()
i1 = int(input())
i2 = int(input())
print(Hamming.hammingDistance(i1, i2))
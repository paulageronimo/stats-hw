
from math import sqrt
from statistics import mean
# Calculating SD and stuff

def square(list):
  return [i ** 2 for i in list]

def listOfZs(t, M, s):
  return [round((x - M)/s, 2) for x in t]

def listOfTs(zs):
  return [round(z*10+50, 2) for z in zs]
    
t1 = [900, 600, 800, 700, 850, 750]

t2 = [30, 25, 26, 31, 29, 32]

t3 = [83, 85, 89, 93, 87, 84]

# Mean, xbar
M1, M2, M3 = 776, 28, 87
print('Means: ', M1, M2, M3)

# summation of list
sX1, sX2, sX3 = sum(t1), sum(t2), sum(t3)
print('ΣX: ', sX1, sX2, sX3)
# summation of list items squared
sX1sq, sX2sq, sX3sq = sum(square(t1)), sum(square(t2)), sum(square(t3))
print('ΣX^2: ', sX1sq, sX2sq, sX3sq)
# n
n1, n2, n3 = len(t1), len(t2), len(t3)
print('n: ', n1, n2, n3)
# SD
s1, s2, s3 = 50, 3, 4
z1, z2, z3 = listOfZs(t1, M1, s1), listOfZs(t2, M2, s2), listOfZs(t3, M3, s3)

T1, T2, T3 = listOfTs(z1), listOfTs(z2), listOfTs(z3)

print("\nStandard Deviation")
print("S=", s1,"S=", s2, "S=", s3)
print("* * * * * * *")
print("standard scores")
print("z:", z1)
print("------------------")
print("z:", z2)
print("------------------")
print("z:", z3)

for i in range(0,6):
  print(round(z1[i]+z2[i]+z3[i], 2))
  

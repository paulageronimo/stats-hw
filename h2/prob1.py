
from math import sqrt
from statistics import mean

from numpy import sort
# Calculating SD and stuff

def square(list):
  return [i ** 2 for i in list]

def listOfZs(t, M, s):
  return [round((x - M)/s, 2) for x in t]

def listOfTs(zs):
  return [round(z*10+50, 2) for z in zs]

t1 = [13,16,18,19,20,20,21,28,32,34,36,43,46,46,48,48,72,91]
print(sort(t1))
sqt1 = square(t1)
print(sqt1)
t2 = [0]
sqt2 = []
print(sqt2)
# Mean, xbar
M1, M2 = mean(t1), mean(t2)
print('Means: ', M1, M2)
# summation of list
sX1, sX2 = sum(t1), sum(t2)
print('ΣX: ', sX1, sX2)
# summation of list items squared
sX1sq, sX2sq = sum(square(t1)), sum(square(t2))
print('ΣX^2: ', sX1sq, sX2sq)
# n
n1, n2 = len(t1), len(t2)
print('n: ', n1, n2)
# SD
s1, s2 = round(sqrt((sX1sq - (sX1**2 / n1))/(n1-1)), 2), round(sqrt((sX2sq - (sX2**2 / n1))/(n1-1)), 2)
# z1, z2 = listOfZs(t1, M1, s1), listOfZs(t2, M2, s2)
# T1, T2 = listOfTs(z1), listOfTs(z2)

z1= listOfZs(t1, M1, s1)
T1= listOfTs(z1)

print("\nStandard Deviation")
print("S=", s1,"S=", s2)
# print("* * * * * * *")
# print("standard scores")
# print("z:", z1, "\nT: ", T1)
# print("------------------")
# print("z:", z2, "\nT:", T2)
# print("* * * * * * *")


# t1, t2
# M1, M2
def stdevCals(M, s):
  return [round(M+(i*s), 2) for i in range(-3,4)]

print(stdevCals(M1, s1))
print(stdevCals(M2, s2))

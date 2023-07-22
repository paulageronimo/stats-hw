
from math import sqrt
from statistics import mean
# Calculating SD and stuff

def square(list):
  return [i ** 2 for i in list]

def listOfZs(t, M, s):
  return [round((x - M)/s, 2) for x in t]

def listOfTs(zs):
  return [round(z*10+50, 2) for z in zs]
    

n1 = 10
sX1sq = 763
sX1 = 83

# SD
s1= sqrt((sX1sq - (sX1**2 / n1))/(n1-1))
# z1= listOfZs(t1, M1, s1)
# T1= listOfTs(z1)

print("\nStandard Deviation")
print("S=", s1)
# print("* * * * * * *")
# print("standard scores")
# print("z:", z1, "\nT: ", T1)
# print("------------------")
# print("z:", z2, "\nT:", T2)
# print("* * * * * * *")


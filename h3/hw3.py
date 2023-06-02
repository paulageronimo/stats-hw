import matplotlib.pyplot as plt
from math import sqrt
from statistics import mean
from numpy import array, dot

def square(list):
  return [i ** 2 for i in list]


def inR(r):
  if r < 0:
    directionality = "indirect"
  elif r > 0:
    directionality = "direct"
  else:
    directionality = 'indirect or direct'
    
  r = abs(r)
  
  if r > .8:
    relationship = "very strong"
  elif r > .6:
    relationship = 'strong'
  elif r > .4:
    relationship = 'moderate'
  elif r > .2:
    relationship = 'weak'
  elif r > .01:
    relationship = 'very weak'
  else:
    relationship = 'no'
  return f"There is a {relationship} {directionality} relationship between X and Y"

def inR2(r):
  return f"{round(r**2,2)*100}% of Y can be explained by x"

def in1_R2(r):
  return f"{(1-round(r**2,2))*100}% of Y cannot be explained by x"

def calcR(sXY, sX, sY, sX2, sY2, n):
  r_top = sXY - (sX * sY)/n
  r_bottom = sqrt((sX2-(sX**2)/n)*(sY2-(sY**2)/n))
  print(" * "*10)
  print(f"\t{sXY} - ({sX} * {sY})/{n}")
  print("----------------------")
  print(f"√{sX2}-({sX}^2)/{n})*({sY2}-({sY}^2)/{n}))")
  print(" * "*10)
  print(f"\t{sXY - (sX * sY)/n}")
  print("----------------------")
  print(f"√{sX2-(sX**2)/n})*({sY2-(sY**2)/n}))")
  print(" * "*10)
  r = r_top/r_bottom
  print("r = \t", r)
  print("r^2 = \t", r**2)
  print("1-r^2= \t", 1-r**2)
  print(" * "*10)

  print(inR(r))
  print(inR2(r))
  print(in1_R2(r))
  return 

def hw(x, y):
  print("\n\n\n* * * *\nHW PROBLEM\n* * * *")
  print('X^2', square(x))
  print('Y^2', square(y))
  print()
  print('Cross Product: ', end=' ')
  n = len(x)
  for i in range(0,n):
    print(x[i]*y[i], end=' ')
  sXY = dot(array(x), array(y))
  
  print("=", sXY)

  print()
  # Mean, xbar
  Mx, My = mean(x), mean(y)
  print('Means: ', round(Mx,2), My)
  # summation of list
  sX, sY = sum(x), sum(y)
  print('ΣX: ', sX,'\tΣY: ',  sY)
  # summation of list items squared
  sX2, sY2 = sum(square(x)), sum(square(y))
  print('ΣX^2: ', sX2,'\tΣY^2: ', sY2)
  print()
  
  calcR(sXY, sX, sY, sX2, sY2, n)
  
  
  # plt.scatter(x, y)
  # plt.show()
  

x1 = [8,8,5,9,8,2]
y1 = [13,10,9,13,15,9]

x2 = [7, 8, 5, 9, 8, 6, 5]
y2 = [14,12,10,18,17,14,11]

x3 = [5,2,6,9,8,9,8,9]
y3 = [9,6,2,2,8,7,2,1]

# hw(x1, y1)
hw(x3, y3)
# calcR(13937, 202, 409, 7280, 28365, 6)

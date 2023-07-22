from math import sqrt
from statistics import mean

def calcB1(sXY, sX, sY, sX2, n):
  b1_top = sXY - (sX * sY)/n
  b1_bottom = (sX2-(sX**2)/n)
  print(" * "*10)
  print(f"\t{sXY} - ({sX} * {sY})/{n}")
  print("----------------------")
  print(f"{sX2}-({sX}^2)/{n}")
  print(" * "*10)
  b1 = round(b1_top/b1_bottom,2)
  print('b1 = ', b1)

  return b1

def calcB0(b1, Mx, My):
  b0 = round((My-Mx*b1),2)
  print('b0 = ', f'{My} - {b1}({Mx})', ' = ', b0)
  return b0

def regressionEq(b1, b0, X1, X2):
  # Interpret the slope for the data
  # Use X and Y from HW 3
  if b1 > 0:
    posORneg = 'up'
  else:
    posORneg = 'down'
  print(f"For every 1 point increase in X, Y goes {posORneg}, on average, by {abs(b1)} units")
  print(f"Y' = {b0} + ({b1})X")
  # Determine Y' for X = 6.5 and X = 3.5
  yp = round(Y_Prime(b0, b1, X1),2)
  print(f"If X = {X1}  {b0} + {b1} * {X1} = {yp}")
  yp = round(Y_Prime(b0, b1, X2),2)
  print(f"If X = {X2}  {b0} + {b1} * {X2} = {yp}")

def Y_Prime(b0, b1, x):
  return b0 + b1 * x

# x1 = [8,8,5,9,8,2]
# y1 = [13,10,9,13,15,9]
# Mx = round(mean(x1),2)
# print("_x = ", Mx)
# My = round(mean(y1),2)
# print("_y = ", My)
# Determine the regression 
# equation for the data by finding b0 and b1
# b0 : intercept ; b1: slope
# print(f"\n\n\n* * * * * FOR 1 * * * * *\n\n\n")
# b1 = calcB1(484, 40, 69, 302, 6)
# b0 = calcB0(b1, x, y)
# regressionEq(x1, y1, b1, b0, X1 = 6.5, X2 = 3.5)

# x2 = [7, 8, 5, 9, 8, 6, 5]
# y2 = [14,12,10,18,17,14,11]
# Mx = round(mean(x2),2)
# print("_x = ", Mx)
# My = round(mean(y2),2)
# print("_y = ", My)
# print(f"\n\n\n* * * * * FOR 2 * * * * *\n\n\n")
# b1 = calcB1(681, 48, 96, 344, len(x2))
# b0 = calcB0(b1, x, y)
# regressionEq(x2,y2, b1, b0, X1 = 6.5, X2 = 4.5)

# x3 = [5,2,6,9,8,9,8,9]
# y3 = [9,6,2,2,8,7,2,1]
# Mx = round(mean(x3),2)
# print("_x = ", Mx)
# My = round(mean(y3),2)
# print("_y = ", My)
# print(f"\n\n\n* * * * * FOR 3 * * * * *\n\n\n")
# b1 = calcB1(239, 56, 37, 436, len(x3))
# b0 = calcB0(b1, x, y)
# regressionEq(x3,y3, b1, b0, X1 = 6.5, X2 = 3.5)

# print(f"\n\n\n* * * * * FOR 4 * * * * *\n\n\n")
# b1 = calcB1(13937, 202, 409, 7280, 6)
# Mx = round(202/6,2)
# print("_x = ", Mx)
# My = round(409/6,2)
# print("_y = ", My)
# b0 = calcB0(b1, Mx, My)
# regressionEq(b1, b0, X1 = 28, X2 = 42)

print(f"\n\n\n* * * * * FOR 4 * * * * *\n\n\n")
b1 = calcB1(7507, 112, 531, 1592, 8)
Mx = round(112/8,2)
# print(b1)
print("_x = ", Mx)
My = round(531/8,2)
print("_y = ", My)
b0 = calcB0(b1, Mx, My)
regressionEq(b1, b0, X1 = 0, X2 = 0)
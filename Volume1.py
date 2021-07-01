import math

x1 = 8.1725

y1 = 516.8463

z1 = 193.2398



x2 = 71.8196

y2 = 376.4121

z2 = -39.2224



x3 = 370.5856

y3 = -20.2995

z3 = 237.2197



l1 = abs(x2 - x1)

print(" l1 =", l1)

b1 = abs(y2 - y1)

print(" b1 =", b1)

d1 = abs(z2 - z1)

print(" d1 =", d1)


l2 = abs(x2 - x3)

print(" l2 =", l2)

b2 = abs(y2 - y3)

print(" b2 =", b2)

d2 = abs(z2 - z3)

print(" d2 =", d2)

l3 = abs(x3 - x1)

print(" l3 =", l3)

b3 = abs(y3 - y1)

print(" b3 =", b3)

d3 = abs(z3 - z1)

print(" d3  =", d3)

l = (l1 + l2 + l3)/3

print("Average Length = ", l)

b = (b1 + b2 + b3)/3

print("Average Breadth = ", b)

d = (d1 + d2 + d3)/3

print("Average Depth = ", d)


area = l * b

print("2 D area =", area)

surface_area = 2 * (l * b + b * d + l * d)

print("Surface Area =", surface_area)

volume = l * b * d

print("Volume = ", volume)

lateral_surface_area = 2 * d * (l + b)

print("Lateral Surface Area = ", lateral_surface_area)


perimeter = 4 * (l + b + d)

print("Perimeter =", perimeter)













# length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# print("Length of the Crack=", length1)

# breadth1 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

# print("Breadth of the Crack", breadth1)


# length2 = math.sqrt((xx2 - xx1)**2 + (yy2 - yy1)**2)

# print("Length of the Crack=", length2)


# breadth2 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

# print("Breadth of the Crack", breadth2)


# length3 = math.sqrt((xxx2 - xxx1)**2 + (yyy2 - yyy1)**2)

# print("Length of the Crack=", length3)


# breadth3 = math.sqrt((aaa2 - aaa1)**2 + (bbb2 - bbb1)**2)

# print("Breadth of the Crack", breadth3)

# AverageLength = ((length1 + length2 + length3)/3)
# AverageBreadth = ((breadth1 + breadth2 + breadth3)/3)

# print("Average Length = ", AverageLength)
# print("Average Breadth = ", AverageBreadth)

# area = AverageLength * AverageBreadth

# print("Area = ", area)

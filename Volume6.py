import math

x1 = 3.7403

y1 = 242.5049

z1 = 145.0617



x2 = 178.1658

y2 = 8.2645

z2 = 53.1363



x3 = 339.1136

y3 = 65.7322

z3 = 186.9951



l1 = abs(x2 - x1)

print(" l1 =", abs(l1))

b1 = abs(y2 - y1)

print(" b1 =", abs(b1))

d1 = abs(z2 - z1)

print(" d1 =", abs(d1))


l2 = abs(x2 - x3)

print(" l2 =", abs(l2))

b2 = abs(y2 - y3)

print(" b2 =", abs(b2))

d2 = abs(z2 - z3)

print(" d2 =", abs(d2))

l3 = abs(x3 - x1)

print(" l3 =", abs(l3))

b3 = abs(y3 - y1)

print(" b3 =", abs(b3))

d3 = abs(z3 - z1)

print(" d3  =", (d3))

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









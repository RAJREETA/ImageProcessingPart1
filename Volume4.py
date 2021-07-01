import math

x1 = -13.8147

y1 = 332.2942

z1 = 712.4549



x2 = -26.0932

y2 = 327.8565

z2 = 218.3614



x3 = 344.8245

y3 = 340.5446

z3 = 28.3418



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










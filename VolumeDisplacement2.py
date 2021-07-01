import math

x1 = -9.1107

y1 = 319.4911

z1 = 248.5533



x2 = 92.6845

y2 = 322.6175

z2 = 200.4937



x3 = -4.1317

y3 = 235.721

z3 = -12.7757

l1 = x2 - x1

print(" l1 =", l1)

b1 = y2 - y1

print(" b1 =", b1)

d1 = z2 - z1

print(" d1 =", d1)


l2 = x2 - x3

print(" l2 =", l2)

b2 = y2 - y3

print(" b2 =", b2)

d2 = z2 - z3

print(" d2 =", d2)

l3 = x3 - x1

print(" l3 =", l3)

b3 = y3 - y1

print(" b3 =", b3)

d3 = z3 - z1

print(" d3  =", d3)

s1 = math.sqrt((l1*l1) + (b1*b1) + (d1 * d1))

print("Distant 1 =", s1)

s2 = math.sqrt((l2*l2) + (b2*b2) + (d2 * d2))

print("Distant 2 =", s2)

s3 = math.sqrt((l3*l3) + (b3*b3) + (d3 * d3))

print("Distant 3 =", s3)


area = s1 * s2

print("2 D area =", area)

surface_area = 2 * (s1 * s2 + s1 * s3 + s2 * s3)

print("Surface Area =", surface_area)

volume = s1 * s2 * s3

print("Volume = ", volume)

lateral_surface_area = 2 * s3 * (s1 +s2)

print("Lateral Surface Area = ", lateral_surface_area)


perimeter = 4 * (s1 + s2 + s3)

print("Perimeter =", perimeter)
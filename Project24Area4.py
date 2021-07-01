import math

x1 = 315
x2 = 62
y1 = 21
y2 = 307

length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Length of the Crack=", length1)

a1 = 5
a2 = 265
b1 = 498
b2 = 180

breadth1 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth1)

xx1 = 414
xx2 = 312
yy1 = 501
yy2 = 259

length2 = math.sqrt((xx2 - xx1)**2 + (yy2 - yy1)**2)

print("Length of the Crack=", length2)

aa1 = 1
aa2 = 201
bb1 = 198
bb2 = 19

breadth2 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth2)

xxx1 = 514
xxx2 = 214
yyy1 = 369
yyy2 = 265

length3 = math.sqrt((xxx2 - xxx1)**2 + (yyy2 - yyy1)**2)

print("Length of the Crack=", length3)

aaa1 = 43
aaa2 = 26
bbb1 = 184
bbb2 = 303

breadth3 = math.sqrt((aaa2 - aaa1)**2 + (bbb2 - bbb1)**2)

print("Breadth of the Crack", breadth3)

AverageLength = ((length1 + length2 + length3)/3)
AverageBreadth = ((breadth1 + breadth2 + breadth3)/3)

print("Average Length = ", AverageLength)
print("Average Breadth = ", AverageBreadth)

area = AverageLength * AverageBreadth

print("Area = ", area)

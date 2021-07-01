import math

x1 = 209
x2 = 286
y1 = 74
y2 = 289

length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Length of the Crack=", length1)

a1 = 231
a2 = 216
b1 = 106
b2 = 124

breadth1 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth1)

xx1 = 281
xx2 = 286
yy1 = 19
yy2 = 289

length2 = math.sqrt((xx2 - xx1)**2 + (yy2 - yy1)**2)

print("Length of the Crack=", length2)

aa1 = 217
aa2 = 200
bb1 = 148
bb2 = 176

breadth2 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth2)

xxx1 = 212
xxx2 = 286
yyy1 = 48
yyy2 = 270

length3 = math.sqrt((xxx2 - xxx1)**2 + (yyy2 - yyy1)**2)

print("Length of the Crack=", length3)

aaa1 = 235
aaa2 = 247
bbb1 = 214
bbb2 = 193

breadth3 = math.sqrt((aaa2 - aaa1)**2 + (bbb2 - bbb1)**2)

print("Breadth of the Crack", breadth3)

AverageLength = ((length1 + length2 + length3)/3)
AverageBreadth = ((breadth1 + breadth2 + breadth3)/3)

print("Average Length = ", AverageLength)
print("Average Breadth = ", AverageBreadth)

area = AverageLength * AverageBreadth

print("Area = ", area)

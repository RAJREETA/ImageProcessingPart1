import math

x1 = 123
x2 = 10
y1 = 20
y2 = 315

length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Length of the Crack=", length1)

a1 = 110
a2 = 74
b1 = 81
b2 = 107

breadth1 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth1)

xx1 = 133
xx2 = 7
yy1 = 45
yy2 = 286

length2 = math.sqrt((xx2 - xx1)**2 + (yy2 - yy1)**2)

print("Length of the Crack=", length2)

aa1 = 77
aa2 = 80
bb1 = 132
bb2 = 159

breadth2 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth2)

xxx1 = 118
xxx2 = 11
yyy1 = 62
yyy2 = 256

length3 = math.sqrt((xxx2 - xxx1)**2 + (yyy2 - yyy1)**2)

print("Length of the Crack=", length3)

aaa1 = 61
aaa2 = 27
bbb1 = 189
bbb2 = 217

breadth3 = math.sqrt((aaa2 - aaa1)**2 + (bbb2 - bbb1)**2)

print("Breadth of the Crack", breadth3)

AverageLength = ((length1 + length2 + length3)/3)
AverageBreadth = ((breadth1 + breadth2 + breadth3)/3)

print("Average Length = ", AverageLength)
print("Average Breadth = ", AverageBreadth)

area = AverageLength * AverageBreadth

print("Area = ", area)

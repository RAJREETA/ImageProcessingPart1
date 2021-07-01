import math

x1 = 150
x2 = 8
y1 = 21
y2 = 249

length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Length of the Crack=", length1)

a1 = 110
a2 = 93
b1 = 86
b2 = 101

breadth1 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth1)

xx1 = 137
xx2 = 18
yy1 = 40
yy2 = 210

length2 = math.sqrt((xx2 - xx1)**2 + (yy2 - yy1)**2)

print("Length of the Crack=", length2)

aa1 = 106
aa2 = 93
bb1 = 86
bb2 =101

breadth2 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth2)

xxx1 = 116
xxx2 = 40
yyy1 = 65
yyy2 = 178

length3 = math.sqrt((xxx2 - xxx1)**2 + (yyy2 - yyy1)**2)

print("Length of the Crack=", length3)

aaa1 = 103
aaa2 = 88
bbb1 = 137
bbb2 = 140

breadth3 = math.sqrt((aaa2 - aaa1)**2 + (bbb2 - bbb1)**2)

print("Breadth of the Crack", breadth3)

AverageLength = ((length1 + length2 + length3)/3)
AverageBreadth = ((breadth1 + breadth2 + breadth3)/3)

print("Average Length = ", AverageLength)
print("Average Breadth = ", AverageBreadth)

area = AverageLength * AverageBreadth

print("Area = ", area)

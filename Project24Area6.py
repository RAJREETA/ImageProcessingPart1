import math

x1 = 147
x2 = 184
y1 = 13
y2 = 217

length1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Length of the Crack=", length1)

a1 = 154
a2 = 143
b1 = 89
b2 = 100

breadth1 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth1)

xx1 = 167
xx2 = 145
yy1 = 221
yy2 = 20

length2 = math.sqrt((xx2 - xx1)**2 + (yy2 - yy1)**2)

print("Length of the Crack=", length2)

aa1 = 168
aa2 = 154
bb1 = 111
bb2 = 126

breadth2 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)

print("Breadth of the Crack", breadth2)

xxx1 = 171
xxx2 = 149
yyy1 = 186
yyy2 = 33

length3 = math.sqrt((xxx2 - xxx1)**2 + (yyy2 - yyy1)**2)

print("Length of the Crack=", length3)

aaa1 = 173
aaa2 = 161
bbb1 = 138
bbb2 = 147

breadth3 = math.sqrt((aaa2 - aaa1)**2 + (bbb2 - bbb1)**2)

print("Breadth of the Crack", breadth3)

AverageLength = ((length1 + length2 + length3)/3)
AverageBreadth = ((breadth1 + breadth2 + breadth3)/3)

print("Average Length = ", AverageLength)
print("Average Breadth = ", AverageBreadth)

area = AverageLength * AverageBreadth

print("Area = ", area)

import math
a = input().split()
A = float(a[0]) * float(a[2]) * math.cos(float(a[1])) * math.cos(float(a[3])) - float(a[0]) * float(a[2]) * math.sin(float(a[1])) * math.sin(float(a[3]))
B = float(a[0]) * float(a[2]) * math.cos(float(a[1])) * math.sin(float(a[3])) + float(a[0]) * float(a[2]) * math.sin(float(a[1])) * math.cos(float(a[3]))
if 0 > A > -0.005:
    print("0.00", end='')
else:
    print("%.2f" % A, end='')
if 0 > B > -0.005:
    print("+0.00i")
elif B >= 0:
    print("+%.2fi" % B)
else:
    print("%.2fi" % B)

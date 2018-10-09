N = [int(x) for x in input().split()]
A1, A2, A3, A4, A5 = 0, 0, 0, 0, -1
b=1
count =0
count2=0
for i in N[1:]:
    if i % 10 == 0:
        A1 += i
    if i % 5 == 1:
        count2+=1
        A2 += i*b
        b *= -1
    if i % 5 == 2:
        A3 += 1
    if i % 5 == 3:
        A4 += i
        count += 1
    if i % 5 == 4:
        if i > A5:
            A5 = i
print("N" if A1 == 0 else A1, "N" if count2 == 0 else A2, "N" if A3 == 0 else A3, "N" if A4 == 0 else "%.1f" % (A4/count), "N" if A5 == -1 else A5)
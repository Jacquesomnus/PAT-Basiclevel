N = int(input())
A, B = 0, 0
for i in range(N):
    a = input().split()
    if int(a[1]) == int(a[0])+int(a[2]) and int(a[3]) != int(a[0])+int(a[2]):
        B += 1
    if int(a[3]) == int(a[0])+int(a[2]) and int(a[1]) != int(a[0])+int(a[2]):
        A += 1
print(A, B)

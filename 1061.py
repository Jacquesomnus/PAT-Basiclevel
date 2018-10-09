N, M = input().split()
a = input().split()
b = input().split()
for i in range(int(N)):
    count = 0
    c = input().split()
    for j in range(int(M)):
        if c[j] == b[j]:
            count += int(a[j])
    print(count)
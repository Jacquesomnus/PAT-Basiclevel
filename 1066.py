M, N, A, B, a = input().split()
for i in range(int(M)):
    b = input().split()
    n = ''
    for j in range(int(N)):
        if int(A) <= int(b[j]) <= int(B):
            n += ' ' + a.zfill(3)
        else:
            n += ' ' + b[j].zfill(3)
    print(n.lstrip())

A, B, D = input().split()
C = int(A) + int(B)
res = ''
if C == 0:
    print(0)
else:
    while C > 0:
        res += str(C % int(D))
        C //= int(D)
    print(int(res[::-1]))
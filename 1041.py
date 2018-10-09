N = int(input())
dict = {}
for i in range(N):
    id, num1, num2 = input().split()
    dict[num1] = (id, num2)
M = int(input())
z = input().split()
for i in range(M):
    print(' '.join(dict[z[i]]))
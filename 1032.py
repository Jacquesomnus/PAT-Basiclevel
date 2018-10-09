# 超时待修改
L = [0]*100005
N = int(input())
max = -1
maxindex = -1
for i in range(N):
    k, v = input().split()
    L[int(k)] += int(v)
    if L[int(k)] > max:
        max = L[int(k)]
        maxindex = int(k)
print(maxindex, max)

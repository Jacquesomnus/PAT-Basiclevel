num = input().split()
count = 0
N = int(num[0])
for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j:
            count += int(num[i] + num[j])
print(count)
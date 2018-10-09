N, C = input().split()
print(C * int(N))
for i in range(int(int(N) / 2 + 0.5) - 2):
    print(C + ' ' * (int(N) - 2) + C)
print(C * int(N))
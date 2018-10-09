n = int(input())
B, S, N = n//100, n % 100//10, n % 10 + 1
print("B"*B+"S"*S, end="")
for i in range(1, N):
    print(i, end="")
